# NOTA PARA EL REVISOR:
# Hice todo mi proyecto en inglés. Esto con la finalidad de practicar el idioma.
# En caso de haber algún problema, lo puedo cambiar a español.
# Gracias por su comprensión


class InfoMessage:
    """Workout information message."""
    def __init__(self,
                training_type: str,
                duration: float,
                distance: float,
                speed: float,
                calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        """Show information about the workout."""
        return (f'Type of workout: {self.training_type}, '
                f'Duration: {self.duration} hrs, '
                f'Distance: {self.distance} km, '
                f'Average speed: {self.speed} km/h, '
                f'Calories burned: {self.calories}.'
        )


class Training:
    """Base training class."""

    M_IN_KM = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Get distance in км."""
        return self.action * (self.LEN_STEP / Training.M_IN_KM)

    def get_mean_speed(self) -> float:
        """Get average moving speed."""
        distance_covered = self.get_distance()
        return distance_covered / self.duration

    def get_spent_calories(self) -> float:
        """Get calories burned."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Return an informational message about the completed workout."""
        oMessage = InfoMessage(self.__class__.__name__, self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories())
        return oMessage


class Running(Training):
    """Training: Run."""

    LEN_STEP = 0.65

    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)


class SportsWalking(Training):
    """Workout: Race walking."""

    LEN_STEP = 0.65
    
    def __init__(self, action: int, duration: float, weight: float, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        average_speed = self.get_mean_speed()
        training_time_in_minutes = self.duration * 60
        return (18 * average_speed + 1.79) * self.weight / self.M_IN_KM * training_time_in_minutes


class Swimming(Training):
    """Workout: Swimming."""

    LEN_STEP = 1.38

    def __init__(self, action: int, duration: float, weight: float, length_pool: int, count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool


# ------------

def read_package(workout_type: str, data: list) -> Training:
    """Read data received from sensors."""
    workout_types = {
        'RUN': Running,
        'WLK': SportsWalking,
        'SWM': Swimming,
    }

    oTraining = workout_types[workout_type](*data)
    return oTraining


def main(training: Training) -> None:
    """Main function."""

    info = training.show_training_info()
    print(info.get_message())


# ------------


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

