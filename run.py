# -*- coding: utf-8 -*-

import config
from __init__ import create_app

if __name__ == "__main__":
    app = create_app(config)

    app.run('localhost', port=8088, debug=True)
