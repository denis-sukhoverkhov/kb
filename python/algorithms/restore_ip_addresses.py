# Function to get all the valid ip-addresses
def GetAllValidIpAddress(result, givenString,
                         index, count, ipAddress):
    # If index greater than givenString size
    # and we have four block
    if len(givenString) == index and count == 4:

        # Add ip-address to the results
        result.append(ipAddress)
        return

    # To add one index to ip-address
    if len(givenString) < index + 1:
        return

    # Select one digit and call the
    # same function for other blocks
    ipAddress = ipAddress + [givenString[index: index + 1]]

    GetAllValidIpAddress(result, givenString, index + 1,
                         count + 1, ipAddress)

    # Backtrack to generate another poosible ip address
    # So we remove two index (one for the digit
    # and other for the dot) from the end
    ipAddress = ipAddress[:-1]

    # Select two consecutive digits and call
    # the same function for other blocks
    if (len(givenString) < index + 2 or
            givenString[index] == '0'):
        return

    ipAddress = ipAddress + [givenString[index:index + 2]]

    GetAllValidIpAddress(result, givenString, index + 2,
                         count + 1, ipAddress)

    # Backtrack to generate another poosible ip address
    # So we remove three index from the end
    # ipAddress = ipAddress[:-2]

    # # Select three consecutive digits and call
    # # the same function for other blocks
    # if (len(givenString) < index + 3 or
    #         int("".join(givenString[index:index + 3])) > 255):
    #     return
    # ipAddress += [givenString[index:index + 3]]
    # GetAllValidIpAddress(result, givenString,
    #                      index + 3, count + 1, ipAddress)
    #
    # # Backtrack to generate another poosible ip address
    # # So we remove four index from the end
    # ipAddress = ipAddress[:-3]


def restoreIpAddresses(A):
    result = []
    GetAllValidIpAddress(result, A, 0, 0, [])

    # Print all the generated ip-addresses
    return result


if __name__ == "__main__":
    # str = '25525511135'
    # print(restoreIpAddresses(str))

    str = '5232459'
    print(restoreIpAddresses(str))
