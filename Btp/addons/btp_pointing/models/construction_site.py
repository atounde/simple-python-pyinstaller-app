# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ConstructionSite(models.Model):
    _inherit = 'construction_site.construction_site'

    temporary_staff_ids = fields.One2many('btp_pointing.temporary_staff_for_construction_site', 'construction_site_id',
                                          string='Personnel temporaire')

    @api.multi
    def generate_daily_pointing(self):
        for construction in self:
            if construction:
                pointing_id = self.env['btp_pointing.pointing'].create({
                    'construction_site_id': construction.id,
                })
                price_survey = self.env['btp_price_survey.price_survey'].search(
                    [('construction_site', '=', pointing_id.construction_site_id.id)], limit=1,
                    order='id desc')
                for pricesurvey in price_survey:
                    for stage in pricesurvey.stages:
                        pointing_stage_id = self.env[
                            'btp_pointing.pointing.stage'].create({
                            'name': stage.id,
                            'pointing_id': pointing_id.id,
                        })
                        pointing_from_construction_site = self.env[
                            'btp_pointing.temporary_staff_for_construction_site'].search(
                            [('construction_site_id', '=', construction.id)])
                        for staff in pointing_from_construction_site:
                            self.env[
                                'btp_pointing.pointing.stage.temporary_staff'].create({
                                'name': staff.name.id,
                                'pointing_stage_id': pointing_stage_id.id,
                            })

        return {
            'name': 'Pointages',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_id': pointing_id.id,
            'res_model': 'btp_pointing.pointing'
        }
