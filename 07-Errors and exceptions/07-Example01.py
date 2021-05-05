# Errors and Exceptions
# syntax:
# try:                     --> run  <some code>
#     <some code>
# except:                  --> except if an error occurs run <some more code>
#     <some more code>
# finally:                 --> then finally run <again some code> regardless of error
#     <again some code>

def some_function():
    try:
        number = 10 + '10'
    except:
        print("There's a Type error")
    finally:
        print("End of the function, This line will always be printed")

some_function()