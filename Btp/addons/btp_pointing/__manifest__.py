# -*- coding: utf-8 -*-
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
{
    "name": "BTP Pointing",
    "version": "10.0",
    "author": "Baamtu SARL",
    "description": """BTP pointing module for shared features
    """,
    "website": "http://www.baamtu.com",
    "depends": ['btp_price_survey'],
    "category": "BTP",
    "data": [
        'security/ir.model.access.csv',
        'views/temporary_staff_for_construction_site_view.xml',
        'views/construction_site_view.xml',
        'views/pointing_stage_temporary_staff_view.xml',
        'views/pointing_stage_view.xml',
        'views/pointing_view.xml',
    ],
    "demo": [],
    'test': [],
    'installable': True
}
