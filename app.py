from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()
dict = {'Bob goes to space': '3 Stars',
        'The Revengers': '4 Stars',
        'Handy Man Can': '1 Stars'}

movie_repository.create_movie('Bob goes to space', "directory 1", '3 Stars')
movie_repository.create_movie('The Revengers', "directory 2", '4 Stars')
movie_repository.create_movie('Handy Man Can', "directory 3", '1 Stars')


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO:

    return render_template('list_all_movies.html', list_movies_active=True, dict=dict)


@app.get('/movies/new')
def create_movies_form():

    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    title = request.form.get('title')
    rating = request.form.get('rating')
    dict[title] = rating
    movie_repository.create_movie(request.form.get(
        'title'), request.form.get('director'), request.form.get('rating'))

    print(request.form)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3

    search_active = False

    search = request.args.get('search-field')
    print(search)
    if search is not None:
        search_active = True

        mr = movie_repository.get_movie_by_title(search)
        print(mr.title)

        return render_template('search_movies.html', search_active=search_active, movie_repository=mr)

    return render_template('search_movies.html', search_active=search_active)
