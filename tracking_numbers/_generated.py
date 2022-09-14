# DO NOT EDIT - Generated by codegen.py
import re

from tracking_numbers.checksum_validator import Mod10
from tracking_numbers.checksum_validator import Mod7
from tracking_numbers.checksum_validator import NoChecksum
from tracking_numbers.checksum_validator import S10
from tracking_numbers.checksum_validator import SumProductWithWeightsAndModulo
from tracking_numbers.definition import AdditionalValidation
from tracking_numbers.definition import TrackingNumberDefinition
from tracking_numbers.serial_number import DefaultSerialNumberParser
from tracking_numbers.serial_number import PrependIf
from tracking_numbers.serial_number import UPSSerialNumberParser
from tracking_numbers.types import Courier
from tracking_numbers.types import Product
from tracking_numbers.value_matcher import ExactValueMatcher
from tracking_numbers.value_matcher import RegexValueMatcher


DEFINITIONS = [
    TrackingNumberDefinition(
        courier=Courier(code="dhl", name="DHL"),
        product=Product(name="DHL Express"),
        number_regex=re.compile(
            "\\s*(?P<SerialNumber>([0-9]\\s*){9})(?P<CheckDigit>([0-9]\\s*))",
        ),
        tracking_url_template="http://www.dhl.com/en/express/tracking.html?brand=DHL&AWB=%s",
        serial_number_parser=DefaultSerialNumberParser(prepend_if=None),
        checksum_validator=Mod7(),
        additional_validations=[],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="dhl", name="DHL"),
        product=Product(name="DHL Express Air"),
        number_regex=re.compile(
            "\\s*(?P<SerialNumber>([0-9]\\s*){10})(?P<CheckDigit>[0-9]\\s*)",
        ),
        tracking_url_template="http://www.dhl.com/en/express/tracking.html?brand=DHL&AWB=%s",
        serial_number_parser=DefaultSerialNumberParser(prepend_if=None),
        checksum_validator=Mod7(),
        additional_validations=[],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="amazon", name="Amazon"),
        product=Product(name="Amazon Logistics"),
        number_regex=re.compile(
            "\\s*T\\s*B\\s*A\\s*(?P<SerialNumber>([0-9]\\s*){12,12})\\s*",
        ),
        tracking_url_template=None,
        serial_number_parser=DefaultSerialNumberParser(prepend_if=None),
        checksum_validator=NoChecksum(),
        additional_validations=[],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="usps", name="United States Postal Service"),
        product=Product(name="USPS 20"),
        number_regex=re.compile(
            "\\s*(?P<SerialNumber>(?P<ServiceType>([0-9]\\s*){2})(?P<ShipperId>([0-9]\\s*){9})(?P<PackageId>([0-9]\\s*){8}))(?P<CheckDigit>[0-9]\\s*)",
        ),
        tracking_url_template="https://tools.usps.com/go/TrackConfirmAction?tLabels=%s",
        serial_number_parser=DefaultSerialNumberParser(prepend_if=None),
        checksum_validator=Mod10(odds_multiplier=1, evens_multiplier=3),
        additional_validations=[
            AdditionalValidation(
                regex_group_name="ServiceType",
                value_matchers=[
                    ExactValueMatcher(value="71"),
                    ExactValueMatcher(value="73"),
                    ExactValueMatcher(value="77"),
                    ExactValueMatcher(value="81"),
                ],
            ),
        ],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="usps", name="United States Postal Service"),
        product=Product(name="USPS 34v2"),
        number_regex=re.compile(
            "\\s*(?P<RoutingApplicationId>4\\s*2\\s*0\\s*)(?P<DestinationZip>([0-9]\\s*){5})(?P<RoutingNumber>([0-9]\\s*){4})(?P<SerialNumber>(?P<ApplicationIdentifier>9\\s*[2345]\\s*)?(?P<ShipperId>([0-9]\\s*){8})(?P<PackageId>([0-9]\\s*){11}))(?P<CheckDigit>[0-9]\\s*)",
        ),
        tracking_url_template="https://tools.usps.com/go/TrackConfirmAction?tLabels=%s",
        serial_number_parser=DefaultSerialNumberParser(prepend_if=None),
        checksum_validator=Mod10(odds_multiplier=1, evens_multiplier=3),
        additional_validations=[],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="usps", name="United States Postal Service"),
        product=Product(name="USPS 91"),
        number_regex=re.compile(
            "\\s*(?:(?P<RoutingApplicationId>4\\s*2\\s*0\\s*)(?P<DestinationZip>([0-9]\\s*){5}))?(?P<SerialNumber>(?P<ApplicationIdentifier>9\\s*[12345]\\s*)?(?P<SCNC>([0-9]\\s*){2})(?P<ServiceType>([0-9]\\s*){2})(?P<ShipperId>([0-9]\\s*){8})(?P<PackageId>([0-9]\\s*){11}|([0-9]\\s*){7}))(?P<CheckDigit>[0-9]\\s*)",
        ),
        tracking_url_template="https://tools.usps.com/go/TrackConfirmAction?tLabels=%s",
        serial_number_parser=DefaultSerialNumberParser(
            prepend_if=PrependIf(
                matches_regex=re.compile("^(?!9[1-5]).+"),
                content="91",
            ),
        ),
        checksum_validator=Mod10(odds_multiplier=1, evens_multiplier=3),
        additional_validations=[],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="fedex", name="FedEx"),
        product=Product(name="FedEx Express (12)"),
        number_regex=re.compile(
            "\\s*(?P<SerialNumber>([0-9]\\s*){11})(?P<CheckDigit>[0-9]\\s*)",
        ),
        tracking_url_template="https://www.fedex.com/apps/fedextrack/?tracknumbers=%s",
        serial_number_parser=DefaultSerialNumberParser(prepend_if=None),
        checksum_validator=SumProductWithWeightsAndModulo(
            weights=[3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1],
            first_modulo=11,
            second_modulo=10,
        ),
        additional_validations=[],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="fedex", name="FedEx"),
        product=Product(name="FedEx Express (34)"),
        number_regex=re.compile(
            "\\s*1\\s*0\\s*0\\s*[0-9]\\s*[0-9]\\s*([0-9]\\s*){10}(?P<DestinationZip>([0-9]\\s*){5})(?P<SerialNumber>([0-9]\\s*){13})(?P<CheckDigit>[0-9]\\s*)",
        ),
        tracking_url_template="https://www.fedex.com/apps/fedextrack/?tracknumbers=%s",
        serial_number_parser=DefaultSerialNumberParser(prepend_if=None),
        checksum_validator=SumProductWithWeightsAndModulo(
            weights=[1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1],
            first_modulo=11,
            second_modulo=10,
        ),
        additional_validations=[],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="fedex", name="FedEx"),
        product=Product(name="FedEx SmartPost"),
        number_regex=re.compile(
            "\\s*(?P<ApplicationIdentifier>9\\s*2\\s*)?(?P<SerialNumber>(?P<ServiceType>([0-9]\\s*){3})(?P<ShipperId>([0-9]\\s*){9})(?P<PackageId>([0-9]\\s*){7}))(?P<CheckDigit>([0-9]\\s*))",
        ),
        tracking_url_template="https://www.fedex.com/apps/fedextrack/?tracknumbers=%s",
        serial_number_parser=DefaultSerialNumberParser(
            prepend_if=PrependIf(matches_regex=re.compile("^(?!92).+"), content="92"),
        ),
        checksum_validator=Mod10(odds_multiplier=1, evens_multiplier=3),
        additional_validations=[],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="fedex", name="FedEx"),
        product=Product(name="FedEx Ground"),
        number_regex=re.compile(
            "\\s*(?P<SerialNumber>([0-9]\\s*){14})(?P<CheckDigit>([0-9]\\s*))",
        ),
        tracking_url_template="https://www.fedex.com/apps/fedextrack/?tracknumbers=%s",
        serial_number_parser=DefaultSerialNumberParser(prepend_if=None),
        checksum_validator=Mod10(odds_multiplier=3, evens_multiplier=1),
        additional_validations=[],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="fedex", name="FedEx"),
        product=Product(name="FedEx Ground (SSCC-18)"),
        number_regex=re.compile(
            "\\s*(?P<ShippingContainerType>([0-9]\\s*){2})(?P<SerialNumber>([0-9]\\s*){15})(?P<CheckDigit>[0-9]\\s*)",
        ),
        tracking_url_template="https://www.fedex.com/apps/fedextrack/?tracknumbers=%s",
        serial_number_parser=DefaultSerialNumberParser(prepend_if=None),
        checksum_validator=Mod10(odds_multiplier=1, evens_multiplier=3),
        additional_validations=[
            AdditionalValidation(
                regex_group_name="ShippingContainerType",
                value_matchers=[
                    ExactValueMatcher(value="00"),
                    ExactValueMatcher(value="01"),
                    ExactValueMatcher(value="02"),
                    ExactValueMatcher(value="04"),
                ],
            ),
        ],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="fedex", name="FedEx"),
        product=Product(name="FedEx Ground 96 (22)"),
        number_regex=re.compile(
            "\\s*(?P<ApplicationIdentifier>9\\s*6\\s*)(?P<SCNC>([0-9]\\s*){2})(?P<ServiceType>([0-9]\\s*){3})(?P<SerialNumber>(?P<ShipperId>([0-9]\\s*){7})(?P<PackageId>([0-9]\\s*){7}))(?P<CheckDigit>[0-9]\\s*)",
        ),
        tracking_url_template="https://www.fedex.com/apps/fedextrack/?tracknumbers=%s",
        serial_number_parser=DefaultSerialNumberParser(prepend_if=None),
        checksum_validator=Mod10(odds_multiplier=3, evens_multiplier=1),
        additional_validations=[],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="fedex", name="FedEx"),
        product=Product(name="FedEx Ground GSN"),
        number_regex=re.compile(
            "\\s*(?P<ApplicationIdentifier>9\\s*6\\s*)(?P<SCNC>([0-9]\\s*){2})([0-9]\\s*){5}(?P<GSN>([0-9]\\s*){10})[0-9]\\s*(?P<SerialNumber>([0-9]\\s*){13})(?P<CheckDigit>[0-9]\\s*)",
        ),
        tracking_url_template="https://www.fedex.com/apps/fedextrack/?tracknumbers=%s",
        serial_number_parser=DefaultSerialNumberParser(prepend_if=None),
        checksum_validator=SumProductWithWeightsAndModulo(
            weights=[1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1],
            first_modulo=11,
            second_modulo=10,
        ),
        additional_validations=[],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="ups", name="UPS"),
        product=Product(name="UPS"),
        number_regex=re.compile(
            "\\s*1\\s*Z\\s*(?P<SerialNumber>(?P<ShipperId>(?:[A-Z0-9]\\s*){6,6})(?P<ServiceType>(?:[A-Z0-9]\\s*){2,2})(?P<PackageId>(?:[A-Z0-9]\\s*){7,7}))(?P<CheckDigit>[A-Z0-9]\\s*)",
        ),
        tracking_url_template="https://wwwapps.ups.com/WebTracking/track?track=yes&trackNums=%s",
        serial_number_parser=UPSSerialNumberParser(),
        checksum_validator=Mod10(odds_multiplier=2, evens_multiplier=1),
        additional_validations=[
            AdditionalValidation(
                regex_group_name="ServiceType",
                value_matchers=[
                    ExactValueMatcher(value="01"),
                    ExactValueMatcher(value="02"),
                    ExactValueMatcher(value="03"),
                    ExactValueMatcher(value="12"),
                    ExactValueMatcher(value="13"),
                    ExactValueMatcher(value="15"),
                    ExactValueMatcher(value="22"),
                    ExactValueMatcher(value="32"),
                    ExactValueMatcher(value="33"),
                    ExactValueMatcher(value="41"),
                    ExactValueMatcher(value="42"),
                    ExactValueMatcher(value="44"),
                    ExactValueMatcher(value="66"),
                    ExactValueMatcher(value="72"),
                    ExactValueMatcher(value="78"),
                    ExactValueMatcher(value="90"),
                    ExactValueMatcher(value="A0"),
                    ExactValueMatcher(value="A1"),
                    ExactValueMatcher(value="A2"),
                    ExactValueMatcher(value="A8"),
                    ExactValueMatcher(value="A9"),
                    ExactValueMatcher(value="AA"),
                    ExactValueMatcher(value="YW"),
                ],
            ),
        ],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="s10", name="S10 International Standard"),
        product=Product(name="S10"),
        number_regex=re.compile(
            "\\s*(?P<ServiceType>([A-Z]\\s*){2})(?P<SerialNumber>([0-9]\\s*){8})(?P<CheckDigit>([0-9]\\s*))(?P<CountryCode>([A-Z]\\s*){2})",
        ),
        tracking_url_template=None,
        serial_number_parser=DefaultSerialNumberParser(prepend_if=None),
        checksum_validator=S10(),
        additional_validations=[
            AdditionalValidation(
                regex_group_name="ServiceType",
                value_matchers=[
                    RegexValueMatcher(pattern=re.compile("E[A-Z]")),
                    RegexValueMatcher(pattern=re.compile("L[A-Z]")),
                    RegexValueMatcher(pattern=re.compile("M[A-Z]")),
                    RegexValueMatcher(pattern=re.compile("Q[A-M]")),
                    RegexValueMatcher(pattern=re.compile("R[A-Z]")),
                    RegexValueMatcher(pattern=re.compile("U[A-Z]")),
                    RegexValueMatcher(pattern=re.compile("V[A-Z]")),
                    RegexValueMatcher(pattern=re.compile("C[A-Z]")),
                    RegexValueMatcher(pattern=re.compile("H[A-Z]")),
                    RegexValueMatcher(
                        pattern=re.compile("([BDNPZ][A-Z]|A[V-Z]|G[AD])"),
                    ),
                ],
            ),
            AdditionalValidation(
                regex_group_name="CountryCode",
                value_matchers=[
                    ExactValueMatcher(value="AF"),
                    ExactValueMatcher(value="AL"),
                    ExactValueMatcher(value="DZ"),
                    ExactValueMatcher(value="AO"),
                    ExactValueMatcher(value="AG"),
                    ExactValueMatcher(value="AR"),
                    ExactValueMatcher(value="AM"),
                    ExactValueMatcher(value="AU"),
                    ExactValueMatcher(value="AT"),
                    ExactValueMatcher(value="AZ"),
                    ExactValueMatcher(value="BS"),
                    ExactValueMatcher(value="BH"),
                    ExactValueMatcher(value="BD"),
                    ExactValueMatcher(value="BB"),
                    ExactValueMatcher(value="BY"),
                    ExactValueMatcher(value="BE"),
                    ExactValueMatcher(value="BZ"),
                    ExactValueMatcher(value="BJ"),
                    ExactValueMatcher(value="BT"),
                    ExactValueMatcher(value="BO"),
                    ExactValueMatcher(value="BA"),
                    ExactValueMatcher(value="BW"),
                    ExactValueMatcher(value="BR"),
                    ExactValueMatcher(value="BN"),
                    ExactValueMatcher(value="BG"),
                    ExactValueMatcher(value="BF"),
                    ExactValueMatcher(value="BI"),
                    ExactValueMatcher(value="KH"),
                    ExactValueMatcher(value="CM"),
                    ExactValueMatcher(value="CA"),
                    ExactValueMatcher(value="CV"),
                    ExactValueMatcher(value="CF"),
                    ExactValueMatcher(value="TD"),
                    ExactValueMatcher(value="CL"),
                    ExactValueMatcher(value="CN"),
                    ExactValueMatcher(value="HK"),
                    ExactValueMatcher(value="CO"),
                    ExactValueMatcher(value="KM"),
                    ExactValueMatcher(value="CG"),
                    ExactValueMatcher(value="CR"),
                    ExactValueMatcher(value="HR"),
                    ExactValueMatcher(value="CU"),
                    ExactValueMatcher(value="CY"),
                    ExactValueMatcher(value="CZ"),
                    ExactValueMatcher(value="CI"),
                    ExactValueMatcher(value="KP"),
                    ExactValueMatcher(value="CD"),
                    ExactValueMatcher(value="DK"),
                    ExactValueMatcher(value="DJ"),
                    ExactValueMatcher(value="DM"),
                    ExactValueMatcher(value="DO"),
                    ExactValueMatcher(value="EC"),
                    ExactValueMatcher(value="EG"),
                    ExactValueMatcher(value="SV"),
                    ExactValueMatcher(value="GQ"),
                    ExactValueMatcher(value="ER"),
                    ExactValueMatcher(value="EE"),
                    ExactValueMatcher(value="ET"),
                    ExactValueMatcher(value="FJ"),
                    ExactValueMatcher(value="FI"),
                    ExactValueMatcher(value="FR"),
                    ExactValueMatcher(value="GA"),
                    ExactValueMatcher(value="GM"),
                    ExactValueMatcher(value="GE"),
                    ExactValueMatcher(value="DE"),
                    ExactValueMatcher(value="GH"),
                    ExactValueMatcher(value="GB"),
                    ExactValueMatcher(value="GR"),
                    ExactValueMatcher(value="GD"),
                    ExactValueMatcher(value="GT"),
                    ExactValueMatcher(value="GN"),
                    ExactValueMatcher(value="GW"),
                    ExactValueMatcher(value="GY"),
                    ExactValueMatcher(value="HT"),
                    ExactValueMatcher(value="HN"),
                    ExactValueMatcher(value="HU"),
                    ExactValueMatcher(value="IS"),
                    ExactValueMatcher(value="IN"),
                    ExactValueMatcher(value="ID"),
                    ExactValueMatcher(value="IR"),
                    ExactValueMatcher(value="IQ"),
                    ExactValueMatcher(value="IE"),
                    ExactValueMatcher(value="IL"),
                    ExactValueMatcher(value="IT"),
                    ExactValueMatcher(value="JM"),
                    ExactValueMatcher(value="JP"),
                    ExactValueMatcher(value="JO"),
                    ExactValueMatcher(value="KZ"),
                    ExactValueMatcher(value="KE"),
                    ExactValueMatcher(value="KI"),
                    ExactValueMatcher(value="KR"),
                    ExactValueMatcher(value="KW"),
                    ExactValueMatcher(value="KG"),
                    ExactValueMatcher(value="LA"),
                    ExactValueMatcher(value="LV"),
                    ExactValueMatcher(value="LB"),
                    ExactValueMatcher(value="LS"),
                    ExactValueMatcher(value="LR"),
                    ExactValueMatcher(value="LY"),
                    ExactValueMatcher(value="LI"),
                    ExactValueMatcher(value="LT"),
                    ExactValueMatcher(value="LU"),
                    ExactValueMatcher(value="MG"),
                    ExactValueMatcher(value="MW"),
                    ExactValueMatcher(value="MY"),
                    ExactValueMatcher(value="MV"),
                    ExactValueMatcher(value="ML"),
                    ExactValueMatcher(value="MT"),
                    ExactValueMatcher(value="MR"),
                    ExactValueMatcher(value="MU"),
                    ExactValueMatcher(value="MX"),
                    ExactValueMatcher(value="MD"),
                    ExactValueMatcher(value="MC"),
                    ExactValueMatcher(value="MN"),
                    ExactValueMatcher(value="ME"),
                    ExactValueMatcher(value="MA"),
                    ExactValueMatcher(value="MZ"),
                    ExactValueMatcher(value="MM"),
                    ExactValueMatcher(value="NA"),
                    ExactValueMatcher(value="NR"),
                    ExactValueMatcher(value="NP"),
                    ExactValueMatcher(value="NL"),
                    ExactValueMatcher(value="NZ"),
                    ExactValueMatcher(value="NI"),
                    ExactValueMatcher(value="NE"),
                    ExactValueMatcher(value="NG"),
                    ExactValueMatcher(value="NO"),
                    ExactValueMatcher(value="OM"),
                    ExactValueMatcher(value="PK"),
                    ExactValueMatcher(value="PA"),
                    ExactValueMatcher(value="PG"),
                    ExactValueMatcher(value="PY"),
                    ExactValueMatcher(value="PE"),
                    ExactValueMatcher(value="PH"),
                    ExactValueMatcher(value="PL"),
                    ExactValueMatcher(value="PT"),
                    ExactValueMatcher(value="QA"),
                    ExactValueMatcher(value="RO"),
                    ExactValueMatcher(value="RU"),
                    ExactValueMatcher(value="RW"),
                    ExactValueMatcher(value="KN"),
                    ExactValueMatcher(value="LC"),
                    ExactValueMatcher(value="VC"),
                    ExactValueMatcher(value="WS"),
                    ExactValueMatcher(value="SM"),
                    ExactValueMatcher(value="ST"),
                    ExactValueMatcher(value="SA"),
                    ExactValueMatcher(value="SN"),
                    ExactValueMatcher(value="RS"),
                    ExactValueMatcher(value="SC"),
                    ExactValueMatcher(value="SL"),
                    ExactValueMatcher(value="SG"),
                    ExactValueMatcher(value="SK"),
                    ExactValueMatcher(value="SI"),
                    ExactValueMatcher(value="SB"),
                    ExactValueMatcher(value="SO"),
                    ExactValueMatcher(value="ZA"),
                    ExactValueMatcher(value="SS"),
                    ExactValueMatcher(value="ES"),
                    ExactValueMatcher(value="LK"),
                    ExactValueMatcher(value="SD"),
                    ExactValueMatcher(value="SR"),
                    ExactValueMatcher(value="SZ"),
                    ExactValueMatcher(value="SE"),
                    ExactValueMatcher(value="CH"),
                    ExactValueMatcher(value="SY"),
                    ExactValueMatcher(value="TJ"),
                    ExactValueMatcher(value="TZ"),
                    ExactValueMatcher(value="TH"),
                    ExactValueMatcher(value="MK"),
                    ExactValueMatcher(value="TL"),
                    ExactValueMatcher(value="TG"),
                    ExactValueMatcher(value="TO"),
                    ExactValueMatcher(value="TT"),
                    ExactValueMatcher(value="TN"),
                    ExactValueMatcher(value="TR"),
                    ExactValueMatcher(value="TM"),
                    ExactValueMatcher(value="TV"),
                    ExactValueMatcher(value="UG"),
                    ExactValueMatcher(value="UA"),
                    ExactValueMatcher(value="AE"),
                    ExactValueMatcher(value="US"),
                    ExactValueMatcher(value="UY"),
                    ExactValueMatcher(value="UZ"),
                    ExactValueMatcher(value="VU"),
                    ExactValueMatcher(value="VA"),
                    ExactValueMatcher(value="VE"),
                    ExactValueMatcher(value="VN"),
                    ExactValueMatcher(value="YE"),
                    ExactValueMatcher(value="ZM"),
                    ExactValueMatcher(value="ZW"),
                ],
            ),
        ],
    ),
    TrackingNumberDefinition(
        courier=Courier(code="ontrac", name="OnTrac"),
        product=Product(name="OnTrac"),
        number_regex=re.compile(
            "\\s*C\\s*(?P<SerialNumber>([0-9]\\s*){13})(?P<CheckDigit>[0-9]\\s*)",
        ),
        tracking_url_template="http://www.ontrac.com/trackingres.asp?tracking_number=%s",
        serial_number_parser=DefaultSerialNumberParser(
            prepend_if=PrependIf(matches_regex=re.compile("^(?!4).+$"), content="4"),
        ),
        checksum_validator=Mod10(odds_multiplier=2, evens_multiplier=1),
        additional_validations=[],
    ),
]
