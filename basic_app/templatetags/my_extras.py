from django import template
register = template.Library()

# decorator


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of the "arg" string
    """
    return value.replace(arg, '')


# register.filter('cut', cut)
