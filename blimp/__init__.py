import json
import inspect
import urllib

import requests


API_ENDPOINT = 'https://app.getblimp.com/api/v2'


class Client(object):

    def __init__(self, username, api_key, app_id, secret):
        headers = {
            'content-type': 'application/json',
            'authorization': 'ApiKey %s:%s' % (username, api_key),
            'x_blimp_appid': app_id,
            'x_blimp_secret': secret
        }

        self.session = requests.session()
        default_headers = self.session.headers
        self.session.headers = dict(default_headers.items() + headers.items())

        # Dynamically enable endpoints
        self._attach_endpoints()

    def _attach_endpoints(self):
        """Dynamically attach endpoint callables to this client"""
        for name, endpoint in inspect.getmembers(self):
            is_class = inspect.isclass(endpoint)
            is_subclass = is_class and issubclass(endpoint, self.Endpoint)
            not_endpoint = endpoint is not self.Endpoint

            if is_subclass and not_endpoint:
                endpoint_instance = endpoint(self.session)
                setattr(self, name.lower(), endpoint_instance)

    class Endpoint(object):

        def __init__(self, session):
            self.session = session
            self.endpoint = self.__class__.__name__.lower()

        def _expanded_path(self, path=None):
            if path:
                path = (self.endpoint, str(path))
            else:
                path = (self.endpoint, )

            return '/{expanded_path}'.format(
                expanded_path='/'.join(p for p in path if p)
            )

        def _generate_url(self, path, params):
            if params:
                return '{API_ENDPOINT}{path}/?{params}'.format(
                    API_ENDPOINT=API_ENDPOINT,
                    path=self._expanded_path(path),
                    params=urllib.urlencode(params)
                )
            else:
                return '{API_ENDPOINT}{path}/'.format(
                    API_ENDPOINT=API_ENDPOINT,
                    path=self._expanded_path(path)
                )

        def _process_request(self, request):
            try:
                return request.json()
            except ValueError:
                return request.raise_for_status()

        def _request(self, method, url, payload=None):
            request = self.session.request(method, url, data=json.dumps(payload))
            return self._process_request(request)

        def get(self, path=None, params={}):
            url = self._generate_url(path, params)
            return self._request(method='get', url=url)

        def post(self, path=None, params={}):
            url = self._generate_url(path, None)
            return self._request(method='post', url=url, payload=params)

        def put(self, path=None, params={}):
            url = self._generate_url(path, params)
            return self._request(method='put', url=url, payload=params)

        def delete(self, path=None):
            url = self._generate_url(path, None)
            return self._request(method='delete', url=url)

    class ApiResource(Endpoint):
        def __call__(self, identifier=None, params={}):
            return self.get(path=identifier, params=params)

        def create(self, params={}):
            return self.post(params=params)

        def update(self, identifier, params={}):
            return self.put(path=identifier, params=params)

        def delete(self, identifier):
            return super(Client.ApiResource, self).delete(path=identifier)

        def schema(self):
            return self.get(path='schema')

    class Company(ApiResource):
        pass

    class Project(ApiResource):
        pass

    class Goal(ApiResource):
        pass

    class Task(ApiResource):
        pass

    class Comment(ApiResource):
        pass

    class File(ApiResource):
        pass
