from jinja2 import Template

persons =[
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

html = """
{% macro list_users(list_of_users) -%}
<ul>
{% for u in list_of_users -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(users) list_users(users) %}
    <ul>
    <li>age: {{users.old}}
    <li>weight: {{users.weight}}
    </ul>
{% endcall -%}
"""

tm = Template(html)
msg = tm.render(users = persons)

print(msg)