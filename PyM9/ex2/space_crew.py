"""
Exercise 2: Space Crew Management
Objective: Master nested Pydantic models and complex data relationships.
"""

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Enum defining the possible crew ranks."""

    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    """Pydantic model for validating individual crew member data."""

    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Pydantic model for validating space mission data with nested crew."""

    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        """Apply mission safety rules after all fields are validated."""

        # Rule 1: Mission ID must start with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        # Rule 2: Must have at least one Commander or Captain
        senior_ranks = {Rank.commander, Rank.captain}
        has_senior = any(
            member.rank in senior_ranks for member in self.crew
        )
        if not has_senior:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        # Rule 3: Long missions (> 365 days) need 50% experienced crew
        if self.duration_days > 365:
            experienced = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            ratio = experienced / len(self.crew)
            if ratio < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) require at least 50% "
                    "of crew with 5+ years of experience"
                )

        # Rule 4: All crew members must be active
        inactive = [m.name for m in self.crew if not m.is_active]
        if inactive:
            raise ValueError(
                f"All crew members must be active. "
                f"Inactive members: {', '.join(inactive)}"
            )

        return self


def main() -> None:
    """Demonstrate SpaceMission validation with valid and invalid missions."""

    print("Space Mission Crew Validation")
    print("=" * 41)

    # Define crew members for the valid mission
    commander = CrewMember(
        member_id="CM001",
        name="Sarah Connor",
        rank=Rank.commander,
        age=42,
        specialization="Mission Command",
        years_experience=18,
    )

    lieutenant = CrewMember(
        member_id="CM002",
        name="John Smith",
        rank=Rank.lieutenant,
        age=35,
        specialization="Navigation",
        years_experience=10,
    )

    officer = CrewMember(
        member_id="CM003",
        name="Alice Johnson",
        rank=Rank.officer,
        age=29,
        specialization="Engineering",
        years_experience=6,
    )

    # Create a valid mission
    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 6, 1, 9, 0, 0),
        duration_days=900,
        crew=[commander, lieutenant, officer],
        mission_status="planned",
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for member in valid_mission.crew:
        print(
            f"  - {member.name} ({member.rank.value})"
            f" - {member.specialization}"
        )

    print("=" * 41)

    # Attempt an invalid mission: no Commander or Captain in crew
    print("\nExpected validation error:")
    try:
        cadet = CrewMember(
            member_id="CM004",
            name="Bob Lee",
            rank=Rank.cadet,
            age=22,
            specialization="Maintenance",
            years_experience=1,
        )

        SpaceMission(
            mission_id="M2024_BAD",
            mission_name="Doomed Expedition",
            destination="Jupiter",
            launch_date=datetime(2024, 7, 1, 9, 0, 0),
            duration_days=200,
            crew=[cadet],  # Invalid: no Commander or Captain
            budget_millions=500.0,
        )
    except ValidationError as exc:
        for error in exc.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
