# -*- coding: utf-8 -*-
from odoo import http


class WebsitePersons(http.Controller):
    @http.route('/persons/all/', auth='public', website=True)
    def index(self, **kwargs):
        persons = http.request.env['website.persons']
        return http.request.render('website_persons.index', {
            'persons': persons.search([])[-5:]
        })

    @http.route('/page/add_person', type='http', auth='public', website=True, methods=['POST', 'GET'])
    def create(self, *args, **kwargs):
        vals = http.request.httprequest
        person = http.request.env['website.persons']
        return http.request.render('website_persons.create', {
            'add_person': person.create(vals)
        })
