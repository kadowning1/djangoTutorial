from django.shortcuts import render

# Create your views here.

from .models import Room

# rooms = [
#     {
#         'id': '1',
#         'name': 'Lets Learn Python'
#     },
#     {
#         'id': '2',
#         'name': 'Lets Learn Java'
#     },
#     {
#         'id': '3',
#         'name': 'Lets Learn HTML'
#     },
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request, pk):

    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def test(request):
    return render(request, 'test.html')
