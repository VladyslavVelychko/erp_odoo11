# -*- coding: utf-8 -*-
{
    'name': "Website persons",
    'summary': """New persons from website""",
    'author': "Vladyslav Velychko",
    'contributors': [
        "Vladyslav Velychko <velyk95@gmail.com>",
    ],
    'website': "https://www.upwork.com/o/profiles/users/_~01dd5450be8c435142/",
    'category': 'Website',
    'version': '0.1.0',
    'depends': [
        'base',
        'website'
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
