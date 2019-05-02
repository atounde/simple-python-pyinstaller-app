# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ConsumptionExecution(models.Model):
    _name = 'btp_price_survey.consumption_execution'
    _inherit = 'btp_price_survey.abstract_evaluation'

    stage_ids = fields.One2many('btp_price_survey.consumption_execution.stage', 'consumption_execution_id',
                                string='Étapes', readonly=True,
                                states={'draft': [('readonly', False)], 'is_running': [('readonly', False)]})

