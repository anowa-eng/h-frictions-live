import re

_eq = lambda k, v: lambda item: item.get(k) == v
_lt = lambda k, v: lambda item: item.get(k) < v
_gt = lambda k, v: lambda item: item.get(k) > v
_lt_eq = lambda k, v: lambda item: item.get(k) <= v
_gt_eq = lambda k, v: lambda item: item.get(k) >= v
_contains = lambda k, v: lambda item: v in item.get(k)

def matching_function(k, v):
    if '_lt' in k: return 'e'
def filter_list(_list, **kwargs):
    new_list = _list
    for k in kwargs:
        v = kwargs[k]
        new_list = list(filter(
            lambda item: item.get(k) == v,
            new_list
        ))
    return new_list
