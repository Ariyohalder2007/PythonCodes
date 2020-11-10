class employee:
    
    def __init__(self, name, email, e_id, e_resi):
        self.name=name
        self.email=email
        self.e_id=e_id
        self.e_resi=e_resi
    def display(self):
        print(self.name, self.email, self.e_id, self.e_resi)
    
employee=employee("Ariyo", "alok@gmail.com", 23, "Very Good employee")
employee.display()
# Ariyo Halder