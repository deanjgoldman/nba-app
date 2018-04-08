from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import SelectField

import nbapi

app = Flask(__name__)

app.secret_key = 's3cr3t'
csrf = CSRFProtect(app)

teams = [(x, x) for x in nbapi.team_names]
seasons = [(x, x) for x in nbapi.seasons()]


class TeamForm(FlaskForm):
    team_name = SelectField("Team Name", choices=teams)
    season = SelectField("Season", choices=seasons)


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        form = TeamForm()
        return render_template("index.html", form=form)
    else:
        roster = nbapi.get_roster(request.values["team_name"],
                                  request.values['season'])
        return render_template("index.html", roster=roster.to_html())

if __name__ == "__main__":
    app.run(debug=True)
