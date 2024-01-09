from odoo import models, fields, api

class ManusiaDoodex (models.Model):
    _name = 'doodex.manusia'
    _description = 'deskripsi global manusia'
    _rec_name = 'name'

    name = fields.Char(string='Nama', required=True)
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female')])
    alamat = fields.Char(string="Alamat")

    posisi = fields.Many2one(comodel_name='doodex.karyawan', string='kelompok pegawai')