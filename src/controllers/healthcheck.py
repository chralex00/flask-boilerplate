from flask import current_app as app
from datetime import datetime

def healthcheck():
    app.logger.info(f"GET /api/healthcheck API called at {datetime.today()}")
    return {
        "service_name": "flask-boilerplate",
        "status": "up"
    }