# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class Profession(models.Model):
    _name = 'btp_base.profession'

    name = fields.Char(string='Nom', size=64, required=True)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', "Cette profession existe déjà!"),
    ]