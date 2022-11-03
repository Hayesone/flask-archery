from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template("landing.html")


@app.route('/our-services')
def shop_services():
    return render_template("subcategory/shop-services.html")


@app.route('/archery-coaching')
def coaching_development():
    return render_template("subcategory/coaching-dev.html")


@app.route('/starting-out-archery')
def starting_out_archery():
    return render_template("subcategory/starting_out_archery.html")


# region Our Services content pages
@app.route('/our-services/corporate-events')
def ss_corporate():
    return render_template("subcategory/services/corporate.html")


@app.route('/our-services/parties')
def ss_parties():
    return render_template("subcategory/services/parties.html")


@app.route('/our-services/compound-bow-check-up')
def ss_compound():
    return render_template("subcategory/services/compound-checkup.html")


@app.route('/our-services/recurve-bow-check-up')
def ss_recurve():
    return render_template("subcategory/services/recurve-checkup.html")


@app.route('/our-services/arrow-building')
def ss_arrow():
    return render_template("subcategory/services/arrow-building.html")


@app.route('/our-services/string-making')
def ss_string():
    return render_template("subcategory/services/string-making.html")


# endregion

# Shop routes straight to the shop

# region Coaching & Development

@app.route('/archery-coaching/one-to-one-coaching')
def coaching_1to1():
    return render_template("subcategory/archery-coaching/1-1-coaching.html")


@app.route('/archery-coaching/group-coaching-courses')
def coaching_group():
    return render_template("subcategory/archery-coaching/group-coaching.html")


@app.route('/archery-coaching/third-eye-archery-training')
def coaching_third():
    return render_template("subcategory/archery-coaching/third-eye.html")


# endregion

# region Info on Archery & Products

@app.route('/starting-out-archery/have-a-go-sessions')
def starting_out_have_a_go():
    return render_template("subcategory/starting-out-in-archery/have-a-go.html")


@app.route('/starting-out-archery/beginner-courses')
def starting_out_beginners():
    return render_template("subcategory/starting-out-in-archery/beginners-courses.html")


@app.route('/starting-out-archery/your-first-kit')
def starting_out_your_first_kit():
    return render_template("subcategory/starting-out-in-archery/your-first-kit.html")


@app.route('/starting-out-archery/local-clubs')
def starting_out_local_clubs():
    return render_template("subcategory/starting-out-in-archery/local-clubs.html")

# No route for kent archery as direct link out

# No route for archery gb  as direct link out


if __name__ == '__main__':
    app.run()
