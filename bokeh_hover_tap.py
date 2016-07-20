# coding=utf-8
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, TapTool, HoverTool, CustomJS
from bokeh.plotting import Figure
from bokeh.layouts import row

output_file("layout.html")

source = ColumnDataSource(
    data=dict(x=[2,3,5], y=[8,5,2]),
    name='source'
)

p1 = Figure(plot_width=550, plot_height=550, sizing_mode="fixed", title="With inspect behavior")
p1.circle(x='x', y='y', source=source, size=50)
p1.add_tools(TapTool(behavior='inspect', callback=CustomJS(code="alert('foo');")))
p1.add_tools(HoverTool())

p2 = Figure(plot_width=550, plot_height=550, sizing_mode="fixed", title="With select behavior")
p2.circle(x='x', y='y', source=source, size=50)
p2.add_tools(TapTool(behavior='select', callback=CustomJS(code="alert('foo');")))
p2.add_tools(HoverTool())

layout = row(p1, p2)

show(layout)
