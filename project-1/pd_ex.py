import pandas as pd
import numpy as np 
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

df = pd.read_excel("sales-funnel.xlsx")
df.head()
print(df.head())
sales_report = pd.pivot_table(df, index=["Manager", "Rep", "Product"], values=["Price", "Quantity"],
                           aggfunc=[np.sum, np.mean], fill_value=0)
sales_report.head()

#jinja2
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("templates/myreport.html")
#context
template_vars = {"title" : "Sales Funnel Report - National",
                 "national_pivot_table": sales_report.to_html()}

html_out = template.render(template_vars)
rendered_file = open('templates/myreport_rendered.html', 'w')
rendered_file.write(html_out)

HTML(string=html_out).write_pdf("report.pdf",  stylesheets=["static/style.css"])