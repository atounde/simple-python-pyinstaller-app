# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SmallMaterial(models.Model):
    _name = 'btp_base.resource.small_material'
    _inherit = 'btp_base.resource'
    _description = 'Petit matériel'


    @api.model
    def _get_default_type(self):
        return 'small_material'

    type = fields.Selection(default=_get_default_type)
    mark = fields.Char('Marque')
    year_of_purchase = fields.Char("Année d'acquisition")
