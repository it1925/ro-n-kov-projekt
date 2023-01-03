from flask_appbuilder import ModelRestApi
from flask_appbuilder.api import BaseApi, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.filters import BaseFilter
from sqlalchemy import or_

from . import appbuilder, db
from .models import ModelCategory, ModelFiles
from marshmallow import fields, Schema


class ModelCategoryApi(ModelRestApi):
    resource_name = 'category'
    datamodel = SQLAInterface(ModelCategory)
    allow_browser_login = True
    
class ModelFilesApi(ModelRestApi):
    resource_name='models'
    datamodel= SQLAInterface(ModelFiles)
    allow_browser_login = True


db.create_all()
appbuilder.add_api(ModelCategoryApi)
appbuilder.add_api(ModelFilesApi)