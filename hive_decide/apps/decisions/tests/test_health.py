"""Smoke test: the API is mounted and the test database is PostgreSQL."""

import pytest
from django.db import connection
from django.test import Client


@pytest.mark.django_db
def test_health_reports_ok_and_reachable_database():
    response = Client().get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": True}


@pytest.mark.django_db
def test_tests_run_on_postgresql():
    assert connection.vendor == "postgresql"
