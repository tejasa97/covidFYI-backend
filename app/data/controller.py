# from app.data import data_bp
# from app.data.models import InfoType, Entry, Location
# from itertools import chain
# from flask import jsonify, request, make_response, abort, Response
# import json

# @data_bp.route('/')
# def ping():

#     return json.dumps({
#         "hello" : "world"
#     })

# @data_bp.route('/states/')
# def list_states():

#     response = {}

#     locations = Location.query.with_entities(Location.state).distinct().order_by(Location.state).all()
#     response = {
#         'states': list(chain(*locations))
#     }

#     return Response(json.dumps(response), 
#         mimetype='application/json', status=200)

# @data_bp.route('/info_types/')
# def list_info_types():

#     response = {}
#     info_types = InfoType.query.all()

#     for info_type in info_types:
#         response[info_type.name] = {
#                 'description' : info_type.description,
#                 'active'      : info_type.active,
#                 'states'      : list(chain(*info_type.entries.join(Location).\
#                     distinct(Location.state).values('state')))
#             }

#     return Response(json.dumps(response), 
#         mimetype='application/json', status=200)

# @data_bp.route('/states/<string:state_name>/')
# def get_state(state_name):

#     response = {}
    
#     locations = Location.query.filter(Location.state==state_name).distinct('city').join(Entry).all()

#     for loc in locations:
#         response[loc.city] = [entry.toJson() for entry in loc.entries]

#     return Response(json.dumps(response), 
#         mimetype='application/json', status=200)
        