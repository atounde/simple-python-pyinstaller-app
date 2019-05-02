# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ConstructionSettings(models.Model):
    _name = "construction.settings"
     
    setting_id = fields.Many2one("btp_base.company.settings",
                                    string="Libellé",
                                    ondelete="cascade")
    construction_id = fields.Many2one("construction_site.construction_site",
                                    string="Chantier", 
                                    ondelete="cascade", 
                                    readonly=True)
    settings_value = fields.Float(string="Valeur")
    number_rotation = fields.Integer(string="Nombre de rotation / J")
    name = fields.Char(related="setting_id.name", readonly=True)
    sql_constraints = [('unique_settings','UNIQUE(name)',"Les paramètres doivent être unique"),
    ]


class ConstructionsCompanySettings(models.Model):
    _inherit = "construction_site.construction_site"

    def get_default_setting(self):
        company_user_id = self.env.user.company_id.id
        settings_env = self.env['btp_base.company.settings'].search([('company_id','=',company_user_id)])
        settings_values = []
        for setting in settings_env:
            settings_values.append({'name':setting.name, 'setting_id':setting.id})
        return settings_values
    
    settings_ids = fields.One2many ("construction.settings", 
                                    "construction_id", 
                                    default=get_default_setting,
                                    string="Paramètres initiaux", 
                                    ondelete="cascade")
