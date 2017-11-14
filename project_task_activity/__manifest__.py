# -*- coding: utf-8 -*-

{
    "name": "Project Task Activity",
    'version': '10.0',
    'category': 'Tools',
    'sequence': 14,
    'author':  'ADHOC SA & Yurii Khomych',
    'website': 'https://github.com/YuriiKhomych/odoo_project',
    'summary': '',
    'description': """
    Project Task Activity
    Move module from 8 to 10 version odoo and add mail.thread functionality
    """,
    'depends': [
        'base',
        'project',
        'mail',
    ],
    'external_dependencies': {
    },
    'data': [
        'view/activities_menuitem.xml',
        'view/project_view.xml',
        'view/task_view.xml',
        'security/ir.model.access.csv',
        'security/project_security.xml',
        'data/project_activity_data.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
