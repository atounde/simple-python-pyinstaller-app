# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StageCategory(models.Model):
    _name = 'btp_price_survey.stage.category'

    name = fields.Char('Nom', required=True)
    analytical_account = fields.Many2one('btp_price_survey.analytical_account', string='N° compte analytique')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', "Ce nom existe déjà.\n Veuillez choisir un autre nom pour continuer!"),
    ]