from django.utils.functional import partition
from flask import jsonify
from marshmallow import pre_dump, fields


from config.constants import marshmallow, db

from .models import *

class InfoSetupSchema(marshmallow.ModelSchema):
    crew_profession = marshmallow.Method('get_crew_name')
    class Meta:
        model = Info

    def get_crew_name(self,obj):
        crew_name = db.session.query(CrewIdentifier.name).filter(CrewIdentifier.id==obj.crew_id).first()
        return crew_name.name



class MovieSetupSchema(marshmallow.ModelSchema):
    info = marshmallow.Nested('InfoSetupSchema',many=True,exclude=['created_on','updated_on','title','id','crew_identifier'])
    class Meta:
        model = Title


MovieSetupSerializer = MovieSetupSchema()
MovieSetupListSerializer = MovieSetupSchema(many=True,exclude=['created_on','updated_on'])