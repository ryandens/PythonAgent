import time
from guppy import hpy

class AgentMiddleware(object):

    def __init__(self, app):
        self.app = app
        self.current_max_id = 0
        self.heapy = hpy()

    def trace_calls(frame, event, arg):
        if event != 'call':
            return
        co = frame.f_code
        func_name = co.co_name
        if func_name == 'write':
            # Ignore write() calls from print statements
            return
        func_line_no = frame.f_lineno
        func_filename = co.co_filename
        caller = frame.f_back
        caller_line_no = caller.f_lineno
        caller_filename = caller.f_code.co_filename
        print 'Call to %s on line %s of %s from line %s of %s' % \
              (func_name, func_line_no, func_filename,
               caller_line_no, caller_filename)
        return

    def __call__(self, environ, start_response):
        print('Request Method', environ.get('REQUEST_METHOD'))
        print('Path Info', environ.get('PATH_INFO'))
        print('Query String', environ.get('QUERY_STRING'))



        response_interception = {}

        def demo_start_response(status, headers, exc_info=None):
            response_interception.update(status=status, response_headers=headers, exc_info=exc_info)
            return start_response(status, headers, exc_info)

        start = time.time()
        self.heapy.setrelheap()

        try:
            response = self.app(environ, demo_start_response)

            try:
                for event in response:
                    yield event
            finally:
                if hasattr(response, 'close'):
                    response.agent_id = self.current_max_id
                    self.current_max_id += 1
                    response.close()
            heapy_result = self.heapy.heap()
            print("Start Time", "Difference")
            print(start, time.time() - start)

            str_count = 0

            for index in range(0, len(heapy_result)):
                if heapy_result[index].kind.arg is str:
                    str_count = heapy_result[index].count
                    break
            print("NUMBER OF STRINGS: ", str_count)

        except Exception as exception:
            raise exception


