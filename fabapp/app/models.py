from flask import Markup, url_for, session
from flask_appbuilder.security.sqla.models import User
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref, query
from flask_appbuilder import Model

"""
You can use the extra Flask-AppBuilder fields and Mixin's
AuditMixin will add automatic timestamp of created and modified by who
"""


class ModelCategory(AuditMixin, Model):
    __tablename__ = "model_category"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    """ model_id = Column(Integer, ForeignKey('model_files.id')) """
    
    def __repr__(self):
        return self.name

class ModelFiles(AuditMixin, Model):
    __tablename__ = "model_files"
    id = Column(Integer, primary_key=True)
    file = Column(FileColumn, nullable=False)
    description = Column(String(150))
    category_id = Column(Integer, ForeignKey('model_category.id'))
    model_category = relationship(ModelCategory)

    @renders('created_by')
    def change_on(self):
        return Markup('<b>'+ self.created_by +'</b>')
        
        
    def file_name(self):
        return (str(self.file))
    
    def __repr__(self):
        return self.file