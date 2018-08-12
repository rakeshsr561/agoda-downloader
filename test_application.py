from application import extract_file_name
from application import extract_site_details_from_line
from application import get_site_configs


def test_extract_file_name():
    assert extract_file_name('http://agoda.com/test.html') == 'test.html'


def test_extract_site_details_from_line():
    response = extract_site_details_from_line('http://agoda.com/test.html,user,password')
    assert response.get('user_name') == 'user'
    assert response.get('password') == 'password'
    assert response.get('protocol') == 'http'
    assert response.get('host_name') == 'agoda.com'
    assert response.get('url') == 'http://agoda.com/test.html'
    assert response.get('user_name') == 'user'