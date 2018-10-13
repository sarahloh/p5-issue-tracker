from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Ticket, Comment
from .forms import TicketForm, CommentForm
from issue_tracker import settings

def all_tickets(request):
    """
    Return the tickets.html file
    """
    tickets = Ticket.objects.all()
    return render(request, "tickets.html", {'tickets':tickets})


def get_ticket(request, pk):
    """
    Return a single Ticket object based on the ticket ID and
    render it to the 'ticket.html' template.
    Or return a 404 error if ticket not found
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    try:
        comments = Comment.objects.filter(ticket=ticket)
    except Comment.DoesNotExist:
        print ("No comments in the database yet.")
        comments = None
    comment_form = CommentForm()
    return render(request, "ticket.html", {
        'ticket': ticket,
        'comments': comments,
        'comment_form':comment_form
    })


def create_or_edit_ticket(request, pk=None):
    """
    Create or edit a ticket depending if the ticket ID is null or not
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            ticket.user = request.user
            ticket.save()
            return redirect(get_ticket, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, "ticketform.html", {'form': form})


@login_required
def upvote_ticket(request, pk, category, user_id):
    """
    Add an upvote to a ticket
    Redirect to payment if ticket category is feature
    Or return a 404 error if post not found
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    if category == 'BUG':
        ticket.upvotes += 1
        upvoter = User.objects.get(id=user_id)
        ticket.upvoted_by.add(upvoter)
        ticket.save()
        return redirect(all_tickets)
    else:
        return redirect(complete_payment)

def add_comment(request, ticket_pk):
    """
    Add a comment to a ticket
    """
    try:
        ticket = Ticket.objects.get(pk=ticket_pk)
    except Ticket.DoesNotExist:
        print("No ticket found.")
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.ticket = ticket
        comment.save()
    return redirect(get_ticket, ticket_pk)


def complete_payment(request):
    """
    Return the payments.html file
    """
    context = { "stripe_key": settings.STRIPE_PUBLISHABLE }
    return render(request, "payment.html", context)

def checkout(request):
    """
    Complete payment transaction using Stripe
    """
    if request.method == "POST":
        token = request.POST.get("stripeToken")
    try:
        charge  = stripe.Charge.create(
            amount      = 100,
            currency    = "usd",
            source      = token,
            description = "Feature ticket implementation fund"
        )
    except stripe.error.CardError as ce:
        return False, ce

    else:
        return redirect('thankyou')

def thankyou(request):
    """
    Return the thankyou page
    """
    return render(request, "thankyou.html")
