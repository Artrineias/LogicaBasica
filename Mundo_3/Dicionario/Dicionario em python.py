pessoas = {}
pessoas['name'] = input("Name:")
pessoas["averega"] = float(input(f'average of {pessoas["name"]}:'))
if pessoas["averega"]>= 7:
    pessoas["situation"] = "approved"
else:
    pessoas["situation"] = "disapproved"
for k,v in pessoas.items():
    print(f"- {k} is equal to {v}")
