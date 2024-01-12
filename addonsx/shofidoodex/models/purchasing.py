from odoo import models, fields, api, _

class DoodexPurchasing (models.Model):
    _inherit = 'res.partner'

    is_purchasing = fields.Boolean(string='Is Purchasing', default=False)
    