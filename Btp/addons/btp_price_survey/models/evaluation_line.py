# -*- coding: utf-8 -*-
from odoo import models, fields, api


class EvaluationLineBtp(models.Model):
    _name = 'btp_price_survey.abstract_evaluation.line'
    _inherit = 'btp_price_survey.weekly_planning'

    stage_id = fields.Many2one('btp_price_survey.stage', string='Étape')
    execution_id = fields.Many2one('btp_price_survey.execution', string='Suivi de chantier', ondelete="cascade")
    forecast_id = fields.Many2one('btp_price_survey.forecast', string='Prévision', ondelete="cascade")
    analytical_account = fields.Many2one(related='stage_id.analytical_account', string='N° compte analytique')
    unit = fields.Many2one(related='stage_id.unit', string='Unité')
    unit_price = fields.Float('Prix unitaire')
    weekly_quantity = fields.Float('Qté hebdo', compute='_compute_weekly_quantity', store=True)
    weekly_amount = fields.Float('Mnt hebdo', compute='_compute_weekly_amount', store=True)
    global_quantity = fields.Float('Qté globale', compute='_compute_global_quantity', store=True)
    global_amount = fields.Float('Mnt global', compute='_compute_global_amount', store=True)

    @api.one
    @api.depends('monday_quantity', 'tuesday_quantity', 'wednesday_quantity', 'thursday_quantity', 'friday_quantity',
                 'saturday_quantity', 'sunday_quantity')
    def _compute_weekly_quantity(self):
        self.weekly_quantity = self.monday_quantity + self.tuesday_quantity + self.wednesday_quantity + self.thursday_quantity + self.friday_quantity + self.saturday_quantity + self.sunday_quantity

    @api.one
    @api.depends('weekly_quantity', 'unit_price')
    def _compute_weekly_amount(self):
        self.weekly_amount = self.unit_price * self.weekly_quantity

    @api.one
    @api.depends('stage_id', 'weekly_quantity')
    def _compute_global_quantity(self):
        evaluation_obj = None
        if self.forecast_id:
            evaluation_obj = self.env['btp_price_survey.forecast'].search(
                [('construction_site_id', '=', self.forecast_id.construction_site_id.id), ('state', '=', 'close')],
                limit=1,
                order='id desc')
        if self.execution_id:
            evaluation_obj = self.env['btp_price_survey.execution'].search(
                [('construction_site_id', '=', self.execution_id.construction_site_id.id), ('state', '=', 'close')],
                limit=1,
                order='id desc')
        if not evaluation_obj:
            self.global_quantity = self.weekly_quantity
        else:
            for line in evaluation_obj.line_ids:
                if line.stage_id == self.stage_id:
                    self.global_quantity = line.global_quantity + self.weekly_quantity

    @api.onchange('stage_id')
    def _onchange_unit_price(self):
        if self.stage_id:
            self.unit_price = self.stage_id.price_total

    @api.one
    @api.depends('global_quantity', 'unit_price')
    def _compute_global_amount(self):
        self.global_amount = self.unit_price * self.global_quantity
