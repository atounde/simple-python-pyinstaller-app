# -*- coding: utf-8 -*-
from odoo import models, fields, api


class TemporaryStaffForConstructionSite(models.Model):
    _name = 'btp_pointing.temporary_staff_for_construction_site'

    name = fields.Many2one('btp_base.temporary_staff', string='Nom')
    category = fields.Many2one(related='name.category', string='Catégorie')
    construction_site_id = fields.Many2one('construction_site.construction_site', string='Chantier')
