import logging
from flask import Flask, make_response
from utils import list_files

app = Flask(__name__)

logger = logging.getLogger('listfile')


@app.route("/storage/<path:prefix>")
@app.route("/storage", defaults={"prefix": ""})
def storage(prefix):
    contents, success = list_files(prefix)
    logger.info("*****Start listing directory {}".format(prefix))
    if not success:
        return make_response({"error": "failed"}, 500)
    return make_response({"files": contents}, 200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
