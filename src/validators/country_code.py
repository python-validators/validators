"""Country Codes."""

# local
from validators.utils import validator

# fmt: off
alpha_2 = {
    "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ",
    "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS",
    "BT", "BV", "BW", "BY", "BZ",
    "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW",
    "CX", "CY", "CZ",
    "DE", "DJ", "DK", "DM", "DO", "DZ",
    "EC", "EE", "EG", "EH", "ER", "ES", "ET",
    "FI", "FJ", "FK", "FM", "FO", "FR",
    "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT",
    "GU", "GW", "GY",
    "HK", "HM", "HN", "HR", "HT", "HU",
    "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT",
    "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI",
    "KM", "KN", "KP", "KR", "KW", "KY", "KZ",
    "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY",
    "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS",
    "MT", "MU", "MV", "MW", "MX", "MY", "MZ",
    "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ",
    "OM",
    "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY",
    "QA",
    "RE", "RO", "RS", "RU", "RW",
    "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS",
    "ST", "SV", "SX", "SY", "SZ",
    "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ",
    "UA", "UG", "UM", "US", "UY", "UZ",
    "VC", "VE", "VG", "VI", "VN", "VU",
    "WF", "WS",
    "YE", "YT",
    "ZA", "ZM", "ZW",
}
alpha_3 = {
    "ABW", "AFG", "AGO", "AIA", "ALA", "ALB", "AND", "ARE", "ARG", "ARM", "ASM", "ATA", "ATF",
    "ATG", "AUS", "AUT", "AZE",
    "BDI", "BEL", "BEN", "BES", "BFA", "BGD", "BGR", "BHR", "BHS", "BIH", "BLM", "BLR", "BLZ",
    "BMU", "BOL", "BRA", "BRB", "BRN", "BTN", "BVT", "BWA",
    "CAF", "CAN", "CCK", "CHE", "CHL", "CHN", "CIV", "CMR", "COD", "COG", "COK", "COL", "COM",
    "CPV", "CRI", "CUB", "CUW", "CXR", "CYM", "CYP", "CZE",
    "DEU", "DJI", "DMA", "DNK", "DOM", "DZA",
    "ECU", "EGY", "ERI", "ESH", "ESP", "EST", "ETH",
    "FIN", "FJI", "FLK", "FRA", "FRO", "FSM",
    "GAB", "GBR", "GEO", "GGY", "GHA", "GIB", "GIN", "GLP", "GMB", "GNB", "GNQ", "GRC", "GRD",
    "GRL", "GTM", "GUF", "GUM", "GUY",
    "HKG", "HMD", "HND", "HRV", "HTI", "HUN",
    "IDN", "IMN", "IND", "IOT", "IRL", "IRN", "IRQ", "ISL", "ISR", "ITA",
    "JAM", "JEY", "JOR", "JPN",
    "KAZ", "KEN", "KGZ", "KHM", "KIR", "KNA", "KOR", "KWT",
    "LAO", "LBN", "LBR", "LBY", "LCA", "LIE", "LKA", "LSO", "LTU", "LUX", "LVA",
    "MAC", "MAF", "MAR", "MCO", "MDA", "MDG", "MDV", "MEX", "MHL", "MKD", "MLI", "MLT", "MMR",
    "MNE", "MNG", "MNP", "MOZ", "MRT", "MSR", "MTQ", "MUS", "MWI", "MYS", "MYT",
    "NAM", "NCL", "NER", "NFK", "NGA", "NIC", "NIU", "NLD", "NOR", "NPL", "NRU", "NZL",
    "OMN",
    "PAK", "PAN", "PCN", "PER", "PHL", "PLW", "PNG", "POL", "PRI", "PRK", "PRT", "PRY", "PSE",
    "PYF",
    "QAT",
    "REU", "ROU", "RUS", "RWA",
    "SAU", "SDN", "SEN", "SGP", "SGS", "SHN", "SJM", "SLB", "SLE", "SLV", "SMR", "SOM", "SPM",
    "SRB", "SSD", "STP", "SUR", "SVK", "SVN", "SWE", "SWZ", "SXM", "SYC", "SYR",
    "TCA", "TCD", "TGO", "THA", "TJK", "TKL", "TKM", "TLS", "TON", "TTO", "TUN", "TUR", "TUV",
    "TWN", "TZA",
    "UGA", "UKR", "UMI", "URY", "USA", "UZB",
    "VCT", "VEN", "VGB", "VIR", "VNM", "VUT",
    "WLF", "WSM",
    "YEM",
    "ZAF", "ZMB", "ZWE",
}
numeric = {
    "004", "008", "010", "012", "016", "020", "024", "028", "031", "032",
    "036", "040", "044", "048", "050", "051", "052", "056", "060", "064",
    "068", "070", "072", "074", "076", "084", "086", "090", "092", "096",
    "100", "104", "108", "112", "116", "120", "124", "132", "136", "140",
    "144", "148", "152", "156", "158", "162", "166", "170", "174", "175",
    "178", "180", "184", "188", "191", "192", "196", "203", "204", "208",
    "212", "214", "218", "222", "226", "231", "232", "233", "234", "238",
    "239", "242", "246", "248", "250", "254", "258", "260", "262", "266",
    "268", "270", "275", "276", "288", "292", "296", "300", "304", "308",
    "312", "316", "320", "324", "328", "332", "334", "340", "344", "348",
    "352", "356", "360", "364", "368", "372", "376", "380", "384", "388",
    "392", "398", "400", "404", "408", "410", "414", "417", "418", "422",
    "426", "428", "430", "434", "438", "440", "442", "446", "450", "454",
    "458", "462", "466", "470", "474", "478", "480", "484", "492", "496",
    "498", "499", "500", "504", "508", "512", "516", "520", "524", "528",
    "531", "533", "534", "535", "540", "548", "554", "558", "562", "566",
    "570", "574", "578", "580", "581", "583", "584", "585", "586", "591",
    "598", "600", "604", "608", "612", "616", "620", "624", "626", "630",
    "634", "638", "642", "643", "646", "652", "654", "659", "660", "662",
    "663", "666", "670", "674", "678", "682", "686", "688", "690", "694",
    "702", "703", "704", "705", "706", "710", "716", "724", "728", "729",
    "732", "740", "744", "748", "752", "756", "760", "762", "764", "768",
    "772", "776", "780", "784", "788", "792", "795", "796", "798", "800",
    "804", "807", "818", "826", "831", "832", "833", "834", "840", "850",
    "854", "858", "860", "862", "876", "882", "887", "894",
}
# fmt: on


def get_code_type(format_type: str):
    """Returns the type of country code."""
    if format_type.isdigit():
        return "numeric"
    if format_type.isalpha():
        if len(format_type) == 2:
            return "alpha2"
        if len(format_type) == 3:
            return "alpha3"
    return "invalid"


@validator
def country_code(value: str, /, *, iso_format: str = "auto"):
    """Validates given country code.

    This performs a case-sensitive [ISO 3166][1] country code validation.

    [1]: https://www.iso.org/iso-3166-country-codes.html

    Examples:
        >>> country_code('GB', iso_format='alpha3')
        # Output: False
        >>> country_code('USA')
        # Output: True
        >>> country_code('840', iso_format='numeric')
        # Output: True
        >>> country_code('iN', iso_format='alpha2')
        # Output: False
        >>> country_code('ZWE', iso_format='alpha3')
        # Output: True

    Args:
        value:
            Country code string to validate.
        iso_format:
            ISO format to be used. Available options are:
            `auto`, `alpha2`, `alpha3` and `numeric`.

    Returns:
        (Literal[True]):
            If `value` is a valid country code.
        (ValidationError):
            If `value` is an invalid country code.
    """
    if not value:
        return False

    if not (1 < len(value) < 4):
        return False

    if iso_format == "auto" and (iso_format := get_code_type(value)) == "invalid":
        return False

    if iso_format == "alpha2":
        return value in alpha_2
    if iso_format == "alpha3":
        return value in alpha_3
    return value in numeric if iso_format == "numeric" else False
