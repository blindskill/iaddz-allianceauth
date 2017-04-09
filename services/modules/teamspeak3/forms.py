from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from .manager import Teamspeak3Manager


class TeamspeakJoinForm(forms.Form):
    username = forms.CharField(widget=forms.HiddenInput())

    def clean(self):
        if Teamspeak3Manager._get_userid(self.cleaned_data['username']):
            return self.cleaned_data
        raise forms.ValidationError(_("Unable to locate user %s on server") % self.cleaned_data['username'])
