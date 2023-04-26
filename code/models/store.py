from db import db

#creates a mapping
class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    #cascade=all, delete - this deletes the parent (store) and all children (items)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
