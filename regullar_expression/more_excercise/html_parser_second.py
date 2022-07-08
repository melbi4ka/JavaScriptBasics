import re

pattern_one = r"<title>(?P<title>.*)</title>"
pattern_two = r"<body>(?P<body>.*)</body>"
tag_pattern = r"<[/=\"\.a-z\s]+>"
text = input()

result_one = re.finditer(pattern_one, text)

for match in result_one:
    if match:
        print(f"Title: {match.group('title')}")

result_two = re.finditer(pattern_two, text)

for match in result_two:
    if match:
        match_with_additions = match.group('body')

        match_no_additions = re.split(tag_pattern, match_with_additions)
        match_no_additions = "".join(match_no_additions)
        match_no_additions = match_no_additions.replace("\\n", "")
        print(f"Content: {match_no_additions}")
