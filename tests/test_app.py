import pytest
from app import app

@pytest.fixture
def client():
    # Configure Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Game Rating Prediction" in response.data
