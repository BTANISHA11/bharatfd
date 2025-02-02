from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .serializers import FAQSerializer

@api_view(["GET"])
def faq_list(request):
    lang = request.GET.get("lang", "en")
    faqs = FAQ.objects.all()
    data = [{"id": faq.id, "question": faq.get_translation(lang), "answer": faq.answer} for faq in faqs]
    return Response(data)
