import os


def get_mysql_uri():
    host = os.environ.get('DB_HOST', None)
    port = os.environ.get('DB_PORT', 3306)
    password = os.environ.get('MYSQL_PASSWORD', None)
    user = os.environ.get('MYSQL_USER', None)
    db_name = os.environ.get('MYSQL_DATABASE', None)
    return f"mysql://{user}:{password}@{host}:{port}/{db_name}"


def get_api_url():
    host = os.environ.get('API_HOST', 'localhost')
    port = 8000 if host == 'localhost' else 80
    return f"http://{host}:{port}"
