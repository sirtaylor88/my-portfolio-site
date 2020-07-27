from django.shortcuts import render, redirect
from django.views.generic import View
from portfolio.models import Publication

class PublicationsView(View):
    def get(self, *args, **kwargs):
        order_by = self.request.GET.get("order_by", "title")
        print(order_by)
        qs = Publication.objects.all().order_by(order_by)
        context = {
            "request": self.request,
            "tab": self.request.GET.get("tab", "thesis")
        }
        if self.request.GET.get("direction", "asc") == "asc":
            qs = Publication.objects.all().order_by(order_by)
            context["direction"] = "asc"
        else:
            qs = Publication.objects.all().order_by("-" + order_by)
            context["direction"] = "desc"
        context["publications"] = qs
        return render(self.request, "publications.html", context)
