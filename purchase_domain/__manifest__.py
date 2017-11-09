# -*- coding: utf-8 -*-
{
    'name': "purchase_domain",

    'summary': """
        Add domain for purchase order partner_id
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Yurii Khomych",
    'website': "https://github.com/YuriiKhomych/odoo_project",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'purchase'
    ],

    # always loaded
    'data': [
        'views/purchase_order.xml',
    ],
}