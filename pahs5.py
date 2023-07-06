class TreatmentPackage:
    def __init__(self, title, doctor, hospital, cost, requirements):
        self.title = title
        self.doctor = doctor
        self.hospital = hospital
        self.cost = cost
        self.requirements = requirements

    def showMissingRequirements(self, documents):
        missing_requirements = []
        for requirement in self.requirements:
            if requirement not in documents:
                missing_requirements.append(requirement)
        return missing_requirements

    def PackConfirmed(self):
        print("Treatment package confirmed.")


class SystemController:
    def __init__(self) -> None:
        self.treatmentPacks = []
        
    def newPackage(self):
        title = input("Enter the title of the treatment package: ")
        doctor = input("Enter the name of the supervising doctor: ")
        hospital = input("Enter the name of the hospital or clinic: ")
        cost = float(input("Enter the cost of the treatment package: "))
        requirements = input(
            "Enter the prerequisite documents (separated by commas): ").split(",")
        
        package = TreatmentPackage(title, doctor, hospital, cost, requirements)
        self.treatmentPacks.append(package)
        
        return package

    def selectTreatment(self, treatment_packages):
        print("Available Treatment Packages:")
        for index, package in enumerate(treatment_packages):
            print(f"{index + 1}. {package.title}")
        selection = int(input("Select a treatment package: "))
        return treatment_packages[selection - 1]

    def CheckPayment(self):
        # Payment logic goes here
        return True

    def ErrorDocuments(self):
        print("Error: Missing or incorrect documents.")

    def cancelTreatmentPackage(self):
        print("Treatment package canceled.")
        
         



class MedicalRecorder:
    def __init__(self):
        self.AvailablePacks = []
        self.NonAvailablePacks = []
        self.docsperPacks = {}

    def showpacks(self):
        for index, package in enumerate(self.AvailablePacks):
            print(f"{index + 1}. {package.title}")

    def getRequirementsPack(self, package_type):
        return self.docsperPacks.get(package_type, [])

    def PackAdded(self, treatment_package):
        self.AvailablePacks.append(treatment_package)


class CustomerHandler:
    def __init__(self, name, medicalRecorder, systemController):
        self.name = name
        self.packs = []
        self.money = 0.0
        self.documents = []
        self.medicalRecorder = medicalRecorder
        self.systemController = systemController

    def uploadDocument(self, document):
        self.documents.append(document)

    def payBill(self, bill):
        self.money -= bill

    def addTreatment(self):
        pack = TreatmentPackage("Package 1", "Dr. Smith", "Hospital A", 1000.0, ["Document 1", "Document 2"])
        docs = self.medicalRecorder.getRequirementsPack()
        missings = pack.showMissingRequirements(docs)
        if len(missings) != 0:
            self.systemController.ErrorDocuments()
        self.packs.append(pack)
        return pack


class HealthSupervisor:
    def __init__(self):
        self.patientList = []

    def checkDocuments(self, patient):
        if len(patient.documents) == 0:
            return False
        return True

    def calculateBill(self, treatment_package):
        return treatment_package.cost

    def assignPatient(self, patient):
        self.patientList.append(patient)


def initialize():
    system_controller = SystemController()
    medical_recorder = MedicalRecorder()
    health_supervisor = HealthSupervisor()
    customer_handler = CustomerHandler("", medical_recorder, system_controller)
    return system_controller, medical_recorder, health_supervisor, customer_handler

  
        
    

def main():
    system_controller, medical_recorder, health_supervisor, customer_handler = initialize()

    medical_recorder.showpacks()
    pack = customer_handler.addTreatment()
    health_supervisor.assignPatient("Patient")
    checkResult = health_supervisor.checkDocuments()
    if checkResult != True:
        system_controller.ErrorDocuments()
        
    bill = health_supervisor.calculateBill()
    customer_handler.payBill(bill)
    result = system_controller.CheckPayment()
    if result == True:
        pack.PackConfirmed()
    
    medical_recorder.PackAdded(pack)
    