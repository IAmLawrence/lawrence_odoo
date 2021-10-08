from odoo import fields, api, models


class MyBooks(models.Model):
    _name = 'my.books'

    name = fields.Char(string="Name")
    author = fields.Char(string="Author")
    published_date = fields.Date(string="Date")
    status = fields.Selection([
        ('new', 'New'),
        ('old', 'Old'),
        ('damage', 'Damage'),
    ], string="Status")
    desc = fields.Text(string="Description")
