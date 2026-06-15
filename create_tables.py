from database import Base,engine
from models import Product,Stock_movement,Supplier,Category

Base.metadata.create_all(engine)
print('tables has been created')