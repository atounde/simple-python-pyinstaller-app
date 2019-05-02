# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class GenerateEvaluation(models.TransientModel):
    _name = 'btp_price_survey.generate_forecast'

    construction_site_id = fields.Many2one('construction_site.construction_site', string='Chantier', required=True)
    planned_start_date = fields.Date(string="Date de début", required=True)
    planned_end_date = fields.Date(string="Date de Fin", required=True)

    @api.multi
    def generate_forecast(self):
        running_forecast = self.env['btp_price_survey.forecast'].search(
            [('construction_site_id', '=', self.construction_site_id.id), ('state', '=', 'is_running')])
        if running_forecast:
            raise ValidationError(
                "Attention, ce chantier a une prévision en cours\n Veuillez la terminer pour continuer!.")
        price_survey_obj = self.env['btp_price_survey.price_survey'].search(
            [('construction_site', '=', self.construction_site_id.id)])
        forecast_id = self.env['btp_price_survey.forecast'].create({
            'construction_site_id': self.construction_site_id.id,
            'planned_start_date': self.planned_start_date,
            'planned_end_date': self.planned_end_date,
        })
        for stage in price_survey_obj.stages:
            self.env['btp_price_survey.abstract_evaluation.line'].create({
                'forecast_id': forecast_id.id,
                'stage_id': stage.id,
                'unit_price': stage.price_total
            })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_id': forecast_id.id,
            'res_model': 'btp_price_survey.forecast'
        }