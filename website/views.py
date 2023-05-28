from django.shortcuts import render
from django.utils import translation
from django.conf import settings
from django.views.generic.base import RedirectView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request, f"{request.get_host().split('.')[0]}/index.html")

class SetLanguage(RedirectView):
    url = "http://ar.ahgaff.local:8000"

    def get_redirect_url(self, *args, **kwargs):
        lang = self.request.GET.get('l', 'en')
        translation.activate(lang)
        print(self.request.get_host())
        self.request.session[settings.LANGUAGE_SESSION_KEY] = lang
        return f"http://{lang}.ahgaff.local:8000"