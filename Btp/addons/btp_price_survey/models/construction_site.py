# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ConstructionSite(models.Model):
    _name = 'construction_site.construction_site'
    _inherit = 'construction_site.construction_site'

    executed_budget = fields.Float(compute='_compute_executed_budget', string="Budjet executé")
    execution_rate = fields.Float(string="Taux d'execution", compute="_taux")

    @api.one
    def _compute_executed_budget(self):
        execution_obj = self.env['btp_price_survey.execution'].search(
            [('construction_site_id.id', '=', self.id),('state', 'in', ['is_running','close'])], limit=1, order='id desc')
        self.executed_budget = execution_obj.executed_budget if execution_obj else 0

    @api.one
    @api.depends('estimated_budget', 'executed_budget')
    def _taux(self):
        if self.estimated_budget != 0:
            self.execution_rate = float(self.executed_budget * 100) / self.estimated_budget
