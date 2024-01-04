from pathlib import Path
import krisha_kz


def to_resource(path: str):
    return (
        Path(krisha_kz.__file__)
        .parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )
