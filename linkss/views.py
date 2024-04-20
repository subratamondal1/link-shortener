from django.shortcuts import render, HttpResponse

from .models import Link

# Create your views here.
def index(request) -> HttpResponse:
    links = Link.objects.all()
    context = {
        "links":links
    }
    return render(request=request, template_name="links/index.html", context=context)
