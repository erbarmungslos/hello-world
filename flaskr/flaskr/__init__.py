from .wsgi import app
from . import controller

app.run(host='0.0.0.0', port=8000, debug=True)
