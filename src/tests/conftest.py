import os
import asyncio
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def test_client():
    # Use SQLite in-memory database for tests
    os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///:memory:"

    # Import app after env is set so engine picks up test DB
    from main import app

    with TestClient(app) as client:
        yield client


