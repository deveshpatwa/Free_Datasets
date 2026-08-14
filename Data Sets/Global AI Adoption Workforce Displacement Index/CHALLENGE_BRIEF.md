# Data Challenge

## 🎯 Your Role

You are a labour market analyst at a global think tank advising governments and employers on the workforce impact of artificial intelligence. Your director has asked you to investigate how AI adoption is reshaping employment across countries, industries, and skill categories between 2021 and 2024, with particular attention to the shift since the arrival of generative AI tools in late 2022.

## 📊 The Scenario

Your think tank has been commissioned by an international policy coalition to produce a briefing on AI-driven workforce displacement and reskilling needs. Member governments want to understand which industries and skill categories are most exposed to AI-driven change, how adoption rates have shifted since generative AI tools became mainstream, and where reskilling investment is failing to keep pace with job displacement. Your findings will directly inform funding allocations for national reskilling programmes due to be announced later this year.

### Dataset Overview

- **Dimensions**: 4 dimension tables (country, industry, skill category, date)
- **Facts**: 1 fact table recording quarterly AI adoption and workforce displacement metrics
- **Scope**: Spans 2021-Q1 to 2024-Q4 (16 quarters)
- **Rows**: 300 fact records across 30 countries, 25 industries, and 8 skill categories
- ** Data is synthetic **

### Key Business Metrics

- **ai_adoption_rate** — percentage of the workforce in a given country/industry/skill segment actively using AI tools
- **displacement_risk_index** — composite 0–10 score estimating a segment's exposure to AI-driven job displacement
- **jobs_displaced_count** / **jobs_created_count** — net employment shift attributable to AI adoption
- **reskilling_investment_usd** — capital invested in workforce reskilling for the segment
- **data_confidence_score** — a 0–1 measure of how reliable the underlying survey data is for that record

## 🔍 Analysis Areas

Look for patterns and insights across these key areas:

- How AI adoption rates differ before and after the generative AI era (post-Q4 2022) across industries
- Which skill categories carry the highest displacement risk, and whether reskilling investment is proportional to that risk
- Whether developed and emerging economies are adopting AI at different rates, and what that implies for the global jobs gap
- Where job creation is offsetting (or failing to offset) job displacement at a country or industry level

## ❓ Guiding Questions

Use these questions to guide your analysis. They're starting points — feel free to explore further.

### Temporal Trends
- How has ai_adoption_rate changed quarter over quarter since the generative AI era began in Q4 2022?
- Is the rate of job displacement accelerating or stabilising across 2023–2024?
- Which quarters show the steepest rise in ai_tool_usage_hours_per_week?

### Industry & Skill Analysis
- Which industries combine high automation_susceptibility with low avg_ai_investment_pct_revenue, suggesting under-preparedness?
- Which skill categories show the largest gap between ai_replaceability_score and median_reskilling_duration_months?
- Are creative and interpersonal skill categories more resilient to displacement than administrative or manual ones?

### Country-Level Patterns
- How does displacement_risk_index correlate with digital_infrastructure_score and stem_graduates_per_100k by country?
- Do countries with more mature ai_policy_maturity show better job creation-to-displacement ratios?
- Which regions show the widest gap between developed and emerging economy adoption rates?

### Reskilling & Investment
- Is reskilling_investment_usd keeping pace with jobs_displaced_count at an industry level?
- Which combination of country and industry shows the largest shortfall between displacement risk and reskilling spend?

## 💡 Impact & Purpose

Your analysis should help policy stakeholders:

- Identify which countries, industries, and skill groups need urgent reskilling investment
- Understand how the generative AI era has changed the pace of workforce displacement
- Make the case for where coalition funding should be targeted
- Anticipate which segments are likely to face the sharpest disruption over the next two years

## 📋 Deliverables

Create a professional analytical report that includes:

1. **Executive Summary**
   - Key findings and recommendations
   - High-impact insights in plain language

2. **Detailed Analysis**
   - Visualisations showing trends and patterns across time, industry, and geography
   - Statistical summaries and breakdowns by skill category and development tier
   - Answers to the guiding questions

3. **Actionable Insights**
   - What you discovered and why it matters for policy decisions
   - Recommended next steps for reskilling investment targeting
   - Areas for deeper investigation

## 📁 Data Dictionary

See `DATA_DICTIONARY.md` for detailed descriptions of all tables and columns.

## 🚀 Getting Started

1. **Explore the data**: Start with summary statistics and distributions across countries, industries, and skill categories
2. **Check for issues**: Look for missing values, outliers, and data quality concerns (data_confidence_score is a useful filter)
3. **Visualise relationships**: Create charts showing adoption trends over time and displacement risk by segment
4. **Test hypotheses**: Use the guiding questions to structure your analysis
5. **Synthesise insights**: Connect findings across dimensions to build a coherent policy narrative

---
