import csv
from google_play_scraper import app as fetch_app # I hate the name "app"
from concurrent.futures import ThreadPoolExecutor, as_completed

# List from the Google Play API
COUNTRY_CODES = [
	"us", "gb", "ca", "au", "de", "fr", "it", "es", "br", "in", "mx", "ru",
	"jp", "kr", "cn", "id", "tr", "sa", "ae", "nl", "be", "ch", "se", "no",
	"dk", "fi", "pl", "cz", "hu", "sk", "ro", "pt", "gr", "ie", "nz", "sg",
	"my", "ph", "th", "vn", "za", "eg", "ar", "cl", "co", "pe", "ua", "il",
	"hk", "tw", "pk", "bd", "lk", "ng", "ke", "ma", "dz", "tn", "ve", "uy",
	"cr", "pa", "do", "ec", "gt", "hn", "bo", "py", "sv", "qa", "kw", "om",
	"bh", "jo", "lb", "iq", "ir", "kz", "ge", "az", "am", "by", "rs", "ba",
	"me", "mk", "al", "si", "hr", "lt", "lv", "ee", "is", "lu", "mt", "cy"
]

def fetch_price(package, country):
	try:
		result = fetch_app(
			package,
			lang='en',
			country=country
		)
	except Exception: # in case of a 404
		print(f"WARN: could not find the app {package} for {country}")
		result = {}

	return {
		'Country': country,
		'Price': result.get('price', 'ERR'),
		'Currency': result.get('currency', 'ERR'),
	}

if __name__ == "__main__":
	package = input("The package name (write it in full ex. com.rockstargames.gtasa): ")
	
	# thread so it wont take forever
	results = []
	with ThreadPoolExecutor(max_workers=20) as executor:
		futures = [executor.submit(fetch_price, package, code) for code in COUNTRY_CODES]
		for future in as_completed(futures):
			results.append(future.result())

	# Sort by country and export to CSV
	results.sort(key=lambda x: x['Country'])
	csv_filename = f"{package.replace(".", "_")}__prices.csv" # not to trip file explorer with . in the name
	with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
		fieldnames = ['Country', 'Price', 'Currency']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		for row in results:
			writer.writerow({key: row.get(key, '') for key in fieldnames})
