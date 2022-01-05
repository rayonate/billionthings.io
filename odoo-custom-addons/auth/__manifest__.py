# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Auth',
    'version': '1.0',
    'summary': 'Billiothings',
    'sequence': 10,
    'description': """Billiothings""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com/app/billing',
    'images': ['images/accounts.jpeg', 'images/bank_statement.jpeg', 'images/cash_register.jpeg', 'images/chart_of_accounts.jpeg', 'images/customer_invoice.jpeg', 'images/journal_entries.jpeg'],
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/website_form.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'auth/static/css/auth.css',
            'auth/static/js/auth.js',
        ], },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '',
    'assets': {},
    'license': 'LGPL-3',
}
