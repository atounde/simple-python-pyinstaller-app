# -*- coding: utf-8 -*-

from odoo import models, fields, api


class city(models.Model):
    _name = 'city.city'

    name = fields.Char(string="Nom", required=True)
