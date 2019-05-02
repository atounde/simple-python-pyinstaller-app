# -*- coding: utf-8 -*-
from odoo import models

class PriceSurveyReport(models.AbstractModel):
    _name = 'report.report_xlsx.price_survey_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, survey):
        for object in survey:
            row = 2
            col = 0
            sheet = workbook.add_worksheet()
            bg_color = workbook.add_format()
            bg_color.set_bg_color('yellow')
            sheet.set_column('A:A', 30)
            sheet.set_column('B:B', 20)
            sheet.set_column('C:C', 20)
            sheet.set_column('D:D', 20)
            sheet.set_column('E:E', 20)
            headers = ['Ressource','Quantité','Prix unitaire', 'Prix Total']
            content = []
            for stage in object.stages:
                sheet.write(row, col, stage.name, bg_color)
                for head in headers:
                    col+=1
                    sheet.write(row, col, head)
                col = 0
                row+=1
                for value in stage.line_ids:
                    format_currency = workbook.add_format({'num_format': '#,##0'})
                    col+=1
                    sheet.write(row, col, str(value.name.name))
                    col+=1
                    sheet.write(row, col, value.quantity, format_currency)
                    col+=1
                    sheet.write(row, col, value.unit_price, format_currency)
                    col+=1
                    sheet.write(row, col, value.price_total, format_currency)
                    col = 0
                    row+=1
                row+=1
                align = workbook.add_format({'align':'center','valign':'vcenter'})
                labels = ["TOTAL", "Marge "+ str(stage.profit_margin_rate) + "%", "Prix de vente"]
                for label in labels:
                    range = "B{0}:D{0}".format(row)
                    sheet.merge_range(range, label, align)
                    row+=1
                row-=1
                selling_price_style = workbook.add_format({'num_format': '#,##0'})
                selling_price_style.set_bg_color('yellow')
                sheet.write('E'+ str(row), stage.selling_price, selling_price_style)
                row-=2
                sheet.write('E'+ str(row), stage.price_total, format_currency)
                row+=1
                sheet.write('E'+ str(row), stage.selling_price - stage.price_total, format_currency)
                row+=4