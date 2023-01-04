import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_basicauth import BasicAuth

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["BASIC_AUTH_USERNAME"] = os.environ.get("BASIC_AUTH_USERNAME")
app.config["BASIC_AUTH_PASSWORD"] = os.environ.get("BASIC_AUTH_PASSWORD")

db = SQLAlchemy(app)
marsh = Marshmallow(app)
basic_auth = BasicAuth(app)


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(160), nullable=False)
    counter = db.Column(db.Integer)

    def __init__(self, text, counter):
        self.text = text
        self.counter = counter


class TextView(marsh.Schema):
    class Meta:
        fields = ("id", "text", "counter")


text_view = TextView()
texts_view = TextView(many=True)


@app.route("/", methods=["GET"])
@app.route("/text", methods=["GET"])
def get_texts():
    all_texts = Text.query.all()
    result = texts_view.dump(all_texts)

    return jsonify(result)


@app.route("/text/<id>", methods=["GET"])
def get_text(id):
    text = db.session.query(Text).with_for_update().filter_by(id=id).one_or_none()
    if text is not None:
        text.counter += 1
        db.session.commit()

    return text_view.jsonify(text)


@app.errorhandler(404)
def text_too_short(e):
    return "<h1>400</h1><p>Message too short</p>", 400


@app.route("/text", methods=["POST"])
@basic_auth.required
def add_text():
    text = request.form["text"]
    if text == "":
        return text_too_short(400)
    else:
        new_text = Text(text, 0)
        db.session.add(new_text)
        db.session.commit()

    return text_view.jsonify(new_text), 201


@app.route("/text/<id>", methods=["PUT"])
@basic_auth.required
def update_text(id):
    uptext = Text.query.get(id)
    text = request.form["text"]
    if text != "":
        uptext.text = text
        uptext.counter = 0
        db.session.commit()

    return text_view.jsonify(uptext), 200


@app.route("/text/<id>", methods=["DELETE"])
@basic_auth.required
def delete_text(id):
    text = Text.query.get(id)
    db.session.delete(text)
    db.session.commit()

    return text_view.jsonify(text), 204


if __name__ == "__main__":
    app.run(debug=True)
