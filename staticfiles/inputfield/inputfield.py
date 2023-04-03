from django_components import component


@component.register("inputfield")
class Inputfield(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found.
    # To customize which template to use based on context you can override def get_template_name() instead of
    # specifying the below variable.
    template_name = "inputfield/inputfield.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self, label, field, form):
        return {
            "label": label,
            "field": field,
            "form": form,
        }

    # class Media:
        # js = "inputfield/inputfield.html"
        # css = "inputfield/inputfield.css"
