#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify, request, make_response, abort
from models import storage
from models.city import City
from models.place import Place

@app_views.route('/cities/<city_id>/places', strict_slashes=False)
def places_by_city(city_id):
    list_place = []
    city = storage.get("City", city_id)
    if city:
        for place in city.places:
            list_place.append(place.to_dict())
        return jsonify(list_place)
    return jsonify({"error": "Not found"}), 404

@app_views.route('/places/<place_id>')
def places_by_id(place_id):
    place = storage.get("Place", place_id)
    if place:
        return jsonify(place.to_dict())
    return jsonify({"error": "Not found"}), 404

@app_views.route('/places/<place_id>', methods=['DELETE'])
def del_place(place_id):
    place = storage.get("Place", place_id)
    if place:
        storage.delete(place)
        storage.save()
        return jsonify({}), 200
    return jsonify({"error": "Not found"}), 404

@app_views.route('/cities/<city_id>/places', strict_slashes=False, methods=['POST'])
def create_place(city_id):
    if not request.get_json():
        return make_response(jsonify({"error": 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": 'Missing name'}), 400)
    if 'user_id' not in request.get_json():
        return make_response(jsonify({"error": 'Missing user_id'}), 400)
    
    city = storage.get("City", city_id)
    if not city:
        abort(404)
    
    place = request.get_json()
    user = storage.get("User", place["user_id"])
    if not user:
        abort(404)
    
    place['city_id'] = city_id
    new_place = Place(**place)
    storage.new(new_place)
    storage.save()
    return jsonify(new_place.to_dict()), 201

@app_views.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    place = storage.get('Place', place_id)
    if not place:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({"error": 'Not a JSON'}), 400)
    params = request.get_json()
    skip = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
    for key, value in params.items():
        if key not in skip:
            setattr(place, key, value)
    storage.save()
    return jsonify(place.to_dict())

@app_views.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Not found"}), 404

