class PersonMiddlewareThree(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print __name__+'.__call__.before'
        response = self.get_response(request)
        print __name__+'.__call__.after'
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print __name__+'.process_view.call'
        return None

    def process_exception(self, request, exception):
        print __name__+'.process_exception.call'
        return None
