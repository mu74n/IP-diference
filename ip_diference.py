def ip_type(ip):
    if IPv4(ip) == True:
        print (ip,"is IPv4")
    elif IPv6(ip) == True:
        print (ip,"is IPv6")
    else:
        print ("This is not an IP adress")

def IPv4(adress):
    """Return True if you parameter is an IPv4, otherwise return False. """
    try:
        times = adress.count(".")
        if times < 3:
            return False
        else:
            bit_list = adress.split(".")
            int_list = transform_integer(bit_list)
            count = 0
            is_ipv4 = True
            if len(int_list) > 4:
                is_ipv4 = False
            else:
                for i in int_list:
                    if i not in range (256):
                        is_ipv4 =  False
                        break
                    elif i in range (256):
                        count += 1
    except ValueError:
        return ("Wrong Value")
    except:
        return ("Error")
    return is_ipv4


def IPv6 (adress):
    char_num = list(range(10))
    hexadecimal =transform_string(char_num) + ["A","B","C","D","E","F"]
    segment = adress.split(":")
    ipv6 = True
    if len(segment) > 8:
        ipv6 = False
    elif len(segment) < 8 and "" not in segment:
        ipv6 = False
    else:
        for i in segment:
            if i == "" and segment.index(i) > 0 and segment.index(i) < len(segment) - 1:
                pass
            elif ipv6 == False:
                break
            else:
                for j in i:
                    if j not in hexadecimal:
                        ipv6 = False
                        break
    return ipv6
                
def transform_integer(bit_list):
    """Transform numeric characters into integers. """
    try:
        int_list = []
        for i in bit_list:    
            int_list.append(int(i))
    except ValueError:
        return ("Wrong Value")
    except:
        return ("Error")
    return int_list

def transform_string(bit_list):
    """Transform numbers into numeric characters . """
    try:
        int_list = []
        for i in bit_list:    
            int_list.append(str(i))
    except ValueError:
        return ("Wrong Value")
    except:
        return ("Error")
    return int_list

if __name__ == "__main__":
    def main():
        cont = ""
        while cont != "n":
            ip = input("Insert an IP: \n")
            ip_type(ip)
            cont = input("Do you want to insert another IP? Just press enter.\n Otherwise press n to exit.\n")
        

    main()