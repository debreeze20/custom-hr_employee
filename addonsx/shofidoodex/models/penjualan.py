from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class DoodexPenjualan(models.Model):
    _name = 'doodex.penjualan'
    _description = 'model.technical.name'
    _rec_name = 'referensi'

    referensi = fields.Char(
        string="No. Reference",
        required=True, copy=False, readonly=True,
        default=lambda self: _('New'))
    
    
    # referensi = fields.Char(string='No. Referensi')
    membership = fields.Boolean(string='Apakah member?', default=False)
    nama_nonmember = fields.Char(string='Nama')
    pelanggan_id = fields.Many2one(comodel_name='doodex.pelanggan', string='ID Pelanggan')
    id_member_penjualan = fields.Char(compute='_compute_id_member_penjualan', string='Nama member')
    tgl_transaksi = fields.Datetime(string='Tanggal transaksi', default=fields.Datetime.now())
    detailpenjualan_ids = fields.One2many(comodel_name='doodex.detailpenjualan', inverse_name='penjualan_id', string='penjualan')
    total_bayar = fields.Char(compute='_compute_total_bayar', string='total bayar')    
    total_qty = fields.Char(compute='_compute_total_qty', string='total_qty')  
    
    @api.depends('detailpenjualan_ids')
    def _compute_total_bayar(self):
        for rec in self:
            total = sum(self.env['doodex.detailpenjualan'].search([('penjualan_id','=',rec.id)]).mapped('subtotal')) 
            # print(a)
            # total = sum(a)
            rec.total_bayar = total

    @api.depends('detailpenjualan_ids.qty')
    def _compute_total_qty(self):
        for rec in self:
            total_qty = sum(rec.detailpenjualan_ids.mapped('qty')) 
            rec.total_qty = total_qty

    
    @api.depends('pelanggan_id')
    def _compute_id_member_penjualan(self):
        for rec in self:
            rec.id_member_penjualan = rec.pelanggan_id.name

    @api.model
    def create(self,vals):
        if vals.get('referensi', _("New")) == _("New"):                
           vals['referensi'] = self.env['ir.sequence'].next_by_code('referensi.penjualan') or _("New")
        record = super(DoodexPenjualan, self).create(vals)
        return record
    
    def unlink(self):
        if self.detailpenjualan_ids:
            a = []
            for detail in self:
                a = self.env['doodex.detailpenjualan'].search([('penjualan_id', '=', detail.id)])
            print(a)
            for barang in a:
                barang.barang_id.stok += barang.qty
        record = super(DoodexPenjualan, self).unlink()


class DoodexDetailPenjualan (models.Model):
    _name = 'doodex.detailpenjualan'
    _description = 'model.technical.name'

    penjualan_id = fields.Many2one(comodel_name='doodex.penjualan', string='Penjualan')
    barang_id = fields.Many2one(comodel_name='barang.doodex', string='Nama Barang')
    harga_satuan = fields.Integer(string='Harga satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='subtotal')
    subtotal_qty = fields.Integer(compute='_compute_subtotal_qty', string='subtotal_qty')
    
    # @api.depends('qty')
    # def _compute_subtotal_qty(self):
    #     for rec in self:
    #         rec.subtotal_qty = sum(rec.qty)
    
    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.harga_satuan*rec.qty


    @api.onchange('barang_id')
    def _onchange_barang(self):
        self.harga_satuan = self.barang_id.harga
    
    @api.constrains('qty')
    def _checkQuantity(self):
        for record in self:
            if record.qty < 1:
                raise ValidationError('masa beli {} cuma {} pcs.'.format(record.barang_id.nama_barang, record.qty))
            elif record.qty > record.barang_id.stok :
                raise ValidationError('Stok {} tidak cukup atau melebihi stok kami.'.format(record.barang_id.nama_barang))

    @api.model
    def create (self, vals): 
        record = super(DoodexDetailPenjualan, self).create(vals)
        if record.qty:
            self.env['barang.doodex'].search([('id', '=', record.barang_id.id)]).write({'stok' : record.barang_id.stok-record.qty})
        return record