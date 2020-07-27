from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    def get(self, *args, **kwargs):
        context = {
            "request": self.request
        }
        return render(self.request, "home.html", context)

class BioView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "bio.html")

class PortfolioView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "portfolio.html")
