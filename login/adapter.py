from allauth.account.adapter import DefaultAccountAdapter
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from django.shortcuts import render
from crispy_forms.utils import render_crispy_form
from django.template.context_processors import csrf

class AuthenticationAdapter(DefaultAccountAdapter):

    # def respond_email_verification_sent(self, request, user):
        # return HttpResponseRedirect("/")

    def ajax_response(self, request, response, redirect_to=None, form=None, data=None):
        resp = {}
        status = response.status_code

        if redirect_to:
            status = 200
            resp["location"] = redirect_to
        if form:
            if request.method == "POST":
                if form.is_valid():
                    status = 200
                else:
                    status = 400
            else:
                status = 200
        
        return JsonResponse({'form':render_crispy_form(form, context=csrf(request))}, status=status)
