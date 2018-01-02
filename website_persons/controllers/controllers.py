# -*- coding: utf-8 -*-
from odoo import http

# class WebsitePersons(http.Controller):
#     @http.route('/website_persons/website_persons/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_persons/website_persons/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_persons.listing', {
#             'root': '/website_persons/website_persons',
#             'objects': http.request.env['website_persons.website_persons'].search([]),
#         })

#     @http.route('/website_persons/website_persons/objects/<model("website_persons.website_persons"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_persons.object', {
#             'object': obj
#         })