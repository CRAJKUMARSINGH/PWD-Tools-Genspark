import streamlit as st


st.set_page_config(page_title="Other PWD Tools", layout="wide")

st.title("PWD Tools - Additional Modules")
st.caption("These modules are scaffolded and can be expanded to full functionality.")

tools = [
	{"name": "🔒 Security Refund", "desc": "Security deposit refund calculations", "status": "Scaffolded"},
	{"name": "📊 Excel se EMD", "desc": "Hand Receipt Generator from Excel files", "status": "Scaffolded"},
	{"name": "📈 Financial Progress", "desc": "Track progress and LDs", "status": "Scaffolded"},
	{"name": "💰 Bill & Deviation", "desc": "Billing with deviation tracking", "status": "External linked in dashboard"},
]

cols = st.columns(2)
for i, t in enumerate(tools):
	with cols[i % 2]:
		st.subheader(t["name"]) 
		st.write(t["desc"])
		st.info(f"Status: {t['status']}")


