from django.http import HttpResponse, HttpResponseNotFound

'''
This only works when you set DEBUG=False
https://docs.djangoproject.com/en/1.10/topics/http/views/#customizing-error-views
'''
def my_custom_page_not_found_view(request):
    html = '<html><body>404!</body></html>'
    return HttpResponseNotFound(html)
