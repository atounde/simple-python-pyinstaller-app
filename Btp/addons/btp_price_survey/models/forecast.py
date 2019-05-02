# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Forecast(models.Model):
    _name = 'btp_price_survey.forecast'
    _inherit = 'btp_price_survey.abstract_evaluation'

    line_ids = fields.One2many('btp_price_survey.abstract_evaluation.line', 'forecast_id',
                               string="Lignes de prévision hebdomadaire", readonly=True,
                               states={'draft': [('readonly', False)], 'is_running': [('readonly', False)]})

    @api.multi
    def generate_consumption_forecast(self):
        for forecast in self:
            if forecast:
                running_consumption_forecast = self.env['btp_price_survey.consumption_forecast'].search(
                    [('construction_site_id', '=', self.construction_site_id.id), ('state', '=', 'is_running')])
                if running_consumption_forecast:
                    raise ValidationError(
                        "Attention, ce chantier a une prévision de consommation en cours\n Veuillez la terminer pour continuer!.")
                consumption_forecast_id = self.env['btp_price_survey.consumption_forecast'].create({
                    'construction_site_id': forecast.construction_site_id.id,
                    'planned_start_date': forecast.planned_start_date,
                    'planned_end_date': forecast.planned_end_date,
                })
                evaluation_lines = self.env['btp_price_survey.abstract_evaluation.line'].search(
                    [('forecast_id', '=', self.id)])
                for evaluation in evaluation_lines:
                    consumption_forecast_stage_id = self.env['btp_price_survey.consumption_forecast.stage'].create({
                        'name': evaluation.stage_id.id,
                        'consumption_forecast_id': consumption_forecast_id.id,
                    })
                    price_survey_stages = self.env['btp_price_survey.price_survey'].search(
                        [('construction_site', '=', forecast.construction_site_id.id)]).stages
                    for price_survey_stage in price_survey_stages:
                        if price_survey_stage.id == consumption_forecast_stage_id.name.id:
                            for line in price_survey_stage.line_ids:
                                self.env['btp_price_survey.consumption_forecast.stage.line'].create({
                                    'resource_category_id': line.name.id,
                                    'consumption_forecast_stage_id': consumption_forecast_stage_id.id,
                                })
        return {

            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_id': consumption_forecast_id.id,
            'res_model': 'btp_price_survey.consumption_forecast'
        }
