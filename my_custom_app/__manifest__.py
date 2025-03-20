{
    'name': 'My Custom App',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'A custom Odoo module',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}