from common.models import *

class Title(TimeStampedBaseModel):
    """
    """
    __tablename__ = 'title'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), name='name')
    isAdult = Column(Integer,name='isAdult')
    startYear = Column(String, name='startYear')
    releasedate = Column(DateTime, name='releasedate')
    runtimeMinutes = Column(String, name='runtimeMinutes')
    genres = Column(Boolean, default=False)
    pic_url = Column(String,name='pic_url')
    description = Column(String(2000),name='description')
    rating = Column(Float)
    language = Column(String(100),name='language')

    info = db.relationship('Info', backref='title', lazy=True)

    def __repr__(self):
        return self.name



class Info(TimeStampedBaseModel):
    __tablename__ = 'info'

    id = Column(Integer, primary_key=True)
    title_id = Column(Integer, ForeignKey('title.id'))
    crew_id = Column(Integer,ForeignKey('crew_identifier.id'))
    crew_name = Column(String(256),name='crew_name')

    def __repr__(self):
        return self.crew_name


class CrewIdentifier(TimeStampedBaseModel):
    __tablename__ = 'crew_identifier'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), name='name')
    info = db.relationship('Info',backref='crew_identifier',lazy=True)

    def __repr__(self):
        return self.name
