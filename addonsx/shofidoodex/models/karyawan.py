from odoo import models, fields

class DoodexKaryawan(models.Model):
    _name = 'doodex.karyawan'
    _inherit = 'doodex.manusia'
    _description = 'doodex.karyawan'
    _rec_name = 'id_karyawan'

    id_karyawan = fields.Char(string='ID karyawan')
    
    bagian = fields.Selection(string='posisi', selection=[('accounting', 'Accounting'), ('kasir', 'Kasir'),('kebersihan', 'Kebersihan')], required=True)
    
    daftarkaryawan = fields.One2many(comodel_name='doodex.manusia', inverse_name='posisi', string='daftar karyawan')
    gaji = fields.Integer(string='Gaji per bulan') 
    foto = fields.Binary(string='Foto')

    # kode = fields.Char(string='Kode')

    # @api.onchange('name')
    # def _onchange_kode(self):
    #     if self.name == 'accounting':
    #         self.kode = 'acc'
    #     elif self.name == 'kasir':
    #         self.kode = 'ks'
    #     elif self.name == 'makanankering':
    #         self.kode = 'mk'