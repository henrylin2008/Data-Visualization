from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)    # count how many times each number appears in results
    frequencies.append(frequency)       # append the value to hte frequencies list

# print(frequencies)      # [161, 176, 168, 149, 176, 170] = [1, 2, 3, 4, 5, 6]

# visualize the results.
x_values = list(range(1, die.num_sides+1))  # convert the range to a list for plotly
data = [Bar(x=x_values, y=frequencies)]     # Bar: data set formatted as a bar chart

x_axis_config = {'title': 'Result'}     # title for x_axis
y_axis_config = {'title': 'Frequency of Result'}    # title for y_axis
# Layout() speciies the layout and configuration of the graph as a whole
my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')   # generate the plot and store it in d6.html file
