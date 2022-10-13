import re

pattern = r"(.*?<a ?href=\".+\">.+<\/a>.*)"
text = input()

while text != "end":
    matches = re.findall(pattern, text)
    # print(matches)
    if matches:
        match = "".join(matches)
        # print(match)

        if "<a " in match:
            match = match.replace("<a","[URL")
        elif "<a" in match:
            match = match.replace("<a", "[URL ")
        if "\">" in match:
            match = match.replace("\">", "\"]")
        if "</a>" in match:
            match = match.replace("</a>", "[/URL]")

        print(match)

    else:
        print(text)

    text = input()

    
