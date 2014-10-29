from modeltranslation.translator import translator, TranslationOptions
from .models import New

for model in [New]:
    if hasattr(model, '_translation_fields'):
        translation_option = type("{0}Translation".format(model.__name__), (TranslationOptions,), {
            'fields': model._translation_fields,
        })
        translator.register(model, translation_option)