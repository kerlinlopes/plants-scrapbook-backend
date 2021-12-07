"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "PlantController@index").name("index"),
        Get("/@id", "PlantController@show").name("show"),
        Post("/", "PlantController@create").name("create"),
        Put("/@id", "PlantController@update").name("update"),
        Delete("/@id", "PlantController@destroy").name("destroy")
    ], prefix="/plants", name="plants")
]