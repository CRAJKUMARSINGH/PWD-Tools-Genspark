from pathlib import Path

import streamlit as st


st.set_page_config(page_title="PWD Tools - Dashboard & Review", layout="wide")

st.title("🏗️ PWD Tools - Dashboard")
st.caption("Streamlit viewer that links to tools and shows color/landing screenshots.")

# Instructions for accessing desktop tools
st.info("ℹ️ **Desktop Tools Access**: To use the desktop tools (those with disabled buttons), please run the main desktop application using `python pwd_main_landing.py` or the provided batch files.")

# Tool registry - KEEPING ONLY SIMPLE TOOLS
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
]

base_dir = Path("screenshots")

# Landing screenshot
landing = base_dir / "landing" / "main.png"
left, right = st.columns([1, 1])
with left:
    st.subheader("Main Landing (Desktop)")
    if landing.exists() and landing.stat().st_size > 0:
        try:
            st.image(str(landing), width='stretch')
        except Exception as e:
            st.warning("Could not load landing screenshot. File may be corrupted.")
            st.info("Run `python auto_run_tools.py` locally to generate screenshots.")
    else:
        st.info("Landing screenshot not found or is empty. Run `python auto_run_tools.py` locally to generate.")

st.divider()
st.subheader("Tools")

cols = st.columns(4)
for i, tool in enumerate(TOOLS):
    with cols[i % 4]:
        st.markdown(f"{tool['icon']} **{tool['name']}**")
        st.caption(tool["desc"]) 
        # Link handling
        if tool["external_url"]:
            st.link_button("Open Web Tool", tool["external_url"], key=f"web_{tool['key']}")
        else:
            st.button("Desktop Tool (local)", disabled=True, help="Desktop tools run locally via the desktop app", key=f"desktop_{tool['key']}")
        # Screenshots if present
        tool_dir = base_dir / tool["key"]
        images = sorted(tool_dir.glob("*.png")) if tool_dir.exists() else []
        if images:
            # Filter out empty files
            valid_images = [img for img in images if img.stat().st_size > 0]
            if valid_images:
                try:
                    # Use unique keys for each image
                    image_paths = [str(p) for p in valid_images[:3]]
                    captions = [p.name for p in valid_images[:3]]
                    st.image(image_paths, caption=captions, width='stretch')
                except Exception as e:
                    st.write("Could not load screenshots.")
            else:
                st.write("No valid screenshots found.")
        else:
            st.write("No screenshots yet.")