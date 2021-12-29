# -*- coding: utf-8 -*-
import json
from odoo import api, http
from odoo.http import request
import base64


class AdsProfile(http.Controller):

     @http.route('/addprofiles/create/', type="http", website=True, auth='public')
     def book_webform(self, **kw):
        print("testing one two three")
        print(request.env.user)
        print(request.env.user[0])
        print(request.env.user == request.env.user[0])
        name = request.env.user.name
        return request.render('ads_profiles.create_addprofiles', {
           'name': request.env.user.name
        })

     @http.route('/addprofiles/create/action', type="http", website=True, auth='public')
     def library_book_create(self, **kw):
        print('------------print POST data', kw)
        user = request.env.user
        bt_title = kw.get('bt_title')
        service = request.env['res.partner'].sudo().create(kw)
        service.write({'user_id': user.id})
        profile = request.env['res.partner'].sudo().search(
            [('bt_title', '=', bt_title)])
        print(profile.id)
        id = profile.id
        return request.render('ads_profiles.create_addprofileImages', {
           'id': id
        })

     @http.route('/addprofiles/images/create/action', type="http", website=True, auth='public')
     def profile_address_create(self, **kw):
        print('==============profile-update-data=============', kw)
        id = kw.get('id')

        #image_1920 = kw.get('image_1920')

        #file = kw.get('image_1920')
        #image_1920 = file.read() 

   
        profile = request.env['res.partner'].sudo().search([('id', '=', id)])
        #profile.write({'image_1920': image_1920.encode('base64')})
        print("+++++++++++++++++profile get+++++++++++++++++++++", profile)
        return request.render('ads_profiles.create_address', {
           'id': id
        })

     @http.route('/addprofiles/address/create/action', type="http", website=True, auth='public')
     def profile_adcreate(self, **kw):
        print('==============profile-update-data=============', kw)
        id = kw.get('id')
        profile = request.env['res.partner'].sudo().search([('id', '=', id)])
        print('==============profile=============', profile)
        street = kw.get('street')
        street2 = kw.get('street2')
        city = kw.get('city')
        province = kw.get('province')
        zip = kw.get('code')
        phone = kw.get('phone')
        mobile = kw.get('mobile')
        email = kw.get('email')
        profile.write({'street': street, 'street2': street2, 'city': city, 'province': province,
                      'zip': zip, 'phone': phone, 'mobile': mobile, 'email': email})
        print("+++++++++++++++++profile get+++++++++++++++++++++", profile)
        return request.render('ads_profiles.create_addprofiles', {})

     @http.route("/check_title", auth='public', methods=['POST'], type='json', csrf=False)
     def check_slug(self, **values):
        """
        check for existing business slugs asynchronously 
        """
        value = json.loads(request.httprequest.data)
        profiles = request.env['res.partner'].sudo().search(
            [('bt_title', '=', value.get('bt_title'))]
        )
        output = None
        if profiles.exists():
            output = {
                'data': {
                    'code': 200,
                    'exists': True,
                    'message': "Title is already Taken"
                }
            }
        else:
            output = {
                'data': {
                    'code': 200,
                    'exists': False,
                    'message': "Title Slug is available"
                }
            }
        return output


     