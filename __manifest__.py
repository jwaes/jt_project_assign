# -*- coding: utf-8 -*-
{
    'name': "jt_project_assign",

    'summary': "Auto assign users to project stages",

    'description': "",

    'author': "jaco tech",
    'website': "https://jaco.tech",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project Management',
    'version': '15.0.1.0.6',

    # any module necessary for this one to work correctly
    'depends': ["project"],

    # always loaded
    'data': [
        "views/project_project.xml",
    ],

}