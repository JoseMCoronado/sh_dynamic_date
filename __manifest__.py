# -*- coding: utf-8 -*-
{
    'name': 'Dynamic Date Ranges: Sales, Purchase & Accounting',
    'category': 'Accounting',
    'author': 'GFP Solutions',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
This custom module for Odoo Enterprise (Online/On Premise) creates a set number of dynamic date ranges
for the Accounting, Sales, and Purchases modules.

Accounting: Based on date_due
Sales: Based on date_order
Purchase: Based on date_order

THIS MODULE IS PROVIDED AS IS - INSTALLATION AT USERS' OWN RISK - AUTHOR OF MODULE DOES NOT CLAIM ANY
RESPONSIBILITY FOR ANY BEHAVIOR ONCE INSTALLED.
        """,
    'depends': ['base','account_accountant','purchase'],
    'data': [
        'data/filter_views.xml',
    ],
    'installable': True,
}
