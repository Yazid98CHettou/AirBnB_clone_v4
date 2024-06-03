#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify, request, make_response, abort
from models import storage
from models.amenity import Amenity

@app_views.route('/amenities', strict_slashes=False)
def all_amenities():
    amenities_list = []
    amenities_obj = storage.all("Amenity")
    for _, value in amenities_obj.items():
        amenities_list.append(value.to_dict())
    return jsonify(amenities_list)

@app_views.route('/amenities/<amenity_id>')
def amenity(amenity_id):
    amenity = storage.get("Amenity", amenity_id)
    if amenity:
        return jsonify(amenity.to_dict())
    return jsonify({"error": "Not found"}), 404

@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def del_amenity(amenity_id):
    amenity = storage.get("Amenity", amenity_id)
    if amenity:
        storage.delete(amenity)
        storage.save()
        return jsonify({})
    return jsonify({"error": "Not found"}), 404

@app_views.route('/amenities', strict_slashes=False, methods=['POST'])
def create_amenity():
    if not request.get_json():
        return make_response(jsonify({"error": 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": 'Missing name'}), 400)
    amenity = request.get_json()
    new_amenity = Amenity(**amenity)
    storage.new(new_amenity)
    storage.save()
    return jsonify(new_amenity.to_dict()), 201

@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    amenity = storage.get('Amenity', amenity_id)
    if not amenity:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({"error": 'Not a JSON'}), 400)
    params = request.get_json()
    skip = ['id', 'created_at', 'updated_at']
    for key, value in params.items():
        if key not in skip:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict())

@app_views.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Not found"}), 404

