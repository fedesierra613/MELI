from fastapi.testclient import TestClient
from app.main import app
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app


client = TestClient(app)

def test_mutant_detection():
    response = client.post("/mutant/", json={"dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]})
    assert response.status_code == 200
    assert response.json() == {"status": "Mutant detected"}

def test_human_detection():
    response = client.post("/mutant/", json={"dna":["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"]})
    assert response.status_code == 403
    assert response.json() == {"detail": "Not a mutant"}

def test_stats_endpoint():
    response = client.get("/stats")
    assert response.status_code == 200
