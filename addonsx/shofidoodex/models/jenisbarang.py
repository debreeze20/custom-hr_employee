from odoo import models, fields, api

class DoodexJenisBarang(models.Model):
    _name = 'doodex.jenisbarang'
    _description = 'model.technical.name'
    _rec_name = 'kode'

    name = fields.Selection(string='jenis', selection=[('detergen', 'Detergen'), ('bahanmakanan', 'BahanMakanan'),('makanankering', 'MakananKering'),('buah', 'Buah'),('minuman', 'Minuman'),('makananinstan', 'MakananInstan')])
    letak = fields.Integer(string='No. Rak')
    daftarbarang = fields.One2many(comodel_name='barang.doodex', inverse_name='jenis', string='daftarbarang')

    kode = fields.Char(string='Kode')

    @api.onchange('name', 'letak')
    def _onchange_kode(self):
        if self.name == 'detergen':
            self.kode = 'dt'+str(self.letak)
        elif self.name == 'bahanmakanan':
            self.kode = 'bm'+str(self.letak)
        elif self.name == 'buah':
            self.kode = 'bu'+str(self.letak)
        elif self.name == 'minuman':
            self.kode = 'mn'+str(self.letak)
        elif self.name == 'makananinstan':
            self.kode = 'mi'+str(self.letak)