# -*- coding: utf-8 -*-
# from odoo import http


# class ServiceProfiles(http.Controller):
#     @http.route('/service_profiles/service_profiles/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/service_profiles/service_profiles/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('service_profiles.listing', {
#             'root': '/service_profiles/service_profiles',
#             'objects': http.request.env['service_profiles.service_profiles'].search([]),
#         })

#     @http.route('/service_profiles/service_profiles/objects/<model("service_profiles.service_profiles"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('service_profiles.object', {
#             'object': obj
#         })
