from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello - polls.index")

def detail(request, question_id):
	 return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s" % question_id
	return HttpResponse(response)

def vote(request, question_id):
	response = "You are voting on question %s" % question_id
	return HttpResponse(response)
