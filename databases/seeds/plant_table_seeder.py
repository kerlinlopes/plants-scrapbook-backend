"""PlantTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Plant import Plant

class PlantTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Plant.create({"name": "Honeysuckle", "description": "is a large, volubilate shrub of the genus Lonicera", "image": "https://cdn.britannica.com/03/75903-050-52BFC20C/yellow-orange-honeysuckle.jpg"})
        Plant.create({"name": "Poppy", "description": "have lobed or dissected leaves, milky sap, often nodding buds on solitary stalks, and four- to six-petaled flowers with numerous stamens surrounding the ovary.", "image": "https://www.gardeningknowhow.com/wp-content/uploads/2011/06/poppy-1.jpg"})
        Plant.create({"name": "Lavender", "description": "small, branching and spreading shrubs with grey-green leaves and long flowering shoots", "image": "https://www.provenwinners.com/sites/provenwinners.com/files/imagecache/500x500/ifa_upload/lavandula_sweet_romance_apj18_10.jpg"})
