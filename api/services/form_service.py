from api.repositories.form_repository import FormRepository


def save_form(data):
    FormRepository().save_form(data)


def get_forms():
    return FormRepository().get_forms()
