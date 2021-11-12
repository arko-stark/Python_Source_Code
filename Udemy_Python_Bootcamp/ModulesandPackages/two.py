# two.py
import one

print('Top Level is two.py')

one.func()

if __name__ == "__main__":
    print('two.py is being run directly ')
else :
    print('Two.py has been imported')