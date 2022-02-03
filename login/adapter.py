from allauth.account.adapter import DefaultAccountAdapter
from django.http import HttpResponse, HttpResponseRedirect

class AuthenticationAdapter(DefaultAccountAdapter):

    pass
    # def respond_email_verification_sent(self, request, user):
        # return HttpResponseRedirect("/")