# -*- oding:utf-8 -*-

from flask import request

from admin import admin
from admin.upload import FileUpload


# @admin.route("/filehandler")
# def filehandler():
#     action = request["action"]
#     if action == "uploadimage":
#         file = request.files[0]
#         upload = FileUpload(file)
#         return  upload.save()
#     elif action == "uploadfile":
#         pass
