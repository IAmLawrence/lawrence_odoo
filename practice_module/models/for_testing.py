from odoo import fields, api, models
from addons.website.tools import get_video_embed_code


# dito sa model viewer na 3d need dito yung module na web_widget_model_viewer para gumana
class ModelViewer3D(models.Model):
    _name = 'model.viewer.3d'

    name = fields.Char(string="Name")
    model_viewer = fields.Binary(string="Image")


# sa embed video naman na to pwedeng ma play yung naka lagay na link sa mismong form view ni odoo
# dito need naka install yung ecommerce app (website_sale module)
class EmbeddedVideo(models.Model):
    _name = 'embedded.video'

    name = fields.Char(string="Name")
    video_url = fields.Char('Video URL',
                            help='URL of a video for showcasing your books.')
    embed_code = fields.Char(compute="_compute_embed_code")

    @api.depends('video_url')
    def _compute_embed_code(self):
        for rec in self:
            rec.embed_code = get_video_embed_code(rec.video_url)
