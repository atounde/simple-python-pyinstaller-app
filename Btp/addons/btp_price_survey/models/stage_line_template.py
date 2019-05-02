# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StageLineTemplate(models.Model):
    _name = 'btp_price_survey.template.stage.line'

    stage_id = fields.Many2one('btp_price_survey.template.stage', string="Étape")

class Machine(models.Model):
    _name = 'btp_price_survey.template.machine'
    _inherit = 'btp_price_survey.template.stage.line'
    _description = 'Engin'
    
    name = fields.Many2one('btp_base.resource.category', string="Ressources", 
    required=True, domain="[('type', '=', 'machine')]")

class Vehicle(models.Model):
    _name = 'btp_price_survey.template.vehicle'
    _inherit = 'btp_price_survey.template.stage.line'
    _description = 'Véhicule'

    name = fields.Many2one('btp_base.resource.category', string="Ressources", required=True, 
    domain="[('type', '=', 'vehicle')]")
    distance = fields.Many2one('btp_base.company.settings', string="Distance")
    number_of_rotation = fields.Many2one('btp_base.company.settings', string="Nombre de rotation")

class Material(models.Model):
    _name = 'btp_price_survey.template.material'
    _inherit = 'btp_price_survey.template.stage.line'
    _description = 'Matériau'
    
    name = fields.Many2one('btp_base.resource.category', string="Ressources", 
    required=True, domain="[('type', '=', 'material')]")

class SmallMaterial(models.Model):
    _name = 'btp_price_survey.template.small_material'
    _inherit = 'btp_price_survey.template.stage.line'
    _description = 'Petit matériel'
    
    name = fields.Many2one('btp_base.resource.category', string="Ressources", 
    required=True, domain="[('type', '=', 'small_material')]")

class TemporaryStaff(models.Model):
    _name = 'btp_price_survey.template.temporary_staff'
    _inherit = 'btp_price_survey.template.stage.line'
    _description = 'Personnel temporaire'
    
    name = fields.Many2one('btp_base.resource.category', string="Ressources", 
    required=True, domain="[('type', '=', 'temporary_staff')]")

class Misc(models.Model):
    _name = 'btp_price_survey.template.misc'
    _inherit = 'btp_price_survey.template.stage.line'
    _description = 'Divers'
    
    name = fields.Many2one('btp_base.resource.category', string="Ressources", 
    required=True, domain="[('type', '=', 'misc')]")

