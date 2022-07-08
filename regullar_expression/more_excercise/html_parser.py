import re

pattern_one = r"<title>(?P<title>.*)</title>"
pattern_two = r"<body>(?P<body>.*)</body>"
ahref_pattern = r"<a href=\".*\">"
text = input()

result_one = re.finditer(pattern_one, text)

for match in result_one:
    if match:
        print(f"Title: {match.group('title')}")

result_two = re.finditer(pattern_two,text)

for match in result_two:
    if match:
        unmatched = ["<p>", "</p>", "\\n", "<a>", "</a>", "<html>", "</html>"]
        match_without_additions = match.group('body')
        for el in unmatched:
            while el in match_without_additions:
                match_without_additions = match_without_additions.replace(el, "")

        x = re.split(ahref_pattern, match_without_additions)
        print(f"Content: {''.join(x)}")
