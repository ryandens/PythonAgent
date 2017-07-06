import time
from guppy import hpy

class AgentMiddleware(object):
    responses = []
    total_str_count = 0

    def __init__(self, app):
        self.app = app
        self.current_max_id = 0
        self.heapy = hpy()

    def __call__(self, environ, start_response):
        response_interception = {}
        
        def demo_start_response(status, headers, exc_info=None):
            print(headers)
            response_interception.update(status=status, response_headers=headers, exc_info=exc_info)
            return start_response(status, headers, exc_info)

        start = time.time()
        self.heapy.setrelheap()

        try:
            if environ.get('PATH_INFO') == "/agent_statistics":
                status = '200 OK'
                output = self.agent_statistics()
                response_headers = [('Content-Type', 'text/html; charset=utf-8'),
                                    ('Content-Length', str(len(output)))]
                start_response(status, response_headers)

                yield output
            else:
                response = self.app(environ, demo_start_response)

                try:
                    for event in response:
                        yield event
                finally:
                    if environ.get('PATH_INFO') != "/agent_statistics" and hasattr(response, 'close'):
                        response.agent_id = self.current_max_id
                        self.responses.append(response)
                        self.current_max_id += 1
                        response.close()

                heapy_result = self.heapy.heap()
                time_diff = time.time() - start
                str_count = 0

                for index in range(0, len(heapy_result)):
                    if heapy_result[index].kind.arg is str:
                        str_count = heapy_result[index].count
                        break

                self.total_str_count += str_count
                self.responses[-1].strings_created = str_count
                self.responses[-1].path_info = environ.get('PATH_INFO')
                self.responses[-1].time = time_diff
                self.responses[-1].heap_size = heapy_result.size

        except Exception as exception:
            raise exception

    def agent_statistics(self):
        output = 'Total Strings created: ' + str(self.total_str_count)

        output += '<br/>'
        output += '<br/>'

        output += '<table><thead><tr>' \
                  '<th>Id</th>' \
                  '<th>Strings Created</th>' \
                  '<th>Path</th>' \
                  '<th>Time(seconds)</th>' \
                  '<th>Memory(bytes)</th>' \
                  '</thead></tr>'
        for resp in self.responses:
            output += '<tbody><tr>' + \
                      '<td>' + str(resp.agent_id) + '</td>' + \
                      '<td>' + str(resp.strings_created) + '</td>' + \
                      '<td>' + str(resp.path_info) + '</td>' + \
                      '<td>' + str(resp.time) + '</td>' + \
                      '<td>' + str(resp.heap_size) + '</td>' + \
                      '</tbody></tr>'
        output += '</table'

        return output


