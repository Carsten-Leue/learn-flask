import os
import tempfile

import pytest

from ..iplink import createIpLinkMock
from ..app import create_app


@pytest.fixture
def client():
    app = create_app(createIpLinkMock)
    with app.test_client() as client:
        yield client

def test_show_devices(client):
    rv = client.get('/')
    print(rv.data) 
    
def test_show_device(client):
    rv = client.get('/Carsten-Device')
    print(rv.data) 
        