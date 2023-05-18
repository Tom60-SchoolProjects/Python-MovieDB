# MovieDB

It is a movie management site where you can see a list of movies with their details and sometimes watch them.

Functionalities :
- Poster
- Title
- Description
- Year
- Actors
- Direction/Producer
- Face detection on the movie poster
- Watch GIF movie

## Installation

Go to release and download the [last version](https://github.com/Tom60chat/MovieDB/releases/latest) of the project.
Extract the archive and open a terminal in the folder.
Type this command to install all dependencies.
```shell
poetry install
```

## Usage

To launch the server, type this command in the terminal.
```shell
poetry run flask run
```

And go to http://localhost:5000/


## Movie management

You can add or delete movie with [Insomnia](https://insomnia.rest/) and [clone this workspace](https://insomnia.rest/run/?label=MovieDB&uri=https%3A%2F%2Fraw.githubusercontent.com%2FTom60chat%2FMovieDB%2Fmain%2FInsomnia.json)