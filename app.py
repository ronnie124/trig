from flask import Flask, render_template, request, jsonify
from fractions import Fraction

import json
import logic

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/forum/')
def forum_home():
    return render_template("forum_home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/trigonometry/')
def trigonometry():
    return render_template("trigonometry.html")

@app.route('/algebra/')
def algebra():
    return render_template("algebra.html")

@app.route('/trianglesolver', methods=["GET"])
def triangle_get():
    return render_template("trianglesolver.html")

@app.route('/pythag', methods=["GET"])
def pythag_get():
    return render_template("pythag.html")

@app.route('/distance', methods=["GET"])
def distance_get():
    return render_template("distance.html")

@app.route('/sectorarea', methods=["GET"])
def sectorarea_get():
    return render_template("sectorarea.html")

@app.route('/sectorarea', methods=["POST"])
def sectorarea_post():
    print("SectorArea POST running...")
    content_dict = request.json
    for key in content_dict:
        print(key, '->', content_dict[key])

    logic.sector_area_receive(content_dict)

    return render_template("sectorarea.html", result=result)

@app.route('/pythag', methods=["POST"])
def pythag_post():
    print("Pythagorean POST running...")
    a_data = [request.form.get("a-pythag"), False]
    b_data = [request.form.get("b-pythag"), False]
    c_data = [request.form.get("c-pythag"), False]


    # fixme: Need to fix the data handling before fixing this function and sending data to logic.
    #data = check_lists(a_data,b_data,c_data) # Fix when data movement is fixed. (check_lists is deprecated)
    #a_data = [data[0], data[1]]
    #b_data = [data[2], data[3]]
    #c_data = [data[4], data[5]]

    #result = pythag_calculate(a_data, b_data, c_data)
    return render_template("pythag.html")

@app.route('/distance', methods=["POST"])
def distance_post():
    x1 = [request.form.get("x1"), False]
    x2 = [request.form.get("x2"), False]
    y1 = [request.form.get("y1"), False]
    y2 = [request.form.get("y2"), False]
    verified = True

    #data = check_lists(x1,x2,y1,y2)
    #for ver in data:
    #    print("Iterating:",ver)
    #   if ver is False:
    #        print("Found you bitch, you need all values.")
    #        verified = False

    #result = distance_calculate([data[0], data[2]], [data[4], data[6]], verified)
    return render_template("distance.html")



if __name__=="__main__":
    app.run(debug=True)