from odoo import models, fields, api


class Awards(models.Model):
    _name = 'service.award'

    image = fields.Binary(string='Service Image')
    name = fields.Char(string='Award Name')
    description = fields.Char(string='description')
    business_id = fields.Many2one('res.partner', string='Business')
    