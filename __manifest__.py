# -*- coding: utf-8 -*-

{
    'name': 'Development Projects',
    'version': '1.0',
    'category': 'Services/DevelopmentProject',
    'sequence': 20,
    'summary': 'Development Projects Custom Fields',
    'description': '',
    'depends': [
        'project',
    ],
    'data': [
        'security/development_project_security.xml',
        'security/ir.model.access.csv',

        'views/project_task_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
