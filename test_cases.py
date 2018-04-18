test_cases = [
    {"type": "pos", "id": '15'},
    {"type": "neg", "id": '2.5'},
    {"type": "neg", "id": '0'},
    {"type": "neg", "id": '-1'},
    {"type": "neg", "id": "True"},
    {"type": "neg", "id": "False"},
    {"type": "neg", "id": "special$#@$%"},
    {"type": "neg", "id": "string space"},
    {"type": "neg", "id": {}},
    {"type": "neg", "id": ""},
    {"type": "neg", "id": "\\u0192\\u0224\\u0193\\u0225\\u0194\\u0226\\u0195\\u0227\\u0196\\u0228"},
    {"type": "neg", "id": "abcd\\\\123"},
    {"type": "neg", "id": "abcd/12/3"},
    {"type": "neg", "id": "abcd:123"},
    {"type": "neg", "id": "abcd.123"},
    {"type": "neg", "id": []    },
    {"type": "neg", "id": "[abcd]/123"},
    {"type": "neg", "id": "ABCD"},
    {"type": "neg", "id": "select * from users;"},
    {"type": "neg", "id": "abcd;123"},

]

if test_cases[0]['id'] == 'pos':
    print("good")

print(test_cases[0]['id'])

# for key, value in test_cases:
#     #new_t = t
#     #if t['type'] == 'pos':
#
#     #print(new_t)
#
#     string = t['id']
#     print(string)
#     print(type(string))
#     print(string.split())



    # stringList = string.split()
    # print(string)
    # print(stringList)