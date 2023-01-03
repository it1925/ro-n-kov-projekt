from flask import Markup, url_for
from flask_appbuilder.security.sqla.models import User
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from flask_appbuilder import Model

"""
You can use the extra Flask-AppBuilder fields and Mixin's
AuditMixin will add automatic timestamp of created and modified by who
"""

class MyUser(User):
    __tablename__ = 'ab_user'
    extra = Column(String(256))

class ModelCategory(AuditMixin, Model):
    __tablename__ = "model_category"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)


class ModelFiles(Model):
    __tablename__ = "model_files"
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("model_category.id"))
    model_category = relationship("ModelCategory")
    file = Column(FileColumn, nullable=False)
    img = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    description = Column(String(150))

    def download(self):
        return Markup(
            '<a href="'
            + url_for("ProjectFilesModelView.download", filename=str(self.file))
            + '">Download</a>'
        )

    def file_name(self):
        return (str(self.file))