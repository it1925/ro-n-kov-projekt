import os
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView, CompactCRUDMixin
from flask_appbuilder import BaseView, expose
from flask import render_template
from app.models import ModelCategory, ModelFiles
from app import appbuilder, db, app


class ProjectFilesModelView(ModelView):
    datamodel = SQLAInterface(ModelFiles)

    label_columns = {"file_name": "File Name", "download": "Download"}
    add_columns = ["file", "description", "model_category"]
    edit_columns = ["file", "description", "model_category"]
    list_columns = ["file_name", "download"]
    show_columns = ["file_name", "download"]


class ProjectModelView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(ModelCategory)
    related_views = [ProjectFilesModelView]

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
    route_base = "/test"
    
    @expose("/")
    def run(self):
        return self.render_template("myIndex.html", file_list=os.listdir(app.config["UPLOAD_FOLDER"]))

db.create_all()
appbuilder.add_view(
    ProjectModelView, "List ModelCategory", icon="fa-table", category="ModelCategory"
)
appbuilder.add_view(ProjectFilesModelView, "List ModelFiles", category="ModelFiles")
appbuilder.add_view_no_menu(HomePage())
