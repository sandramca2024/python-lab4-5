from abc import ABC, abstractmethod

# Abstract base class for Studio Services
class StudioService(ABC):
    @abstractmethod
    def provide_service(self):
        pass

# Subclass 1
class RecordingService(StudioService):
    def provide_service(self):
        return "Congrats! You get to use the recording studio."

# Subclass 2
class MixingService(StudioService):
    def provide_service(self):
        return "Congrats! You get to use the mixing facilities."

# Subclass 3
class InstrumentService(StudioService):
    def provide_service(self):
        return "Congrats! You get to use an instrument."

def demonstrate_polymorphism():
    services = [RecordingService(), MixingService(), InstrumentService()]
    
    print("\nDemonstrating Polymorphism in Studio Services:")
    for service in services:
        
        print(service.provide_service())

def main():
    while True:
        print("\nStudio Management System")
        print("1. Recording Service")
        print("2. Mixing Service")
        print("3. Instrument Service")
        print("4. Demonstrate Polymorphism")
        print("5. Exit")
        
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            service = RecordingService()
            print(service.provide_service())

        elif choice == 2:
            service = MixingService()
            print(service.provide_service())

        elif choice == 3:
            service = InstrumentService()
            print(service.provide_service())

        elif choice == 4:
            
            demonstrate_polymorphism()

        elif choice == 5:
            print("Exiting the Studio Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
