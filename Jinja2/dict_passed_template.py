from jinja2 import Template

per = {'name': 'Федор', 'age': 34}

tm = Template("Мне {{ p['age'] }} и зовут {{ p['name'] }}")
msg = tm.render(p = per)

print(msg)