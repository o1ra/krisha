from pathlib import Path
import krisha_kz_tests


def to_resource(path: str):
    return (
        Path(krisha_kz_tests.__file__)
        .parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )
