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
        exclude = ('user', 'is_published')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Название товара содержит недопустимые слова')
        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']
        forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Описание товара содержит недопустимые слова')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
