# Part 2 Discovery Worksheet

**Date:** September 11, 2026  
**Team members:** Deva Rane  
Replace names if you worked with a pair or group.

## Roles

| Role | Full name | Notes |
|------|-----------|--------|
| Manager / Coordinator | Deva Rane | Kept the group on the notebook tasks |
| Presenter / Spokesperson | Deva Rane | Prepared the findings below |
| Recorder / Quality Control | Deva Rane | Checked that numbers match the notebook |
| Reflector / Process Analyst | Deva Rane | Notes at the bottom |

If the team has 3 people, combine Manager and Presenter.  
If the team has 2 people, also combine Recorder and Reflector.

**Files used:** `scorecard.csv`, `jupyter_tutorial.ipynb`, `scorecard_discovery.ipynb`

---

## Jupyter notebook practice

We completed the Dataquest Jupyter tutorial **up to but not including** the Example Analysis section.

What we practiced:
- Running markdown vs code cells (Shift+Enter)
- Functions, variables, and kernel state
- `%matplotlib inline` plots
- `%timeit` / `%%timeit` magics
- `help()` documentation
- A small pandas DataFrame

---

## College Scorecard discovery

### 1. What is one row?

One row is **one institution** (college, university, or other postsecondary school), not one student.

### 2. Size of the file

- About **6,273** institutions
- Dozens of useful columns in our subset (the raw file has thousands of columns)
- States/territories represented: **59**
- States with the most institutions: California, New York, Texas, Florida, Pennsylvania

### 3. Control type (who operates the school)

| Control | Meaning | Count (approx.) |
|---------|---------|-----------------|
| 1 | Public | 2,047 |
| 2 | Private nonprofit | 1,901 |
| 3 | Private for-profit | 2,325 |

### 4. Data quality

- **Admission rate** is missing for a large share of schools.
- **SAT average** is missing even more often.
- Some numeric fields can be the string `PrivacySuppressed`; we converted those to missing values.
- Because of missing data, we should not treat SAT or admission rate as complete for every college.

### 5. Selectivity

Among 4-year schools with enrollment of at least 200 and a reported admission rate:
- Typical admission rates are **high** (most schools are not extremely selective).
- The most selective names include Caltech, Stanford, Harvard, Yale, Columbia, Chicago, MIT, and Princeton (admission rates around 3–5%).

### 6. Cost

- **Public** in-state tuition is the lowest on average.
- **Private nonprofit** list tuition is the highest.
- Sticker tuition is not the same as net price after aid.

### 7. Earnings after college

- Median earnings about 10 years after entry are higher at many private nonprofit and STEM/health institutions.
- For-profit schools in this file have lower typical earnings.
- High tuition does not guarantee high later earnings.

### 8. Claims we can support

1. Public colleges generally have lower in-state sticker prices than private nonprofit colleges.
2. Extreme selectivity is rare in this dataset.
3. Institutional averages hide differences by major and by student.

### 9. Claims we should not make

1. That this file ranks teaching quality.
2. That missing admission rate means a school is not selective.
3. That list tuition is what students actually pay.

---

## Reflector notes

The important process step was agreeing on **what each column measures** before drawing conclusions. The easy mistake is treating incomplete columns (SAT, admission rate) as if they cover every school.

---

## What to upload

Submit these files in the GitHub Classroom assignment (each student submits the pair/group files):

**Part 1**
- `part1/speedingticket.py`
- `part1/heatingcooling.py`
- `part1/countinput.py`
- `part1/stocktrading.py`

**Part 2**
- `part2/jupyter_tutorial.ipynb`
- `part2/scorecard_discovery.ipynb`
- this worksheet (`part2/discovery_worksheet.md`)

Put pair/group names in the program header docstrings and in the role table above before you upload.
