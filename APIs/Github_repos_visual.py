# Create an interactive bar chart
import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"       # break between owner and description
    labels.append(label)

# Make visualization
data = [{
    'type': 'bar',      # Bar type graph
    'x': repo_names,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',   # custom blue color
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},     # dark gray line that's 1.5 pixels wide
    },
    'opacity': 0.6,     # soften the appearance of the chart
}]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'titlefont': {'size': 28},      # font size of the overall chart title
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},  # x-axis title font size
        "tickfont": {'size': 14},   # tick label
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='github_repos.html')
