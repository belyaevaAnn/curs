from django.shortcuts import render
from django.views import View


class MainPage(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context=context)


class AdminPage(View):
    def get(self, request):
        context = {}
        return render(request, 'admin.html', context=context)


class EnterPage(View):
    def get(self, request):
        context = {}
        return render(request, 'enter.html', context=context)


class FormReviewPage(View):
    def get(self, request):
        context = {}
        return render(request, 'form_review.html', context=context)


class MasterPage(View):
    def get(self, request):
        context = {}
        return render(request, 'master.html', context=context)


class MaterialPage(View):
    def get(self, request):
        context = {}
        return render(request, 'material.html', context=context)


class OrderPage(View):
    def get(self, request):
        context = {}
        return render(request, 'order.html', context=context)


class ReviewPage(View):
    def get(self, request):
        context = {}
        return render(request, 'review.html', context=context)


class ServicePage(View):
    def get(self, request):
        context = {}
        return render(request, 'service.html', context=context)