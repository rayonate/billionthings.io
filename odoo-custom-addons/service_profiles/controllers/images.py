from odoo import http
from odoo.http import request
import json


class BusinessImage(http.Controller):
    @http.route('/images/create/', type="http", website=True, auth='public')
    def service_images_webform(self, **kw):
        return request.render('service_profiles.create_image', {})
