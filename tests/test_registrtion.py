import requests

def test_registration():
    url = 'http://localhost:5000/regitration'
    data = {
        'name': 'John Doe',
        'age': '30',
        'address': '123 Main St',
        'contact': '555-555-5555',
        'email': 'johndoe@example.com'
    }
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert 'John Doe' in response.text
    assert '30' in response.text
    assert '123 Main St' in response.text
    assert '555-555-5555' in response.text
    assert 'johndoe@example.com' in response.text
