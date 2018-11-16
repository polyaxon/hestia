def memoize(func):
    """
    Provides memoization for methods on a specific instance.
    Results are cached for given parameter list.

    See also: http://en.wikipedia.org/wiki/Memoization

    N.B. The cache object gets added to the instance instead of the global scope.
    Therefore cached results are restricted to that instance.
    The cache dictionary gets a name containing the name of the decorated function to
    avoid clashes.

    Example:

        class MyClass(object):
            @memoize
            def foo(self, a, b):
                return self._do_calculation(a, b)

    HINT: - The decorator does not work with keyword arguments.
    """

    cache_name = '__CACHED_{}'.format(func.__name__)

    def wrapper(self, *args):
        cache = getattr(self, cache_name, None)
        if cache is None:
            cache = {}
            setattr(self, cache_name, cache)
        if args not in cache:
            cache[args] = func(self, *args)
        return cache[args]

    return wrapper
