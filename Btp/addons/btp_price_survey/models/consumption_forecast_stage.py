# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ConsumptionForecastStage(models.Model):
    _name = 'btp_price_survey.consumption_forecast.stage'

    name = fields.Many2one('btp_price_survey.stage', string='Étape', required=True)
    analytical_account = fields.Char(related='name.analytical_account_mane', string='N° compte analytique')
    consumption_forecast_id = fields.Many2one('btp_price_survey.consumption_forecast',
                                              string="Prévision de consommation", ondelete="cascade")
    line_ids = fields.One2many('btp_price_survey.consumption_forecast.stage.line', 'consumption_forecast_stage_id',
                               string='Lignes de consommation')
    weekly_amount = fields.Float('Montant hebdo', compute='_compute_weekly_amount', store=True)
    global_amount = fields.Float('Montant global', compute='_compute_global_amount', store=True)

    @api.one
    @api.depends('line_ids.weekly_amount')
    def _compute_weekly_amount(self):
        self.weekly_amount = sum(line.weekly_amount for line in self.line_ids)

    @api.one
    @api.depends('line_ids.global_amount')
    def _compute_global_amount(self):
        self.global_amount = sum(line.global_amount for line in self.line_ids)
