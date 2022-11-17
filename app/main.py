import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda x:x['Continent']=='South America', data))

  country = list(map(lambda x:x['Country/Territory'], data))
  result = list(map(lambda x:x['World Population Percentage'], data))
  charts.generate_pie_chart(country,result)
  
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()