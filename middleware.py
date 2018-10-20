class SimpleMiddleware(object):
    def __init__(self,app):
        self.app = app
    def __call__(self, environ, start_response):
        print(environ)
        arr = ['/api/v1/bus/readAllBusMania','/api/v1/bus/readOneBusMania']
        if (environ['PATH_INFO'] in arr):
            return self.app(environ, start_response)

        try:
            if (environ['HTTP_AUTHORIZATION'] != "aaa"):
                return self.app('', start_response('401 Unauthorize',[("Content-type",'text/html')]))
        except:
                return self.app('', start_response('401 Unauthorize',[("Content-type",'text/html')]))

        return self.app('', start_response('400 balek beull',[("Content-type",'text/html')]))
        # return self.app(environ, start_response)
