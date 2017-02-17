from django.http import HttpResponse
from polls.models import Question


def index(request):
    # https://docs.djangoproject.com/en/1.10/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
     return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s" % question_id
    return HttpResponse(response)

def vote(request, question_id):
    response = "You are voting on question %s" % question_id
    return HttpResponse(response)
