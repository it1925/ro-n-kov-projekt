import os
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from flask_appbuilder.views import ModelView, CompactCRUDMixin
from flask_appbuilder import BaseView, expose
from flask import render_template
from flask import request, g
from app.models import ModelCategory, ModelFiles
from app import appbuilder, db, app


def get_user():
    return g.user

class FilesView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(ModelFiles, db.session)
    base_filters = [['created_by', FilterEqualFunction, get_user],]
    
    label_columns = {"file_name": "File Name", "download": "Download"}
    add_columns = ["file", "description", "model_category"]
    edit_columns = ["file", "description", "model_category"]
    list_columns = ["file_name", "model_category", "created_by"]
    show_columns = ["file_name", "model_category", "created_by"]
    

class CategoryView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(ModelCategory)
    related_views = [FilesView]
    

    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"

    add_columns = ["name"]
    edit_columns = ["name"]
    list_columns = ["name", "created_by"]
    show_fieldsets = [
        ("Info", {"fields": ["name"]}),
        (
            "Audit",
            {
                "fields": ["created_by", "created_on", "changed_by", "changed_on"],
                "expanded": False,
            },
        ),
    ]
    

class HomePage(BaseView):
    route_base = "/homepage"
    
    
    @expose("/")
    def run(self):
        return self.render_template("myIndex.html", response = db.session.query(ModelFiles).all())
    
    @expose("/<string:param1>")
    def param1(self, param1):
        return self.render_template("modelview.html", param1 = param1, response = db.session.query(ModelFiles).filter_by(file = (param1)).first())
        

db.create_all()
appbuilder.add_view(
    CategoryView, "List ModelCategory", icon="fa-table", category="Categories"
)
appbuilder.add_view(FilesView, "List ModelFiles")
appbuilder.add_view_no_menu(HomePage())
