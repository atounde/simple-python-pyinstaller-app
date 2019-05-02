# -*- coding: utf-8 -*-
from odoo import models, fields, api


class QuotationLineCategory(models.Model):
    _name = 'btp_price_survey.quotation.line.category'
    _order = 'analytical_account_mane asc'

    analytical_account_mane = fields.Char(related='analytical_account.name', string="N° compte analytique",
                                          readonly=True, store=True)
    analytical_account = fields.Many2one(related='name.analytical_account', string='N° compte analytique',
                                         readonly=True, store=True)
    name = fields.Many2one('btp_price_survey.stage.category', string="Catégories de lignes de devis", required=True)
    quotation_lines = fields.One2many('btp_price_survey.quotation.line', 'category_id',
                                      string='Lignes de dévis')
    total_price = fields.Float(string='Total', compute='_compute_total_price', store=True)
    quotation_id = fields.Many2one('btp_price_survey.quotation', string='Devis')

    @api.one
    @api.depends('quotation_lines')
    def _compute_total_price(self):
        self.total_price = sum(line.total_price for line in self.quotation_lines)
