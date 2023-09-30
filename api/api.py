import os
import random
import re
from tmdbv3api import TMDb
from tmdbv3api import Movie

from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_cors import CORS
# from flask_session import Session
from tempfile import mkdtemp
from datetime import datetime
from helpers import apology, trailer
from difflib import SequenceMatcher
# import openai
# import movieposters as mp

app = Flask(__name__)
CORS(app)

app.config["TEMPLATES_AUTO_RELOAD"] = True
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# Session(app)


tmdb = TMDb()
tmdb.api_key = '39efdc94b5e403f01fd0d0343658a990'
movie = Movie()
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# openai.api_key = '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'


@app.route("/home")
def home():
    # def generate_prompt():
    #         return """suggest me the top 10 popular movies of all time, without the years"""

    # response = openai.Completion.create(
    #             model="text-davinci-003",
    #             prompt=generate_prompt(),
    #             temperature=0.7,
    #             max_tokens=256,
    #             top_p=1,
    #             frequency_penalty=0,
    #             presence_penalty=0
    #         )
    # res = str(response.choices[0].text)
    
    # lines = res.split("\n")
    # result = []
    # for line in lines[2:]:
    #     parts = line.split(". ")
    #     id = int(parts[0])
    #     name = parts[1]
    #     result.append({"id": id, "name": name, "poster": ""})
    # for i in result:
    #     link = mp.get_poster(title=i['name'])
    #     i['poster'] = link
    # print(result)
    # movies = result
    movies = [
    {'id': 1, 'title': 'The Godfather', 'poster': '/3bhkrj58Vtu7enYsRolD1fZdja1.jpg'}, 
    {'id': 2, 'title': 'Avatar', 'poster': '/jRXYjXNq0Cs2TcJjLkki24MLp7u.jpg'},
    {'id': 3, 'title': 'The Shawshank Redemption', 'poster': '/hBcY0fE9pfXzvVaY4GKarweriG2.jpg'},
    {'id': 4, 'title': 'The Dark Knight', 'poster': '/qJ2tW6WMUDux911r6m7haRef0WH.jpg'},
    {'id': 5, 'title': 'Schindler’s List', 'poster': '/sF1U4EUQS8YHUYjNl3pMGNIQyr0.jpg'},
    {'id': 6, 'title': 'Pulp Fiction', 'poster': '/fIE3lAGcZDV1G6XM5KmuWnNsPp1.jpg'},
    {'id': 7, 'title': 'Star Wars', 'poster': '/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg'},
    {'id': 8, 'title': 'The Lord of the Rings: The Fellowship of the Ring', 'poster': '/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg'},
    {'id': 9, 'title': 'Goodfellas', 'poster': "/aKuFiU82s5ISJpGZp7YkIr3kCUd.jpg"},
    {'id': 10, 'title': 'The Wolf of Wall Street', 'poster': "/34m2tygAYBGqA9MXKhRDtzYd4MR.jpg"}
    ]
    print(movies)
    return jsonify(movies)

@app.route("/moviename", methods = ["GET", "POST"])
def inputs():
    if request.method == 'GET':
        data = [{"id": 1, "name": "bruh"}]
        return jsonify(data)
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        title1 = data.get('title1')
        print(title1)
        title2 = data.get('title2')
        output = f'the output is {title1}, {title2}'
        print(title1, title2)
        movies = []
        if title1:
            x = movie.search(title1) # getting a list of movies with that name
            title1 = re.sub('[\W_]+', '', title1)
            if len(x) < 1:
                return apology("What you've inputted is either a TV show or a movie released in a parallel universe")
            title1_id = 0
            similarity_dict = {}
            for item in x:
                original_title1 = item["original_title"].upper()
                similarity_score = similar(re.sub('[\W_]+', '', original_title1), title1.upper())
                similarity_dict[item] = similarity_score
            item = max(similarity_dict, key=similarity_dict.get)     #using similarity score to obtain the right title a user looks for
            title1_id = item["id"]
            print("hi")
            print(item["id"])
            print("bye")
            print(item["original_title"])
            print(len(movie.recommendations(movie_id=title1_id))) #for some reason the API can't find recommendations for 'The good, the bad and the ugly'
            # print(original_title1, title1_id)
            # ensuring that title1 exists
            if title1_id == None or title1_id == 0:
                title1 = None
            else:
                recommendations1 = movie.recommendations(movie_id=title1_id)
                for item in recommendations1:
                    movies.append(item["original_title"])

        if title2:
            title2 = re.sub(r'[^\w\s]', '', title2)
            y = movie.search(title2)  # getting a list of movies with that name
            title2_id = 0
            for item in y:
                original_title2 = item["original_title"].upper()
                if title2 in re.sub(r'[^\w\s]', '', original_title2) or re.sub(r'[^\w\s]', '', original_title2) in title2:
                    title2_id = item["id"]
                    break
                else:
                    title2_id = None
            print(original_title2)
            if title2_id == None or title2_id == 0:
                title2 = None
            else:
                recommendations2 = movie.recommendations(movie_id=title2_id)
                for item in recommendations2:
                    movies.append(item["original_title"])


        if len(movies) > 0:
            if title1 in movies:
                movies.remove(title1)
            if title2 in movies:
                movies.remove(title2)

            # random_movie = random.choice(movies) # returns a random movie from the recommended movies list
            # z = movie.search(random_movie)
            # for item in z:
            #     # if item["original_title"] in session["data"]:
            #     #     print(item["original_title"])
            #     #     movies.remove(item["original_title"])
            #     # else:
            #     #     session["data"].append(item["original_title"])
            #     if item["original_title"] == random_movie:
            #         random_movie_poster = item.poster_path
            #         trailer_key = trailer(item["id"])
            #         break
            # print(random_movie_poster)
            # print(trailer_key)
            # print(movies)
        recommended_movies = []
        for idx, movie_name_ in enumerate(movies):
            rec_movies = movie.search(movie_name_)
            for i in rec_movies:
                if i["original_title"] == movie_name_:
                    rec_poster = i.poster_path
                    break
            recommended_movies.append({"id": idx+1, "title": movie_name_, "poster": rec_poster})
        print(recommended_movies)
        return jsonify(recommended_movies)
        # return jsonify({"title": random_movie, "poster": random_movie_poster})
    # if request.method == 'POST':
    #     # list of recommended movies
    #     movies = []
    #     title1 = request.form.get("title_1").upper()
    #     title2 = request.form.get("title_2").upper()

    #     if not title1 and not title2:
    #         return apology("Come on! You've gotta have a favourite movie")

    #     if title1:
    #         x = movie.search(title1) # getting a list of movies with that name
    #         title1 = re.sub('[\W_]+', '', title1)
    #         if len(x) < 1:
    #             return apology("What you've inputted is either a TV show or a movie released in a parallel universe")
    #         title1_id = 0
    #         similarity_dict = {}
    #         for item in x:
    #             original_title1 = item["original_title"].upper()
    #             similarity_score = similar(re.sub('[\W_]+', '', original_title1), title1.upper())
    #             similarity_dict[item] = similarity_score
    #             # if title1 in re.sub(r'[^\w\s]', '', original_title1) or re.sub(r'[^\w\s]', '', original_title1) in title1:
    #             # print(re.sub('[\W_]+', '', original_title1), title1.upper())
    #             # if title1.upper() == re.sub('[\W_]+', '', original_title1): #there is something WRONG WITH THIS LINE: FIX IT!!!!!!!!!!!!!!!!!! || ***UPDATE: found the problem. we aren't accounting for the fact that what if certain special characters like & can be input as "and" but the program doesn't know that.
    #             #     print("YESSIRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    #             #     title1_id = item["id"]
    #             #     break
    #             # elif title1.upper() in re.sub('[\W_]+', '', original_title1) or re.sub('[\W_]+', '', original_title1) in title1.upper(): #there is something WRONG WITH THIS LINE: FIX IT!!!!!!!!!!!!!!!!!!
    #             #     print("YESSIRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    #             #     title1_id = item["id"]
    #             #     break
    #             # else:
    #             #     title1_id = None
    #         item = max(similarity_dict, key=similarity_dict.get) #using similarity score to obtain the right title a user looks for
    #         title1_id = item["id"]
    #         print("hi")
    #         print(item["id"])
    #         print("bye")
    #         print(item["original_title"])
    #         print(len(movie.recommendations(movie_id=title1_id))) #for some reason the API can't find recommendations for 'The good, the bad and the ugly'
    #         # print(original_title1, title1_id)
    #         # ensuring that title1 exists
    #         if title1_id == None or title1_id == 0:
    #             title1 = None
    #         else:
    #             recommendations1 = movie.recommendations(movie_id=title1_id)
    #             for item in recommendations1:
    #                 movies.append(item["original_title"])

    #     if title2:
    #         title2 = re.sub(r'[^\w\s]', '', title2)
    #         y = movie.search(title2)  # getting a list of movies with that name
    #         title2_id = 0
    #         for item in y:
    #             original_title2 = item["original_title"].upper()
    #             if title2 in re.sub(r'[^\w\s]', '', original_title2) or re.sub(r'[^\w\s]', '', original_title2) in title2:
    #                 title2_id = item["id"]
    #                 break
    #             else:
    #                 title2_id = None
    #         print(original_title2)
    #         if title2_id == None or title2_id == 0:
    #             title2 = None
    #         else:
    #             recommendations2 = movie.recommendations(movie_id=title2_id)
    #             for item in recommendations2:
    #                 movies.append(item["original_title"])


    #     if len(movies) > 0:
    #         if title1 in movies:
    #             movies.remove(title1)
    #         if title2 in movies:
    #             movies.remove(title2)
    #         for i in session["data"]:
    #             if i in movies:
    #                 movies.remove(i)
    #         if len(movies) == 0:
    #             movies = session["data"]
    #             session["data"] = []

    #         random_movie = random.choice(movies) # returns a random movie from the recommended movies list
    #         z = movie.search(random_movie)
    #         for item in z:
    #             # if item["original_title"] in session["data"]:
    #             #     print(item["original_title"])
    #             #     movies.remove(item["original_title"])
    #             # else:
    #             #     session["data"].append(item["original_title"])
    #             if item["original_title"] == random_movie:
    #                 session["data"].append(item["original_title"])
    #                 random_movie_poster = item.poster_path
    #                 trailer_key = trailer(item["id"])
    #                 break
    #         # print(random_movie_poster)
    #         # print(trailer_key)
    #         print(session["data"])
    #         print(movies)
    #         # print(movies)
    #         return render_template("generate.html", movie = random_movie, poster = random_movie_poster, key = trailer_key)
    #     else:
    #         return apology("I'm sorry but I did'nt watch this movie, so i couldn't find any recommendations.")