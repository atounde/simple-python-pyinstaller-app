# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PointingStageTemporaryStaff(models.Model):
    _name = 'btp_pointing.pointing.stage.temporary_staff'

    name = fields.Many2one('btp_base.temporary_staff', string='Nom', required=True)
    category = fields.Many2one(related='name.category', string='Catégorie', required=True)
    task = fields.Char('Tâche effectuée')
    pointing_stage_id = fields.Many2one('btp_pointing.pointing.stage',
                                        string="Étape de pointages")
