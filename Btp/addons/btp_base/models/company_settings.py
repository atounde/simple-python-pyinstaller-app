# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CompanySettings(models.Model):
    _name = "btp_base.company.settings"

    name = fields.Char(string="Libellé", required=True)
    code = fields.Char(string="Code", required=True, )
    company_id = fields.Many2one("res.company", string="Société")

    _sql_constraints = [('code_unique','UNIQUE(code)',"Un code doit être unique !"),
    ]

class Company(models.Model):
    _inherit = "res.company"

    settings_ids = fields.One2many ("btp_base.company.settings", "company_id", string="Paramètres initiaux")