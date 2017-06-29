import time


class AgentMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('Request Method', environ.get('REQUEST_METHOD'))
        print('Path Info', environ.get('PATH_INFO'))
        print('Query String', environ.get('QUERY_STRING'))

        response_interception = {}

        def demo_start_response(status, headers, exc_info=None):
            response_interception.update(status=status, response_headers=headers, exc_info=exc_info)
            return start_response(status, headers, exc_info)

        start = time.time()

        try:
            response = self.app(environ, demo_start_response)
            print("response", response)
            print("response interception", response_interception)

            try:
                for event in response:
                    yield event
            finally:
                if hasattr(response, 'close'):
                    response.close()

            print("Start Time", "Difference")
            print(start, time.time() - start)

        except Exception as exception:
            raise exception
