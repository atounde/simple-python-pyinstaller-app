# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AnalyticalAccount(models.Model):

      _name = 'btp_price_survey.analytical_account'

      name = fields.Char('Numéro', required=True)

      _sql_constraints = [
            ('number_uniq', 'unique(name)', "Ce numéro existe déjà.\n Veuillez choisir un autre numéro pour continuer!"),
      ]