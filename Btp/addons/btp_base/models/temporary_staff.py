# -*- coding: utf-8 -*-
from odoo import models, fields, api


class TemporaryStaff(models.Model):
    _name = 'btp_base.temporary_staff'
    _inherit = 'btp_base.resource'

    @api.model
    def _get_default_type(self):
        return 'temporary_staff'

    code = fields.Char('Code', copy=False, size=16)
    type = fields.Selection(default=_get_default_type)

    _sql_constraints = [
        ('code_uniq', 'unique(code)', "Ce code existe déjà.\n Veuillez choisir un autre code pour continuer!"),
    ]

    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('btp_base.temporary_staff')
        temporary_staff = super(TemporaryStaff, self).create(vals)
        return temporary_staff