# Data Dictionary

**Theme:** Global AI Adoption & Workforce Displacement Index
**Date Range:** 2021-Q1 to 2024-Q4
**Currency:** USD

---

## Table of Contents

- [dim_country](#dim_country)
- [dim_industry](#dim_industry)
- [dim_skill_category](#dim_skill_category)
- [dim_date](#dim_date)
- [fact_workforce_ai_index](#fact_workforce_ai_index)

---

## dim_country

**Type:** DIMENSION
**Primary Key:** `country_id`
**Rows:** 30

### Description

One row per country tracked in the index, with macroeconomic and digital readiness attributes used to explain differences in AI adoption and displacement risk.

### Columns

| Column Name | Data Type | Nullable | Unique | Description |
|---|---|---|---|---|
| `country_id` | integer | No | Yes (PK) | Unique country identifier |
| `country_code` | string | No | Yes | ISO 3166-1 alpha-2 country code |
| `country_name` | string | No | Yes | Full country name |
| `region` | string | No | No | Geographic macro-region |
| `development_tier` | string | No | No | Developed or Emerging economy classification |
| `gdp_per_capita_usd` | float | No | No | GDP per capita in USD |
| `digital_infrastructure_score` | float | No | No | 0–100 composite score of digital infrastructure quality |
| `ai_policy_maturity` | string | No | No | Nascent, Developing, Established, or Advanced |
| `internet_penetration_pct` | float | No | No | Percentage of population with internet access |
| `stem_graduates_per_100k` | float | No | No | Annual STEM graduates per 100,000 population |

---

## dim_industry

**Type:** DIMENSION
**Primary Key:** `industry_id`
**Rows:** 25

### Description

One row per industry sector, capturing how exposed each sector is to automation and how aggressively it is investing in AI.

### Columns

| Column Name | Data Type | Nullable | Unique | Description |
|---|---|---|---|---|
| `industry_id` | integer | No | Yes (PK) | Unique industry identifier |
| `industry_name` | string | No | Yes | Industry name |
| `industry_sector` | string | No | No | High-level sector grouping |
| `automation_susceptibility` | float | No | No | 0–100 score of how susceptible the industry is to automation |
| `avg_ai_investment_pct_revenue` | float | No | No | Average AI investment as a percentage of revenue |
| `ai_adoption_stage` | string | No | No | Exploring, Piloting, Scaling, or Mature |
| `global_workforce_millions` | float | No | No | Estimated global workforce size in millions |
| `primary_ai_use_case` | string | No | No | The most common AI application in this industry |

---

## dim_skill_category

**Type:** DIMENSION
**Primary Key:** `skill_category_id`
**Rows:** 8

### Description

One row per broad skill category used to classify which kinds of work are most exposed to AI-driven displacement or augmentation.

### Columns

| Column Name | Data Type | Nullable | Unique | Description |
|---|---|---|---|---|
| `skill_category_id` | integer | No | Yes (PK) | Unique skill category identifier |
| `skill_category_name` | string | No | Yes | Skill category name |
| `skill_category_code` | string | No | Yes | Short code for the skill category |
| `ai_replaceability_score` | float | No | No | 0–100 score of how replaceable this skill category is by AI |
| `ai_augmentation_potential` | float | No | No | 0–100 score of how much AI can augment (rather than replace) this skill category |
| `median_reskilling_duration_months` | float | No | No | Typical time required to reskill a worker out of this category |
| `typical_education_level` | string | No | No | Typical education or training level associated with this category |
| `global_worker_share_pct` | float | No | No | Approximate share of the global workforce in this category (sums to ~100% across all rows) |

---

## dim_date

**Type:** DIMENSION
**Primary Key:** `date_id`
**Rows:** 16

### Description

One row per calendar quarter from 2021-Q1 to 2024-Q4, flagging pandemic-affected periods and the onset of the generative AI era (from Q4 2022, following the launch of mainstream generative AI tools).

### Columns

| Column Name | Data Type | Nullable | Unique | Description |
|---|---|---|---|---|
| `date_id` | integer | No | Yes (PK) | Unique date period identifier |
| `year` | integer | No | No | Calendar year (2021–2024) |
| `quarter` | integer | No | No | Calendar quarter (1–4) |
| `year_quarter_label` | string | No | Yes | Human-readable label, e.g. "2023-Q2" |
| `period_start_date` | date | No | No | First date of the quarter |
| `is_pandemic_period` | boolean | No | No | True if the quarter falls within the COVID-19 disruption period |
| `generative_ai_era` | boolean | No | No | True from 2022-Q4 onward, marking the mainstream generative AI period |

---

## fact_workforce_ai_index

**Type:** FACT
**Primary Key:** `index_id`
**Rows:** 300
**Grain:** one row per country × industry × skill category × quarter observation

### Description

Core fact table recording quarterly AI adoption, productivity impact, and workforce displacement metrics for a sampled combination of country, industry, skill category, and time period.

### Columns

| Column Name | Data Type | Nullable | Unique | Description |
|---|---|---|---|---|
| `index_id` | integer | No | Yes (PK) | Unique record identifier |
| `country_id` | integer | No | No (FK → dim_country) | Country dimension foreign key |
| `industry_id` | integer | No | No (FK → dim_industry) | Industry dimension foreign key |
| `skill_category_id` | integer | No | No (FK → dim_skill_category) | Skill category dimension foreign key |
| `date_id` | integer | No | No (FK → dim_date) | Date dimension foreign key |
| `ai_adoption_rate` | float | No | No | Percentage (0–100) of the workforce segment actively using AI tools |
| `productivity_impact_score` | float | No | No | 0–10 composite score of AI's productivity impact on this segment |
| `displacement_risk_index` | float | No | No | 0–10 composite score of displacement risk for this segment |
| `jobs_displaced_count` | integer | No | No | Estimated jobs displaced by AI adoption in this segment |
| `jobs_created_count` | integer | No | No | Estimated jobs created by AI adoption in this segment |
| `reskilling_investment_usd` | float | No | No | Capital invested in reskilling for this segment, in USD |
| `avg_wage_change_pct` | float | Yes | No | Average wage change (%) attributable to AI adoption; null where wage data is unavailable |
| `ai_tool_usage_hours_per_week` | float | Yes | No | Average weekly hours of AI tool usage per worker; null where usage data is unavailable |
| `workforce_size` | integer | No | No | Total workforce size for this segment |
| `data_confidence_score` | float | No | No | 0–1 score reflecting the reliability of the underlying survey data |

---

## Relationships

### Foreign Key Constraints

| From Table | From Column | To Table | To Column | Type |
|---|---|---|---|---|
| fact_workforce_ai_index | `country_id` | dim_country | `country_id` | Many To One |
| fact_workforce_ai_index | `industry_id` | dim_industry | `industry_id` | Many To One |
| fact_workforce_ai_index | `skill_category_id` | dim_skill_category | `skill_category_id` | Many To One |
| fact_workforce_ai_index | `date_id` | dim_date | `date_id` | Many To One |

---

## Data Quality & Characteristics

### Missing Values
`avg_wage_change_pct` and `ai_tool_usage_hours_per_week` each contain a small number (~3%) of nulls in the fact table, representing segments where survey data was unavailable. All other columns are fully populated.

### Unique Constraints
Primary key columns are unique with no nulls across all tables.

### Temporal Coverage
All `period_start_date` values fall within 2021-01-01 to 2024-10-01 (start of 2024-Q4).

---

*Dictionary generated on 2026-06-30*
