from odoo import models, fields, api, _

class DoodexKomisaris(models.Model):
    _inherit = 'res.partner'

    gaji = fields.Integer(string='Gaji')
    