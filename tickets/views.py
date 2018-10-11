from django.shortcuts import render

def get_tickets(request):
    """
    Return the tickets.html file
    """
    return render(request, "tickets.html")