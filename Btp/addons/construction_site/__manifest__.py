# -*- coding: utf-8 -*-
{
    'name': "Construction site",

    'summary': """
      Gestion des chantiers""",
    'description': """
        Ce module permet de faire la gestion des chantiers
    """,
    'author': "Baamtu",
    'website': "http://www.baamtu.com",

    'category': 'BTP',
    'version': '0.1',
    'depends': ['base', 'btp_base'],
    'data': [
        'security/ir.model.access.csv',
	    'views/construction_site_view.xml',
        'views/city_view.xml',
        'views/construction_settings_views.xml',
    ],
}
