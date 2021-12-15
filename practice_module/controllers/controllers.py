# -*- coding: utf-8 -*-
from odoo import http


class PracticeModule(http.Controller):
    @http.route('/practice_module/all_books/', auth='public', website=True)
    def index(self, **kw):
        rec = http.request.env['my.books'].search([])

        return http.request.render('practice_module.my_books_web_temp', {
            'books_rec': rec,
        })

    @http.route('/practice_module/<model("my.books"):b>', auth='public', website=True)
    def books(self, b):
        return http.request.render('practice_module.books_web_temp', {
            'rec': b,
        })

        # output = ""
        # for x in rec:
        #     print('xxx>', x['name'])
        #     output += x['name'] + "<br/>"
        # return "Sales Order " + "<br/>" + output


#     @http.route('/practice_module/practice_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('practice_module.listing', {
#             'root': '/practice_module/practice_module',
#             'objects': http.request.env['practice_module.practice_module'].search([]),
#         })

#     @http.route('/practice_module/practice_module/objects/<model("practice_module.practice_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('practice_module.object', {
#             'object': obj
#         })
