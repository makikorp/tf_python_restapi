import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from models import ItemModel

#from db import items
from db import db
from schemas import ItemSchema, ItemUpdateSchema


blp = Blueprint("items", __name__, description="api operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item
        #raise NotImplementedError("Getting an item is not implemented")
        # try:
        #     return items[item_id]
        # except KeyError:
        #     abort(404, message="Item not found.")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)
        if item:
            item.carbs = item_data["carbs"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)
        
        db.session.add(item)
        db.session.commit()

        return item
        #raise NotImplementedError("Getting an item is not implemented")             
        # item_data = request.get_json()
        # try:
        #     item = items[item_id]
        #     item |= item_data

        #     return item
        # except KeyError:
        #     abort(404, message="Item not found")

    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted"}
        #raise NotImplementedError("Getting an item is not implemented")        
        # try:
        #     del items[item_id]
        #     return {"message": "Item deleted."}
        # except KeyError:
        #     abort(404, message="Item not found.")    

@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()
        # raise NotImplementedError("Getting an item is not implemented")
        # return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")
        return item

        #        raise NotImplementedError("Getting an item is not implemented")
        # for item in items.values():
        #     if (
        #         item_data["name"] == item["name"]
        #         and item_data["store_id"] == item["store_id"]
        #     ):
        #         abort(400, message=f"Item already exists.")
        
        # item_id = uuid.uuid4().hex
        # item = {**item_data, "id": item_id}
        # items[item_id] = item
        # return item, 201

