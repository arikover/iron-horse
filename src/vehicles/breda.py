from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="breda",
        base_numeric_id=9120,
        name="Breda E32",
        power=900,
        intro_year=1961,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=40, vehicle_length=8, spriterow_num=0
    )

    return consist
