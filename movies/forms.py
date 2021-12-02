import datetime

from django import forms
from django.core.exceptions import ValidationError

from .models import *


class TextName(forms.Form):
    your_name = forms.CharField(
        label="Твое имя",
        help_text="Attention!",
        initial=datetime.date.today,
        max_length=100,
        widget=forms.Textarea,
        required=False,
        error_messages={"required": "Egghead, what did you do?"}
    )

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ["Text", "Name", "Email"]


# class Comment(forms.ModelForm):
#     # slug = CharField(validators=[validate_Age])
#     class Meta:
#         model = DirectorsActors
#         fields = ["Name", "Age", "Description", "Image"]
        # widgets = {
        #     "Name": forms.Textarea(attrs={"cols": 10, "rows": 10}),
        # }
        # labels = {
        #     "Name":_("Имя быстро"),
        #     "Age":_("Возраст какой а?"),
        # }
        #
        # help_texts={
        #     "Name": _("Имя нужно в латинице")
        # }

    #
    # def clean_name(self):
    #     name = self.cleaned_data["Name"]
    #     if len(name)>6:
    #         raise ValidationError("Ты шо правила не читал?")
    #     return name
