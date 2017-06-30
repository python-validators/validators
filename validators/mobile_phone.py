from .utils import validator
import re

locales = {
  'ar-DZ': '^(\+?213|0)(5|6|7)\d{8}$',
  'ar-SY': '^(!?(\+?963)|0)?9\d{8}$',
  'ar-SA': '^(!?(\+?966)|0)?5\d{8}$',
  'en-US': '^(\+?1)?[2-9]\d{2}[2-9](?!11)\d{6}$',
  'cs-CZ': '^(\+?420)? ?[1-9][0-9]{2} ?[0-9]{3} ?[0-9]{3}$',
  'de-DE': '^(\+?49[ \.\-])?([\(]{1}[0-9]{1,6}[\)])?([0-9 \.\-\']{3,20})((x|ext|extension)[ ]?[0-9]{1,4})?$',
  'da-DK': '^(\+?45)?(\d{8})$',
  'el-GR': '^(\+?30)?(69\d{8})$',
  'en-AU': '^(\+?61|0)4\d{8}$',
  'en-GB': '^(\+?44|0)7\d{9}$',
  'en-HK': '^(\+?852\-?)?[569]\d{3}\-?\d{4}$',
  'en-IN': '^(\+?91|0)?[789]\d{9}$',
  'en-KE': '^(\+?254|0)?[7]\d{8}$',
  'en-NG': '^(\+?234|0)?[789]\d{9}$',
  'en-NZ': '^(\+?64|0)2\d{7,9}$',
  'en-UG': '^(\+?256|0)?[7]\d{8}$',
  'en-RW': '^(\+?250|0)?[7]\d{8}$',
  'en-TZ': '^(\+?255|0)?[67]\d{8}$',
  'en-ZA': '^(\+?27|0)\d{9}$',
  'en-ZM': '^(\+?26)?09[567]\d{7}$',
  'es-ES': '^(\+?34)?(6\d{1}|7[1234])\d{7}$',
  'fi-FI': '^(\+?358|0)\s?(4(0|1|2|4|5|6)?|50)\s?(\d\s?){4,8}\d$',
  'fa-IR': '^(\+?98[\-\s]?|0)9[0-39]\d[\-\s]?\d{3}[\-\s]?\d{4}$',
  'fr-FR': '^(\+?33|0)[67]\d{8}$',
  'he-IL': '^(\+972|0)([23489]|5[0248]|77)[1-9]\d{6}',
  'hu-HU': '^(\+?36)(20|30|70)\d{7}$',
  'lt-LT': '^(\+370|8)\d{8}$',
  'id-ID': '^(\+?62|0[1-9])[\s|\d]+$',
  'it-IT': '^(\+?39)?\s?3\d{2} ?\d{6,7}$',
  'ko-KR': '^((\+?82)[ \-]?)?0?1([0|1|6|7|8|9]{1})[ \-]?\d{3,4}[ \-]?\d{4}$',
  'ja-JP': '^(\+?81|0)\d{1,4}[ \-]?\d{1,4}[ \-]?\d{4}$',
  'ms-MY': '^(\+?6?01){1}(([145]{1}(\-|\s)?\d{7,8})|([236789]{1}(\s|\-)?\d{7}))$',
  'nb-NO': '^(\+?47)?[49]\d{7}$',
  'nl-BE': '^(\+?32|0)4?\d{8}$',
  'nn-NO': '^(\+?47)?[49]\d{7}$',
  'pl-PL': '^(\+?48)? ?[5-8]\d ?\d{3} ?\d{2} ?\d{2}$',
  'pt-BR': '^(\+?55|0)\-?[1-9]{2}\-?[2-9]{1}\d{3,4}\-?\d{4}$',
  'pt-PT': '^(\+?351)?9[1236]\d{7}$',
  'ro-RO': '^(\+?4?0)\s?7\d{2}(\'|\s|\.|\-)?\d{3}(\s|\.|\-)?\d{3}$',
  'en-PK': '^((\+92)|(0092))-{0,1}\d{3}-{0,1}\d{7}$|^\d{11}$|^\d{4}-\d{7}$',
  'ru-RU': '^(\+?7|8)?9\d{9}$',
  'sr-RS': '^(\+3816|06)[- \d]{5,9}$',
  'tr-TR': '^(\+?90|0)?5\d{9}$',
  'vi-VN': '^(\+?84|0)?((1(2([0-9])|6([2-9])|88|99))|(9((?!5)[0-9])))([0-9]{7})$',
  'zh-CN': '^(\+?0?86\-?)?1[345789]\d{9}$',
  'zh-TW': '^(\+?886\-?|0)?9\d{8}$',
}


@validator
def mobile_phone(value, locale=None):
    """
    Validate a mobile phone number.

    Inspired by validate.js. It returns True if a number is a valid phone
    number and False otherwise

    Examples::

        >>> mobile_phone('+1(202)-555-0178')
        True

        >>> mobile_phone('+1(202)-555-017')
        ValidationFailure(func=mobile_phone, args={'locale': None, 'value': '+1(202)-555-017'})

        >>> mobile_phone('0705887887', 'en-KE')
        True
    """
    # remove dashes, brackets and spaces
    value = re.sub('[^0-9+]+', '', value)
    print value
    if locale:
        if locale in locales.keys():
            pattern = locales.get(locale)
            match = re.match(pattern, value)
            if match:
                return True
            return False
        else:
            raise AssertionError('locale {0} is not available'.format(locale))
    else:
        # locale wasn't provided
        matched = False
        for _, pattern in locales.iteritems():
            match = re.match(pattern, value)
            if match:
                matched = True
        if matched:
            return True
        return False
