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

    def btn_done(self):
        self.state = 'done'

    def btn_cancel(self):
        self.state = 'cancel'


