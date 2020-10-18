from django import template

register = template.Library()


@register.filter(name='range_bunk')
def _range(_min, args=None):
    _max, _step = None, None
    if args:
        if not isinstance(args, int):
            _max, _step = map(int, args.split(','))
        else:
            _max = args
    args = filter(None, (_min, _max, _step))


@register.filter(name='range')
def filter_range(start, end):
    return range(start, end)
