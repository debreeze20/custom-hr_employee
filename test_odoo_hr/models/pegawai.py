from odoo import models, fields, api, _

class OdooPegawai(models.Model):
    # _inherit = 'res.partner'
    _inherit = 'hr.employee'

    # gaji = fields.Integer(string='Gaji')
    kesehatan = fields.Char(string='No BPJS Kesehatan')
    ketenagakerjaan = fields.Char(string='No BPJS Ketenagakerjaan')
    goldar = fields.Selection(string='Golongan Darah', selection=[('o', 'O'), ('a', 'A'),('b', 'B'),('ab', 'AB'),])
    rhesus = fields.Selection(string='Rhesus Darah', selection=[('negatif', 'Negatif'), ('positif', 'Positif'),])
    medical = fields.Text(string='Medical Record')
    
    