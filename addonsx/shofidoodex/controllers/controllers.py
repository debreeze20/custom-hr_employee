# -*- coding: utf-8 -*-
# from odoo import http


# class Shofidoodex(http.Controller):
#     @http.route('/shofidoodex/shofidoodex', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shofidoodex/shofidoodex/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('shofidoodex.listing', {
#             'root': '/shofidoodex/shofidoodex',
#             'objects': http.request.env['shofidoodex.shofidoodex'].search([]),
#         })

#     @http.route('/shofidoodex/shofidoodex/objects/<model("shofidoodex.shofidoodex"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shofidoodex.object', {
#             'object': obj
#         })
