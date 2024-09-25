from flask import Blueprint

routes = Blueprint('routes', __name__)

from .ColorList import ColorList
from .ManagerCar import ManagerCar
from .ManagerOwner import ManagerOwner
from .ManagerPedestrian import ManagerPedestrian
from .ManagerTransfer import ManagerTransfer
from .ModelList import ModelList
from .OwnerCars import OwnerCars

routes.add_url_rule("/car", view_func=ManagerCar.as_view('ManagerCar'), methods=['GET','POST'])
routes.add_url_rule("/list/colors", view_func=ColorList.as_view('ColorList'), methods=['GET'])
routes.add_url_rule("/list/models", view_func=ModelList.as_view('ModelList'), methods=['GET'])
routes.add_url_rule("/owner", view_func=ManagerOwner.as_view('ManagerOwner'), methods=['GET','POST'])
routes.add_url_rule("/owner/cars", view_func=OwnerCars.as_view('OwnerCars'), methods=['GET'])
routes.add_url_rule("/pedestrian", view_func=ManagerPedestrian.as_view('ManagerPedestrian'), methods=['GET'])
routes.add_url_rule("/transfer", view_func=ManagerTransfer.as_view('ManagerTransfer'), methods=['PUT'])