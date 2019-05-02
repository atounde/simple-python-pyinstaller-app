# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ConsumptionForecast(models.Model):
    _name = 'btp_price_survey.consumption_forecast'
    _inherit = 'btp_price_survey.abstract_evaluation'

    stage_ids = fields.One2many('btp_price_survey.consumption_forecast.stage', 'consumption_forecast_id',
                                string='Étapes', readonly=True,
                                states={'draft': [('readonly', False)], 'is_running': [('readonly', False)]})
