# -*- coding: utf-8 -*-

from odoo import models, fields, api



class BusinesProfile(models.Model):
    _name = 'business.profile'
    _description = 'Business Profile'
 
   
    businessType = fields.Selection([
        ('saloon', 'Saloon'),
        ('restaurant', 'Restaurant')
    ], )
    businessName = fields.Char()
    businessSlug = fields.Char()
    description = fields.Text()
    userId = fields.Char()
    status = fields.Selection([
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'rejected'),
    ], default='pending')



#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


#access_business_profile,busines.profile,model_busines_profile,group_service_providers,1,1,1,1
