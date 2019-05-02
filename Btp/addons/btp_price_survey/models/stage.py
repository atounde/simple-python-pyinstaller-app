# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Stage(models.Model):
    _name = 'btp_price_survey.stage'
    _order = 'analytical_account_mane asc'

    name = fields.Char('Nom', required=True)
    analytical_account_mane = fields.Char(related='analytical_account.name', string="N° compte analytique",
                                          readonly=True, store=True)
    analytical_account = fields.Many2one('btp_price_survey.analytical_account', string='N° compte analytique',
                                         required=True)
    unit = fields.Many2one('btp_base.resource.unit', string="Unité", required=True)
    profit_margin_rate = fields.Float(string='Marge bénéficiaire')
    selling_price = fields.Float(string='Prix de vente', compute='_compute_selling_price', store=True)
    line_ids = fields.One2many('btp_price_survey.stage.line', 'stage_id', string="Lignes d'étape", copy=True)
    category = fields.Many2one('btp_price_survey.stage.category', string="Catégorie")
    price_total = fields.Float(string='Prix de revient', compute='_compute_price_total', store=True)
    price_survey = fields.Many2one('btp_price_survey.price_survey', string="Étude de prix")

    @api.onchange('price_survey')
    def onchange_profit_margin_rate(self):
        if self.price_survey:
            self.profit_margin_rate = self.price_survey.profit_margin_rate.settings_value

    _sql_constraints = [
        ('name_uniq', 'unique(name,price_survey)',
         "Le nom d'une étape doit être unique.\n Veuillez corriger pour continuer!"),
    ]

    @api.one
    @api.depends('line_ids')
    def _compute_price_total(self):
        self.price_total = sum(line.price_total for line in self.line_ids)

    @api.one
    @api.depends('profit_margin_rate', 'price_total')
    def _compute_selling_price(self):
        self.selling_price = (1 + self.profit_margin_rate / 100) * self.price_total

    @api.one
    @api.constrains('profit_margin_rate')
    def _check_is_valid_profit_margin_rate(self):
        if self.profit_margin_rate < 0:
            raise ValidationError("Attention, le pourcentage de la marge bénéficiare ne doit être négatif.")
