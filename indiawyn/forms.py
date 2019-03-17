from wtforms_alchemy import ModelForm
from .models import *


class TitleForm(ModelForm):
    class Meta:
        model = Title

class InfoForm(ModelForm):
    class Meta:
        model = Info

class CrewIdentifier(ModelForm):
    class Meta:
        model = CrewIdentifier