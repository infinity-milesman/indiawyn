import os

from flask.views import MethodView
from sqlalchemy import desc
from werkzeug.utils import secure_filename


from .serializers import *
from flask import jsonify, request, render_template, redirect, url_for, flash

from config.constants import db_session, app
from .models import *


def movies(title_id=None):
    single_movie_serializer = MovieSetupSerializer
    many_movie_serializer = MovieSetupListSerializer
    if title_id:
        portal = db.session.query(Title).filter(Title.id == title_id).first()
        # portal = Title.query.filter_by(Title.id==title_id).first()
        if not portal:
            return jsonify({'details': '{} Does not Exists'.format(title_id)}), 404

        output = single_movie_serializer.dump(portal).data
        info = output['info']
        actor_list = []
        director_list = []
        writer_list = []
        for i in info:
            prof = (i['crew_profession'])
            if prof == 'Actor':
                actor_list.append(i['crew_name'])
            elif prof == 'Director':
                director_list.append(i['crew_name'])
            else:
                writer_list.append(i['crew_name'])
        new_dict = dict(actors=actor_list, directors=director_list, writers=writer_list)
        output['info'] = new_dict
        from dateutil.parser import parse
        get_date_obj = parse(output['releasedate'])
        print(get_date_obj.year)
        output['release_year'] = get_date_obj.year
        output['releasedate'] = get_date_obj.date()
        context = {'movie': output}
        return render_template('indiawyn/detailed.html', **context)

    portals = Title.query.all()
    output = many_movie_serializer.dump(portals).data
    # print(output)
    for title in output:
        info = title['info']
        actor_list = []
        director_list = []
        writer_list = []
        for i in info:
            prof = (i['crew_profession'])
            if prof == 'Actor':
                actor_list.append(i['crew_name'])
            elif prof == 'Director':
                director_list.append(i['crew_name'])
            else:
                writer_list.append(i['crew_name'])
        new_dict = dict(actors=actor_list, directors=director_list, writers=writer_list)
        title['info'] = new_dict
        from dateutil.parser import parse
        get_date_obj = parse(title['releasedate'])
        title['release_year'] = get_date_obj.year
        title['releasedate'] = get_date_obj.date()
    context = {'movies': output}
    return render_template('indiawyn/index.html', **context)


class MovieSetupAPI(MethodView):
    single_movie_serializer = MovieSetupSerializer
    many_movie_serializer = MovieSetupListSerializer

    def get(self, title_id=None):
        print(title_id)
        if title_id:
            portal = db.session.query(Title).filter(Title.id==title_id).first()
            # portal = Title.query.filter_by(Title.id==title_id).first()
            if not portal:
                return jsonify({'details': '{} Does not Exists'.format(title_id)}), 404

            output = self.single_movie_serializer.dump(portal).data
            info = output['info']
            actor_list = []
            director_list = []
            writer_list = []
            for i in info:
                prof = (i['crew_profession'])
                if prof == 'Actor':
                    actor_list.append(i['crew_name'])
                elif prof == 'Director':
                    director_list.append(i['crew_name'])
                else:
                    writer_list.append(i['crew_name'])
            new_dict = dict(actors=actor_list, directors=director_list, writers=writer_list)
            output['info'] = new_dict
            return jsonify(output), 200

        portals = Title.query.all()
        output = self.many_movie_serializer.dump(portals).data
        # print(output)
        for title in output:
            info = title['info']
            actor_list = []
            director_list = []
            writer_list = []
            for i in info:
                prof = (i['crew_profession'])
                if prof == 'Actor':
                    actor_list.append(i['crew_name'])
                elif prof == 'Director':
                    director_list.append(i['crew_name'])
                else:
                    writer_list.append(i['crew_name'])
            new_dict = dict(actors=actor_list, directors=director_list,writers = writer_list)
            title['info'] = new_dict
            # title['releasedate'] = title['releasedate'].date
            print(title['releasedate'])
            from dateutil.parser import parse
            get_date_obj = parse(title['releasedate'])
            print(get_date_obj.year)
            title['release_year'] = get_date_obj.year
            title['releasedate']=get_date_obj.date()
        return jsonify(output), 200


movie_setup_api = MovieSetupAPI.as_view('movies_api')