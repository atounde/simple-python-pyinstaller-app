# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Quotation(models.Model):
    _name = 'btp_price_survey.quotation'

    name = fields.Many2one("construction_site.construction_site", string="Chantier",required=True)
    lines_categories = fields.One2many('btp_price_survey.quotation.line.category', 'quotation_id',
                                              string='Catégories de lignes de devis')
    amount_untaxed = fields.Float(string='Total HT', compute='_compute_amount_untaxed', store=True)
    tax = fields.Float(string='TVA')
    amount_taxed = fields.Float(string='Total TTC', compute='_compute_amount_taxed', store=True)

    @api.one
    @api.depends('lines_categories')
    def _compute_amount_untaxed(self):
        self.amount_untaxed = sum(line.total_price for line in self.lines_categories)

    @api.one
    @api.depends('amount_untaxed')
    def _compute_amount_taxed(self):
        self.amount_taxed = ((self.amount_untaxed * self.tax) / 100) + self.amount_untaxed
