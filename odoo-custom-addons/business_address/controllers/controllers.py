# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class BusinesAddress(http.Controller):

     @http.route('/profiles/address/create/action', type="http", website=True, auth='public')
     def library_profile_create(self, **kw):
        print('------------print POST data', kw)
        request.env['business.profile'].sudo().create(kw)
        return request.render('business_address.create_address', {})