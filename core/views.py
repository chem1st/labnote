from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Synthesis


class SynthesisList(ListView):
	model = Synthesis
	template_name = 'synthesis_list.html'
	context_object_name = 'synths'


class SynthesisDetail(DetailView):
	model = Synthesis
	template_name = 'synthesis_detail.html'
	context_object_name = 'synthesis'
