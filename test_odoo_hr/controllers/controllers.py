# -*- coding: utf-8 -*-
# from odoo import http


# class TestOdooHr(http.Controller):
#     @http.route('/test_odoo_hr/test_odoo_hr', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_odoo_hr/test_odoo_hr/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_odoo_hr.listing', {
#             'root': '/test_odoo_hr/test_odoo_hr',
#             'objects': http.request.env['test_odoo_hr.test_odoo_hr'].search([]),
#         })

#     @http.route('/test_odoo_hr/test_odoo_hr/objects/<model("test_odoo_hr.test_odoo_hr"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_odoo_hr.object', {
#             'object': obj
#         })
