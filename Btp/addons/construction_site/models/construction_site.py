# -*- coding: utf-8 -*-

from odoo import models, fields, api


class construction_site(models.Model):
    _name = 'construction_site.construction_site'

    name = fields.Char(string="Nom", required=True)
    city = fields.Many2one('city.city', string='Ville', required=True)
    estimated_budget = fields.Float(string="Budjet estimé", required=True)
    executed_budget = fields.Float(string="Budjet executé", required=True)
    execution_rate = fields.Float(string="Taux d'execution")
