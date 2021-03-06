from flask import Blueprint, render_template, redirect, url_for, flash, request
from services.AnimalService import AnimalService
from forms import SearchForm, CreateAnimal


animals = Blueprint('animals', __name__)

animalService = AnimalService()


@animals.route('/', methods=['GET', 'POST'])
def search():
    search_form, create_form = SearchForm(), CreateAnimal()
    if search_form.validate_on_submit():
        result_search = animalService.search_by_name(name=search_form.name.data)
        content = {
            'result_search': result_search,
        }
        return render_template("search.html", content=content, search_form=search_form, create_form=create_form)
    return render_template("search.html", search_form=search_form, create_form=create_form, content=None)


@animals.route('/create', methods=['GET', 'POST'])
def create_animal():
    search_form, create_form = SearchForm(), CreateAnimal()
    if create_form.validate():
        animalService.create(create_form.name_animal.data,
                             create_form.type_animal.data,
                             create_form.speed_animal.data,
                             create_form.predator_animal.data)
        flash("Животное успешно создано!")
        return redirect(url_for('animals.search'))
    return render_template("search.html", search_form=search_form, create_form=create_form, content=None)