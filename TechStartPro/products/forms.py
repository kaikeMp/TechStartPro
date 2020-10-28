from django import forms
from .models import Product, Category

class ProductRegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=200, label="Product's Name", required=True)
    description = forms.CharField(max_length=200, label="Product's Description", required=True)
    value = forms.DecimalField(decimal_places=2, max_digits=6, label="Product's Value", required=True)
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    class Meta:
       model = Product
       fields = ['id', 'name', 'description', 'value', 'category']

class LoadCategoriesForm(forms.Form):
    categories_csv = forms.FileField(allow_empty_file=False)
