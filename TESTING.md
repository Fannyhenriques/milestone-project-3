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

## Authentication

## Saved Recipes

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

