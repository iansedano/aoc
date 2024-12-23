import pprint
import re

p = pprint.PrettyPrinter(width=200).pprint


def verifyHeight(height):
    match = re.match(r"(\d+\.\d+|\d+)(cm|in)", height)
    if not match:
        return False
    h = match[1]
    unit = match[2]

    if unit == "in":
        number = float(h)
        return number >= 59 and number <= 76
    elif unit == "cm":
        number = float(h)
        return number >= 150 and number <= 193


required = {
    # birth
    "byr": lambda year: bool(re.match(r"\d{4}", year))
    and int(year) >= 1920
    and int(year) <= 2002,
    # issue
    "iyr": lambda year: bool(re.match(r"\d{4}", year))
    and int(year) >= 2010
    and int(year) <= 2020,
    # expiration
    "eyr": lambda year: bool(re.match(r"\d{4}", year))
    and int(year) >= 2020
    and int(year) <= 2030,
    # height
    "hgt": verifyHeight,
    # hair color
    "hcl": lambda color: bool(re.match("#[a-f0-9]{6}", color)),
    # eye color
    "ecl": lambda color: color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    # password id
    "pid": lambda id: bool(re.match("[0-9]{9}", id)),
    # "cid"
}


def checkEntry(document):

    length = len(document.keys())

    print("len", length, end=" ")
    # p(document)

    for req_key in required.keys():
        # print("req_key", req_key, end=" | ")
        if req_key not in document:
            # print("FALSE")
            return False

    for key, value in document.items():
        # print("testing", key, value, end =" | ")
        if key in required:
            if not required[key](value):
                # print("FALSE")
                return False
    # print("\n")
    return True


with open("./input-day04.txt", mode="r") as f:
    entries = []
    current_entry = []
    for line in f:
        if line != "\n":
            current_entry.append(line.strip())
        elif line == "\n":
            attribs = []
            for line in current_entry:
                elements = line.split(" ")
                attribs.extend(elements)
            document = {}
            for attrib in attribs:
                key, value = attrib.split(":")
                document[key] = value


entries = input.split("\n\n")
print("number of passports", len(entries))
invalid_passports = 0
valid_passports = 0

it = 0
for entry in entries:
    it += 1
    # print(f"\n\npassport {it}")
    if checkEntry(entry) == False:
        invalid_passports += 1
    else:
        valid_passports += 1

print(
    "\n\nINVALID PASSPORTS",
    invalid_passports,
    "\nVALID PASSPORTS (176 too many)",
    valid_passports,
)
