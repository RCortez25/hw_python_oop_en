class InfoMessage:
    """Workout information message."""
    pass


class Training:
    """Base training class."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        pass

    def get_distance(self) -> float:
        """Get distance in км."""
        pass

    def get_mean_speed(self) -> float:
        """Get average moving speed."""
        pass

    def get_spent_calories(self) -> float:
        """Get calories burned."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Return an informational message about the completed workout."""
        pass


class Running(Training):
    """Training: Run."""
    pass


class SportsWalking(Training):
    """Workout: Race walking."""
    pass


class Swimming(Training):
    """Workout: Swimming."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Read data received from sensors."""
    pass


def main(training: Training) -> None:
    """Main function."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

