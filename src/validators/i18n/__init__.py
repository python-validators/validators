"""i18n."""

# local
from .es import es_cif, es_doi, es_nie, es_nif
from .fi import fi_business_id, fi_ssn
from .fr import fr_department, fr_ssn
from .ind import ind_aadhar, ind_pan
from .ru_inn import ru_inn

__all__ = (
    "fi_business_id",
    "fi_ssn",
    "es_cif",
    "es_doi",
    "es_nie",
    "es_nif",
    "fr_department",
    "fr_ssn",
    "ind_aadhar",
    "ind_pan",
    # Russian Individual Tax Number
    "ru_inn"
)
