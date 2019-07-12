from django.shortcuts import render
from .models import Dataset, Participant

def home(request):
	return render(request, "home.html", {})

def about(request):
	return render(request, "about.html", {})

def index(request):
	all_participants = Participant.objects.all()
	context = {
		'all_participants': all_participants,
	}
	return render(request, "index.html", context)

def detail(request, participant_id, dataset):
	return render(request, "detail.html", {'participant_id': participant_id, 'dataset': dataset})