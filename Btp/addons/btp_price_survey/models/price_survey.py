# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

class PriceSurvey(models.Model):
    _name = 'btp_price_survey.price_survey'
    _description = "Étude de prix"
    _order = "id desc"

    @api.one
    @api.depends('construction_site.name', 'number')
    def _compute_name(self):
        report_obj = self.env['ir.actions.report']
        report = report_obj.search([('model', '=', "btp_price_survey.price_survey")])
        now = datetime.now().strftime("%d_%m_%Y")
        report.write({'name':str(self.construction_site.name) + "_ETUDE_DE_PRIX_" + str(now)})
        if self.construction_site and self.number:
            self.name = self.construction_site.name + " " + self.number

    name = fields.Char(string="Nom", compute='_compute_name', store=True)
    construction_site = fields.Many2one('construction_site.construction_site', string="Chantier", copy=False)
    profit_margin_rate = fields.Many2one("construction.settings", string='Marge bénéficiaire')
    stages = fields.One2many('btp_price_survey.stage', 'price_survey', string="Étapes", copy=True)
    number = fields.Char('Numéro', readonly=True)

    _sql_constraints = [
        ('construction_site_uniq', 'unique(construction_site)',
         "Une étude de prix a déjà été créée pour le chantier sélectionné.\n Veuillez corriger pour continuer!"),
    ]

    @api.model
    def create(self, vals):
        vals['number'] = self.env['ir.sequence'].next_by_code('btp_price_survey.price_survey')
        price_survey = super(PriceSurvey, self).create(vals)
        return price_survey