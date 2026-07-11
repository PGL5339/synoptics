import importlib
import pkgutil

import streamlit as st

import data

from helpers import (
    build_rows_from_synoptic,
    render_copyable_table,
)


def load_synoptics():

    synoptics = {}

    for module_info in pkgutil.iter_modules(data.__path__):

        module = importlib.import_module(
            f"data.{module_info.name}"
        )

        synoptics[module.DISPLAY_NAME] = module.SYNOPTIC

    return synoptics


st.set_page_config(
    page_title="Pathology Synoptic Generator",
    layout="centered",
)

st.title("Pathology Synoptic Generator")

synoptics = load_synoptics()

selected = st.selectbox(
    "Choose Synoptic",
    list(synoptics.keys()),
)

rows = build_rows_from_synoptic(
    synoptics[selected]
)

if st.subheader("Preview"):
    render_copyable_table(rows)