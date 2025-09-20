from abc import ABC, abstractmethod

class SelfDrivingVehicle(ABC):

    def drivetoDestination(self, origin, dest):
        return "Driving to Destination"
    
    @abstractmethod
    def steerVehicle():
        pass

class DriveMotorcycle(SelfDrivingVehicle):
    def steerVehicle():
        return "Steering motorcycle"