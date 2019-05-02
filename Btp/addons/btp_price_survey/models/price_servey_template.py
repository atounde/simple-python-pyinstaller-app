# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PriceServeyTemplate(models.Model):
    _name = 'btp_price_survey.template'

    name = fields.Many2one('btp_price_survey.template.stage', string="Nom", required=True)
    company_id = fields.Many2one('res.company', string="Société", copy=True)

    class Company(models.Model):
        _inherit = "res.company"

        price_servey_template_ids = fields.One2many("btp_price_survey.template", "company_id", string='Étude de prix')