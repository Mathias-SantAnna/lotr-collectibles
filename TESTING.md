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

When the Python code is finished, a code validation test is run through [PEP8 &#40;Python Enhancement Proposal&#41; online](http://pep8online.com) to verify if the code adheres to readability and consistency rules and best practices for Python code.

The validator customizes and checks a number of `py` files, which are shown below.

**lotr App**

- `asgi.py`, `settings.py`, `urls.py` and `wsgi.py`: There is *line too long* error and it is all corrected.

**bag App**

- `apps.py`, `contexts.py`, `urls.py` and `views.py`: There are *trailing whitespace*, *two blank lines*, *no newline at end of file*, *line too long* warnings and errors, and they are all corrected.

**checkout App**

- `init.py`, `admin.py`, `apps.py`, `forms.py`, `models.py`, `signals.py`, `urls.py`, `views.py`, `webhook_handler.py` and `webhooks.py`: There are *no newline at end of file*, *trailing whitespace*, *line too long*, *too many blank lines*, *at least two spaces before inline comment*, *expected 2 blank lines*, *blank line contains whitespace* warnings and errors and they are all corrected.

**home App**

- `admin.py`, `apps.py`, `contexts.py`, `forms.py`, `models.py`, `urls.py` and `views.py`: There are *trailing whitespace*, *no newline at end of file* and *line too long* warnings and errors and they are all corrected.

**products App**

- `admin.py`, `apps.py`, `forms.py`, `models.py`, `urls.py`, `views.py` and `widgits.py`: There are *no newline at end of file*, *line too long*, *blank line contains whitespace* warnings and errors and they are all corrected.

**profiles App**

- `apps.py`, `forms.py`, `models.py`, `urls.py`, and `views.py`: There are *no newline at end of file*, *line too long* and *trailing whitespace* warnings and errors and they are all corrected.

> **Note**<br>
> All Python code complies with PEP8 guidance except [4 Allauth Password Validators](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/auth-pwd-validators.png) that cannot be broken into separate lines

<div align="right"><a href="#testing-top">🔝</a></div>

---

— **Functions** —

On the website, there are various features that are controlled by the `views.py` file in each app (and in some situations, by `contexts.py`). To see if these functions work as expected, a manual test is performed.

**bag App:**

- View bag: Products in the bag can be viewed by simply clicking the bag icon or a process your order button &#10004;
- Add bag: Products can be added from the product page by clicking an add to shopping bag button.  &#10004;
- Adjust bag: Products can be adjusted in the bag. Change the quantity of the product and remove it &#10004;
- Special Offer: Free collectibles appear for any order €300 or more. This is not run by `views.py` but should work when the total purchase is €300 or more &#10004;
- Display: Price per product, discount price and total value including delivery cost show based on the products in the bag &#10004;

**checkout App:**

- Checkout: Checkout is completed by filling out the form and entering your credit card information, then hitting the "Complete Order" button. Products in the bag can be views by clicking the bag icon or a process your order button &#10004;
- Checkout Success: When the order is completed, it generates an order in the database and saves the information. It also displays the user's checkout success page &#10004;
- Confirmation email: A confirmation email is sent when the order is completed (that is, when the Stripe payment is completed) &#10004;
- Stripe: When the order is processed, it creates a record of [payment_intent, charge.succeeded and payment_intent.succeeded](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/stripe-function.png) &#10004;

**home App:**

- Sign up for our newsletter here: When a valid and unique email address is submitted, it is saved in the database as Subscribed = True status &#10004;

**products App:**

- Product Display: Products are organized into groups of categories, categories, brands, sale items, and all items. They can be sorted in both ascending and descending order by price, category, and product name. A keyword can be used to search for products. &#10004;
- Product Details Display: By clicking on a product image, you can get more information about it. It shows product category, ID, description, price, size (if applicable), discount price (if applicable) &#10004;
- Only an authorised user (admin) is able to add, edit, and delete products. &#10004;

**profile App:**

- Profile: Users get access to the profile page, where they may change their personal information and see their order history. &#10004;
- Profile (Admin): Edit and Delete buttons appear on each product for admin users, and there is a page for adding products. &#10004;

---

### Defensive Programme

There are some pages that are only accessible to permitted users. This is to ensure that non-authorized users are unable to access certain sites.

- **Profile page**: The profile page is only accessible to logged-in users. Users are led to the login page if they type `/profile/` into the URL unless they are already logged in.

- **Add Product page**: Only the administrator has access to this page. If users are not logged in when they type `/products/add/` into the URL, they are taken to the login page. If users are logged in, they are taken to the main page, which includes a search box [an error message](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/add-product.png) unless Admin user 

- **Edit Product page and Delete product function**: Same as "Add Product"

- **Order History**: Only the person who purchased the product gets access to the order history. Users are sent to the profile page with the order history URL specified if they are not the user who purchased the product showing [an error message](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/product-history.png)

<div align="right"><a href="#testing-top">🔝</a></div>

---

### Web Browser

— **Visibilities and functionalities** —

All major browsers, including **Chrome**, **Safari**, **Firefox**, and **Microsoft Edge**, are compatible with the website. All of them are subjected to the tests outlined below to guarantee that all visual elements are displayed and that functionality works properly in those browsers. Except for Chrom, which was used to construct the website.

1. Open the webpage in a browser to run a visual test. Check all of the pages to make sure they're in order (both desktop and mobile sizes).
2. Use all of the functions provided in the Python Functions test.

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

A few issues in the project are addressed in order to solve them, but they remain unsolved issues owing to my present expertise and/or time constraints.

**Low Performance on Mobile Size**

- I'm unable to improve it due to my present skill set (which may require me to plan and develop the website from a performance standpoint) and lack of time. As I continue to learn, I hope to have the expertise in the near future.

**Increment and Decrement Buttons**

- For the products increment & decrement buttons are not disabled. If `id` is used for this, one of them works but the other one does not (and `id` cannot be used for html validation's duplicate id error). When the keyword `class` is used, when one of them is disabled, the other is disabled as well. Setting a unique class might work, but I'm not sure how to achieve it in JavaScript using a Django template, and since it's not a big deal, I'll leave it as an unsolved problem.

**Sorting Products By Price Including Discounted Price**

- On product pages, the sort function sorts by the original price but ignores the reduced price. As a result, some products [do not look like sorted by price correctly](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/sort.png). Because the original price field and the discount price field are in separate tables, they can't be compared directly, hence this problem can't be remedied unless the database structure is modified.

**Save Delivery Info On Checkout**

- If logged in users wish, users can save the delivery information on the checkout page. There is a check box for this, however even if it is unticked, the information is saved for some reason. I looked through the code but couldn't figure out why this occurred, so I'm going to leave it as an unsolved problem.

**Register Page**

- On the Register page, the user name, which is the second field, is auto-focused. When open the page, the first field, which is an email address, should be auto-focused. Try to fix this but no access to `forms.py` for the Register page as it is Allauth package, and as it is not a major issue, leave it as an unsolved issue

**Full Name**

- If registered users edit Default Delivery Information on their profile page, several fields are pre-filled when they proceed to the checkout page. A full name field collects the first and last names of users' personal information. Users must enter details in order to retrieve data from the fields. Tried to get a first and last name upon registration, but these fields are restricted by Allauth, therefore it is not possible to add them. Attempting to add first and last name fields to the profile page produces Stripe difficulties. Because it isn't a serious problem, decide to leave it unresolved.

**Error Message of Subscribe to Newsletter Form**

- Notice that when the "Update Information" option is clicked during the last examination of the website before submission, the [error message for Subscribe to Newsletters comes up](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/error-message.png). Check `contexts.py` in the Home App, which has the Subscribe to Newsletters function, and `views.py` in the Profile App, which has the Update Information function, for any mistakes, such as the same variable being used, which could be the source of the problem. I couldn't discover any clear mistakes on them, and I wasn't sure how to fix them, so I posted it on the Code Institute slack. Obtain feedback to propose a flaw, but not the cure, therefore call tutor support. It is [confirmed that when the "Update Information" button is clicked, Subscribe to Newsletters function is NOT working](https://github.com/Mathias-SantAnna/lotr-collectibles/blob/main/readme/testing/posts-from-tutor.png) (meaning both Update Information and Subscribe to Newsletters functionalities work independently and appropriately), and the instructor suspects a browser is to blame but can't pinpoint it. Try using a different browser, but the problem persists. Search the internet for the answer or comparable issues but are unable to locate it. After spending around 6 hours trying to identify and address the problem but failing to do so, it was decided to leave it as an unsolved issue.

> **Note**<br>
> Surprisingly, this only occurs when the "Update Information" button on the Profile page is pressed. On the Product Details page, there is a form that performs a POST operation, but no error notice appears when the button is pressed.

<div align="right"><a href="#testing-top">🔝</a></div>