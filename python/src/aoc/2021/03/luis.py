file = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

folder = []
line = ""
for char in file:
    if char == "\n":
        folder.append(line)
        line = ""
        continue
    line += char
folder.append("01010")
# print(folder,len(folder))
oxigen = co2 = new = []
count0 = count1 = 0
# find which is the most common bit in that position
def indicator1(folder, i):
    # i is the index position in the binary
    # folder is a list with a lot of binaries
    indicator_oxi = ""
    count0 = count1 = 0
    for x in folder:
        if x[i] == "1":
            count1 += 1
        elif x[i] == "0":
            count0 += 1
        if count1 + count0 == len(folder):
            if count1 >= count0:
                indicator_oxi = "1"
            else:
                indicator_oxi = "0"
    return indicator_oxi


def indicator2(folder, i):
    # i is the index position in the binary
    # folder is a list with a lot of binaries
    indicator_co2 = ""
    count0 = count1 = 0
    for x in folder:
        if x[i] == "1":
            count1 += 1
        elif x[i] == "0":
            count0 += 1
        if count1 + count0 == len(folder):
            if count1 >= count0:
                indicator_co2 = "0"
            else:
                indicator_co2 = "1"
    return indicator_co2


# find the oxigen
new.extend(folder)
while len(new) > 1:
    for i in range(5):
        c = indicator1(new, i)
        # print(c,i)
        for x in new:
            if x[i] != c:
                # print(x)
                new.remove(x)
# print(new,len(new),i)

# find the co2
new2 = []
new2.extend(folder)
while len(new2) > 1:
    for z in range(5):
        c = indicator2(new2, z)
        # print(c,i)
        for x in new2:
            if x[z] != c:
                # print(x)
                new2.remove(x)
                if len(new2) == 2:
                    break
# print(new2,len(new2),z)

# make numbers from binary to decimal
def binmak(list):
    i = len(list) - 1
    bin_num = 0
    for x in list:
        bin_num += int(x) * (2 ** i)
        # print(i,int(x),bin_num)
        i -= 1
        if i == -1:
            break
    return bin_num


# print(new,new2)
new_str = "".join(new)
new2_str = "".join(new2)
new = list(new_str)
new2 = list(new2_str)
print(new, new2)

# get the result
e = binmak(new)  # oxigen
f = binmak(new2)  # co2
print(e, f, e * f)
