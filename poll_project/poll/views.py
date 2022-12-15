from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'poll/home.html', context)

def create(request):
    context = {}
    return render(request, 'poll/create.html', context)

# Since votes and results deal with specific polls, we introduce poll_id

def vote(request, poll_id):
    context = {}
    return render(request, 'poll/votes.html', context)

def results(request, poll_id):
    context = {}
    return render(request, 'poll/results.html', context)