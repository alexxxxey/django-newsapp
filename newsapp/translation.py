from modeltranslation.translator import translator, TranslationOptions, AlreadyRegistered
from .models import New
from settings_newsapp import ENABLE_CATEGORIES

for model in [New,]:
    if hasattr(model, '_translation_fields'):
        translation_option = type("{0}Translation".format(model.__name__), (TranslationOptions,), {
            'fields': model._translation_fields,
        })
        try:
            translator.register(model, translation_option)
        except AlreadyRegistered:
            pass


if ENABLE_CATEGORIES:
	from .models import NewCategory

	for model in [NewCategory,]:
	    if hasattr(model, '_translation_fields'):
	        translation_option = type("{0}Translation".format(model.__name__), (TranslationOptions,), {
	            'fields': model._translation_fields,
	        })
	        try:
	            translator.register(model, translation_option)
	        except AlreadyRegistered:
	            pass
