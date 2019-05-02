# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StageLine(models.Model):
    _name = 'btp_price_survey.stage.line'

    name = fields.Many2one('btp_base.resource.category', string="Ressource", required=True)
    quantity = fields.Float(string='Quantité', default=1)
    fuel_quantity = fields.Integer('Quantité carburant/j', compute='_compute_fuel_quantity', store=True)
    performance = fields.Float('Rendement/j', default=1)
    fuel_price = fields.Float('Prix Carburant')
    duration = fields.Integer('Durée/h', default=8)
    unit_price = fields.Float(string="Prix unitaire", compute='_compute_unit_price', store=True)
    price_total = fields.Float(string='Total', compute='_compute_price_total', store=True)
    stage_id = fields.Many2one('btp_price_survey.stage', string="Etape")

    @api.one
    @api.depends('name.price', 'fuel_price', 'fuel_quantity', 'performance')
    def _compute_unit_price(self):
        self.unit_price = (self.name.price + self.fuel_price * self.fuel_quantity) / self.performance \
            if self.performance != 0 else 0

    @api.one
    @api.depends('name.hourly_cost')
    def _compute_fuel_quantity(self):
        self.fuel_quantity = self.name.hourly_cost * self.duration

    @api.one
    @api.depends('unit_price', 'quantity')
    def _compute_price_total(self):
        self.price_total = self.unit_price * self.quantity

    @api.onchange('name')
    def _onchange_fuel_price(self):
        self.fuel_price = self.name.fuel.price if self.name.type == 'machine' or self.name.type == 'vehicle' else 0

    @api.one
    @api.constrains('performance')
    def _check_is_valid_performance(self):
        if self.performance <= 0:
            raise ValidationError("Attention, le rendement de la ressource doit être strictement positif.")

    @api.one
    @api.constrains('quantity')
    def _check_is_valid_quantity(self):
        if self.quantity <= 0:
            raise ValidationError("Attention, la quantité de la ressource doit être strictement positive.")
