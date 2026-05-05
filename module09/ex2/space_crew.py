from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = False
        for member in self.crew:
            if member.rank == Rank.commander or member.rank == Rank.captain:
                has_leader = True
                break
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = []
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced.append(member)
            total_crew = len(self.crew)
            experienced_count = len(experienced)
            if experienced_count < total_crew / 2:
                raise ValueError(
                    "Long missions require at least 50% experienced "
                    "crew (5+ years)"
                )

        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")

        return self


def main() -> None:
    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 1, 15, 10, 30, 00),
        duration_days=900,
        crew=[
            CrewMember(
                member_id="C01",
                name="Sarah Connor",
                rank=Rank.commander,
                age=38,
                specialization="Mission Command",
                years_experience=12,
                is_active=True
            ),
            CrewMember(
                member_id="C02",
                name="John Smith",
                rank=Rank.lieutenant,
                age=32,
                specialization="Navigation",
                years_experience=6,
                is_active=True
            ),
            CrewMember(
                member_id="C03",
                name="Alice Johnson",
                rank=Rank.officer,
                age=29,
                specialization="Engineering",
                years_experience=4,
                is_active=True
            )
        ],
        mission_status="planned",
        budget_millions=2500.0
    )
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    crew_size = len(valid_mission.crew)
    print(f"Crew size: {crew_size}")
    print("Crew members:")
    for member in valid_mission.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")
    print("=========================================")

    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 1, 15, 10, 30, 0),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C01",
                    name="Sarah Connor",
                    rank=Rank.lieutenant,
                    age=38,
                    specialization="Mission Command",
                    years_experience=12,
                    is_active=True
                ),
                CrewMember(
                    member_id="C02",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=32,
                    specialization="Navigation",
                    years_experience=6,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=2500.0
        )
        print(invalid_mission)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
