from Hello import app
import pytest
import json

@pytest.fixture
def client():
    return app.test_client()

def test_pinger(client):
    res = client.get('/ping')
    assert res.status_code==200
    assert res.json == {'Message' : 'Hi I am pinging.............'}

def test_predictions(client):
    res = client.post('/predict')
    assert res.status_code==200
    test_data = {
    "Gender":"Male",
    "Married":"No",
    "ApplicantIncome":5000000,
    "LoanAmount":50000,
    "Credit_History":1.0
    }
    resp=client.post("/predict", json=test_data)
    assert resp.status_code==200

    assert res.json == {"loan_approval_status": "Rejected"}