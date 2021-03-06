offices = []


class Office:
    """The Office model"""

    def __init__(self):
        self.offices = offices

    def create_office(self, officeType, name):
        """ Create a office method """
        office = {
            "id": len(self.offices) + 1,
            "officeType": officeType,
            "name": name
        }
        self.offices.append(office)
        return office

    def get_all_offices(self):
        """ Get all offices method """
        return self.offices

    def get_specific_office(self, id):
        """ Get specific office method """
        for office in self.offices:
            if office['id'] == id:
                return office

    def search(self, id):
        """ Search a specific office by name"""
        for office in self.offices:
            if office['id'] == id:
                return True
