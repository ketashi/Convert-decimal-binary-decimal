#!/usr/bin/python3

from pwn import *
import signal

#Verify parameters
if len(sys.argv) == 1:
    log.failure("Route: %s -param <numbers> : more information use --help o -h"%sys.argv[0])
    sys.exit(1)

#help de ayuda
def help():
    data = """
    help options convert:
        -dbinary:   convert decimal to binary
        -bdecimal:  convert binary to decimal
        -dhex:      convert decimal to hexadecimal
        -bhex:      convert binary to hexadecimal
        -hdecimal:  convert hexadecimal to decimal
        -hbinary:   convert hexadecimal to binary """
    print(data)
    sys.exit(1)
#func exit Ctrl + C        
def def_handler(sig,frame):
    print("\n\n[!]Saliendo...\n")
    sys.exit(1)

#global variables
bytes=[1,2,4,8]
hexs=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

def dbinary(numbers):
    data=""
    content=""
    for number in numbers:
        data=""
        while number:
            if number == 1:
                data += str(number)
                break
            else:
                data += str(number%2)
                number = number//2

        data = data[::-1]
        content += data + "."
    content = content[:-1]
    return content

def bdecimal(numbers):
    content=""
    for number in numbers:
        data=0
        number = number[::-1]
        for c in range(len(number)):
            if number[c] == "1":
                data += 2**c
        content += str(data) + "."
    content = content[:-1]
    return content

def dhex(numbers):
    content=""
    for number in numbers:
        data=""
        while number >= 16:
            if number >= 16:
                cocient = number%16
                number = number//16

            for hex in range(16):
                if cocient == hex:
                    data += hexs[cocient]
            
        if number < 16:
            for hex in range(16):
                if number == hex:
                    data += hexs[number]

        data = data[::-1]
        content += data + "."
    content = content[:-1]
    return content


def hdecimal(numbers):
    content=""
    for number in numbers:
        number = number.upper()
        number = number[::-1]
        result = 0
        for c in range(len(number)):
            for hex in range(16):
                if number[c] == hexs[hex]:
                    data = hex
            data = data * 16**c
            result += data
        content += str(result) + ":"
    content = content[:-1]
    return content

#Main
def main():
    try:
        #global
        parameter = str(sys.argv[1])
        if len(sys.argv) > 1:
            if parameter == "-dbinary":
                numbers = sys.argv[2]
                list_numbers = list(numbers.split("."))
                list_numbers = list(map(int,list_numbers))
                content = dbinary(list_numbers)
                if content:
                    log.success("numbers %s to convert binary: %s"%(sys.argv[2],content))
            
            elif parameter == "-bdecimal":
                numbers = sys.argv[2]
                list_numbers = list(numbers.split("."))
                list_numbers = list(map(str,list_numbers))
                content = bdecimal(list_numbers)
                if content:
                    log.success("numbers %s to convert decimal: %s"%(sys.argv[2],content))
           
            elif parameter == "-dhex":
                numbers = sys.argv[2]
                list_numbers = list(numbers.split("."))
                list_numbers = list(map(int,list_numbers))
                content = dhex(list_numbers)
                content = content.replace(".",":")
                if content:
                    log.success("numbers %s to convert hexadecimal: %s"%(sys.argv[2],content))
            
            elif parameter == "-bhex":
                numbers = sys.argv[2]
                list_numbers = list(numbers.split("."))
                list_numbers = list(map(str,list_numbers))
                result = bdecimal(list_numbers)
                result = list(result.split("."))
                result = list(map(int,result))
                content = dhex(result)
                content = content.replace(".",":")
                if content:
                    log.success("numbers %s to convert hexadecimal: %s"%(sys.argv[2],content))
            
            elif parameter == "-hdecimal":
                numbers = sys.argv[2]
                list_numbers = list(numbers.split(":"))
                list_numbers = list(map(str,list_numbers))
                content = hdecimal(list_numbers)
                if content:
                    log.success("numbers %s to convert decimal: %s"%(sys.argv[2],content))
            
            elif parameter == "-hbinary":
                numbers = sys.argv[2]
                list_numbers = list(numbers.split(":"))
                list_numbers = list(map(str,list_numbers))
                results = hdecimal(list_numbers)
                results = list(results.split(":"))
                results = list(map(int,results))
                content = dbinary(results)
                content = content.replace(".",":")
                if content:
                    log.success("numbers %s to convert binary: %s"%(sys.argv[2],content))
             
            else:
                help()
                sys.exit(1)
        else:
            help()
            sys.exit(1)

    except:
        log.failure("Route: %s -param <numbers> : more information use --help o -h"%sys.argv[0])
        sys.exit(1)

#Ctrl + C
signal.signal(signal.SIGINT, def_handler)

if __name__ == "__main__":
    main()
