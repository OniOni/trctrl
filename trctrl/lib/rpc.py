import requests


class TrClient(object):

    def __init__(self, host="localhost", port=9091):
        self.host = "http://{}:{}/transmission/rpc".format(host, port)
        self._key = None

    def headers(self):
        if self._key:
            return {
                'X-Transmission-Session-Id': self._key
            }

        return None

    def send(self, method, args=None):
        res = requests.post(
            self.host,
            headers=self.headers(),
            json={
                'method': method,
                'arguments': args
            }
        )

        if res.status_code == 409:
            self._key = res.headers['X-Transmission-Session-Id']
            res = self.send(method, args)

        return res
