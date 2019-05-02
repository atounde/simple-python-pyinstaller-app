# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Material(models.Model):
    _name = 'btp_base.resource.material'
    _inherit = 'btp_base.resource'
    _description = 'Matériau'


    @api.model
    def _get_default_type(self):
        return 'material'

    type = fields.Selection(default=_get_default_type)
