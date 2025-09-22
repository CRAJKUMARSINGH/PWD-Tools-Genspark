import os
from pathlib import Path

import streamlit as st


st.set_page_config(page_title="PWD Tools - Visual Review", layout="wide")

st.title("PWD Tools - Landing & Tools Visual Review")
st.write("This app displays screenshots captured from the desktop app to review color templates and landing page elegance.")

base_dir = Path("screenshots")

if not base_dir.exists():
	st.warning("No screenshots found. Run `python auto_run_tools.py` locally to generate them.")
	st.stop()

tool_dirs = sorted([p for p in base_dir.iterdir() if p.is_dir()])

tabs = st.tabs([p.name for p in tool_dirs]) if tool_dirs else []

for tab, tool_dir in zip(tabs, tool_dirs):
	with tab:
		st.header(tool_dir.name.replace("_", " ").title())
		images = sorted(tool_dir.glob("*.png"))
		if not images:
			st.info("No images found for this tool.")
			continue
		cols = st.columns(3)
		for idx, img_path in enumerate(images):
			with cols[idx % 3]:
				st.image(str(img_path), caption=img_path.name, use_container_width=True)

landing = base_dir / "landing" / "main.png"
st.divider()
st.subheader("Main Landing Page")
if landing.exists():
	st.image(str(landing), caption="Main Landing Page", use_container_width=True)
else:
	st.info("Landing screenshot not found. It will appear after running the automation.")


