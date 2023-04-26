import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from models import StoreModel


#from db import stores
from db import db
from schemas import StoreSchema

blp = Blueprint("stores", __name__, description="api operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store
    #    raise NotImplementedError("Getting an item is not implemented")        
    #     try:
    #         return stores[store_id]
    #     except KeyError:
    #         abort(404, message="Store not found.")

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted"}
    #     try:
    #         del stores[store_id]
    #         return {"message": "Store deleted"}
    #     except KeyError:
    #         abort(404, message="Store not found.")

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()
        #store = StoreModel.get_or_404(store_id)        
        #raise NotImplementedError("Getting an item is not implemented")
        # return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A store with that name already exists"
            ) 
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the store.")
        return store
        
        #raise NotImplementedError("Getting an item is not implemented")        
        # store_data = request.get_json()
        # for store in stores.values():
        #     if store_data["name"] == store["name"]:
        #         abort(400, message=f"Store already exists.")

        # store_id = uuid.uuid4().hex
        # store = {**store_data, "id": store_id}
        # stores[store_id] = store

        # return store
