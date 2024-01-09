from odoo import models, fields, api

class BarangDoodex (models.Model):
    _name = 'barang.doodex'
    _description = 'doodex.dekripsi'   
    _rec_name = 'nama_barang'

    name = fields.Char(string='nama')
    nama_barang = fields.Char(string='nama barang')

    description = fields.Char(string='deskripsi')
    jenis = fields.Many2one(comodel_name='doodex.jenisbarang', string='kelompok barang')
    stok = fields.Integer(string='stok')
    harga = fields.Integer(string='harga barang')
    supplier_ids = fields.Many2many(comodel_name='doodex.supplier', string='Supplier')
    harga_modal = fields.Integer(string='Harga Modal')