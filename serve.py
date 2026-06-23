import os
import sys

port = os.environ.get("PORT", "9621")
sys.argv = ["lightrag-server", "--host", "0.0.0.0", "--port", port]

from lightrag.api.lightrag_server import main
main()
