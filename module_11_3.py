def introspection_info(obj):
    date = {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'methods': [attr for attr in dir(obj) if callable(getattr(obj, attr))],
        'module': __name__
    }
    return date


number_info = introspection_info(42)
print(number_info)

number_info = introspection_info('room')
print(number_info)

number_info = introspection_info([1, 3, 5])
print(number_info)

number_info = introspection_info((42, 'room', [1, 3, 5]))
print(number_info)
