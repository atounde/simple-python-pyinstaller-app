# -*- coding: utf-8 -*-
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
{
    "name": "BTP Price Survey",
    "version": "10.0",
    "author": "Baamtu SARL",
    "description": """BTP price survey module for shared features
    """,
    "website": "http://www.baamtu.com",
    "depends": ['construction_site'],
    "category": "BTP",
    "data": [
        'security/ir.model.access.csv',
        'data/price_survey_data.xml',
        'wizard/generate_quotation_view.xml',
        'views/stage_category_view.xml',
        'views/analytical_account_view.xml',
        'views/stage_line_view.xml',
        'views/stage_view.xml',
        'views/quotation_line_view.xml',
        'views/quotation_line_category_view.xml',
        'views/quotation_view.xml',
        'views/price_survey_view.xml',
        'views/price_servey_template_view.xml',
        'views/evaluation_line_view.xml',
        'views/forecast_view.xml',
        'wizard/generate_forecast_view.xml',
        'views/execution_view.xml',
        'wizard/generate_execution_view.xml',
        'views/consumption_forecast_stage_line_view.xml',
        'views/consumption_forecast_stage_view.xml',
        'views/consumption_forecast_view.xml',
        'views/consumption_execution_stage_line_view.xml',
        'views/consumption_execution_stage_view.xml',
        'views/consumption_execution_view.xml',
        'views/stage_line_template_view.xml',
        'views/stage_template_view.xml',
        'views/company_inherit_view.xml',
        'reports/price_survey_report_view.xml',
        'reports/quotation_report_view.xml',
    ],
    "demo": [],
    'test': [],
    'installable': True
}