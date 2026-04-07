# Databricks Free Edition DAB exercise

This project is a complete Declarative Automation Bundles example for Databricks Free Edition.

## What it does

- Uses **serverless** Lakeflow Jobs (no cluster block).
- Deploys **2 notebooks**:
  - `01_create_table.py`: creates schema and table in `main`.
  - `02_insert_dummy_data.py`: inserts deterministic dummy rows.
- Includes a tiny Python helper module and pytest tests.
- Includes GitHub Actions for:
  - PR validation
  - main branch deployment
- Includes an **optional** dashboard resource file you can enable after you create/export a dashboard from the Databricks UI.

## Local prerequisites

- Databricks CLI >= 0.205
- Python 3.11+
- A Databricks workspace URL and PAT or OAuth profile

## Install CLI

### Windows
```bash
winget install Databricks.DatabricksCLI
databricks version
```

### macOS/Linux
```bash
curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh
databricks version
```

## Configure local auth (PAT example)

```bash
databricks configure --profile FREE
```

Then answer:
- Databricks Host: your workspace URL
- Personal Access Token: your PAT

## Local workflow

```bash
python -m venv .venv
# activate the venv
pip install -r requirements-dev.txt

pytest

databricks bundle validate -t dev --profile FREE
databricks bundle deploy -t dev --profile FREE
databricks bundle run lakeflow_serverless_demo -t dev --profile FREE
databricks bundle summary -t dev --profile FREE
```

## After first deploy

Open the job in Databricks and run it. Then check:

```sql
SELECT * FROM main.dab_demo.customer_events ORDER BY event_id;
```

## Optional dashboard exercise

1. In Databricks SQL or Catalog Explorer, create a simple dashboard over `main.dab_demo.customer_events`.
2. Export it into the bundle:

```bash
databricks bundle generate dashboard --existing-id <dashboard-id> --resource-dir resources --dashboard-dir dashboards
```

3. Update `resources/dashboard.yml` with your SQL warehouse ID.
4. Add the dashboard file and deploy again:

```bash
databricks bundle deploy -t dev --profile FREE
```

## GitHub secrets

Create these repository secrets or environment secrets:
- `DATABRICKS_HOST`
- `DATABRICKS_TOKEN`

## CI/CD behavior

- Pull requests to `main`: run lint/tests/bundle validate
- Pushes to `main`: run lint/tests/validate/deploy
