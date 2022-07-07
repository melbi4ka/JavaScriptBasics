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

# 60/100
# първо правя един патърн за тайтъла <title>(?P<title>.*)</title> - наименувана група с всичко нула или един пъти, между
# отварящ и затварящ тайтъл ми дава заглавието
# после един патърн за бодито <body>(?P<body>.*)</body> - наименувана група с всичко нула или един пъти, между
# отварящ и затварящо боди на контента
# после един за ahref <a href=\".*\"> - отваряща скоба, a href=, ескейпнати кавички, всичко нула или един пъти,
# ескейпнати затварящи кавички, затваряща скоба
# махам тагове, но тук явно дава грешка - описвам ги в лист и после фор и уайл цикъл
# сплитвам по ahref и тук сигурно дава грешка



