from django.template import Library

register = Library()

@register.filter
def partition(master_list, n):
    """
    Break a list into sublists of length ``n``. That is, 
    ``partition(range(10), 4)`` gives::
    
        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10]]
    """
    try:
        n = int(n)
        master_list = list(master_list)
    except (ValueError, TypeError):
        return [master_list]
    return [master_list[i:i+n] for i in range(0, len(master_list), n)]