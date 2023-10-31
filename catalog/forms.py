from django import forms

from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта',
                           'биржа', 'дешево', 'бесплатно',
                           'обман', 'полиция', 'радар']
        data_list = cleaned_data.split()
        for el in data_list:
            if el.lower() in forbidden_words:
                raise forms.ValidationError('Вы используете запрещенные слова, не надо так!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта',
                           'биржа', 'дешево', 'бесплатно',
                           'обман', 'полиция', 'радар']
        data_list = cleaned_data.split()
        for el in data_list:
            if el.lower() in forbidden_words:
                raise forms.ValidationError('Вы используете запрещенные слова, не надо так!')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
