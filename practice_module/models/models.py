# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class practice_module(models.Model):
#     _name = 'practice_module.practice_module'
#     _description = 'practice_module.practice_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
