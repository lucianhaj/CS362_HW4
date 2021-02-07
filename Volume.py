def volume(l, w, h):
    try:
       x = float(l) * float(w) * float(h)
    except FloatingPointError:
        return "error with your input(s) type"
    except ArithmeticError:
        return "invalid input(s) type"
    except ValueError:
        return "One of inputs was not a float"
    except SyntaxError:
        return "Arguments not of the correct format"
    else:
        if float(l) == 0 or  float(w) == 0  or float(h) == 0:
            if float(l) < 0 or float(w) < 0  or float(h) < 0:
                return "Error: negative value"
            else:
                return "No volume"

        elif float(l) < 0 or float(w) < 0 or float(h) < 0:
            return "Error: negative value"
        else:
            return x




