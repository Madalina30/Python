def get_data(html_row):
    row_tds = html_row.findAll('td')
    team_data = list (map(lambda x : x.text, row_tds))
    return team_data
