from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from traindetail.models import Train
import random


# Create your views here.

def index(request):
    train = Train.objects.all()
    return render(request, 'traindetail/index.html', context={'train': train})


def train_detail(request, slug):
    train = get_object_or_404(Train, slug=slug)
    return render(request, 'traindetail/detail.html', context={"train": train})


"""
def random_train(request, slug):
    train = get_object_or_404(Train, slug=slug)
    chiffre = random.randint(1, 2)

    if chiffre == 1:
        slug == "melun"
    elif chiffre == 2:
        slug == "saint-germain-en-laye"
    

    return render(request, "traindetail/detail.html", context={"train": train})
"""

def random_train(request):
    existing_slugs = Train.objects.values_list('slug', flat=True)
    random_slug = random.choice(existing_slugs)
    return redirect('train', slug=random_slug)


def destination_search(request):
    if 'destination' in request.GET:
        destination = request.GET['destination']

        try:
            train = Train.objects.get(destination=destination)
            return redirect('train', slug=train.slug)
        except Train.DoesNotExist:
            pass

    return redirect('index')



