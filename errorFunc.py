import inspect

# def my_function():
#     # Get the name of the current function
#     current_function_name = inspect.currentframe().f_code.co_name
#     return current_function_name


def add(x, y):
    try:
        return x + y
    except:
        return "Error in", inspect.currentframe().f_code.co_name
    
print(add(3, 2))
print(add(3, ""))



def ex(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Capture the function name and the exception
            function_name = inspect.currentframe().f_code.co_name
            return f"Error in {function_name}: {str(e)}"
    return wrapper


@ex
def add(x, y):
    return x + y

print(add(3, "a"))


# except exception as e:
#     db.session.rollback()
#     errorLog("Error in add function", parameters=x,y, function=add() )
#     current.appLogger("Error in add function", parameters = x, y, function=add()
#                       return status !=500)
#     return (
#         "Error in add function, parameters = x,y, function = add(),
#         status 500)
