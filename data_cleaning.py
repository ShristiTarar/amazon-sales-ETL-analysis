{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1753322c-8b03-4a27-bda5-ac1dbb3d3b82",
   "metadata": {},
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# 1. Read the file (with low_memory=False to avoid dtype warnings)\n",
    "df = pd.read_csv(\"Amazon Sale Report.csv.zip\", low_memory=False)\n",
    "\n",
    "# 2. Rename columns to clean names \n",
    "df = df.rename(columns={\n",
    "    \"Order ID\": \"order_id\",\n",
    "    \"Date\": \"order_date\",\n",
    "    \"Status\": \"status\",\n",
    "    \"Fulfilment\": \"fulfilment\",\n",
    "    \"Sales Channel \": \"sales_channel\",\n",
    "    \"ship-service-level\": \"ship_service_level\",\n",
    "    \"Style\": \"style\",\n",
    "    \"SKU\": \"sku\",\n",
    "    \"Category\": \"category\",\n",
    "    \"Size\": \"size\",\n",
    "    \"ASIN\": \"asin\",\n",
    "    \"Courier Status\": \"courier_status\",\n",
    "    \"Qty\": \"qty\",\n",
    "    \"currency\": \"currency\",\n",
    "    \"Amount\": \"amount\",\n",
    "    \"ship-city\": \"ship_city\",\n",
    "    \"ship-state\": \"ship_state\",\n",
    "    \"ship-postal-code\": \"ship_postal_code\",\n",
    "    \"ship-country\": \"ship_country\",\n",
    "    \"promotion-ids\": \"promotion_ids\",\n",
    "    \"B2B\": \"b2b\",\n",
    "    \"fulfilled-by\": \"fulfilled_by\"\n",
    "})\n",
    "\n",
    "# 3. Drop useless columns if present\n",
    "df = df.drop(columns=[\"index\", \"Unnamed: 22\"], errors=\"ignore\")\n",
    "\n",
    "# 4. Fix data types\n",
    "df[\"order_date\"] = pd.to_datetime(\n",
    "    df[\"order_date\"],\n",
    "    format=\"%m-%d-%y\",   # because your dates look like 04-30-22\n",
    "    errors=\"coerce\"\n",
    ")\n",
    "\n",
    "df[\"qty\"] = pd.to_numeric(df[\"qty\"], errors=\"coerce\")\n",
    "df[\"amount\"] = pd.to_numeric(df[\"amount\"], errors=\"coerce\")\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "54edc932-b1f8-412c-9164-9cc21576294f",
   "metadata": {},
   "source": [
    "valid_status = [\"Shipped\", \"Delivered\", \"Complete\"]\n",
    "df = df[df[\"status\"].isin(valid_status)]\n",
    "\n",
    "# Drop rows with no order_id or amount\n",
    "df = df.dropna(subset=[\"order_id\", \"order_date\", \"amount\"])\n",
    "\n",
    "# Date features\n",
    "df[\"year\"] = df[\"order_date\"].dt.year\n",
    "df[\"month_num\"] = df[\"order_date\"].dt.month\n",
    "df[\"month_name\"] = df[\"order_date\"].dt.month_name()\n",
    "df[\"year_month\"] = df[\"order_date\"].dt.to_period(\"M\")\n",
    "df[\"weekday\"] = df[\"order_date\"].dt.day_name()\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "d9984ae3-1f24-458d-89c5-a87a9f2b4896",
   "metadata": {},
   "source": [
    "metros = [\"Delhi\", \"Mumbai\", \"Bengaluru\", \"Hyderabad\", \"Chennai\", \"Kolkata\", \"Pune\"]\n",
    "df[\"city_tier\"] = np.where(df[\"ship_city\"].isin(metros), \"Metro\", \"Non-Metro\")\n",
    "\n",
    "# Order-level revenue & quantity\n",
    "order_level = (\n",
    "    df.groupby(\"order_id\")\n",
    "      .agg({\n",
    "          \"order_date\": \"max\",\n",
    "          \"amount\": \"sum\",\n",
    "          \"qty\": \"sum\",\n",
    "          \"ship_city\": \"first\",\n",
    "          \"ship_state\": \"first\",\n",
    "          \"city_tier\": \"first\"\n",
    "          # Removed 'B2B' column since it doesn't exist in the DataFrame\n",
    "      })\n",
    "      .rename(columns={\"amount\": \"order_revenue\", \"qty\": \"order_qty\"})\n",
    "      .reset_index()\n",
    ")"
   ]
  },
  {
   "cell_type": "raw",
   "id": "ccc7381f-875c-4c75-a5b7-499173d409b3",
   "metadata": {},
   "source": [
    "df.to_csv(\"amazon_sales_clean.csv\", index=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
