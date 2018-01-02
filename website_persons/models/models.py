# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta
from datetime import date, datetime
from odoo import models, fields, api


class Persons(models.Model):
    _name = 'website.persons'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    full_name = fields.Char(compute="_merge_first_last")
    date_of_birth = fields.Date()
    age = fields.Char(compute="_compute_age")
    sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ])
    company_id = fields.Many2one('res.company', required=True)

    @api.onchange('first_name', 'last_name')
    @api.model
    def _merge_first_last(self):
        for record in self:
            if record.first_name and record.last_name:
                record.full_name = record.first_name + ' ' + record.last_name

    @api.onchange('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                dif = relativedelta(date.today(),
                                    datetime.strptime(record.date_of_birth,
                                                      "%Y-%m-%d").date())
                record.age = str(dif.years)
