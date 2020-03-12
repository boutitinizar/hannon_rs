# -*- coding: utf-8 -*-
from odoo import http

# class HannonRs(http.Controller):
#     @http.route('/hannon_rs/hannon_rs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hannon_rs/hannon_rs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hannon_rs.listing', {
#             'root': '/hannon_rs/hannon_rs',
#             'objects': http.request.env['hannon_rs.hannon_rs'].search([]),
#         })

#     @http.route('/hannon_rs/hannon_rs/objects/<model("hannon_rs.hannon_rs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hannon_rs.object', {
#             'object': obj
#         })