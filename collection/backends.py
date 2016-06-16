from registration.backends.simple.views import RegistrationView

# My new reg view, subclassing the RegistrationView from our plugin
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        # The named URL that we want to redirect to after successful registration
        return ('registration_create_business')
