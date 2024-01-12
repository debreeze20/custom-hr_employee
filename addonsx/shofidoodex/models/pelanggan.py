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
    
    tgl_daftar = fields.Date(string='Tanggal Daftar', default=fields.Date.today())
    poin = fields.Integer(string='Poin', readonly=True)
    penjualan_ids = fields.One2many(comodel_name='doodex.penjualan', inverse_name='pelanggan_id', string='Data pembelian')
    total_belanja = fields.Integer(compute='_compute_total_belanja', string='total_belanja')
    level = fields.Char(compute='_compute_level', string='level', default='silver', readonly=True)
    
    @api.onchange('poin')
    def _compute_level(self):
        for rec in self:
            if rec.poin > 500:
                rec.level = 'platinum'
            elif rec.poin > 200:
                rec.level = 'gold'
            else:
                rec.level = 'silver'

    @api.depends('penjualan_ids')
    def _compute_total_belanja(self):
        for rec in self:
            a = self.env['doodex.penjualan'].search([('pelanggan_id','=',rec.id)]).mapped('total_bayar')
            total = sum(a)
            rec.total_belanja = total
            rec.poin = rec.total_belanja // 10000
    
    # penjualan_ids = fields.Char(compute='_compute_penjualan_ids', string='penjualan_ids')
   
    
    # level = fields.Selection(string='Level Member', selection=[('silver','Silver'),('gold','Gold'),('platinum','Platinum')],default='silver')
    def action_gold(self):
        self.write({'state':'golf'})
    def action_platinum(self):
        self.write({'state':'platinum'})


    @api.model
    def create(self,vals):
        if vals.get('referensi_pelanggan', _("New")) == _("New"):                
           vals['referensi_pelanggan'] = self.env['ir.sequence'].next_by_code('id_referensi.pelanggan') or _("New")

        record = super(DoodexPelanggan, self).create(vals)
        return record