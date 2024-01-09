from odoo import models, fields, api, _


class DoodexPelanggan(models.Model):
    _name = "doodex.pelanggan"
    _inherit = "doodex.manusia"
    _description = 'model.technical.name'
    _rec_name = 'referensi_pelanggan'

    # id_member = fields.Char(string='ID Member')
    referensi_pelanggan = fields.Char(
        string="ID Member",
        required=True, copy=False, readonly=True,
        default=lambda self: _('New'))
    
    level = fields.Selection(string='Level Member', selection=[('silver','Silver'),('gold','Gold'),('platinum','Platinum')],default='silver')

    @api.model
    def create(self,vals):
        if vals.get('referensi_pelanggan', _("New")) == _("New"):                
           vals['referensi_pelanggan'] = self.env['ir.sequence'].next_by_code('id_referensi.pelanggan') or _("New")
        record = super(DoodexPelanggan, self).create(vals)
        return record