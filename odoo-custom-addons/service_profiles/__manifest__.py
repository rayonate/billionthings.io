# -*- coding: utf-8 -*-
{
    'name': "Service Profiles",

    'summary': """
        Service Profiles of the service providers
        """,

    'description': """
        Service Profiles of the service providers
    """,

    'author': "Billionthings.io",
    'website': "http://billiothings.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/service_profile.xml',
        'views/web/create_service_profile.xml'

        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '',
    'license': 'LGPL-3',
}
