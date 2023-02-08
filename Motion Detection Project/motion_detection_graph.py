import bokeh.plotting as bp, bokeh.io as bi, bokeh.models as bm, pandas as pd
from capturing_video import df

df["Start"] = pd.to_datetime(df.Start, format="%Y-%m-%d %H:%M:%S")
df["End"] = pd.to_datetime(df.End, format="%Y-%m-%d %H:%M:%S")


df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

column_data_source = bm.ColumnDataSource(data = df)




f = bp.figure(x_axis_type="datetime", height=100, width=500, sizing_mode = "scale_width")

f.yaxis.minor_tick_line_color = None
f.yaxis.ticker.desired_num_ticks=1


hover = bm.HoverTool(tooltips=[("Start", "@Start_string"), ("End","@End_string")])

f.add_tools(hover)



p = f.quad(left="Start", right="End", bottom=0, top=1, color="green", source=column_data_source)


bi.output_file("C:\\mycode\\python\\Functions\\bokeh\\detection.html")

bi.show(f)