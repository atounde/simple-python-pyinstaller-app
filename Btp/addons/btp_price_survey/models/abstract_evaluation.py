# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime


class AbstractEvaluationBtp(models.AbstractModel):
    _name = 'btp_price_survey.abstract_evaluation'

    @api.one
    @api.depends('construction_site_id.name', 'planned_start_date', 'planned_end_date')
    def _compute_name(self):
        if self.construction_site_id and self.planned_start_date and self.planned_end_date:
            self.name = self.construction_site_id.name + " du " + datetime.strptime(self.planned_start_date,
                                                                                    '%Y-%m-%d').strftime(
                '%d-%m-%Y') + " au " + datetime.strptime(self.planned_end_date, '%Y-%m-%d').strftime('%d-%m-%Y')

    name = fields.Char(string="Nom", compute='_compute_name', store=True)
    construction_site_id = fields.Many2one('construction_site.construction_site', string='Chantier', required=True,
                                           readonly=True,
                                           states={'draft': [('readonly', False)], 'is_running': [('readonly', False)]})
    planned_start_date = fields.Date(string="Date de début", required=True, readonly=True,
                                     states={'draft': [('readonly', False)], 'is_running': [('readonly', False)]})
    planned_end_date = fields.Date(string="Date de fin", required=True, readonly=True,
                                   states={'draft': [('readonly', False)], 'is_running': [('readonly', False)]})
    estimated_budget = fields.Float(related='construction_site_id.estimated_budget', string="Budget estimé",
                                    readonly=True,
                                    states={'draft': [('readonly', False)], 'is_running': [('readonly', False)]})
    state = fields.Selection([
        ('draft', 'Brouillon'), ('is_running', 'En cours'), ('close', 'Fermé'), ], string='Etat', readonly=True,
        default='draft')

    _sql_constraints = [
        ('name_uniq', 'unique(name)',
         "Le nom doit être unique.\n Veuillez corriger pour continuer!"),
    ]

    @api.multi
    def action_evaluation_running(self):
        self.state = 'is_running'

    @api.multi
    def action_evaluation_close(self):
        self.state = 'close'
