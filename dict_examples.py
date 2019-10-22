from pprint import pprint

d1 = dict()
capitals = {'Alberta': 'Edmonton', 'BC': 'Victoria',
      'Manitoba': 'Winnipeg', 'Saskatchewan': 'Regina',
      'Ontario': 'Toronto'}
d3 = {}

print(capitals['BC'])
print(len(capitals))
capitals['Quebec'] = 'Quebec City'
pprint(capitals)
capitals['Alberta'] = 'Calgary'
capitals['Alberta'] = 'Edmonton'

print(capitals['Manitoba'])

print(capitals.get('PEI'))
print(capitals.get('PEI', '--not found--'))
print(capitals.get('Saskatchewan'))
capitals['PEI'] = 'Moose Jaw'

more_caps = {
    'Newfoundland and Labrador': 'St. John',
    'PEI': 'Charlottetown',
    'New Brunswick': 'Fredericton',
    'Nova Scotia': 'Halifax',
}
print()
capitals.update(more_caps)
for province, capital in capitals.items():
    print(province, capital)
print()
print(capitals)
print('-' * 60)
pprint(capitals)


