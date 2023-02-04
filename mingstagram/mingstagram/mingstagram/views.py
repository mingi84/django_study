from django.shortcuts import render
from rest_framework.views import APIView

class Sub(APIView):
    def get(self, request):
        print("Call Get Method")
        return render(request, "mingstagram\main.html")

    def post(self, request):
        print("Call Post Method")
        return render(request, "mingstagram\main.html")