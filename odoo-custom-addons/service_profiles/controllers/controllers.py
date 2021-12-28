# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
import os.path


class Busines(http.Controller):

    @http.route('/busines/profiles/approved/', auth='public', website=True)
    def approved_list(self, **kw):
        profiles = request.env['res.partner'].sudo().search(
            [('status', '=', "approved")])
        print('printing profiles----------------------------', profiles)
        print(request.env)
        print(request.env.user)
        print(request.env.user[0])
        print(type(request.env.user))
        for profile in profiles:
            print('-----------printing profiles -----------------',
                  profile.businessName)

        return request.render('service_profiles.profiles_list_page', {
            'profiles': profiles
        })

    @http.route('/profiles/create/', type="http", website=True, auth='public')
    def book_webform(self, **kw):
        print("testing one two three")
        print(request.env.user)
        print(request.env.user[0])
        print(request.env.user == request.env.user[0])
        return request.render('service_profiles.create_profile', {})

    @http.route('/profiles/create/action', type="http", website=True, auth='public')
    def library_book_create(self, **kw):
        print('------------print POST data', kw)
        business_slug = kw.get('business_slug')
        print(business_slug)
        user = request.env.user
        service = request.env['res.partner'].sudo().create(kw)
        service.write({'user_id': user.id})
        return request.render('service_profiles.create_profile', {
            'business_slug': business_slug
        })

    @http.route("/check_business_slug", auth='public', methods=['POST'], type='json', csrf=False)
    def check_method_get(self, **values):
        """
        check for existing business slugs asynchronously 
        """
        value = json.loads(request.httprequest.data)
        profiles = request.env['res.partner'].sudo().search(
            [('business_slug', '=', value.get('business_slug'))]
        )
        output = None
        if profiles.exists():
            output = {
                'data': {
                    'code': 200,
                    'exists': True,
                    'message': "Business Slug is already Taken"
                }
            }
        else:
            output = {
                'data': {
                    'code': 200,
                    'exists': False,
                    'message': "Business Slug is available"
                }
            }
        return output
