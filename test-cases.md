# Test Cases – Cafedaria Website

---

## Positive Test Cases ##

| Test ID | Title               | Pre-conditions        | Steps                                    | Expected Result              | Test Environment                                              |
|---------|---------------------|-----------------------|------------------------------------------|------------------------------|---------------------------------------------------------------|
| TC-01   | Open Home Page      | None                  | Open browser → Navigate to cafedaria.com | Home page loads successfully | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-02   | Navigate to Menu    | Home page loaded      | Click Menu link                          | Menu section is displayed    | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-03   | View Product List   | Menu page opened      | Scroll product list                      | Products are visible         | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-04   | Add Product to Cart | Product list visible  | Click on the item → Add to Cart          | Product added to cart        | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-05   | Open Checkout Page  | Cart contains product | Navigate to checkout                     | Checkout page opens          | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |

---

## Negative Test Cases ##

| Test ID | Title                            | Pre-conditions                  | Steps                                                                                              | Expected Result                                                             | Test Environment                                              |
|---------|----------------------------------|---------------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------|
| TC-06   | Submit Empty Checkout Form       | Checkout page open              | Submit without data                                                                                | Validation errors shown                                                     | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-07   | Invalid Email Format             | Checkout form open              | Enter invalid email → Submit                                                                       | Email validation error                                                      | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-08   | Incorrect address link location  | User is on Home page            | Look at the top header → Click the address link "2130 Fulton Street, San Diego, CA 94117-1080 USA" | Clicking the link should open Google Maps at the correct San Diego location | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-09   | Cart Without Products            | Cart empty                      | Open cart                                                                                          | Informational message shown                                                 | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-10   | Long Text Input at Checkout Form | Checkout Form Form is available | Enter very long text                                                                               | Input limited or error shown                                                | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |

---

## Boundary Test Cases ##

| Test ID | Title                                                         | Pre-conditions             | Steps                                                                          | Expected Result              | Test Environment                                              |
|---------|---------------------------------------------------------------|----------------------------|--------------------------------------------------------------------------------|------------------------------|---------------------------------------------------------------|
| TC-11   | Minimum Quantity                                              | Product page open          | Add 1 item                                                                     | Product added successfully   | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-12   | Maximum Quantity                                              | Product page open          | Add large quantity                                                             | Limit applied or error shown | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-13   | Mobile Resolution 320px                                       | Website accessible         | Resize screen to 320px                                                         | Layout adapts correctly      | Desktop: Chrome, Safari                                       |
| TC-14   | Verify layout is displayed correctly on large desktop screens | User opens Home page       | Open the website on a desktop with screen width ≥ 1440px → Observe page layout | UI scales correctly          | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-15   | Short Text Input at Checkout Form                             | Checkout Form is available | Enter 1 character                                                              | Input accepted               | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |

---

## UI Test Cases ##

| Test ID | Title              | Pre-conditions     | Steps               | Expected Result            | Test Environment                                               |
|---------|--------------------|--------------------|---------------------|----------------------------|----------------------------------------------------------------|
| TC-16   | Header Visibility  | None               | Open any page       | Header visible and aligned | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome  |
| TC-17   | Footer Visibility  | Page loaded        | Scroll down         | Footer visible             | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome  |
| TC-18   | Button Hover State | Page with buttons  | Hover on buttons    | Hover state displayed      | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chromee |
| TC-19   | Image Display      | Catalog page open  | View product images | Images load correctly      | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome  |
| TC-20   | Responsive Layout  | Website accessible | Resize screen       | No UI breaks               | Desktop: Chrome, Safari                                        |
