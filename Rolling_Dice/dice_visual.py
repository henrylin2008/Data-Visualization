from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)    # count how many times each number appears in results
    frequencies.append(frequency)       # append the value to hte frequencies list

# print(frequencies)      # [161, 176, 168, 149, 176, 170] = [1, 2, 3, 4, 5, 6]

# visualize the results.
x_values = list(range(2, max_result+1))  # convert the range to a list for plotly
data = [Bar(x=x_values, y=frequencies)]     # Bar: data set formatted as a bar chart

x_axis_config = {'title': 'Result', 'dtick': 1}     # title for x_axis
y_axis_config = {'title': 'Frequency of Result'}    # title for y_axis
# Layout() speciies the layout and configuration of the graph as a whole
my_layout = Layout(title='Results of rolling two D6 dice 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
# generate the plot and store it in d6_d6.html file
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
