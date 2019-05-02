# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime, date


class Pointing(models.Model):
    _name = 'btp_pointing.pointing'

    @api.one
    @api.depends('construction_site_id.name', 'date')
    def _compute_name(self):
        if self.construction_site_id and self.date:
            self.name = "Pointages " + (self.construction_site_id.name).lower() + " du " + datetime.strptime(self.date,
                                                                                                             '%Y-%m-%d').strftime(
                '%d-%m-%Y')

    name = fields.Char(string="Nom", compute='_compute_name', store=True)
    date = fields.Date(string='Date', required=True, default=date.today())
    construction_site_id = fields.Many2one('construction_site.construction_site', string='Chantier', required=True)
    stage_ids = fields.One2many('btp_pointing.pointing.stage', 'pointing_id',
                                string="Étapes de pointages")

    _sql_constraints = [
        ('name_uniq', 'unique(name)',
         "Le nom doit être unique.\n Veuillez corriger pour continuer!"),
    ]
