# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ConsumptionExecutionLine(models.Model):
    _name = 'btp_price_survey.consumption_execution.stage.line'
    _inherit = 'btp_price_survey.weekly_planning'

    resource_category_id = fields.Many2one('btp_base.resource.category', string='Ressources', required=True)
    unit = fields.Many2one(related='resource_category_id.unit', string='Unité')
    unit_price = fields.Integer(related='resource_category_id.price', string='Prix unitaire')
    consumption_execution_stage_id = fields.Many2one('btp_price_survey.consumption_execution.stage',
                                                     string='Étape de prévision', ondelete="cascade")
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
    @api.depends('resource_category_id', 'weekly_quantity')
    def _compute_global_quantity(self):
        consumption_execution = self.env['btp_price_survey.consumption_execution'].search(
            [('construction_site_id', '=',
              self.consumption_execution_stage_id.consumption_execution_id.construction_site_id.id),
             ('state', '=', 'close')], limit=1, order='id desc')
        if consumption_execution:
            last_consumption_stage = False
            for consumption_execution_stage in consumption_execution.stage_ids:
                if consumption_execution_stage.name == self.consumption_execution_stage_id.name:
                    last_consumption_stage = consumption_execution_stage
            if last_consumption_stage:
                for line in last_consumption_stage.line_ids:
                    if line.resource_category_id == self.resource_category_id:
                        self.global_quantity = line.global_quantity + self.weekly_quantity
        else:
            self.global_quantity = self.weekly_quantity

    @api.one
    @api.depends('global_quantity', 'unit_price')
    def _compute_global_amount(self):
        self.global_amount = self.unit_price * self.global_quantity
