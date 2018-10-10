from django.shortcuts import render

def get_issues(request):
    """
    Return the issues.html file
    """
    return render(request, "issues.html")