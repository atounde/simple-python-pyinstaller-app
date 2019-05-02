# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Misc(models.Model):
    _name = 'btp_base.resource.misc'
    _inherit = 'btp_base.resource'
    _description = 'Divers'

    @api.model
    def _get_default_type(self):
        return 'misc'

    type = fields.Selection(default=_get_default_type)
