# -*- coding:utf-8 -*-
import os

from werkzeug.utils import secure_filename

from admin.upload.config import config, upload_status


# 文件上传类
class FileUpload(object):
    def __init__(self, file):
        self.file = file

    def _allowed_file(self):
        return '.' in self.file.filename and \
               '.' + self.file.filename.rsplit('.', 1)[1].lower() in config["imageAllowFiles"]

    def _check_size(self):
        return 0 < len(self.file.read()) <= config["imageMaxSize"]

    def save_file(self):
        resp = {
            "state": "",
            "url": "",
            "title": "OriginFileName",
            "original": "Result.OriginFileName",
            "error": "Result.ErrorMessage",
        }
        if not self._allowed_file():
            resp["state"] = upload_status["TypeNotAllow"]
            return resp

        # if not self._check_size():
        #      resp["state"] = upload_status["SizeLimitExceed"]
        #      return resp
        filename = secure_filename(self.file.filename)
        try:
            path = os.path.join(config["imagePathFormat"])
            if not os.path.exists(path):
                os.makedirs(path)
            self.file.save(os.path.join(config["imagePathFormat"], filename))
            resp["state"] = upload_status["Success"]
            resp["url"] = config["imagePathFormat"]
            resp["title"] = filename
            resp["original"] = filename
        except IOError as e:
            resp["state"] = upload_status["FileAccessError"]
            resp["error"] = e.strerror
        return resp
