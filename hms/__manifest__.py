{
    'name': 'HMS',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'A Hospital Management System',
    'depends': ['base', 'web'],  # Added 'web' dependency
    'data': [
        'security/ir.model.access.csv',
        'views/patientsData.xml',
        'views/patient_views.xml',
    ],
    'installable': True,
    'application': True,
}