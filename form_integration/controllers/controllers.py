# -*- coding: utf-8 -*-
# from odoo import http


# class FormIntegration(http.Controller):
#     @http.route('/form_integration/form_integration', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/form_integration/form_integration/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('form_integration.listing', {
#             'root': '/form_integration/form_integration',
#             'objects': http.request.env['form_integration.form_integration'].search([]),
#         })

#     @http.route('/form_integration/form_integration/objects/<model("form_integration.form_integration"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('form_integration.object', {
#             'object': obj
#         })
