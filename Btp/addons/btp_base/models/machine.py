# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Machine(models.Model):
    _name = 'btp_base.resource.machine'
    _inherit = 'btp_base.resource'
    _description = 'Engin'

    @api.model
    def _get_default_type(self):
        return 'machine'

    owner_id = fields.Many2one('res.partner', required=True, ondelete='restrict', string='Propriétaire')
    code = fields.Char(string="Code", required=True)
    type = fields.Selection(default=_get_default_type)
    mark = fields.Char('Marque')
    year_of_purchase = fields.Char("Année d'acquisition")

    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Le code de l\'engin doit être unique!'),
    ]
