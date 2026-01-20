"""
Fabric Demo Dashboard
A simple Streamlit app demonstrating future Microsoft Fabric integration.
"""

import streamlit as st
import pandas as pd
import time
import random

# =============================================================================
# FABRIC PLACEHOLDER FUNCTIONS
# These functions simulate Fabric behavior and will be replaced with real
# API calls when connecting to Microsoft Fabric.
# =============================================================================

def trigger_fabric_pipeline(business_case: str) -> dict:
    """
    Trigger a Microsoft Fabric pipeline.

    TODO: Replace with actual Fabric REST API call:
    - Endpoint: https://api.fabric.microsoft.com/v1/workspaces/{workspaceId}/items/{itemId}/jobs/instances?jobType=Pipeline
    - Method: POST
    - Auth: Bearer token from Entra ID (Azure AD)

    Args:
        business_case: The selected business case (Sales, Procurement, Finance)

    Returns:
        dict with pipeline run status
    """
    # Simulate pipeline execution time
    time.sleep(2)

    return {
        "status": "success",
        "run_id": f"run-{random.randint(1000, 9999)}",
        "message": f"Pipeline for {business_case} completed successfully"
    }


def get_fabric_data(business_case: str) -> dict:
    """
    Fetch data from Microsoft Fabric Lakehouse or Warehouse.

    TODO: Replace with actual Fabric connection:
    - Use semantic-link library for direct Fabric access
    - Or use REST API: https://api.fabric.microsoft.com/v1/workspaces/{workspaceId}/lakehouses/{lakehouseId}/tables
    - Auth: Bearer token from Entra ID

    Args:
        business_case: The selected business case

    Returns:
        dict with KPIs and chart data
    """
    # Mock data based on business case
    mock_data = {
        "Sales": {
            "kpis": {"Revenue": "$2.4M", "Orders": "1,234", "Conversion": "3.2%"},
            "chart_data": [120, 150, 180, 140, 200, 220, 190],
            "chart_labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        },
        "Procurement": {
            "kpis": {"Spend": "$890K", "Suppliers": "45", "On-Time": "94%"},
            "chart_data": [45, 52, 48, 61, 55, 49, 58],
            "chart_labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        },
        "Finance": {
            "kpis": {"Budget": "$5.1M", "Variance": "-2.3%", "Forecasted": "$5.3M"},
            "chart_data": [500, 520, 510, 530, 525, 540, 535],
            "chart_labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        }
    }

    return mock_data.get(business_case, mock_data["Sales"])


def embed_powerbi_report(report_id: str) -> str:
    """
    Generate Power BI embed URL for iframe embedding.

    TODO: Replace with actual Power BI Embedded:
    - Use Power BI REST API to get embed token
    - Endpoint: https://api.powerbi.com/v1.0/myorg/groups/{groupId}/reports/{reportId}/GenerateToken
    - Or use publish-to-web URL for public reports
    - Auth: Service Principal or User token

    Args:
        report_id: The Power BI report ID

    Returns:
        Embed URL string
    """
    # Placeholder - return None to indicate no real embed available
    return None


# =============================================================================
# STREAMLIT APP
# =============================================================================

def main():
    # Page config
    st.set_page_config(
        page_title="Fabric Demo Dashboard",
        page_icon="📊",
        layout="wide"
    )

    # --- Header ---
    st.title("Fabric Demo Dashboard")
    st.markdown("""
    This is a **demo UI** showing how a custom dashboard could integrate with
    **Microsoft Fabric**. All data is currently mocked - real Fabric connections
    will be added later.
    """)

    st.divider()

    # --- Business Case Selector ---
    business_case = st.selectbox(
        "Select Business Case",
        options=["Sales", "Procurement", "Finance"],
        index=0
    )

    # Get mock data for selected business case
    data = get_fabric_data(business_case)

    # --- Pipeline Trigger ---
    st.subheader("Pipeline Control")

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Run Fabric Pipeline", type="primary"):
            with st.spinner("Running pipeline..."):
                result = trigger_fabric_pipeline(business_case)
            st.success(f"{result['message']} (ID: {result['run_id']})")

    st.divider()

    # --- KPIs ---
    st.subheader(f"{business_case} KPIs")

    kpi_cols = st.columns(3)
    for i, (label, value) in enumerate(data["kpis"].items()):
        with kpi_cols[i]:
            st.metric(label=label, value=value)

    # --- Charts ---
    st.subheader("Weekly Trend")

    chart_df = pd.DataFrame({
        "Day": data["chart_labels"],
        "Value": data["chart_data"]
    })
    st.bar_chart(chart_df, x="Value", y="Day", horizontal=True)

    st.divider()

    # --- Power BI Placeholder ---
    st.subheader("Power BI Report")

    embed_url = embed_powerbi_report("placeholder-report-id")

    if embed_url:
        # When real embed URL is available, use iframe
        st.components.v1.iframe(embed_url, height=400)
    else:
        # Placeholder box
        st.info(
            "📊 **Power BI Report will be embedded here later**\n\n"
            "This area will display an interactive Power BI report "
            "once the embed integration is configured."
        )


if __name__ == "__main__":
    main()
