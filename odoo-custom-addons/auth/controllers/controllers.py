from odoo.addons.auth_signup.controllers.main import AuthSignupHome


class AuthSignupStreet(AuthSignupHome):
    def _signup_with_values(self, token, values):
        context = self.get_auth_signup_qcontext()
        values.update({'contact_no': context.get('contact_no'),'last_name': context.get('last_name'),'first_name': context.get('first_name')})
        super(AuthSignupStreet, self)._signup_with_values(token, values)
