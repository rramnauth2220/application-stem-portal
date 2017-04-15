#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response, redirect
from django.conf import settings
from account.models import Announcement
from account.forms import *

def home(request):
    """
        This view handles the landing page for the Application portal.
        The page displays the announcements and the login form.
        Link to registration page for coordinators is also included here.
    """
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return HttpResponseRedirect(settings.SITE_URL + 'admin/')
        userprofile = request.user.get_profile()
        if userprofile.is_core_of:
            return redirect('core.views.core_dashboard',username=request.user)
        else:
            return redirect('coord.views.coord_home')
    announcements = Announcement.objects.all()
    login_form = LoginForm()    
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

