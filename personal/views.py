from django.shortcuts import render,get_object_or_404

from .models import Album
from django.http import HttpResponse,Http404
# Create your views here.

def index(request):
        all_albums = Album.objects.all()
        context = {'all_albums': all_albums}
        return render(request, 'personal/index.html', context)
def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    return render(request, 'personal/detail.html', {'album': album})



