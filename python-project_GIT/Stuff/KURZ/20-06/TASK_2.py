class City:
    def __init__(self, city_name='', region_name='', country_name='', num_citizens=0, zip_code='', area_code=''):
        self.city_name = city_name
        self.region_name = region_name
        self.country_name = country_name
        self.num_citizens = num_citizens
        self.zip_code = zip_code
        self.area_code = area_code

    def set_city_name(self, city_name):
        self.city_name = city_name

    def get_city_name(self):
        return self.city_name

    def set_region_name(self, region_name):
        self.region_name = region_name

    def get_region_name(self):
        return self.region_name

    def set_country_name(self, country_name):
        self.country_name = country_name

    def get_country_name(self):
        return self.country_name

    def set_num_citizens(self, num_citizens):
        self.num_citizens = num_citizens

    def get_num_citizens(self):
        return self.num_citizens

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def get_zip_code(self):
        return self.zip_code

    def set_area_code(self, area_code):
        self.area_code = area_code

    def get_area_code(self):
        return self.area_code

    def input_data(self, city_name, region_name, country_name, num_citizens, zip_code, area_code):
        self.city_name = city_name
        self.region_name = region_name
        self.country_name = country_name
        self.num_citizens = num_citizens
        self.zip_code = zip_code
        self.area_code = area_code

    def output_data(self):
        return {
            'city_name': self.city_name,
            'region_name': self.region_name,
            'country_name': self.country_name,
            'num_citizens': self.num_citizens,
            'zip_code': self.zip_code,
            'area_code': self.area_code
        }

# Example usage:
city = City()
city.input_data('New York', 'New York', 'USA', 8419000, '10001', '212')
print(city.output_data())

city.set_city_name('Los Angeles')
print(city.get_city_name())