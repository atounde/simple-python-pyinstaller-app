# -*- coding: utf-8 -*-
from odoo import models, fields, api

TYPES = [
    ('machine', 'Engin'),
    ('vehicle', 'Véhicule'),
    ('material', 'Matériau'),
    ('small_material', 'Petit matériel'),
    ('temporary_staff', 'Personnel temporaire'),
    ('misc', 'Divers'),
]


class Resource(models.Model):
    _name = 'btp_base.resource'
    _description = "Ressource"
    _order = "id desc"

    name = fields.Char(string="Nom", required=True)
    unit = fields.Many2one('btp_base.resource.unit', string="Unité", required=True)
    price = fields.Integer(string="Tarif", required=True)
    type = fields.Selection(TYPES, string='Type', required=True)
    category = fields.Many2one('btp_base.resource.category', string="Catégorie", required=True)

    @api.onchange('category')
    def _onchange_category(self):
        if self.category:
            self.unit = self.category.unit.id
            self.price = self.category.price


class ResourceUnit(models.Model):
    _name = 'btp_base.resource.unit'
    _description = "Unité"
    _order = "id desc"

    name = fields.Char(string="Nom", required=True)


class ResourceCategory(models.Model):
    _name = 'btp_base.resource.category'
    _description = "Catégorie"
    _order = "id desc"

    name = fields.Char(string="Nom", required=True)
    type = fields.Selection(TYPES, string='Type', required=True)
    unit = fields.Many2one('btp_base.resource.unit', string="Unité", required=True)
    fuel = fields.Many2one('btp_base.resource.category', string="Carburant", domain="[('type', '=', 'material')]")
    price = fields.Integer(string="Tarif", required=True)
    hourly_cost = fields.Float('Consommation horaire', default=0)
    number_of_rotation = fields.Float('Nombre de rotation', default=0)
    consumption_in_hundred = fields.Float('Consommation au cent', default=0)

    @api.onchange('type')
    def _onchange_hourly_cost(self):
        if self.type != 'machine':
            self.hourly_cost = 0

    @api.onchange('type')
    def _onchange_number_of_rotation(self):
        if self.type != 'vehicle':
            self.number_of_rotation = 0
            self.consumption_in_hundred = 0

