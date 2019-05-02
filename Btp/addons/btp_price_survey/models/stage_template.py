# -*- coding: utf-8 -*-
from odoo import models, fields, api


class StageTemplate(models.Model):
    _name = 'btp_price_survey.template.stage'
    _description = "Template étape"
    _order = "id desc"

    name = fields.Char('Nom', required="True")
    machine_ids = fields.One2many('btp_price_survey.template.machine', 'stage_id', string="Engins", copy=True)
    vehicle_ids = fields.One2many('btp_price_survey.template.vehicle', 'stage_id', string="Véhicules", copy=True)
    material_ids = fields.One2many('btp_price_survey.template.material', 'stage_id', string="Matériaux", copy=True)
    small_material_ids = fields.One2many('btp_price_survey.template.small_material', 'stage_id',
                                         string="Petits matériels", copy=True)
    temporary_staff_ids = fields.One2many('btp_price_survey.template.temporary_staff', 'stage_id',
                                          string="Personnel temporaire", copy=True)
    misc_ids = fields.One2many('btp_price_survey.template.misc', 'stage_id', string="Divers", copy=True)