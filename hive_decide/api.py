from django.db import connection
from ninja import NinjaAPI, Schema

api = NinjaAPI(title="HiveDecide API", version="1")


class HealthOut(Schema):
    status: str
    database: bool


@api.get("/health", response=HealthOut, auth=None)
def health(request: object) -> HealthOut:
    """Liveness check that also confirms the database answers."""
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        database_ok = cursor.fetchone() == (1,)
    return HealthOut(status="ok", database=database_ok)
