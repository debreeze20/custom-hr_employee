# -*- coding: utf-8 -*-

from odoo import models, fields, api


class shofidoodex(models.Model):
    _name = 'shofidoodex.shofidoodex'
    _description = 'shofidoodex.shofidoodex'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
