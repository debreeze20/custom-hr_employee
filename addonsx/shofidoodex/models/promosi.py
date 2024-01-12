from odoo import models, fields, api, _

class DoodexPromosi (models.Model):
    _inherit = 'res.partner'

    is_promosi = fields.Boolean(string='Is Promosi', default=False)