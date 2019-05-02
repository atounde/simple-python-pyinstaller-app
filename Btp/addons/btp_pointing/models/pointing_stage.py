# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PointingStage(models.Model):
    _name = 'btp_pointing.pointing.stage'

    name = fields.Many2one('btp_price_survey.stage', string='Nom', required=True)
    analytical_account = fields.Char(related='name.analytical_account_mane', string='N° compte analytique')
    pointing_id = fields.Many2one('btp_pointing.pointing',
                                  string="Pointage")
    line_ids = fields.One2many('btp_pointing.pointing.stage.temporary_staff', 'pointing_stage_id',
                               string="Lignes de pointages")
