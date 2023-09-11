import re

test_names = ["Cranell V120 Inspection Checklist [1.0.2]", "Tank [1.0.14]", "Gearbox Invenergy v1.0.40",]

for name in test_names:
    if "[" in name:
        pattern = r'\[[^()]*\]'
        fixed_name = re.sub(pattern, "", name)
        fixed_name.rstrip()
        print(fixed_name)
    else:
        pattern = r'v\s*([\d.]+)'
        fixed_name = re.sub(pattern, "", name)
        fixed_name.rstrip()
        print(fixed_name)
