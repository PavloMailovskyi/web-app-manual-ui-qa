# Test Summary Report

## Project
Cafedaria Website Testing

## Test Period
Manual testing session

## Scope
- Functional testing
- UI testing
- Cross-browser testing
- Cross-device testing
- Exploratory testing

## Test Environment
- Desktop: Chrome, Safari
- Mobile: iPhone Safari, iPhone Chrome

## Test Coverage
- Test Plan
- Test Cases (Positive, Negative, Boundary, UI)
- Checklists (Smoke, Regression, UI)
- Bug Reports
- SQL Checks

## Test Execution Summary

| Item | Count |
|-----|-------|
| Test cases executed | 20 |
| Passed | 19 |
| Failed | 1 |
| Blocked | 0 |
| Not executed | 0 |

## Defects Summary

| Severity | Count |
|--------|-------|
| High | 3 |
| Medium | 1 |
| Low | 0 |

## Defect Source

| Source | Count |
|------|-------|
| Test Case Execution | 1 |
| Exploratory Testing | 3 |

## Key Findings
- Incorrect total price calculation when updating item quantity in the shopping cart
- "Book a Table" functionality returns a server error (503)
- Address link opens incorrect location in Google Maps
- Minor UI issues identified during exploratory testing

## Risks
- Users may abandon checkout due to incorrect price calculation
- Table booking functionality is unavailable due to server-side error
- Incorrect address information may confuse or mislead users

## Conclusion
The Cafedaria website contains several high-severity issues that impact core functionality and user experience.  
It is recommended to fix the identified defects before releasing the application to production.

## QA Engineer
Pavlo Mailovskyi
