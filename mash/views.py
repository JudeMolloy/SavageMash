from django.shortcuts import render
from .models import People


def reset(request):
    objects = People.objects.all()
    for object in objects:
        object.rating = 1400
        object.save()
    return render(request, 'mash/rankings.html')

def rankings(request):
    rankings = People.objects.all().order_by('-rating')[:3]
    context = {'rankings': rankings, }
    return render(request, 'mash/rankings.html', context)


def mash(request):
    people = People.objects.all().order_by('?')[:2]
    people = list(people)

    if request.method == 'POST':
        form = request.POST

        selected = form['name']
        person1 = form['person1']
        person2 = form['person2']
        id1 = form['id1']
        id2 = form['id2']
        print(person1)
        print(person2)

        # Elo Rating System
        # Getting the person's current rating
        Ra = People.objects.get(pk=id1)
        print(Ra)
        Rb = People.objects.get(pk=id2)
        print(Rb)

        # Calculating each players expected rating
        Ea = 1 / (1 + 10**((Rb.rating - Ra.rating) / 400))
        Eb = 1 / (1 + 10**((Ra.rating - Rb.rating) / 400))

        if selected == person1:
            Ra.rating += (16 * (2 - Ea))
            Rb.rating -= (16 * (2 - Eb))
            Ra.save()
            Rb.save()
        elif selected == person2:
            Ra.rating -= (16 * (2 - Ea))
            Rb.rating += (16 * (2 - Eb))
            Ra.save()
            Rb.save()
        else:
            print('ERROR!!!')

    context = {'people': people}
    return render(request, 'mash/index.html', context)
