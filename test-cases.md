# Test Cases – Cafedaria Website

---

## Positive Test Cases ##

| Test ID | Title                | Pre-conditions        | Steps                                    | Expected Result              | Test Environment                                              |
|---------|----------------------|-----------------------|------------------------------------------|------------------------------|---------------------------------------------------------------|
| TC-01   | Open Home Page       | None                  | Open browser → Navigate to cafedaria.com | Home page loads successfully | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-02   | Navigate to Menu     | Home page loaded      | Open Menu section via navigation         | Menu section is displayed    | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-03   | View Product List    | Menu page opened      | Scroll product list                      | Products are visible         | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-04   | Add Product to Cart  | User is logged in     | Select product → Add to cart             | Product added to cart        | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-05   | Proceed to Checkout  | Cart contains product | Open checkout flow                       | Checkout page opens          | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |

---

## Negative Test Cases ##

| Test ID | Title                                      | Pre-conditions                  | Steps                                                                     | Expected Result                         | Test Environment                                              |
|---------|--------------------------------------------|---------------------------------|---------------------------------------------------------------------------|-----------------------------------------|---------------------------------------------------------------|
| TC-06   | Submit Empty Checkout Form                 | Checkout page open              | Submit without data                                                       | Validation errors shown                 | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-07   | Invalid Email Format                       | Checkout form open              | Enter invalid email → Submit                                              | Email validation error                  | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-08   | Incorrect address link location            | User is on Home page            | Click the address link "2130 Fulton Street, San Diego, CA 94117-1080 USA" | Correct Google Maps location opens      | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-09   | Add Product to Cart Without Authorization  | User not logged in              | Attempt to add product to cart                                            | User is prompted to log in or register  | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-10   | Long Text Input at Checkout Form           | Checkout Form Form is available | Enter excessive text                                                      | Input limited or error shown            | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |

---

## Boundary Test Cases ##

| Test ID | Title                             | Pre-conditions             | Steps                                                                          | Expected Result              | Test Environment                                              |
|---------|-----------------------------------|----------------------------|--------------------------------------------------------------------------------|------------------------------|---------------------------------------------------------------|
| TC-11   | Minimum Product Quantity          | Product page open          | Add 1 item                                                                     | Product added successfully   | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-12   | Maximum Quantity                  | Product page open          | Add maximum allowed quantity                                                   | Limit applied or error shown | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-13   | Mobile Resolution 320px           | Website accessible         | Resize screen to 320px                                                         | Layout adapts correctly      | Desktop: Chrome, Safari                                       |
| TC-14   | Large Screen Resolution (≥1440px) | Website accessible         | Open the website on a desktop with screen width ≥ 1440px → Observe page layout | UI scales correctly          | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |
| TC-15   | Minimum Text Input                | Checkout Form is available | Enter 1 character                                                              | Input accepted if valid      | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome |

---

## UI Test Cases ##

| Test ID | Title              | Pre-conditions     | Steps               | Expected Result            | Test Environment                                               |
|---------|--------------------|--------------------|---------------------|----------------------------|----------------------------------------------------------------|
| TC-16   | Header Visibility  | None               | Open any page       | Header visible and aligned | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome  |
| TC-17   | Footer Visibility  | Page loaded        | Scroll down         | Footer visible             | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome  |
| TC-18   | Button Hover State | Page with buttons  | Hover on buttons    | Hover state displayed      | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chromee |
| TC-19   | Image Display      | Catalog page open  | View product images | Images load correctly      | Desktop: Chrome, Safari. Mobile: Iphone Safari, Iphone Chrome  |
| TC-20   | Responsive Layout  | Website accessible | Resize screen       | No UI breaks               | Desktop: Chrome, Safari                                        |
