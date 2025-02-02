from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def get_translation(self, lang="en"):
        cache_key = f"faq_translation_{self.id}_{lang}"
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation

        translation = self.question
        if lang == "hi":
            translation = self.question_hi or translator.translate(self.question, dest="hi").text
        elif lang == "bn":
            translation = self.question_bn or translator.translate(self.question, dest="bn").text

        cache.set(cache_key, translation, timeout=3600)  # Cache for 1 hour
        return translation
