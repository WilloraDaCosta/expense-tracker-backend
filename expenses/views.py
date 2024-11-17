# expenses/views.py
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

def home(request):
    return HttpResponse("Welcome to the Expense Tracker!")  # Or any other message or content you want to show
