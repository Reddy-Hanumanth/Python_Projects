from abc import ABC, abstractmethod

class Library_Item(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self._is_borrowed = False

    @abstractmethod
    def calculate_late_fine(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

    def check_out(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            print(f"success: '{self.title}' has been checked out.")
        else:
            print(f"Error: '{self.title}' is already currently borrowed.")

    def return_item(self):
        self._is_borrowed = False
        print(f"Success: '{self.title}' has been returned")



class Book(Library_Item):
    def __init__(self, title, item_id,author):
        super().__init__(title, item_id)
        self.author = author

    def calculate_late_fine(self,days):
        return days * 50
    
    def display_info(self):
        return f"[Book] ID: {self.item_id} | title: {self.title} | Author: {self.author}" 
    


class DVD(Library_Item):
    def __init__(self, title, item_id,director):
        super().__init__(title, item_id)
        self.director = director

    def calculate_late_fine(self, days):
        return days * 80
    
    def display_info(self):
        return f"[DVD] ID: {self.item_id} | title: {self.title} | director: {self.director}"
    

if __name__ == "__main__":
    catalog = [
        Book("The Great Gatsby", "Boo1", "F. Scott Fitzgerland"),
        DVD("Inception", "D001", "Christopher Nolan"),
        Book("Naraaj", "B002", "Rahat Indori"),
        DVD("RRR", "D002", "Rajmoli")
    ]

    print("--- Library Catalog ---")
    for item in catalog:
        print(item.display_info())

    print("\n--- Tesing Transactions ---")
    catalog[0].check_out()
    # catalog[0].return_item()

    print("\n--- Late Fine Calculation ---")
    for item in catalog:
        fine = item.calculate_late_fine(3)
        print(f"3-days late fine for '{item.title}': ${fine}")