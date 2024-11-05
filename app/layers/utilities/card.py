class Card:
    def __init__(self, url, name, status, last_location, first_seen, user=None, id=None):
        self.url = url
        self.name = name
        self.status = status
        self.last_location = last_location
        self.first_seen = first_seen

        self.user = user
        self.id = id

    def __str__(self):
        return f'IMG URL: {self.title}, name: {self.name}, status: {self.status}, última ubicación: {self.last_location}, primera vez visto: {self.first_seen}, Usuario: {self.user}, Id: {self.id}'
    
    # método equals.
    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return (self.url, self.name, self.status) == \
               (other.url, other.name, other.status)

    # método hashCode.
    def __hash__(self):
        return hash((self.url, self.name, self.status))