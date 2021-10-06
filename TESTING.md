## TESTING <a name="testing-top"></a>

### Html

— **Code Validation** —

After all HTML files have been coded, a code validation test is run using the [W3C Markup Validation Service](https://validator.w3.org/), which is a validator by the World Wide Web Consortium that allows validating HTML and XHTML documents for well-formed markup, as well as any warnings and errors.

**Home Page** (`index.html`): [17 Errors & 2 Warnings] *After fixed, No relevant errors like in the image below
1. Error: An `img` element must have an `alt` attribute, except under certain conditions. For details, consult guidance on providing text alternatives for images.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve the error by putting `alt` attribute

**Products Page** (`products.html`): [0 Errors & 2 Warnings] *Some duplicated errors and warning and they are not repeated below

1. Warning: The `type` attribute is unnecessary for JavaScript resources.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve the warning by removing `type` attribute

**Product Detail Page** (`product_detail.html`): [0 Errors & 0 Warnings]

**Add Product Page** (`add_product.html`): [3 Errors & 0 Warnings]

**Edit Product Page** (`edit_product.html`): [3 Errors & 0 Warnings]

**Shopping Bag Page Desktop Size** (`bag.html`): [20 Errors & 16 Warnings] *Some duplicated errors and warning and they are not repeated below

**Shopping Bag Page Mobile Size** (`bag.html`): [16 Errors & 16 Warnings] *Repeated errors and warnings of Duplicate ID and The first occurence of ID was here

**Checkout Page** (`checkout.html`): [1 Errors & 0 Warnings]

**Checkout Success Page** (`checkout_success.html`): [0 Errors & 0 Warnings]

**Allauth Account Pages** (`signup.html`, `login.html`, `logout.html`, `password_reset`): [0 Errors & 0 Warnings]

> **Note**<br>
> Check only core pages of Allauth templates but as they are Django package, presume no errors or warnings on other Allauth pages

**Toast Messages** (`toast_error.html`, `toast_info.html`, `toast_success.html`, `toast_warning.html`): [0 Errors & 0 Warnings]

**404 and 500 Pages** (`404.html`, `500.html`): [0 Errors & 0 Warnings]

> **Note**<br>
> Check only 404 page but they have the same structure so presume no errors or warnings on 500 page

**Profile & Order History Page** (`profile.html`, `profile_order_history`): [0 Errors & 0 Warnings]




— **Form Validation** —

On the website Lord Of The Rings Collectibles, there are certain forms to fill out. Some are validated on the front end (for example, the @ mark for email input), while others are validated on the back end (e.g. existing user name). A manual test is run to ensure that the validations and form functions are functioning appropriately.

**Search Form**

Any text, including special characters, can be entered into the form (e.g. £, @, [ etc) so there is no form validation for this and the search is processed when the search button is clicked as long as there is a text in the input box. It works fine [when a key word exists in product names or descriptions](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/search-form.png), and when it does not it shows 0 result. [When there is no text in the input field, then it displays an error message](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/search-form-empty.png). The search function is available on all the pages and it works from anywhere on the page.

**Subscribe To Newsletter Form**

Because the form is available on all of the website's pages, try sending an email from a few different ones to see whether it works. All emails are submitted and preserved in the database from any page. [it works fine](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/subscribe-newsletters-success.png). If the email has no @ mark, it gives a warning message that @ mark must be included. There should not be duplicated emails in the system so if the email address already exists, [it displays an error message](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/subscribe-newsletters-error.png). 

**Register and Login Forms**

If an email address or username already exists in the database, the user must be unique, [it displays an error message for register page](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/register-form-email.png). Also, when the passwords do not match, [it displays an error message](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/register-form-password.png). This is similar for the login page that if the email or user name does not exist in the database, [it displays an error message and if password is incorrect, it also displays an error message](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/login-form.png).

**Add Product, Checkout and Stripe Form**

When mandatory fields are left blank or the form is incorrect, [it displays an error message](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/add-product-form.png). For credit card details, it is validated by Stripe and if it is invalid details, [it displays an error message](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/stripe-form.png).

> **Note**<br>
> `{% csrf_token %}` is a safe and random token used to prevent CSRF attacks on all the forms. (and unless there is {% csrf_token %}POST method will not work)<br>
> Based on the manual test, all the forms on the website work properly

---

— **Quality** —

A quality control test is performed using [Lighthouse](https://developers.google.com/web/tools/lighthouse), which is an open-source and one of the automated DevTools for improving the quality of web pages. It includes audits for performance, accessibility, progressive web apps, SEO.

**Home Page** (`index.html`)

- Mobile Size: 
<br>![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/home-mobile.png)

- Desktop Size: 
<br>![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/home-desktop.png)

**Products Page** (`products.html`)

- Mobile Size: 
<br>![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/products-mobile.png)

- Desktop Size: 
<br>![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/products-desktop.png)

**Product Details Page** (`products/<product id>.html`)

- Mobile Size: 
<br>![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/product-details-mobile.png)

- Desktop Size: 
<br>![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/product-details-desktop.png)

**bag Page** (`bag.html`)

- Mobile Size: 
<br>![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/bag-mobile.png)

- Desktop Size: 
<br>![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/bag-desktop.png)

**Checkout Page** (`checkout.html`)

- Mobile Size: 
<br>![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/checkout-mobile.png)

- Desktop Size: 
<br>![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/checkout-desktop.png)

**Profile Page** (`profile.html`)

- Mobile Size: 
<br>![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/profile-mobile.png)

- Desktop Size: 
<br>![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/profile-desktop.png)

> **Note**<br>
> Improve **Accessibility** on those pages by adding `aria-label` on button elements that have no text and by not using headlines (h5 & h6) for `Heading elements are not in a sequentially-descending order` error.  Accessibility has been improved on all the pages and 90 plus scores show on the pages, except the `checkout` page which still shows 88 because there are a lot of fields that don't have a label, which lowers the score (There are no labels deliberately to keep the neat style)<br>
There are some performance difficulties, particularly low scores on mobile size. The type and size of images, as well as unused CSS and JavaScript CDNs, are the main causes of problems. I remember having the similar problems with my prior project, when I couldn't seem to enhance the performance. (e.g. When changing the size or type of the image, it causes another type of error and when trying to limit the use of CDNs, Bootstrap and JavaScript do not work on certain pages) Ideally, the score for all categories should be greater than 90 on both mobile and desktop sizes, and anything below that should be investigated and improved as much as possible. However, because I am nearing the end of the project and am afraid of breaking something by attempting to improve the Performance, I have decided to leave it as is.


<div align="right"><a href="#testing-top">🔝</a></div>

### Css

— **Code Validation** —

When the CSS code is finished, a code validation test is run using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/), which is a validator by the World Wide Web Consortium that allows checking Cascading Style Sheets, to ensure that CSS meets with the standards set by the World Wide Web Consortium.

**`base.css`, `bag.css`, `checkout.css`, `index.css`, `products.css` and `profile.css`** are tested and there are [no errors on any of CSS files](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/css-validation.png).

> **Note**<br>
> There are some [warnings](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/css-warnings.png) related to WebKit, which is one of [web browser rendering engines](https://stackoverflow.com/questions/3468154/what-is-webkit-and-how-is-it-related-to-css), for base.css, index.css and product.css. By looking at the [Stack Overflow](https://stackoverflow.com/questions/52490004/what-are-all-of-these-w3c-css-validation-warnings-about) post and a [Code Institue Slack](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/css-webkit.png) threads, no further actions are required so decided to leave  it alone.

<div align="right"><a href="#testing-top">🔝</a></div>

---

### JavaScript

— **Code Validation** —

When the JavaScript code is finished, it is put through a code validation test using [JSHint](https://jshint.com/), which is a static code analysis tool utilized in software development for verifying if JavaScript source code complies with coding rules.

**`quantity_input_script.html`** (js code in bag app), **`stripe_elements.js`**, **`quantity_input_script.html`** (js code in product app), **`countryfield.js`** and js script on **`bag.html`** are tested. There is a warning of `'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).` so solve the warning by putting `/*jshint esversion: 6 */`.<br> 
`$` this appears as an undefined variable in all files, but it is a jQuery symbol, so it can be disregarded. `Stripe` on `stripe_elements.js` shows as an undefined variable but this derives from Stripe document so it can be ignored.

<div align="right"><a href="#testing-top">🔝</a></div>

---

### Python

— **Code Validation** —

As Python code is completed, a code validation test is carried out by using [PEP8 &#40;Python Enhancement Proposal&#41; online](http://pep8online.com) to see if the code meets guidelines and best practices for the readability and consistency of Python code.

Below is the list of `py` files that are customised and checked by the validator.

**lotr App**

- `asgi.py`, `settings.py`, `urls.py` and `wsgi.py`: There is *line too long* error and it is all fixed

**bag App**

- `apps.py`, `contexts.py`, `urls.py` and `views.py`: There are *trailing whitespace*, *two blank lines*, *no newline at end of file*, *line too long* warnings and errors, and they are all fixed

**checkout App**

- `init.py`, `admin.py`, `apps.py`, `forms.py`, `models.py`, `signals.py`, `urls.py`, `views.py`, `webhook_handler.py` and `webhooks.py`: There are *no newline at end of file*, *trailing whitespace*, *line too long*, *too many blank lines*, *at least two spaces before inline comment*, *expected 2 blank lines*, *blank line contains whitespace* warnings and errors and they are all fixed

**home App**

- `admin.py`, `apps.py`, `contexts.py`, `forms.py`, `models.py`, `urls.py` and `views.py`: There are *trailing whitespace*, *no newline at end of file* and *line too long* warnings and errors and they are all fixed

**products App**

- `admin.py`, `apps.py`, `forms.py`, `models.py`, `urls.py`, `views.py` and `widgits.py`: There are *no newline at end of file*, *line too long*, *blank line contains whitespace* warnings and errors and they are all fixed

**profiles App**

- `apps.py`, `forms.py`, `models.py`, `urls.py`, and `views.py`: There are *no newline at end of file*, *line too long* and *trailing whitespace* warnings and errors and they are all fixed

> **Note**<br>
> All Python code complies with PEP8 guidance except [4 Allauth Password Validators](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/auth-pwd-validators.png) that cannot be broken into separate lines

<div align="right"><a href="#testing-top">🔝</a></div>

---

— **Functions** —

There are some functionalities, which are run by `views.py` file in each app (in some cases by `contexts.py`), on the website. A manual test is carried out to see if these functions work as expected.

**bag App:**

- View bag: Products in the bag can be viewed by clicking the bag icon or a process your order button &#10004;
- Add bag: Products can be added from the product page by clicking an add to shopping bag button.  &#10004;
- Adjust bag: Products can be adjusted in the bag. Change the quantity of the product and remove it &#10004;
- Special Offer: Free collectibles appear for any order €300 or more. This is not run by `views.py` but should work when the total purchase is €300 or more &#10004;
- Display: Price per product, discount price and total value including shipping cost show based on the products in the bag &#10004;

**checkout App:**

- Checkout: Checkout is done by completing the form & credit card details and clicking a complete order button. Products in the bag can be views by clicking the bag icon or a process your order button &#10004;
- Checkout Success: When the order is completed, it creates an order in the database and saves the info. It also shows checkout success page for users &#10004;
- Confirmation email: When the order is succeeded (means payment in Stripe goes through), a confirmation email is sent &#10004;
- Stripe: When the order is completed, it creates a record of [payment_intent, charge.succeeded and payment_intent.succeeded](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/stripe-function.png) &#10004;

**home App:**

- Subscribe to our newsletter: When a unique and valid email is submitted, it saves in the database with Subscribed = True status &#10004;

**products App:**

- Product Display: Products are displayed by group of categories, category, brand, sale products and all products. They can be sorted by price, category and product name both ascending and descending order. Products can be searched by a keyword &#10004;
- Product Details Display: Product details can be viewed by clicking an image of the product. It displays product category, ID, description, price, size (if applicable), discount price (if applicable) &#10004;
- Product Add, Edit and Delete: Only authorised user (admin) is allowed to do these &#10004;

**profile App:**

- Profile: Access to the profile page where users can update the personal details and access to the order history &#10004;
- Profile (Admin): For admin user, Edit and Delete buttons appear on each product and there is a page for Adding product &#10004;

---

### Defensive Programme

There are some pages that only authorised users have access to. This is to test and confirm that non-authorised users have no access to these pages.

- **Profile page**: Only logged in users have access to the profile page. When `/profile/` is typed on URL, unless users are logged in, users are directed to the login page

- **Add Product page**: The page is only accessible by the administrator. When `/products/add/` is typed on URL, if users are not logged in, users are directed to the login page. If users are logged in, then users are directed to the home page with [an error message](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/add-product.png) unless Admin user 

- **Edit Product page and Delete product function**: Same as "Add Product"

- **Order History**: The order history is only accessible to the individual who purchased the product. When the order history URL is entered in case users are not the user who purchased the product, the users are redirected to the profile page with [an error message](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/product-history.png)

<div align="right"><a href="#testing-top">🔝</a></div>

---

### Web Browser

— **Visibilities and functionalities** —

The website is compatible with all major browsers, such as **Chrome**, **Safari**, **Firefox**, **Opera** and **Microsoft Edge**. The tests listed below are run on all of them to ensure that all visual items are displayed and functionality perform properly on those browsers. *With the exception of Chrom, which was used to create the website.

1. To perform a visual test, open the website in a browser. Examine all of the pages to ensure that everything is in order (both desktop and mobile sizes).
2. Complete the Python Functions test by using all of the functions listed.

<details>
<summary>Python Functions</summary><br>

![Python Functions](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/python-functions.png)
</details><br>

> **Note**<br>
> All of the above visibility and functionality operate flawlessly in each browser. [default input display causes an issue on Firefox](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/firefox-input.png) so it is fixed by making it inactive by putting `input[type=number] {-moz-appearance: textfield;}` on `base.css`

<div align="right"><a href="#testing-top">🔝</a></div>

---

### UX

— **Evidence Of Achieving The Website From UX Point Of View** —

There are several critical features to meet the website's primary goals from the user's perspective (both shoppers and the owner), and this is to validate that all the features planned on the website are implemented. **Strategy** and **Scope Planes** are implemented on the website based on the tests carried out in the testing section.

<ins>Strategy Plane</ins>

![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/strategy-plane.png)

<ins>Strategy Plane</ins>

![image](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/scope-plane.png)

<div align="right"><a href="#testing-top">🔝</a></div>

---

### Unsolved Issues

There are a few issues in the project that are addressed to get them solved however they remain unsolved issues due to a lack of my current skill and/or time

**Low Performance on Mobile Size**

- Cannot improve it because of my current skillset (that may need to plan and build the website from the Performance point of view) and time. Hope to have the skillset in the near future as I continue learning 

**Increment and Decrement Buttons**

- For the products increment & decrement buttons are not disabled. If `id` is used for this, one of them works but the other one does not (and `id` cannot be used for duplicate id error on html validation). If `class` is used, when one of them is disabled, another one is also disabled. By setting a unique class, this would work but do not know how to implement this in JavaScript using Django template and it is not a major issue, leave it as an unsolved issue 

**Sorting Products By Price Including Discounted Price**

- Sort function on the product pages, it sorts by the original price but it does not consider the discount price. Therefore, some products [do not look like sorted by price correctly](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/sort.png). The original price field and discount price field are in the different tables so they cannot be directly compared so this cannot be solved unless the current database structure is changed

**Save Delivery Info On Checkout**

- On the checkout page, logged in users can save the delivery info if they wish to. There is a check box as an option, however even the box is unticked, the details are saved for some reason. Looked at the code but cannot figure out why this happens, and as it is not a major issue, leave it as an unsolved issue

**Register Page**

- On the Register page, the user name, which is the second field, is auto-focused. When open the page, the first field, which is an email address, should be auto-focused. Try to fix this but no access to `forms.py` for the Register page as it is Allauth package, and as it is not a major issue, leave it as an unsolved issue

**Full Name**

- For registered users, when they go to the checkout page, they see some fields are pre-filled if they update Default Delivery Information on the profile page. There is a full name field that picks up the first name and last name of users personal info. To retrieve the data from the fields, users must input the details. Try to get first name and last name at the time of registration but cannot add these fields as they are controlled by Allauth. Try to add first name and last name fields on the profile page but that causes some issues on Stripe. It is not a major issue, decide to leave it as an unsolved issue 

**Error Message of Subscribe to Newsletter Form**

- During the final checking of the website before submission, notice that when the "Update Information" button is clicked, the [error message for Subscribe to Newsletters comes up](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/error-message.png). Check `contexts.py` in the  Home App that has Subscribe to Newsletters function and `views.py` in the Profile App that has Update Information function to see if there are any errors on them, like the same variable being used and that might cause the issue. Cannot find any obvious errors on them and not sure how to solve the problem so post it to Code Institute slack. Get feedback to suggest something wrong with it but not the solution so contact tutor support. It is [confirmed that when the "Update Information" button is clicked, Subscribe to Newsletters function is NOT working](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/posts-from-tutor.png) (meaning both Update Information and Subscribe to Newsletters functions are working independently and correctly) and the tutor thinks a browser is causing the issue but cannot identify it. Try to use a different browser but get the same result. Look for the solution or similar issues on the internet but cannot find it. Approx. 4 hours of time is spent but cannot identify and solve the issue, decided to leave it as an unsolved issue 

> **Note**<br>
> Strangely enough, this only happens with the "Update Information" button on the Profile page. There is a form that does a POST action on the Product Details page, and when the button is clicked, no error message comes up 

<div align="right"><a href="#testing-top">🔝</a></div>