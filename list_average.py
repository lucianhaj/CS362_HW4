
def average(list):
    total = 0
    try:
        for i in list:
            total = total + float(i)
    except ValueError:
        return "VError"
    else:
        try:
                average_num = float(total / len(list))
        except ValueError:
            return "VError"
        except ZeroDivisionError:
            return "Zero length for the list"
        except TypeError:
            return "TypeError: a string as list element may be present"
        except SyntaxError:
            return "SyntaxError: empty list may be present"
        else:

            return float(average_num)









