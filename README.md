# Project 4 - Plants Scrapbook BACKEND
#### BY KERLIN

## Project Summary

Building a backend api project with Python-Masonite. Using a postgres database and having 1 model with CRUD routes.


## Models

Models:
```
Plant
 - name: String
 - description: String
 - image: String

```


## Route Table

| Route Name | URL | HTTP | Description |
|-----------|------|-------|-------------|
| INDEX | / | GET | Render all of our plants 
| SHOW | /post/:id | GET | Render an individual plant page
| NEW | /new | GET | render our Form component for creating a new plant
| EDIT | /edit | GET | Renders our Form to edit our plant
| UPDATE | /post/:id | PUT | Renders our Form to update our plant
| DELETE | /post/:id | DELETE | Deletes a plant

