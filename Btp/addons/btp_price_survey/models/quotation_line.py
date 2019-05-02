# -*- coding: utf-8 -*-
from odoo import models, fields, api


class QuotationLine(models.Model):
    _name = 'btp_price_survey.quotation.line'

    category_id = fields.Many2one('btp_price_survey.quotation.line.category',
                                  string='Catégorie de ligne de devis')
    analytical_account = fields.Many2one(related='name.analytical_account', string='N° compte analytique',
                                         readonly=True)
    name = fields.Many2one('btp_price_survey.stage', string="Étape", required=True)
    quantity = fields.Float(string='Quantité', default=1)
    unit = fields.Many2one(related='name.unit', string='Unité', readonly=True)
    unit_price = fields.Float(string='Prix unitaire')
    number_of_days = fields.Integer('Nombre de jours', compute='_compute_number_of_days', store=True)
    total_price = fields.Float(string='Total', compute='_compute_total_price', store=True)

    @api.one
    @api.depends('unit_price', 'quantity')
    def _compute_total_price(self):
        self.total_price = self.unit_price * self.quantity

    @api.onchange('name')
    def _onchange_unit_price(self):
        if self.name:
            self.unit_price = self.name.selling_price

    @api.one
    @api.depends('quantity', 'name', 'name.line_ids.performance', 'name.line_ids.quantity')
    def _compute_number_of_days(self):
        if self.name.line_ids:
            self.number_of_days = int(
                round(self.quantity / min(line.performance * line.quantity for line in self.name.line_ids)))
