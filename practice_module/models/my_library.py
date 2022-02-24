from odoo import fields, api, models
import json
import requests


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

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')],
        string='Status', default='draft')

    user_id = fields.Many2one('res.users', string="User ID")

    def btn_draft(self):
        self.state = 'draft'

    def btn_confirm(self):
        self.state = 'confirm'
        self.user_id.notify_danger("Okay")

    def button_import_tags(self):
        stock_picking_ids = self.browse(self._context.get('active_ids'))
        response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
        for rec in stock_picking_ids:
            for data in response.json()['items']:
                for x in data['tags']:
                    print(x)
                    rec.name = x

    def btn_done(self):
        self.state = 'done'

    def btn_cancel(self):
        self.state = 'cancel'


