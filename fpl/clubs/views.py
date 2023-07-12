from django.shortcuts import get_object_or_404, render
from .models import Club

# Create your views here.
def getClub(request, slug):
    club = get_object_or_404(Club, slug=slug)

    return render(request, 'club.html', {
        'club': club
    })
