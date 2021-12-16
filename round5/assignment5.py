import sys
import contextlib

class TotallyCoolContextManager:
    def __enter__(self):
        print("We are entering a totally cool context manager!\n")
        return self
    def __exit__(self, e_type, e_value, traceback):
        try:
            if e_type is KeyError:
                print("Boss, there is a problem with the key. Not good!\n")
            if e_type is IndexError:
                print("Captain, the index is out of range. Abandon ship!\n")
            if e_type is not KeyError and e_type is not IndexError:
                print("We got some other exception nobody cares about. Continuing mission!\n")
        finally:
            print("We are exiting a totally cool context manager!\n")
            return True

@contextlib.contextmanager
def talk_like_a_pirate_context_manager():
    print ("Ahoy, matey!\n")
    def speak(text):
        text += " Yarr!"
    try:
        yield True
    except KeyError:
        print("Boss, there is a problem with the key. Not good!\n")
    except IndexError:
        print("Captain, the index is out of range. Abandon ship!\n")
    except Exception:
        print("We got some other exception nobody cares about. Continuing mission!\n")
    finally:
        print("Shiver me timbers!\n")
       
    

if __name__ == "__main__":

    normal_array = list(range(10))
    normal_dict = {'Jesus': 'Christ'}

    with TotallyCoolContextManager() as cool:
        print (normal_array[42])
    with cool:
        print (normal_dict['Hello, world!'])
    with cool:
        print (2/0)
    with talk_like_a_pirate_context_manager() as pirate:
        print (normal_array[42])
    with talk_like_a_pirate_context_manager() as pirate:
        print (normal_dict['Hello, world!'])
    with talk_like_a_pirate_context_manager() as pirate:
        print (2/0)