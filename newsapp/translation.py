from modeltranslation.translator import translator, TranslationOptions, AlreadyRegistered
from .models import New

for model in [New]:
    if hasattr(model, '_translation_fields'):
        translation_option = type("{0}Translation".format(model.__name__), (TranslationOptions,), {
            'fields': model._translation_fields,
        })
        try:
            translator.register(model, translation_option)
        except AlreadyRegistered:
            pass
