from flask import Blueprint, render_template
from services.AnimalService import AnimalService
from forms import SearchForm

animals = Blueprint('animals', __name__)

animalService = AnimalService()


@animals.route('/', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        result_search = animalService.search_by_name(name=form.name.data)
        content = {
            'result_search': result_search,
        }
        return render_template("search.html", content=content, form=form)
    return render_template("search.html", form=form, content=None)
