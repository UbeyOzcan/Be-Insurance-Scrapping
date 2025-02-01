from src.auto.Yuzzu import Yuzzu

yuzzu = Yuzzu(url="https://www.yuzzu.be/fr/assurance-auto/simulation",
              license_year="2013",
              birth_date="17071995",
              email="test@example.com",
              first_circulation="052022")

browser = yuzzu.fill_homepage()
browser = yuzzu.fill_vehicle_age_page(browser=browser, first_owner=True)
