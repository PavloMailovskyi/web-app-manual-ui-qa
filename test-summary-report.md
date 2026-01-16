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

## Test Execution Summary

| Item                  | Count |
|-----------------------|-------|
| Test cases executed   | 20    |
| Passed                | 16    |
| Failed / Open         | 4     |
| Blocked               | 0     |
| Not executed          | 0     |

---

## Defects Summary

| Bug ID       | Title                                             | Status | Related Test Case | Severity | Notes / Current Behavior                             |
|--------------|---------------------------------------------------|--------|-------------------|----------|------------------------------------------------------|
| BUG-UI-001   | Incorrect total price in cart                     | Fixed  | Exploratory       | High     | Previously random total price; now fixed             |
| BUG-FUNC-001 | "Book a Table" button returns to top of page      | Open   | Exploratory       | High     | Button does not trigger booking flow; returns to top |
| BUG-FUNC-002 | Address link opens wrong page                     | Open   | TC-08             | Medium   | Opens Contacts page instead of Google Maps location  |
| BUG-FUNC-003 | "Place Order" button not working on Checkout page | Fixed  | Exploratory       | High     | Previously 503 error; now fixed                      |

---

## Defect Source

| Source                  | Count |
|-------------------------|-------|
| Test Case Execution     | 1     |
| Exploratory Testing     | 3     |

---

## Key Findings

| Finding                                                                 |
|-------------------------------------------------------------------------|
| Previously identified incorrect total price bug has been fixed.         |
| "Book a Table" functionality no longer triggers booking flow; returns to top of page. |
| Address link now opens Contacts page instead of Google Maps; functionality changed. |
| Checkout and cart flows stable after fixes.                              |
| Minor UI layout observations during exploratory testing; layout responsive across devices. |

---

## Risks

| Risk                                                                 |
|----------------------------------------------------------------------|
| Users may be confused by non-functional "Book a Table" button.       |
| Incorrect address link may mislead users looking for location directions. |
| Checkout and cart flows now stable, reducing risk of transactional errors. |

---

## Conclusion

| Conclusion                                                                 |
|---------------------------------------------------------------------------|
| The Cafedaria website shows improvement after fixes, with core cart and checkout functionality stable. |
| Remaining issues (“Book a Table” and address link) need clarification or resolution. |
| It is recommended to address these open bugs and update related test cases before final release. |

---

## QA Engineer
Pavlo Mailovskyi
