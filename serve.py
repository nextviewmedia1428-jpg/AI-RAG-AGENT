import os
import sys

# Render sets GUNICORN_CMD_ARGS which makes lightrag's main() return early — remove it
os.environ.pop("GUNICORN_CMD_ARGS", None)

port = os.environ.get("PORT", "9621")
sys.argv = ["lightrag-server", "--host", "0.0.0.0", "--port", port]

from lightrag.api.lightrag_server import main
main()
