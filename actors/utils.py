from django.utils.text import slugify


def first_and_last_name_to_username(first_name, last_name):
    def clean(str_in):
        # Using the replace because default separator for slugify is dash
        return slugify(str_in).replace('-', '_')

    return clean(first_name) + '_' + clean(last_name)