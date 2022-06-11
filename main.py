from re import match

regex_to_have = "....o"
letters_not_have = "c"
not_positions = {
  "a": [0],
  "b": [1]
}

file = open("words.txt", 'r')
parole = [line.rstrip() for line in file.readlines()]


filtered_values = list(filter(lambda v: match("^"+regex_to_have+"$", v), parole))
re_filtered_values = list(filter(lambda v: match(".*" + "".join(['(?=.*{})'.format(elem) for elem in not_positions.keys()]) + ".*", v), filtered_values))
letters_not_have_expect_regex = [letter for letter in letters_not_have if letter not in regex_to_have] if letters_not_have != "" else []
re_re_filtered_values = list(filter(lambda v: not match(".*[" + "|".join(list(letters_not_have_expect_regex)) + "].*", v), re_filtered_values)) if letters_not_have != "" else re_filtered_values

for i, lettera in enumerate(regex_to_have):
    if lettera == ".":
        re_re_filtered_values = [parola for parola in re_re_filtered_values if parola[i] not in letters_not_have]

result = re_re_filtered_values

for key in not_positions:
    for pos in not_positions[key]:
        result = list(filter(lambda v: not match("."*pos + key + "."*(len(regex_to_have)-1-pos), v), result))
  
for letter in not_positions.keys():
    result = [res for res in result if res.count(letter) > regex_to_have.count(letter)]

print(result)
