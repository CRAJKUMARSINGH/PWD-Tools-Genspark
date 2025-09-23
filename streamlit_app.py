from pathlib import Path

import streamlit as st


st.set_page_config(page_title="PWD Tools - Dashboard & Review", layout="wide")

st.title("🏗️ PWD Tools - Dashboard")
st.caption("Streamlit viewer that links to tools and shows color/landing screenshots.")

# Tool registry (10 tools)
TOOLS = [
        {
                "key": "excel_emd",
                "name": "Excel se EMD",
                "icon": "📊",
                "desc": "Hand Receipt Generator from Excel files",
                "external_url": None,
        },
        {
                "key": "bill_note",
                "name": "Bill Note Sheet",
                "icon": "📝",
                "desc": "Bill Note Sheet Generator for PWD documentation",
                "external_url": None,
        },
        {
                "key": "emd_refund",
                "name": "EMD Refund",
                "icon": "💰",
                "desc": "Generate EMD refund receipts and documentation",
                "external_url": None,
        },
        {
                "key": "deductions_table",
                "name": "Deductions Table",
                "icon": "📊",
                "desc": "Calculate all standard deductions for bill amounts",
                "external_url": None,
        },
        {
                "key": "delay_calculator",
                "name": "Delay Calculator",
                "icon": "⏰",
                "desc": "Project delays and timeline analysis",
                "external_url": None,
        },
        {
                "key": "security_refund",
                "name": "Security Refund",
                "icon": "🔒",
                "desc": "Security deposit refund calculations",
                "external_url": None,
        },
        {
                "key": "financial_progress",
                "name": "Financial Progress",
                "icon": "📈",
                "desc": "Track financial progress and LDs",
                "external_url": None,
        },
        {
                "key": "stamp_duty",
                "name": "Stamp Duty",
                "icon": "📋",
                "desc": "Stamp duty calculation for work orders",
                "external_url": None,
        },
        {
                "key": "bill_deviation",
                "name": "Bill & Deviation",
                "icon": "💰",
                "desc": "Billing with deviation tracking",
                "external_url": "https://stream-bill-generator-pjzpbb7a9fdxfmpgpg7t4d.streamlit.app/",
        },
        {
                "key": "tender_processing",
                "name": "Tender Processing",
                "icon": "📋",
                "desc": "Comprehensive tender management",
                "external_url": "https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/",
        },
]

base_dir = Path("screenshots")

# Landing screenshot
landing = base_dir / "landing" / "main.png"
left, right = st.columns([1, 1])
with left:
        st.subheader("Main Landing (Desktop)")
        if landing.exists():
                st.image(str(landing), use_container_width=True)
        else:
                st.info("Landing screenshot not found. Run `python auto_run_tools.py` locally to generate.")

st.divider()
st.subheader("Tools")

cols = st.columns(5)
for i, tool in enumerate(TOOLS):
        with cols[i % 5]:
                st.markdown(f"{tool['icon']} **{tool['name']}**")
                st.caption(tool["desc"])
                # Link handling
                if tool["external_url"]:
                        st.link_button("Open Web Tool", tool["external_url"])
                else:
                        st.button("Desktop Tool (local)", disabled=True, help="Desktop tools run locally via the desktop app")
                # Screenshots if present
                tool_dir = base_dir / tool["key"]
                images = sorted(tool_dir.glob("*.png")) if tool_dir.exists() else []
                if images:
                        st.image([str(p) for p in images[:3]], caption=[p.name for p in images[:3]], use_container_width=True)
                else:
                        st.write("No screenshots yet.")