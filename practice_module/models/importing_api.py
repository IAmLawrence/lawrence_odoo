from odoo import fields, models, api
import json
import requests


class ImportingAPI(models.Model):
    _name = 'importing.api'

    name = fields.Char(string="Name", required=False)
    fields_to_import = fields.Char(string="Fields to import")
    api_link = fields.Char(string="API Link")

    def btn_import_data(self):
        response = requests.get(self.api_link)
        print('>>>>?', response.json())
        for data in response.json()['results']:
            print(data.get('name'))
            self.env['my.books'].create({
                        'name': data.get('name')
                    })

        # working to
        # response = requests.get(self.api_link)
        # for data in response.json()['items']:
        #     print(data)
        #     print('xxx', data['owner'].get('display_name'))
        #
        #     if 'java' in data['tags']:
        #         self.env['my.books'].create({
        #             'name': data['owner'].get('display_name')
        #         })
