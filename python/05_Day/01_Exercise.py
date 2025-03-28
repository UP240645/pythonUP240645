#Level 1
#1
empty_list=list()
# 2
more_than_5 = [1, 2, 3, 4, 5, 6]

# 3
print(len(more_than_5))

# 4
print(more_than_5[0], more_than_5[len(more_than_5) // 2], more_than_5[-1])

# 5
mixed_data_types= ['Angel', 18, 178, 'soltero', 'Mexico,Ags,Ags,Infonavit IV Centenario']

# 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7
print(it_companies)

# 8
print(len(it_companies))

# 9
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])

# 10
it_companies[0] = 'Infosys'
print(it_companies)

# 11
it_companies.append('Facebook')

# 12
it_companies = it_companies[0:len(it_companies) // 2] + ['Dell'] + it_companies[len(it_companies) // 2:]

# 13
it_companies[0] = it_companies[0].upper()

# 14
it_companies_hash = '#'.join(it_companies)

# 15
print('IBM' in it_companies)

# 16
it_companies.sort()

# 17
it_companies.reverse()

# 18
it_companies = it_companies[2:]

# 19
it_companies = it_companies[:len(it_companies) - 3]

# 20
it_companies = it_companies[0:len(it_companies) // 2] + it_companies[len(it_companies) // 2 + 1:]

# 21
it_companies.pop(0)

# 22
it_companies.pop(len(it_companies) // 2)

# 23
it_companies.pop(len(it_companies) - 1)

# 24
it_companies.clear()

# 25
del it_companies

# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end.append(back_end)

# 27
full_stack = front_end
indx = full_stack.index('Redux')
full_stack = full_stack[:indx] + ['Python', 'SQL'] + full_stack[indx:]

# Level 2

# 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(ages[0])
print(ages[-1])
# noinspection PyTypeChecker
print('0.2f'.format((ages[len(ages)//2] + ages[~(len(ages)//2)])/2))
print('0.2f'.format(sum(ages) / len(ages)))
print(ages[-1] - ages[0])
print(abs(ages[0] - sum(ages) / len(ages)))
print(abs(ages[-1] - sum(ages) / len(ages)))
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]

# noinspection PyTypeChecker
print([countries[i]
       for i in range((len(countries) // 2) - (1 if int(len(countries)) % 2 == 0 else 0), len(countries) // 2 + 1)])

length = len(countries)
if length % 2 == 0:
    first_half = countries[:length // 2]
    second_half = countries[length // 2:]
else:
    first_half = countries[:length // 2 + 1]
    second_half = countries[length // 2 + 1:]

scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'][3:]