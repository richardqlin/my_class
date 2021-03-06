from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.views import generic

from .models import Question,Choice,UserProfile

from .forms import UserForm

from django import forms

class SearchForm(forms.Form):
	text=forms.CharField(label='Enter username:')


def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	context={'latest_question_list':latest_question_list}
	return render(request,'polls/index.html',context)

def detail(request, question_id):
	question=get_object_or_404(Question, pk=question_id)
	print question
	return render(request,'polls/detail.html', {'question':question})

def results(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request,'polls/detail.html',{'question':question,'error_message':"You didn't select a choice"})
	else:
		selected_choice.votes+=1
		selected_choice.save()

		return HttpResponseRedirect(reverse("polls:results", args=(question_id,) ))
def update(request):
	if request.method=='POST':
		form=SearchForm(request.POST, None)
		if form.is_valid():
			user=UserProfile.objects.filter(username=form.cleaned_data['text'])
			if request.method=='POST':
				if user.is_valid():
					user.save()
					return HttpResponseRedirect('/polls/contact_update_success/')
				else:
					return render(request,'polls/contact_update.html',{'form':form})
			user=UserForm()
			return render(request,'polls/contact_update.html',{'form':form})

def contact(request):
	print request.POST
	if request.method=='POST':
		form=UserForm(request.POST or None)
		print form
		if form.is_valid():
			cd=form.cleaned_data
			print form
			form.save()
			return HttpResponseRedirect('/polls/contact_success/')		
		else:
			return render(request,'contact.html',{'form':form})
	form=UserForm()
	return render(request,'polls/contact.html',{'form':form})
	
def contact_success(request):
	return render(request,'polls/contact_success.html')

def list(request):
	user=UserProfile.objects.all()
	l=[]
	print user
	for u in user:
		l.append(u)
		print u
	print l
	return render(request,'polls/list.html',{'list':l})


def search(request):
	if request.method=='POST':
		form=SearchForm(request.POST, None)
		if form.is_valid():
			user=UserProfile.objects.filter(username=form.cleaned_data['text'])
			return render(request,'polls/searchpage.html',{'form':form,'user':user})
		else:
			return render(request,'polls/search.html',{'form':form})
	form = SearchForm()
	return render(request,'polls/search.html',{'form':form})
'''
class IndexView(generic.ListView):
	template_name ='polls/index.html'
	context_object_name='latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model=Question
	template_name ='polls/detail.html'

class ResultsView(generic.DetailView):
	model=Question
	template_name ='polls/results.html'

def vote(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request,'polls/detail.html',{'question':question,'error_message':"You didn't select a choice"})
	else:
		selected_choice.votes+=1
		selected_choice.save()

		return HttpResponseRedirect(reverse("polls:results", args=(question_id,) ))
'''