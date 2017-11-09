# -*- coding: utf-8 -*-
from odoo import http

# class PurchaseDomain(http.Controller):
#     @http.route('/purchase_domain/purchase_domain/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_domain/purchase_domain/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_domain.listing', {
#             'root': '/purchase_domain/purchase_domain',
#             'objects': http.request.env['purchase_domain.purchase_domain'].search([]),
#         })

#     @http.route('/purchase_domain/purchase_domain/objects/<model("purchase_domain.purchase_domain"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_domain.object', {
#             'object': obj
#         })