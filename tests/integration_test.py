from datetime import datetime
import requests

URL = "8306_Bobokhonov_AKh-app-1:5000"

class TestIntegration:
    def test_headers(self):
        r = requests.get(f'http://{URL}')
        expected_headers = {
            'Server': 'Werkzeug/2.2.2 Python/3.10.6',
            'Date': 'canonnized',
            'Content-Type': 'text/html; charset=utf-8',
            'Content-Length': '589',
            'Connection': 'close'
        }

        try:
            r.headers['Date'] = datetime.strptime(r.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z')
            r.headers['Date'] = 'canonnized'
        except ValueError:
            r.headers['Date'] = 'ValueErrorDuringParsingDate'

        assert r.headers == expected_headers
