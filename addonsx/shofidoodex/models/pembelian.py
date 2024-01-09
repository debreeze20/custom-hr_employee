from odoo import models, fields, api, _

class DoodexPembelian(models.Model):
    _name = 'doodex.pembelian'
    _description = 'model.technical.name'

    name = fields.Char(string='Kode Pembelian')
    barang_id = fields.Many2one(comodel_name='barang.doodex', string='Nama Barang')
    supplier_id = fields.Many2one(comodel_name='doodex.supplier', string='Supplier')
    qty_beli= fields.Integer(string='Quantity Pembelian')  
    modal = fields.Char(compute='_compute_modal', string='harga beli')
    bayar = fields.Char(compute='_compute_bayar', string='bayar')

    @api.depends('barang_id')
    def _compute_modal(self):
        for rec in self:
            rec.modal = rec.barang_id.harga_modal
    
    @api.depends('barang_id', 'qty_beli')
    def _compute_bayar(self):
        for rec in self:
            rec.bayar = rec.barang_id.harga_modal * rec.qty_beli

    @api.model
    def create(self,vals):
        # if vals.get('referensi', _("New")) == _("New"):                
        #    vals['referensi'] = self.env['ir.sequence'].next_by_code('referensi.pembelian') or _("New")
        record = super(DoodexPembelian, self).create(vals)
        for r in self:
            self.env['barang.doodex'].search([('id', '=', record.barang_id.id)]).write({'stok' : record.barang_id.stok-record.qty_beli})
        return record
    # def unlink(self):
    #     for r in self:
    #         self.barang_id.stok self.qty_beli
    #         record = super(DoodexPembelian, self).unlink()
    def unlink(self):
        # if self.detailpenjualan_ids:
            # a = []
            # for detail in self:
            #     a = self.env['doodex.detailpenjualan'].search([('penjualan_id', '=', detail.id)])
            # print(a)
        record = super(DoodexPembelian, self).unlink()
        for r in self:
            r.barang_id.stok -= r.qty_beli 
        
