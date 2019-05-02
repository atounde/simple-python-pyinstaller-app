# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Execution(models.Model):
    _name = 'btp_price_survey.execution'
    _inherit = 'btp_price_survey.abstract_evaluation'

    line_ids = fields.One2many('btp_price_survey.abstract_evaluation.line', 'execution_id',
                               string="Ligne de suivi hebdomadaire du chantier", readonly=True,
                               states={'draft': [('readonly', False)], 'is_running': [('readonly', False)]})
    executed_budget = fields.Float(string="Budget exécuté",
                                   readonly=True,
                                   states={'draft': [('readonly', False)], 'is_running': [('readonly', False)]})

    @api.onchange('line_ids')
    def _onchange_executed_budget(self):
        if self.line_ids:
            self.executed_budget = sum(line.global_amount for line in self.line_ids if line.execution_id)

    @api.multi
    def generate_consumption_execution(self):
        for execution in self:
            if execution:
                running_consumption_execution = self.env['btp_price_survey.consumption_execution'].search(
                    [('construction_site_id', '=', execution.construction_site_id.id), ('state', '=', 'is_running')])
                if running_consumption_execution:
                    raise ValidationError(
                        "Attention, ce chantier a une consommation en cours\n Veuillez la terminer pour continuer!.")
                consumption_execution_id = self.env['btp_price_survey.consumption_execution'].create({
                    'construction_site_id': execution.construction_site_id.id,
                    'planned_start_date': execution.planned_start_date,
                    'planned_end_date': execution.planned_end_date,
                })
                evaluation_lines = self.env['btp_price_survey.abstract_evaluation.line'].search(
                    [('execution_id', '=', self.id)])
                for evaluation in evaluation_lines:
                    consumption_execution_stage_id = self.env['btp_price_survey.consumption_execution.stage'].create({
                        'name': evaluation.stage_id.id,
                        'consumption_execution_id': consumption_execution_id.id,
                    })
                    price_survey_stages = self.env['btp_price_survey.price_survey'].search(
                        [('construction_site', '=', execution.construction_site_id.id)]).stages
                    for price_survey_stage in price_survey_stages:
                        if price_survey_stage.id == consumption_execution_stage_id.name.id:
                            for line in price_survey_stage.line_ids:
                                self.env['btp_price_survey.consumption_execution.stage.line'].create({
                                    'resource_category_id': line.name.id,
                                    'consumption_execution_stage_id': consumption_execution_stage_id.id,
                                })
        return {

            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_id': consumption_execution_id.id,
            'res_model': 'btp_price_survey.consumption_execution'
        }
