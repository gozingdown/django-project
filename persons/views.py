from django.http import HttpResponse

def name(request, name =  'default_name'):
    html = '<html><body>name:' + name + '</body></html>'
    return HttpResponse(html)
