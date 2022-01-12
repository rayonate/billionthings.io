# -*- coding: utf-8 -*-
from odoo import models, fields

class Attachment(models.Model):
    _inherit = 'ir.attachment'

    attach_rel = fields.Many2many('res.partner', 'attachment', 'attachment_id3', 'document_id',string="Attachment", invisible=1 )