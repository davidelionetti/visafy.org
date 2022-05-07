from visafy_frontend import app
from flask import Markup
from datetime import datetime, timedelta


def brand_text(element='span', class_='color--primary'):
    return Markup('<{} class="{} logo-text">visa<span>f</span>y</{}>'.format(element, class_, element))


def typeahead(id, array, placeholder=None, value=None, container_class=None):
    return Markup(
        '<div class="typeahead-container text-center {}"><input type="text" class="text-center typeahead" id="{}" value="{}" name="input" placeholder=\'{}\' data-provide="typeahead" autocomplete="off"/></div>'.format(
            container_class, id, value, placeholder))


def get_visa_typeform_onclick(country_iso2, country_name, sid, source='', gclid='', fbclid='', cta=''):
    return Markup(
        "openVisaTypeform({'country_iso': '" + country_iso2 + "', 'country_name': '" + country_name + "', 'source': '" + source + "', 'gclid': '" + gclid + "', 'fbclid': '" + fbclid + "', 'cta': '" + cta + "', 'sid': '" + sid + "'});")


app.jinja_env.globals.update(brand_text=brand_text, typeahead=typeahead,
                             visa_onclick_cta=get_visa_typeform_onclick)


def create_slug(string):
    string = string.lower()

    string = string.replace(' ', '-').replace('\'', '-')

    if 'è' in string:
        string = string.replace('è', 'e')
    if 'é' in string:
        string = string.replace('é', 'e')
    if 'à' in string:
        string = string.replace('à', 'a')
    if 'á' in string:
        string = string.replace('á', 'a')
    if 'ò' in string:
        string = string.replace('ò', 'o')
    if 'ù' in string:
        string = string.replace('ù', 'u')
    if 'ì' in string:
        string = string.replace('ì', 'i')

    string = "".join([character for character in string if character.isalnum() or character == '-'])

    string = string.replace('--', '-')

    return string


@app.template_filter('formatdate')
def formattime(value, format='il %d/%m/%Y'):
    today = datetime.now()
    if today.date() == value.date():
        return 'Oggi'
    elif (today - timedelta(days=1)).date() == value.date():
        return 'Ieri'
    else:
        return value.strftime(format)


@app.template_filter('formatdatetime')
def formatdatetime(value, format='il %d/%m/%Y alle %H:%M'):
    today = datetime.now()
    if today.date() == value.date():
        return value.strftime('Oggi alle %H:%M')
    elif (today - timedelta(days=1)).date() == value.date():
        return value.strftime('Ieri alle %H:%M')
    else:
        return value.strftime(format)
