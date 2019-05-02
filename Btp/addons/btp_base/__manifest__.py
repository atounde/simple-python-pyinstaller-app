# -*- coding: utf-8 -*-
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
{
    "name": "BTP base",
    "version": "12.0",
    "author": "Baamtu SARL",
    "description": """BTP base module for shared features
    """,
    "website": "http://www.baamtu.com",
    "depends": ['base'],
    "category": "BTP",
    "data": [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/resource_view.xml',
        'views/machine_view.xml',
        'views/vehicle_view.xml',
        'views/owner_view.xml',
        'views/profession_view.xml',
        'views/sequence_view.xml',
        'views/permanent_staff_view.xml',
        'views/material_view.xml',
        'views/small_material_view.xml',
        'views/misc_view.xml',
        'views/temporary_staff_view.xml',
        'views/company_settings.xml',
    ],
    "demo" : [],
    'test': [],
    'installable': True
}