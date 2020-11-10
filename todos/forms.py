from django import forms
from django.utils import timezone
import datetime


def no_past_dates(value):
    if value < datetime.date.today():
        raise forms.ValidationError("The date cannot be in the past!")
    return value


class TodoForm(forms.Form):
    RECURRING_OPTIONS = (
        ("n", "none"),
        ("d", "day"),
        ("w", "week"),
        ("m", "month"),
        ("y", "year")
    )
    headline = forms.CharField()
    description = forms.CharField()
    deadline = forms.DateField(widget=forms.SelectDateWidget, initial=timezone.now(), validators=[no_past_dates] )
    recurring = forms.ChoiceField(choices=RECURRING_OPTIONS)

