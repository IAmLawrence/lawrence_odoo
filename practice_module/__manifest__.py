# -*- coding: utf-8 -*-
{
    'name': "practice_module",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'website',
        'web_notify',
        'web_widget_model_viewer',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/server_action.xml',
        'views/my_library.xml',
        'views/for_testing.xml',
        'views/templates.xml',
        'views/importing_api.xml',
        'views/menu_items.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
