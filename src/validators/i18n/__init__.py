"""Country."""

# isort: skip_file

# local
from .es import es_cif, es_doi, es_nie, es_nif
from .fi import fi_business_id, fi_ssn
from .fr import fr_department, fr_ssn

__all__ = (
    "fi_business_id",
    "fi_ssn",
    "es_cif",
    "es_doi",
    "es_nie",
    "es_nif",
    "fr_department",
    "fr_ssn",
)
