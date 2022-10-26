from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template("landing.html")


@app.route('/shop-services')
def shop_services():
    return render_template("subcategory/shop-services.html")


@app.route('/coaching-development')
def coaching_development():
    return render_template("subcategory/coaching-dev.html")


@app.route('/info')
def info():
    return render_template("subcategory/info.html")


# Contact Us routes to shop contact us

# region Shop & Services content pages
@app.route('/shop-services/corporate-events')
def ss_corporate():
    return render_template("subcategory/shop-services/corporate.html")


@app.route('/shop-services/parties')
def ss_parties():
    return render_template("subcategory/shop-services/parties.html")


@app.route('/shop-services/compound-bow-check-up')
def ss_compound():
    return render_template("subcategory/shop-services/compound-checkup.html")


@app.route('/shop-services/recurve-bow-check-up')
def ss_recurve():
    return render_template("subcategory/shop-services/recurve-checkup.html")


@app.route('/shop-services/arrow-building')
def ss_arrow():
    return render_template("subcategory/shop-services/arrow-building.html")


@app.route('/shop-services/string-making')
def ss_string():
    return render_template("subcategory/shop-services/string-making.html")


# endregion

# region Coaching & Development

@app.route('/coaching-development/one-to-one-coaching')
def coaching_1to1():
    return render_template("subcategory/coaching-dev/1-1-coaching.html")


@app.route('/coaching-development/group-coaching-courses')
def coaching_group():
    return render_template("subcategory/coaching-dev/group-coaching.html")


@app.route('/coaching-development/third-eye-archery-training')
def coaching_third():
    return render_template("subcategory/coaching-dev/third-eye.html")


# endregion

# region Info on Archery & Products

@app.route('/info/have-a-go-sessions')
def info_have_a_go():
    return render_template("subcategory/info/have-a-go.html")


@app.route('/info/beginner-courses')
def info_beginners():
    return render_template("subcategory/info/beginners-courses.html")


@app.route('/info/your-first-kit')
def info_your_first_kit():
    return render_template("subcategory/info/your-first-kit.html")


@app.route('/info/local-clubs')
def info_local_clubs():
    return render_template("subcategory/info/local-clubs.html")

# No route for kent archery as direct link out

# No route for archery gb  as direct link out


if __name__ == '__main__':
    app.run()
