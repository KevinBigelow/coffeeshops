from django.forms import ModelForm
from collection.models import Business

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'description',)
