# Testing

MealFlow was tested throughout development to confirm that the application works as intended across different pages, screen sizes, browsers and user states.

---

# Code Validation

## HTML Validation

All rendered pages were tested using the [W3C Nu HTML Checker](https://validator.w3.org/nu/).

Django template files contain template syntax and were therefore tested through their rendered deployed pages.
See links below.

| Page | Result |
|---|---|
| Home | [Passed](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2F) |
| Recipe Details | [Passed](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2Frecipe%2F1%2F) |
| Register | [Passed](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2Fregister) |
| Login | [Passed](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2Flogin) |
| My Recipes | [Passed](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2Fmy-recipes%2F) |
| Create Recipe | [Passed](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2Fcreate-recipe%2F) |
| Edit Recipe | [Passed](https://validator.w3.org/nu/?useragent=Validator.nu%2FLV+https%3A%2F%2Fvalidator.w3.org%2Fservices&acceptlanguage=&doc=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2Frecipe%2F1%2Fedit%2F) |

All tested pages passed without errors or warnings.

---

## CSS Validation

The deployed stylesheet was tested using the [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/).
See links below.


| Page | Result |
|---|---|
| Home | [Passed](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv) |
| Recipe Details | [Passed](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2Frecipe%2F1%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv) |
| Register | [Passed](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2Fregister%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv) |
| Login | [Passed](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2Flogin%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv) |
| My Recipes | [Passed](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2Fmy-recipes%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv) |
| Create Recipe | [Passed](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2Fcreate-recipe%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv) |
| Edit Recipe | [Passed](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmealflow-c8de861cd143.herokuapp.com%2Frecipe%2F1%2Fedit%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv) |

The stylesheet passed without errors or warnings.

---

## JavaScript Validation

The JavaScript file was tested using [JSHint](https://jshint.com/).

The project uses ES8 features, including `const`, `let`, arrow functions and asynchronous functions. The following directive was therefore added at the beginning of the JavaScript file:

```js
/* jshint esversion: 8 */
```

The file passed without errors or warnings. JSHint displayed code metrics only.

<p align="center">
  <img
    src="documentation/images/validation-jshint.png"
    alt="JSHint result showing that the JavaScript passed without warnings"
    width="900"
  >
</p>

---

## Python Validation

The project's custom Python files were tested using the [Code Institute Python Linter](https://pep8ci.herokuapp.com/) to check compliance with PEP8 conventions.

| File                 | Validation Result                                                                                                          |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `mealflow/admin.py`  | <img src="documentation/images/testing-ci-admin.png" alt="Code Institute Python Linter result for admin.py" width="700">   |
| `mealflow/forms.py`  | <img src="documentation/images/testing-ci-forms.png" alt="Code Institute Python Linter result for forms.py" width="700">   |
| `mealflow/models.py` | <img src="documentation/images/testing-ci-models.png" alt="Code Institute Python Linter result for models.py" width="700"> |
| `mealflow/urls.py`   | <img src="documentation/images/testing-ci-urls.png" alt="Code Institute Python Linter result for urls.py" width="700">     |
| `mealflow/views.py`  | <img src="documentation/images/testing-ci-views.png" alt="Code Institute Python Linter result for views.py" width="700">   |

All tested files passed without remaining PEP8 errors or warnings.

---

## Django System Checks

Django's built-in system check was run from the project terminal:

```bash
python manage.py check
```

Expected successful result:

```text
System check identified no issues (0 silenced).
```
Result:

<p align="center">
  <img
    src="documentation/images/testing-django-check.png"
    alt="Django system checks showing no issues"
    width="600"
  >
</p>

The project was also checked for model changes without migrations:

```bash
python manage.py makemigrations --check
```

Expected successful result:

```text
No changes detected
```
Result:

<p align="center">
  <img
    src="documentation/images/testing-django-check-1.png"
    alt="Django system checks showing no issues"
    width="600"
  >
</p>

---

# Lighthouse Testing

Google Lighthouse was used to evaluate the deployed application in the following areas:

- Performance
- Accessibility
- Best Practices
- SEO

See results below.

Homepage: 

<p align="center">
  <img
    src="documentation/images/homepage-lighthouse.png"
    alt="Lighthouse result for the MealFlow Home page"
    width="600"
  >
</p>

Login page:

<p align="center">
  <img
    src="documentation/images/lighthouse-login.png"
    alt="Lighthouse result for the MealFlow login page"
    width="600"
  >
</p>

Register page: 

<p align="center">
  <img
    src="documentation/images/lighthouse-register.png"
    alt="Lighthouse result for the MealFlow register page"
    width="600"
  >
</p>

My Recipes page: 

<p align="center">
  <img
    src="documentation/images/lighthouse-my-recipes.png"
    alt="Lighthouse result for the MealFlow my recipes page"
    width="600"
  >
</p>

Create Recipe page: 

<p align="center">
  <img
    src="documentation/images/lighthouse-create.png"
    alt="Lighthouse result for the MealFlow create recipe page"
    width="600"
  >
</p>

Details page: 

<p align="center">
  <img
    src="documentation/images/lighthouse-details.png"
    alt="Lighthouse result for the MealFlow details page"
    width="600"
  >
</p>

Performance scores varied slightly between test runs. The Recipe Details page achieved a slightly lower performance score because the main recipe image is displayed above the fold and is intentionally loaded with high priority to improve the user experience. While this can have a small impact on the initial page load performance, it ensures that the primary page content is visible immediately. To minimise layout shifts, explicit image dimensions were defined, and non-critical images elsewhere in the application are loaded lazily where appropriate.

---

# Manual Feature Testing

## Visitor Features

| Feature | Test | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| Open the Home page | Visit the deployed website | The introduction, navigation, search area and recipe grid are displayed | Worked as expected | Pass |
| Browse recipes | View the recipe grid | Available recipes are displayed as recipe cards | Worked as expected | Pass |
| Open a recipe | Select a recipe card | The corresponding Recipe Details page opens | Worked as expected | Pass |
| Return to recipes | Select **Back to recipes** | The user returns to the Home page | Worked as expected | Pass |
| Search by title | Enter all or part of a recipe title | Matching recipe cards remain visible | Worked as expected | Pass |
| Filter by meal type | Select one or more meal-type filters | Matching recipes are displayed immediately | Worked as expected | Pass |
| Filter by category | Select one or more category filters | Matching recipes are displayed immediately | Worked as expected | Pass |
| Combine filters | Select meal-type and category filters | Only recipes matching the combined criteria are shown | Worked as expected | Pass |
| Clear search and filters | Select **Clear** | The search field and selected filters are reset | Worked as expected | Pass |
| No matching results | Enter a search term with no matching recipes | A clear no-results message is displayed | Worked as expected | Pass |
| Load more recipes | Select **Load more** when more than 16 matching recipes exist | Up to 16 additional recipes are displayed | Worked as expected | Pass |
| Save while logged out | Select **Log in to save recipe** | The Login page opens | Worked as expected | Pass |


**Example screenshots:**

| Search                                                                                                          | Filters                                                                                                                  | Load More                                                                                                       |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| <img src="documentation/images/homepage-search.png" alt="MealFlow search results on the Home page" width="250"> | <img src="documentation/images/homepage-filter.png" alt="MealFlow filtered recipe results on the Home page" width="250"> | <img src="documentation/images/load-more-btn-mobile.png" alt="MealFlow Load More button on mobile" width="250"> |

---

## Authentication

| Feature | Test | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| Open Registration page | Select **Register** in the navigation | The Registration form opens | Worked as expected | Pass |
| Register valid account | Submit a valid username and matching passwords | The account is created, the user is logged in and redirected to Home | Worked as expected | Pass |
| Invalid registration | Submit invalid information | Validation feedback is displayed | Worked as expected | Pass |
| Password mismatch | Enter two different passwords | The account is not created and an error is displayed | Worked as expected | Pass |
| Open Login page | Select **Login** | The Login form opens | Worked as expected | Pass |
| Valid login | Submit correct credentials | The user is authenticated and redirected | Worked as expected | Pass |
| Invalid login | Submit incorrect credentials | An error message is displayed | Worked as expected | Pass |
| Authenticated navigation | Log in successfully | **My Recipes**, **Add Recipe** and **Logout** are displayed | Worked as expected | Pass |
| Logout | Select **Logout** | The user is logged out and visitor navigation is restored | Worked as expected | Pass |


**Example screenshots:**

| Registration validation                                                                                                                 | Login validation                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| <img src="documentation/images/register-fail.png" alt="Registration form displaying validation feedback for invalid input" width="300"> | <img src="documentation/images/login-fail.png" alt="Login form displaying an error message for invalid credentials" width="300"> |

---

## Saved Recipes

| Feature | Test | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| Save recipe | Select **Save recipe** | The button changes to **Saved** and feedback is displayed | Worked as expected | Pass |
| Remove saved recipe | Select **Saved** again | The recipe is removed and the button returns to **Save recipe** | Worked as expected | Pass |
| Save without page reload | Save or remove a recipe | The button and feedback update without a full reload | Worked as expected | Pass |
| View saved recipes | Open **My Recipes** after saving a recipe | The saved recipe appears in the saved section | Worked as expected | Pass |
| Empty saved section | Open **My Recipes** without saved recipes | **You have not saved any recipes yet.** is displayed | Worked as expected | Pass |
| Prevent duplicate saves | Save the same recipe more than once | Only one saved relationship exists | Worked as expected | Pass |

**Example screenshots:**

| Save recipe                                                                                                                | Remove saved recipe                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| <img src="documentation/images/toast-saved-success.png" alt="Success message displayed after saving a recipe" width="300"> | <img src="documentation/images/toast-unsave-success.png" alt="Success message displayed after removing a saved recipe" width="300"> |

| Saved recipes                                                                                                    | Empty saved recipes                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| <img src="documentation/images/my-recipes-saved.png" alt="My Recipes page displaying saved recipes" width="300"> | <img src="documentation/images/my-recipes-norecipes.png" alt="My Recipes page displaying the empty-state message" width="300"> |

---

## Recipe CRUD

## Authorisation

## Administrator Features

# User Story Testing

## Visitor User Stories

## Registered User Stories

## Administrator User Stories

# Form Validation

# Responsive Design Testing

# Browser Compatibility

# Accessibility Testing

# Bugs

## Fixed Bugs

## Known Bugs

