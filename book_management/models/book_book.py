# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, is_html_empty
from datetime import datetime, date, timedelta

import logging
_logger = logging.getLogger(__name__)

class BookBook(models.Model):
    _name = 'book.book'
    _description = 'Administración de Libros'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc, create_date desc'

    name = fields.Char('Título', required=True, help='Título del Libro')
    author = fields.Char('Autor', required=True, help='Autor del Libro')
    book_genre = fields.Selection([('narrativo', 'Narrativo'),
                                   ('lirico', 'Lírico'),
                                   ('poesia', 'Poesia'),
                                   ('dramatico', 'Dramatico'),
                                   ('didactico', 'Didáctico'),
                                   ], required=True, string='Género',  help="Género del Libro")
    price = fields.Monetary('Precio', required=True, help='Precio del Producto')
    date = fields.Char('Fecha', required=True, default=fields.Date.context_today, help='Fecha')
    company_id = fields.Many2one('res.company', 'Compañia', readonly=True, required=True, index=True, default=lambda self: self.env.company)
    currency_id = fields.Many2one(related='company_id.currency_id', string='Moneda')