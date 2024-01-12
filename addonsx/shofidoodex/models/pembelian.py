from odoo import models, fields, api, _

class DoodexPembelian(models.Model):
    _name = 'doodex.pembelian'
    # _inherit = 'doodex.supplier'
    _description = 'model.technical.name'
    _rec_name = 'referensi_pembelian'

    referensi_pembelian = fields.Char(
        string="ID Pembelian",
        required=True, copy=False, readonly=True,
        default=lambda self: _('New'))

    name = fields.Char(string='Kode Pembelian')
    barang_id = fields.Many2one(comodel_name='barang.doodex', string='Nama Barang')
    supplier_id = fields.Many2one(comodel_name='doodex.supplier', string='Supplier')
    qty_beli= fields.Integer(string='Quantity Pembelian')  
    modal = fields.Char(compute='_compute_modal', string='harga beli')
    bayar = fields.Char(compute='_compute_bayar', string='bayar')

    #referensi pembelian
    @api.model
    def create(self,vals):
        if vals.get('referensi_pembelian', _("New")) == _("New"):                
           vals['referensi_pembelian'] = self.env['ir.sequence'].next_by_code('id_referensi.pembelian') or _("New")
        record = super(DoodexPembelian, self).create(vals)
        if record.qty_beli:
            self.env['barang.doodex'].search([('id', '=', record.barang_id.id)]).write({'stok' : record.barang_id.stok+record.qty_beli})
        return record

    #menghitung barang
    @api.depends('barang_id')
    def _compute_modal(self):
        for rec in self:
            rec.modal = rec.barang_id.harga_modal
    
    @api.depends('barang_id', 'qty_beli')
    def _compute_bayar(self):
        for rec in self:
            rec.bayar = rec.barang_id.harga_modal * rec.qty_beli

    #pembelian
    # @api.model
    # def create(self,vals):
    #     record = super(DoodexPembelian, self).create(vals)
    #     if record.qty_beli:
    #         self.env['barang.doodex'].search([('id', '=', record.barang_id.id)]).write({'stok' : record.barang_id.stok+record.qty_beli})
    #     return record

    def unlink(self):
        for r in self:
            r.barang_id.stok -= r.qty_beli 
        record = super(DoodexPembelian, self).unlink()
    
        
    @api.onchange('barang_id')
    def _onchange_barang(self):
        a = self.barang_id.supplier_ids
        b =[]
        for i in a:
            b.append(i.id)
        return {'domain': {'supplier_id':[('id','in', b)]}}