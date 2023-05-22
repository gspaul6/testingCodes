from main import app

def test_get_api_endpoint():
    with app.test_client() as tc:
        response = tc.get('api/ApiEndpoint')
        assert response.status_code == 200
        json_response = response.get_json()
        assert json_response == {'message': 'This is a response from a GET request.'}

def test_post_api_endpoint():
    with app.test_client() as tc:
        response = tc.post('api/ApiEndpoint', json={
            "name": "PAUL"
        })
        assert response.status_code == 200
        json_response = response.get_json()
        assert json_response == {'message': 'Hello nice to meet you, PAUL!'}

# test_api_endpoint()
# test_post_api_endpoint()