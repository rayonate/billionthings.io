from odoo import http
from odoo.http import request
import json


class BusinessImage(http.Controller):
    @http.route('/images/create/', type="http", website=True, auth='public')
    def service_images_webform(self, **kw):
        return request.render('service_profiles.create_image', {})

    @http.route('/images/create/action', type="http", website=True, auth='public')
    def service_images_action_webform(self, **kw):
        print(kw)
        name = kw.get('image')
        file = kw.get('image')
        if 'task_attachment' in request.params:
            attached_files = request.httprequest.files.getlist('task_attachment')
            print(attached_files)
        print(name, file)
        return request.render('service_profiles.create_image', {})