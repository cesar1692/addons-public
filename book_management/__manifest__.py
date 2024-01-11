# -*- coding: utf-8 -*-

{
    'name': 'Administración de Libros',
    'version': '1.0',
    'category': 'libros',
    'summary': 'Administración de Libros',
    'description': """
Administración de Libros
====================================================================

Permite los siguientes items:
------------------------------------------------------
    * Registrar Libros
    * Buscar Libros
    * Filtrar Libros
""",
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/books_books_views.xml',
        'views/menues.xml',
        'report/report_books.xml',
        'report/actions_reports.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
