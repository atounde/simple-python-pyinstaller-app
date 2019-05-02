# -*- coding: utf-8 -*-
from odoo import models

class QuotationReport(models.AbstractModel):
    _name = 'report.report_xlsx.quotation_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, quotations):
        for object in quotations:
            row_index = 2
            col_index = 0
            sheet = workbook.add_worksheet()
            bold_style = workbook.add_format()
            bold_style.set_border()
            bold_style.set_bold()
            sheet.set_column('A:A', 30)
            sheet.set_column('B:B', 20)
            sheet.set_column('C:C', 20)
            sheet.set_column('D:D', 20)
            sheet.set_column('E:E', 30)
            sheet.set_column('F:F', 30)
            align_style = workbook.add_format({'align':'center','valign':'vcenter'})
            align_style.set_bold()
            align_style.set_border(1)
            border_style = workbook.add_format()
            border_style.set_border(1)
            headers = ['N°','DESIGNATION','UNITE', 'QUANTITE RETENUE', 'Prix unitaire (FCFA) HTVA', 'Prix total (FCFA) HTVA']
            doc_title = "DEVIS QUANTITATIF ET ESTIMATIF " + str(object.name.name)
            range_title = "A{0}:F{0}".format(row_index)
            sheet.merge_range(range_title, doc_title, align_style)
            col_index = 0
            row_index+=1
            for head in headers: 
                sheet.write(row_index, col_index, head, bold_style)
                col_index+=1
            row_index+=1
            col_index = 0
            for category in object.lines_categories:
                sheet.write(row_index, col_index, category.analytical_account_mane, bold_style)
                col_index+=1
                stage_name = str(category.name.name)
                sheet.write(row_index, col_index, stage_name.upper(), bold_style)
                compteur_range = list(range(3, 7))
                col_index+=1
                for col in compteur_range:
                    sheet.write(row_index, col_index, " ", border_style)
                    col_index+=1
                row_index+=1
                col_index=0
                lines = []
                for quotation_line in category.quotation_lines:
                    lines = [quotation_line.analytical_account.name, quotation_line.name.name, quotation_line.unit.name, quotation_line.quantity] 
                    format_currency = workbook.add_format({'num_format': '#,##0'})
                    format_currency.set_border(1)
                    for line in lines:
                        sheet.write(row_index, col_index, line, border_style)
                        col_index+=1
                    sheet.write(row_index, col_index, quotation_line.unit_price, format_currency)
                    col_index+=1
                    sheet.write(row_index, col_index, quotation_line.total_price, format_currency)
                    row_index+=1
                    col_index=0
                row_index+=1
                stage_total = "TOTAL " + stage_name.upper()
                range_total = "A{0}:B{0}".format(row_index)
                align_style = workbook.add_format({'align':'left'})
                align_style.set_border(1)
                align_style.set_bold()
                sheet.merge_range(range_total, stage_total, align_style)
                total_style = workbook.add_format({'num_format': '#,##0'})
                total_style.set_bold()
                total_style.set_border(1)
                sheet.write('F'+ str(row_index), category.total_price, total_style)
                col_index=0
            row_index+=1
            align_style = workbook.add_format({'align':'center','valign':'vcenter'})
            align_style.set_bold()
            align_style.set_border()
            labels = ["TOTAL HTVA", "TVA "+ str(object.tax) + "%", "TOTAL TTC"]
            for label in labels:
                range_label = "A{0}:E{0}".format(row_index)
                sheet.merge_range(range_label, label, align_style)
                row_index+=1
            row_index-=3
            sheet.write('F'+ str(row_index), quotations.amount_untaxed, format_currency)
            row_index+=1
            tva = quotations.amount_taxed - quotations.amount_untaxed
            sheet.write('F'+ str(row_index), tva, format_currency)
            row_index+=1
            sheet.write('F'+ str(row_index), quotations.amount_taxed, format_currency)