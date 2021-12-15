# -*- coding: utf-8 -*-

from odoo import models, fields, api



class BusinesProfile(models.Model):
    _name = 'business.profile'
    _description = 'Business Profile'

    title = fields.Char()
    description = fields.Text()


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


#access_business_profile,busines.profile,model_busines_profile,group_service_providers,1,1,1,1
