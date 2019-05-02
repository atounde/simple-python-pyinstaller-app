# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Vehicle(models.Model):
    _name = 'btp_base.resource.vehicle'
    _inherit = 'btp_base.resource'
    _description = 'Véhicule'

    @api.model
    def _get_default_type(self):
        return 'vehicle'

    owner_id = fields.Many2one('res.partner', required=True, ondelete='restrict', string='Propriétaire')
    code = fields.Char(string="Numéro", required=True)
    type = fields.Selection(default=_get_default_type)
    mark = fields.Char('Marque')
    year_of_purchase = fields.Char("Année d'acquisition")

    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Le code du véhicule doit être unique!'),
    ]
