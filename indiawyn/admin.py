from flask_admin.contrib.sqla import ModelView
from .models import *
from config.constants import db
from config.constants import app_admin as indiawyn_setup_admin



class BaseAdminView(ModelView):
    form_excluded_columns = ('created_on', 'updated_on', 'uuid')


class TitleForAdmin(BaseAdminView):
    form_excluded_columns = ('created_on', 'updated_on', 'uuid', 'info')
    column_list = ('name', 'isAdult','info')
    form_choices = {
        'isAdult': [
            ('1', 'Yes'),
            ('0', 'No')
        ]
    }
    pass


class InfoForAdminForAdmin(BaseAdminView):
    pass




class CrewIdentifierForAdmin(BaseAdminView):
    form_excluded_columns = ('created_on', 'updated_on', 'uuid','info')
    pass


indiawyn_setup_admin.add_view(TitleForAdmin(Title,db.session))
indiawyn_setup_admin.add_view(InfoForAdminForAdmin(Info,db.session))
indiawyn_setup_admin.add_view(CrewIdentifierForAdmin(CrewIdentifier,db.session))

