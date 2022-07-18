# **Convert to numbers**


>HELP:

        - dbinary:   convert decimal to binary
        - bdecimal:  convert binary to decimal
        - dhex:      convert decimal to hexadecimal
        - bhex:      convert binary to hexadecimal
        - hdecimal:  convert hexadecimal to decimal
        - hbinary:   convert hexadecimal to binary


>DECIMAL TO BINARY

        -convert decimal to binary
                -input: convert.py -dbinary 14525
                -ouput: [+] numbers 14525 to convert binary: 11100010111101
        -convert multiple decimal to binary
                -input: convert.py -dbinary 14525.10458
                -ouput: [+] numbers 14525.10485 to convert binary: 11100010111101.10100011110101

>BINARY TO DECIMAL

        -convert binary to decimal
                -input: convert.py -bdecimal  11100010111101
                -ouput: [+] numbers  11100010111101 to convert decimal: 14525
        -convert multiple binary to decimal
                -input: convert.py -bdecimal 14525.10458
                -ouput: [+] numbers 11100010111101.10100011110101 to convert decimal: 14525.10485

> DECIMAL TO HEXADECIMAL
        
        -convert decimal to hexadecimal 
                -input: convert.py -dhex 14525
                -ouput: [+] numbers 14525.10485 to convert hexadecimal: 38BD
        -convert multiple decimal to hexadecimal
                -input: convert.py -dbinary 14525.10458
                -ouput: [+] numbers 14525.10485 to convert hexadecimal: 38BD:28F5

> BINARY TO HEXADECIMAL

        -convert binary to hexadecimal
                -input: convert.py -bhex 11100010111101
                -ouput: [+] numbers 11100010111101.10100011110101 to convert hexadecimal: 38BD
        -convert multiple binary to hexadecimal
                -input: convert.py -bhex 11100010111101.10100011110101
                -ouput: [+] numbers 11100010111101.10100011110101 to convert hexadecimal: 38BD:28F5

>HEXADECIMAL TO DECIMAL

        -convert hexadecimal to decimal
                -input: convert.py -hdecimal 38BD 
                -ouput: [+] numbers 38BD:28F5 to convert decimal: 14525 
        -convert multiple hexadecimal to decimal
                -input: convert.py -hdecimal 38BD:28F5 
                -ouput: [+] numbers 38BD:28F5 to convert decimal: 14525:10485

>HEXADECIMAL TO BINARY

        -convert hexadecimal to binary
                -input: convert.py -hbinary 38BD:28F5
                -ouput: [+] numbers 38BD:28F5 to convert binary: 11100010111101:10100011110101 
        -convert multiple hexadecimal to binary
                -input: convert.py -hbinary 38BD:28F5
                -ouput: [+] numbers 38BD:28F5 to convert binary: 11100010111101:10100011110101

