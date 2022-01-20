from odoo import http
from odoo.http import request
import base64

class BusinessImage(http.Controller):
    @http.route('/images/create/', type="http", website=True, auth='public')
    def service_images_webform(self, **kw):
        business_slug = kw.pop('business_slug', None)
        return request.render('service_profiles.create_image', {})

    @http.route('/images/create/action', type="http", website=True, auth='public')
    def service_images_action_webform(self, **kw):
        print("++++++++++++++++Kwargs++++++++++++++++++++++++++++++")
        print(kw)
        business_slug = kw.pop('business_slug', None)
        business = request.env['res.partner'].sudo().search(
            [('business_slug', '=', business_slug)]
        )
        for i in range(5):
            name = f"group[{i}][name]"
            description = f"group[{i}][description]"
            name_post = kw.get(name)
            description_post = kw.get(description)
            if name_post or description_post:
                value = {
                    'name': name_post,
                    'description': description_post,
                    'business_id': business.id
                }
                request.env['service.award'].sudo().create(value)
            
        print("++++++++++++++++++awards created++++++++++++++++")
        print(kw)

        image_1920 = kw.get('logo')
        imageFile=image_1920.read()
        d_imageFile = base64.b64encode(imageFile)
        business.write({'image_1920': d_imageFile })
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if 'images' in request.params:
            attached_files = request.httprequest.files.getlist('images')
            for file_ in attached_files:
                image = file_.read()
                image_as_bytes = base64.b64encode(image)
                value = {
                    'image': image_as_bytes,
                    'business_id': business.id
                }
                print(value)
                image_obj = request.env['service.gallery'].sudo().create(value)
        return request.render('service_profiles.create_image', {})
    
    @http.route('/test/', type="http", website=True, auth='public')
    def service_images_webform(self, **kw):
        business_slug = kw.pop('business_slug', None)
        return request.render('service_profiles.test', {})