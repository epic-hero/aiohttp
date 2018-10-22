import os

class Router:

    def __init__(self, app, web):
        self.web = web
        # static

        # описать методы
        routes = [
            ('GET', '/api/test', self.testHandler),
            # ('GET', '/api/sqr/{value}', self.sqrHandler),
            ('*', '/', self.staticHandler),
            ('*', '/{name}', self.defaultHandler)
        ]
        for route in routes:
            app.router.add_route(route[0], route[1], route[2])

    async def testHandler(self, request):
        return self.web.json_response({'result': 'Hesasasasllo'})

    async def staticHandler(self, request):
        return self.web.FileResponse(os.getcwd() + '/public/index.html')

    async def defaultHandler(self, request):
        return self.web.json_response({'result': 'no route'})

    async def sqrHandler(self, request):
        value = float(request.match_info.get('value'))
        return self.web.json_response({'result': value * value})
