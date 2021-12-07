""" A PlantController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Plant import Plant

class PlantController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", PlantController)
        """
        id = self.request.param("id")
        return Plant.find(id)
        

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", PlantController)
        """
        return Plant.all()


    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", PlantController)
        """
        name = self.request.input("name")
        description = self.request.input("description")
        image = self.request.input("image")
        plant = Plant.create({"name": name, "description": description, "image": image})
        return plant


    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", PlantController)
        """
        name = self.request.input("name")
        description = self.request.input("description")
        image = self.request.input("image")
        id = self.request.param("id")
        Plant.where("id", id).update({"name": name, "description": description, "image": image})
        return Plant.where("id", id).get()
        

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", PlantController)
        """
        id = self.request.param("id")
        plant = Plant.where("id", id).get()
        Plant.where("id", id).delete()
        return plant