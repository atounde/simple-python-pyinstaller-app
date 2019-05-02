# -*- coding: utf-8 -*-
from odoo import models, fields, api


class QuotationWizard(models.TransientModel):
    _name = 'quotation.wizard'

    tax = fields.Float(string='TVA')

    @api.multi
    def generate_quotation(self):
        quotation_categories = {}
        price_survey = self.env['btp_price_survey.price_survey'].browse(self._context.get('active_ids'))
        if price_survey:
            quotation_id = self.env['btp_price_survey.quotation'].create({
                'name': price_survey.construction_site.id,
                'tax': self.tax
            })
            stage_categories = self.env['btp_price_survey.stage.category'].search([])
            for stage_category in stage_categories:
                stage_list = []
                for stage in price_survey.stages:
                    if stage.category == stage_category:
                        stage_list.append(stage)
                quotation_categories[stage_category] = stage_list
            for category, stages in list(quotation_categories.items()):
                quotation_lines = []
                if stages:
                    for stage in stages:
                        quotation_line_vals = {
                            'name': stage.id,
                            'unit_price': stage.selling_price
                        }
                        quotation_lines.append((0, 0, quotation_line_vals))
                    self.env['btp_price_survey.quotation.line.category'].create({
                        'name': category.id,
                        'quotation_lines': quotation_lines,
                        'quotation_id': quotation_id.id
                    })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_id': quotation_id.id,
            'res_model': 'btp_price_survey.quotation'
        }
