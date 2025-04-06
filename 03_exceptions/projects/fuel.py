def main():

    while True:
        fraction = input("Fraction: ")

        try:
            p = convert_percentage(fraction)

            if p == 100 or p == 99:
                print("F")
                break
            elif p == 0 or p == 1:
                print("E")
                break            
            elif p < 100:
                print (p,"%", sep="")                
                break 

        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        except IndexError:
            continue
                

             
def convert_percentage(f):
    f = f.split("/")
    return round(int(f[0]) / int(f[1]) * 100)
    
    
    
main()
