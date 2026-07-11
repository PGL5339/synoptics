from helpers import (
    option_toggle,
    radio,
    radio_toggle,
    radio_other,
    text,
    conditional_radio_multiple,
    conditional_radio_other,
    conditional_value,
    checkbox_group,
    field_label,
    handle_exclusive_checkbox,
)

DISPLAY_NAME = "Prostate, Resection"

SYNOPTIC = [
    ("title", "CASE SUMMARY", "(PROSTATE GLAND: Radical Prostatectomy) Standard(s): AJCC-UICC 8"),

    ("section", "SPECIMEN"),

    radio_other(
        "Procedure",
        [
            "Radical prostatectomy",
            "Not specified",
        ],
    ),

    ("section", "TUMOR"),

    conditional_radio_other(
        "Histologic Type",
        [
            "Acinar adenocarcinoma, conventional (usual)",
            "Acinar adenocarcinoma, signet-ring-like cell",
            "Acinar adenocarcinoma, pleomorphic giant cell",
            "Acinar adenocarcinoma, sarcomatoid",
            "Acinar adenocarcinoma, prostatic intraepithelial neoplasia-like",
            "Intraductal carcinoma",
            "Ductal adenocarcinoma",
            "Adenosquamous carcinoma",
            "Squamous cell carcinoma",
            "Basal cell (adenoid cystic) carcinoma",
            "Adenocarcinoma with neuroendocrine differentiation",
            "Well-differentiated neuroendocrine tumor",
            "Small cell neuroendocrine carcinoma",
            "Large cell neuroendocrine carcinoma",
            "Carcinoma, type cannot be determined",
        ],
        trigger="",
        sublabel="",
        suboptions=[],
    ),

    ("section", "HISTOLOGIC GRADE"),

    conditional_radio_multiple(
        "Grade",
        [
            "Grade group 1 (Gleason Score 3 + 3 = 6)",
            "Grade group 2 (Gleason Score 3 + 4 = 7)",
            "Grade group 3 (Gleason Score 4 + 3 = 7)",
            "Grade group 4 (Gleason Score 4 + 4 = 8)",
            "Grade group 4 (Gleason Score 3 + 5 = 8)",
            "Grade group 4 (Gleason Score 5 + 3 = 8)",
            "Grade group 5 (Gleason Score 4 + 5 = 9)",
            "Grade group 5 (Gleason Score 5 + 4 = 9)",
            "Grade group 5 (Gleason Score 5 + 5 = 10)",
            "Cannot be assessed",
            "Not applicable",
        ],
        conditional_fields={
            "Grade group 2 (Gleason Score 3 + 4 = 7)": [
                radio(
                    "Minor Tertiary Pattern 5 (less than 5%)",
                    [
                        "Not applicable / not identified",
                        "Present",
                    ],
                    key="grade_group_2_tertiary_pattern_5",
                ),
                radio(
                    "Percentage of Pattern 4",
                    [
                        "Less than or equal to 5%",
                        "6 - 10%",
                        "11 - 20%",
                        "21 - 30%",
                        "31 - 40%",
                        "Greater than 40%",
                    ],
                    key="grade_group_2_pattern_4_percentage",
                ),
            ],

            "Grade group 3 (Gleason Score 4 + 3 = 7)": [
                radio(
                    "Minor Tertiary Pattern 5 (less than 5%)",
                    [
                        "Not applicable / not identified",
                        "Present",
                    ],
                    key="grade_group_3_tertiary_pattern_5",
                ),
                radio(
                    "Percentage of Pattern 4",
                    [
                        "Less than 61%",
                        "61 - 70%",
                        "71 - 80%",
                        "81 - 90%",
                        "Greater than 90%",
                    ],
                    key="grade_group_3_pattern_4_percentage",
                ),
            ],

            "Grade group 4 (Gleason Score 4 + 4 = 8)": [
                text(
                    "Percentage of Pattern 4",
                    suffix="%",
                    key="grade_4_44_pattern_4",
                ),
                text(
                    "Percentage of Pattern 5",
                    suffix="%",
                    key="grade_4_44_pattern_5",
                ),
            ],

            "Grade group 4 (Gleason Score 3 + 5 = 8)": [
                text(
                    "Percentage of Pattern 4",
                    suffix="%",
                    key="grade_4_35_pattern_4",
                ),
                text(
                    "Percentage of Pattern 5",
                    suffix="%",
                    key="grade_4_35_pattern_5",
                ),
            ],

            "Grade group 4 (Gleason Score 5 + 3 = 8)": [
                text(
                    "Percentage of Pattern 4",
                    suffix="%",
                    key="grade_4_53_pattern_4",
                ),
                text(
                    "Percentage of Pattern 5",
                    suffix="%",
                    key="grade_4_53_pattern_5",
                ),
            ],

            "Grade group 5 (Gleason Score 4 + 5 = 9)": [
                text(
                    "Percentage of Pattern 4",
                    suffix="%",
                    key="grade_5_45_pattern_4",
                ),
                text(
                    "Percentage of Pattern 5",
                    suffix="%",
                    key="grade_5_45_pattern_5",
                ),
            ],

            "Grade group 5 (Gleason Score 5 + 4 = 9)": [
                text(
                    "Percentage of Pattern 4",
                    suffix="%",
                    key="grade_5_54_pattern_4",
                ),
                text(
                    "Percentage of Pattern 5",
                    suffix="%",
                    key="grade_5_54_pattern_5",
                ),
            ],

            "Grade group 5 (Gleason Score 5 + 5 = 10)": [
                text(
                    "Percentage of Pattern 4",
                    suffix="%",
                    key="grade_5_55_pattern_4",
                ),
                text(
                    "Percentage of Pattern 5",
                    suffix="%",
                    key="grade_5_55_pattern_5",
                ),
            ],

            "Cannot be assessed": text(
                "Specify",
                key="grade_cannot_be_assessed_comment",
            ),

            "Not applicable": text(
                "Specify",
                key="grade_not_applicable_comment",
            ),
        },
    ),

    conditional_radio_multiple(
        "Intraductal Carcinoma (IDC)",
        [
            "Not identified",
            "Present",
        ],
        conditional_fields={
            "Present": [
                conditional_radio_multiple(
                    "IDC Incorporated into Grade",
                    [
                        "Yes",
                        "No",
                        "Cannot be determined",
                    ],
                    key="idc_incorporated_into_grade",
                ),
            ],
        },
    ),

    conditional_radio_multiple(
        "Cribriform Glands",
        [
            "Not applicable",
            "Not identified",
            "Present",
            "Cannot be determined",
        ],
        conditional_fields={
            "Cannot be determined": [
                text(
                    "Explain",
                    key="cribriform_glands_cannot_be_determined",
                ),
            ],
        },
    ),


]