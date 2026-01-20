# Fabric Demo Dashboard

A simple Streamlit dashboard demonstrating how a custom UI could integrate with Microsoft Fabric.

## Overview

This is a **demo application** that simulates Fabric connectivity. All data is currently mocked - real Fabric connections can be added later.

## Features

- **Business Case Selector** - Switch between Sales, Procurement, and Finance views
- **Pipeline Trigger** - Simulated Fabric pipeline execution with loading state
- **KPI Display** - Mock metrics that change based on selected business case
- **Weekly Trend Chart** - Streamlit-native bar chart visualization
- **Power BI Placeholder** - Ready for embedded Power BI reports

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

## Fabric-Ready Architecture

The code includes placeholder functions ready for real Fabric integration:

| Function | Purpose | Future Integration |
|----------|---------|-------------------|
| `trigger_fabric_pipeline()` | Run data pipelines | Fabric REST API |
| `get_fabric_data()` | Fetch data from Lakehouse/Warehouse | Semantic Link or REST API |
| `embed_powerbi_report()` | Embed interactive reports | Power BI Embedded |

Each function contains TODO comments with specific API endpoints and authentication details.

## Next Steps

- [ ] Add Entra ID (Azure AD) authentication
- [ ] Connect to real Fabric pipelines via REST API
- [ ] Embed actual Power BI reports
- [ ] Pull live data from Lakehouse/Warehouse

## Requirements

- Python 3.8+
- Streamlit 1.30+
