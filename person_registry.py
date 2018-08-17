class PersonRegistry():
    def __init__(self):
        self.data_base = {}

    def add_person(self, name,birth_day):
        registered_birt_day = self.get_birh_date(name)
        if registered_birt_day and registered_birt_day != birth_day:
            # update birth_day
            self.data_base[name] = birth_day
        elif not registered_birt_day:
            # insert new birh_day
            self.data_base[name] = birth_day
    
    def get_birh_date(self,name):
        if name in self.data_base.keys():
            return self.data_base[name]
        else:
            return None

    def remove_person(self,name):
        if name in self.data_base.keys():
            del self.data_base[name]