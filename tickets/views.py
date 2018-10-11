from django.shortcuts import render
from .models import Ticket

def all_tickets(request):
    """
    Return the tickets.html file
    """
    tickets = Ticket.objects.all()
    return render(request, "tickets.html", {'tickets':tickets})