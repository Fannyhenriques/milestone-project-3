# MealFlow

<p align="center">
  <img
    src="documentation/images/home-filtered.png"
    alt="Filtered recipe results"
    width="900"
  >
</p>

MealFlow is a full-stack recipe management application built with Django, designed to inspire home cooking and make everyday meal planning a little easier.

Users can browse, search and filter recipes, view complete recipe details and discover new favourites. By creating an account, users can save recipes to their personal collection, share their own recipes with the community, and edit or delete the recipes they have created — keeping everything organised in one convenient place.


## Live Site 

- [View the live MealFlow website](https://mealflow-c8de861cd143.herokuapp.com/)

---

## Table of Contents

- [User Experience](#user-experience)
  - [Strategy Plane](#strategy-plane)
  - [Scope Plane](#scope-plane)
  - [Structure Plane](#structure-plane)
  - [Skeleton Plane](#skeleton-plane)
  - [Surface Plane](#surface-plane)
- [User Stories](#user-stories)
- [Wireframes](#wireframes)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Data Model](#data-model)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Local Development](#local-development)
  - [Cloning](#cloning)
  - [Forking](#forking)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

---

# User Experience

## Strategy Plane

### Purpose

MealFlow provides a simple and accessible place for users to discover, save and manage recipes.
The application allows visitors to browse, search and filter recipes, while registered users can save favourites and create, edit or delete their own recipes.

The main purpose of the application is to:

- Allow visitors to browse available recipes.
- Help users find suitable recipes through search and filtering.
- Present recipe information in a clear and readable format.
- Allow registered users to save recipes for later.
- Allow users to create and manage their own recipes.
- Provide clear feedback after important actions.

### Primary User Needs

Users should be able to:

- Understand the purpose of the application quickly.
- Browse and view recipes without an account.
- Search and filter recipes easily.
- View clear ingredient lists and instructions.
- Register, log in and manage their account securely.
- Save recipes and manage their own contributions.
- Receive clear feedback after important actions.
- Use the application across mobile, tablet and desktop devices.

### Project Goals

The main goals for MealFlow were to:

- Build a full-stack Django application using a relational database.
- Implement user authentication and complete CRUD functionality.
- Allow registered users to save recipes to a personal collection.
- Restrict recipe editing and deletion to the recipe author.
- Implement recipe search and filtering.
- Create an accessible, responsive and intuitive interface.
- Deploy the finished application to Heroku.

---

## Scope Plane

---
## Wireframes

An initial wireframe was created in **Lucidchart** for the Home page to establish the overall structure, including the header, search and filter area, recipe grid and main call-to-action elements.

The final design evolved during development as functionality and responsive behaviour were implemented. Additional pages were created using the Home page wireframe as a visual reference, with consistent navigation, buttons, forms, spacing and card styles throughout the application.

Although some details differ from the original wireframe, the core layout and design direction were retained.

*Initial Home page wireframe created in Lucidchart.*

<table>
  <tr>
    <th>Mobile</th>
    <th>Tablet</th>
    <th>Desktop</th>
  </tr>
  <tr>
    <td>
      <img
        src="documentation/images/wireframe-mobile.png"
        alt="Initial MealFlow Home page mobile wireframe"
        width="200"
      >
    </td>
    <td>
      <img
        src="documentation/images/wireframe-tablet.png"
        alt="Initial MealFlow Home page tablet wireframe"
        width="280"
      >
    </td>
    <td>
      <img
        src="documentation/images/wire-frame-desktop.png"
        alt="Initial MealFlow Home page desktop wireframe"
        width="400"
      >
    </td>
  </tr>
</table>

---

### Core Features

MealFlow includes:

- Public recipe browsing with search, filters and load-more functionality.
- Detailed recipe pages with ingredients and instructions.
- User registration, login and logout.
- Saved recipe collections for registered users.
- Full recipe CRUD for authenticated users.
- Authorisation checks for editing and deleting recipes.
- Responsive navigation and recipe layouts.
- Success messages and toast-style feedback.
- Django admin management.

### Recipe Content

Each recipe includes:

- Title and description.
- Meal type and food category.
- Servings and cooking time.
- Recipe image.
- Ingredients and ordered instructions.
- Author and timestamps.

## Features

### Information Architecture

The main areas of the application are:

#### Home Page

- The Home page is the main landing page for MealFlow. It introduces the purpose of the application and gives users immediate access to the available recipe collection. The page includes the MealFlow logo, responsive navigation, a search and filter form, and a responsive grid of recipe cards.

<p align="center">
  <img
    src="documentation/images/homepage.png"
    alt="homepage"
    width="900"
  >
</p>

- Users can search for recipes by entering a title in the search field. Recipes can also be filtered by meal type and food category using checkbox-style filter buttons. The recipe grid updates immediately when a filter is selected, allowing users to combine multiple options and quickly narrow down the results. The **Clear** button resets the search field and all selected filters.

<p align="center">
  <img
    src="documentation/images/homepage-search.png"
    alt="Filtered recipe results"
    width="900"
  >
</p>

<p align="center">
  <img
    src="documentation/images/homepage-filter.png"
    alt="Filtered recipe results"
    width="900"
  >
</p>


- Each recipe is presented as a card containing an image, title and category. Selecting a card opens the corresponding Recipe Details page, where the user can view the complete recipe. Up to 16 matching recipes are displayed initially. When more recipes are available, a **Load More** button appears and displays the next group of up to 16 recipes.

<p align="center">
  <img
    src="documentation/images/load-more-btn-desktop.png"
    alt="Filtered recipe results"
    width="700"
  >
</p>

- The navigation changes according to the user's authentication status. Visitors can access **Home**, **Register** and **Login**. Authenticated users instead have access to **Home**, **My Recipes**, **Add Recipe** and **Logout**. On smaller screens, the navigation is presented through a hamburger menu to keep the header clear and accessible.

#### Recipe Details Page

Selecting a recipe card opens the corresponding Recipe Details page, where the full recipe is displayed.
The page includes the recipe image, description and key information such as food category, cooking time and number of servings. This is followed by a complete ingredient list and step-by-step cooking instructions.

<p align="center">
  <img
    src="documentation/images/recipe-detail-page1.png"
    alt="Filtered recipe results"
    width="900"
  >
</p>

<p align="center">
  <img
    src="documentation/images/recipe-detail-page2.png"
    alt="Filtered recipe results"
    width="900"
  >
</p>

- The save action changes depending on the user's authentication status. Visitors see a **Log in to save recipe** button, while authenticated users see **Save recipe**. When a recipe is saved, the button changes to **Saved** and a toast message confirms that it has been added to the user's saved recipes. Selecting the button again removes the recipe, restores the **Save recipe** label and displays a confirmation message.

- A **Back to recipes** button is shown at the bottom of the page. When the logged-in user is also the author of the recipe, an additional **Edit recipe** button is displayed, allowing them to update or delete their recipe.

#### Registration Page

Selecting **Register** in the navigation opens the Registration page, where visitors can create an account using Django's built-in `UserCreationForm`.

<p align="center">
  <img
    src="documentation/images/registerpage.png"
    alt="Filtered recipe results"
    width="900"
  >
</p>

The form requires a username, password and password confirmation. Django validates the submitted information and displays error messages when the username is unavailable, the passwords do not match or the password does not meet the required security rules.

<p align="center">
  <img
    src="documentation/images/register-fail.png"
    alt="Filtered recipe results"
    width="700"
  >
</p>

Users who already have an account can follow the **Already have an account? Log in here** link to open the Login page.
After successful registration, the user is logged in automatically and redirected to the Home page.

#### Login Page

The Login page uses the same clean and consistent styling as the Registration page. Existing users can enter their username and password to access authenticated features such as saving recipes and managing their own recipe contributions.

<p align="center">
  <img
    src="documentation/images/loginpage.png"
    alt="Filtered recipe results"
    width="900"
  >
</p>

If the submitted username or password is incorrect, the form displays an error message and the user remains on the page.

<p align="center">
  <img
    src="documentation/images/login-fail.png"
    alt="Filtered recipe results"
    width="700"
  >
</p>

Visitors who do not yet have an account can follow the **Don't have an account? Register here** link to open the Registration page.

#### My Recipes Page

The **My Recipes** page is available to authenticated users and provides a personal overview of both saved and created recipes.

Saved recipes and recipes created by the user are displayed in separate sections using the same responsive recipe-card layout as the Home page. Selecting a card opens the corresponding Recipe Details page.

Saved recipes: 
<p align="center">
  <img
    src="documentation/images/my-recipes-saved.png"
    alt="Filtered recipe results"
    width="900"
  >
</p>

Created recipes: 
<p align="center">
  <img
    src="documentation/images/my-recipes-created.png"
    alt="Filtered recipe results"
    width="900"
  >
</p>

When either section is empty, a clear message is displayed:

- **You have not saved any recipes yet.**
- **You have not created any recipes yet.**

<p align="center">
  <img
    src="documentation/images/my-recipes-norecipes.png"
    alt="Filtered recipe results"
    width="700"
  >
</p>

A **Create recipe** button is displayed near the top of the page and links directly to the Create Recipe page.

#### Create Recipe Page

The **Create Recipe** page is available to authenticated users and provides a structured form for adding a new recipe to MealFlow.

Users can select a food category and meal type, then enter a title, description, ingredients, instructions, number of servings and cooking time. Ingredients are entered one per line, allowing each item to be stored and displayed separately on the Recipe Details page.

<p align="center">
  <img
    src="documentation/images/create-recipe-form.png"
    alt="Filtered recipe results"
    width="700"
  >
</p>

The following fields are required:

- Category
- Title
- Ingredients
- Instructions
- Meal type
- Cooking time

If a required field is left empty, the form displays validation feedback and prevents submission until the missing information is provided. The servings field has a default value of **4**, but users can change it before submitting the form.

After successful submission, the recipe is saved to the database, assigned to the logged-in user and displayed on its Recipe Details page. As user-uploaded images are not currently supported, a default image is assigned automatically based on the selected food category: vegetarian, dessert, chicken, meat or fish.

<p align="center">
  <img
    src="documentation/images/default-recipeimages.png"
    alt="Filtered recipe results"
    width="900"
  >
</p>

#### Edit Recipe Page

Recipe authors can edit recipes they have created. The form is pre-filled with the existing recipe information, allowing the user to update any field.

Users can choose to save their changes, cancel the edit and return to the recipe, or delete the recipe. After a successful update, a confirmation message is displayed and the user is redirected to the Recipe Details page.


<p align="center">
  <img
    src="documentation/images/create-recipe-buttons.png"
    alt="Filtered recipe results"
    width="900"
  >
</p>

<p align="center">
  <img
    src="documentation/images/change-recipe-success-toast.png"
    alt="Filtered recipe results"
    width="900"
  >
</p>

#### Delete Recipe Action

Only the recipe author can delete a recipe.

Selecting **Delete recipe** opens a confirmation dialog to prevent accidental deletion. If the user confirms the action, the recipe is removed from the database and a success message is displayed. If the user cancels, the recipe remains unchanged.


<p align="center">
  <img
    src="documentation/images/confirm-delete-recipe.png"
    alt="Filtered recipe results"
    width="900"
  >
</p>

#### Django Admin

- The Django admin interface is available to authorised administrators and provides central management of the application's data.

- Administrators can create, view, update and delete categories, recipes, ingredients, saved-recipe records and user accounts.

### User Flow

The main user journeys are outlined below. More detailed explanations are provided in the [Features](#features) section.

**Visitors can:**

- Browse, search and filter recipes.
- Open a recipe to view ingredients and instructions.
- Register or log in to access personalised features.

**Registered users can:**

- Save and remove recipes from their collection.
- View saved and created recipes under **My Recipes**.
- Create, edit and delete their own recipes.
- Log out securely.

---
## Skeleton Plane

### Navigation

The main navigation provides access to the core pages of the application and changes according to the user's authentication status.

On smaller screens, it is replaced by an accessible hamburger menu that updates its icon, `aria-expanded` state and label when opened or closed.

### Layout and Interface

MealFlow uses:

- A shared base template with a consistent header and footer.
- Reusable recipe cards and button styles.
- Responsive grid layouts.
- Clearly separated content sections.
- Accessible forms with labels, fieldsets and validation feedback.
- A mobile-first layout that adapts across mobile, tablet and desktop screen sizes.

---
## Surface Plane

### Colour Scheme

The colour scheme was designed to feel warm, natural and welcoming. The palette was created using [Coolors](https://coolors.co/2d2d2d-6a9e6f-f4a261-87ceeb-faf9f6).

<p align="center">
  <img
    src="documentation/images/colors-1.png"
    alt="MealFlow colour palette"
    width="700"
  >
</p>

The main colours are stored as CSS custom properties to maintain consistency across the application:

```css
--color-background: #f8f3ea;
--color-primary: #1b4e47;
--color-secondary: #07bba0;
--color-surface: #ffffff;
```
Additional colours are used for action buttons, destructive actions, borders and validation feedback:

```css
--color-accent: #be435c;
--color-danger: #bc0202;
--color-border: #cfcfcf;
```

<p align="center">
  <img
    src="documentation/images/colors-2.png"
    alt="MealFlow colour palette"
    width="700"
  >
</p>

### Typography

The **Mulish** typeface is used throughout MealFlow to create a clean, modern and readable interface across different screen sizes.

### Responsive Design

MealFlow was developed using a mobile-first approach and adapts across mobile, tablet, laptop and desktop screen sizes.

Responsive features include a hamburger menu, flexible forms, scalable images, responsive recipe grids and adjusted spacing and typography.

Detailed responsive testing can be found in [TESTING.md](TESTING.md).

### Accessibility

Accessibility considerations include:

- Semantic HTML elements.
- A skip link for keyboard users.
- Visually hidden labels where required.
- Descriptive labels for form controls.
- Fieldsets and legends for filter groups.
- Alternative text for recipe images.
- Keyboard-accessible buttons and links.
- Visible focus indicators.
- ARIA attributes for the navigation toggle.
- An `aria-live` region for feedback messages.
- Sufficient colour contrast.
- Confirmation before recipe deletion.

---

# User Stories
## Visitor User Stories

| User Story | Outcome |
|---|---|
| As a visitor, I want to understand the purpose of the website so that I know what MealFlow offers. | The Home page contains a clear introduction and recipe collection. |
| As a visitor, I want to browse available recipes so that I can discover new meal ideas. | Recipe cards are displayed on the Home page. |
| As a visitor, I want to search by recipe title so that I can quickly find a specific recipe. | The Home page includes a title search field. |
| As a visitor, I want to filter recipes so that I can find recipes that suit my needs. | Recipes can be filtered by meal type and food category. |
| As a visitor, I want to view full recipe details so that I can prepare the meal. | Each recipe has a dedicated Recipe Details page. |
| As a visitor, I want to return to the recipe collection so that I can continue browsing. | A **Back to recipes** button links to the Home page. |
| As a visitor, I want to register for an account so that I can save and create recipes. | A Registration page is available. |
| As a visitor, I want to log in so that I can access personalised features. | A Login page is available. |

## Registered User Stories

| User Story | Outcome |
|---|---|
| As a registered user, I want to save recipes so that I can find them again later. | Recipes can be added to the user's saved collection. |
| As a registered user, I want to remove saved recipes so that I can manage my collection. | Saved recipes can be removed without reloading the page. |
| As a registered user, I want to view my saved recipes so that they are available in one place. | Saved recipes appear on the My Recipes page. |
| As a registered user, I want to create recipes so that I can contribute my own content. | Authenticated users can create recipes. |
| As a registered user, I want newly created recipes to appear immediately so that I can access them without delay. | New recipes appear on the Home and My Recipes pages after creation. |
| As a registered user, I want to edit my recipes so that I can correct or improve them. | Recipe authors can edit their own recipes. |
| As a registered user, I want to delete my recipes so that I can remove content I no longer want. | Recipe authors can delete their own recipes. |
| As a registered user, I want a warning before deletion so that I do not remove a recipe accidentally. | A JavaScript confirmation dialog is displayed. |
| As a registered user, I want feedback after completing an action so that I know it succeeded. | Toast-style feedback is displayed after saving, creating, editing or deleting a recipe. |
| As a registered user, I want to log out so that my account remains secure. | A Logout option is available in the navigation. |
## Administrator User Stories

| User Story | Outcome |
|---|---|
| As an administrator, I want to manage recipe categories so that the available options remain accurate. | Categories can be managed through Django admin. |
| As an administrator, I want to manage recipes so that inappropriate or incorrect content can be updated or removed. | Recipes can be managed through Django admin. |
| As an administrator, I want to view recipe ingredients alongside recipes so that recipe content is easier to manage. | Ingredients are displayed as an inline section in the recipe admin interface. |
| As an administrator, I want to manage saved-recipe relationships so that database records can be reviewed. | SavedRecipe records are available in Django admin. |



## Future Features & improvments

Possible future improvements include:

- User-uploaded recipe images.
- Ratings, reviews and recipe comments.
- Nutritional information.
- Ingredient scaling based on servings.
- Additional filters for preparation time and difficulty.
- User profile pages.
- Saved recipe collections and meal planning.
- Recipe sharing and shopping-list generation.
- Email-based password reset.
- Custom 404 and 500 error pages.
- Pagination or infinite scrolling for larger recipe collections.

---

# Data Model

MealFlow uses a relational database together with Django's built-in `User` model.

The main application models are described below.

## Category

The `Category` model stores recipe categories and their fallback images.

| Field | Type | Purpose |
|---|---|---|
| `name` | CharField | Category name |
| `slug` | SlugField | URL-safe category value |
| `default_image` | CharField | Static fallback image path |

## Recipe

The `Recipe` model stores the main recipe data.

| Field | Type | Purpose |
|---|---|---|
| `author` | ForeignKey | User who created the recipe |
| `category` | ForeignKey | Related recipe category |
| `title` | CharField | Recipe title |
| `description` | TextField | Short recipe description |
| `instructions` | TextField | Cooking instructions |
| `meal_type` | CharField | Breakfast, lunch, dinner or dessert |
| `servings` | PositiveIntegerField | Number of servings |
| `cooking_time` | PositiveIntegerField | Total cooking time in minutes |
| `image_name` | CharField | Optional static image filename |
| `created_at` | DateTimeField | Creation timestamp |
| `updated_at` | DateTimeField | Last update timestamp |

## Ingredient

The `Ingredient` model stores individual ingredients linked to a recipe.

| Field | Type | Purpose |
|---|---|---|
| `recipe` | ForeignKey | Related recipe |
| `name` | CharField | Ingredient name |
| `quantity` | CharField | Ingredient quantity |
| `order` | PositiveIntegerField | Display order |

## SavedRecipe

The `SavedRecipe` model connects users with recipes they have saved.

| Field | Type | Purpose |
|---|---|---|
| `user` | ForeignKey | User who saved the recipe |
| `recipe` | ForeignKey | Saved recipe |
| `saved_at` | DateTimeField | Date the recipe was saved |

A unique database constraint prevents the same user from saving the same recipe more than once.

## Data Model Development and Testing

During the early stages of development, sample categories, recipes and ingredients were added manually through the Django admin interface.

This was a deliberate part of the development process. Entering complete recipe data manually made it possible to test the relationships between the models and confirm that the database structure supported the application's requirements.

This process also helped identify missing fields and usability improvements. For example, testing complete recipes showed that the `Recipe` model required fields for the number of servings and total cooking time. The Django admin interface was also improved by adding inline ingredient fields, allowing multiple ingredients to be created and edited together with a recipe.

The local SQLite database is excluded from version control, meaning that records created during local development are not included directly in the GitHub repository. Reusable initial recipe data was therefore exported to a Django fixture and loaded into the production PostgreSQL database during deployment.

A dedicated system user is used as the author of the built-in recipes. This prevents the initial recipe data from depending on a personal administrator account and avoids exposing administrator credentials.

---

# Technologies Used

## Languages

- **HTML5** — Used to structure the application's pages and content.
- **CSS3** — Used for layout, styling, responsive design and visual feedback.
- **JavaScript** — Used for interactive features such as filtering, the hamburger menu, delete confirmation and saving recipes without a full page reload.
- **Python** — Used for the server-side logic, database interaction and Django application functionality.

## Frameworks and Libraries

| Technology | Purpose |
|---|---|
| Django | Back-end framework |
| Gunicorn | Production web server |
| WhiteNoise | Static-file serving |
| dj-database-url | Database URL configuration |
| psycopg2-binary | PostgreSQL database adapter |

## Database

| Environment | Database |
|---|---|
| Local development | SQLite |
| Deployed application | PostgreSQL |

## Tools

| Tool | Purpose |
|---|---|
| Git | Version control |
| GitHub | Repository hosting |
| Visual Studio Code | Code editor |
| Chrome Developer Tools | Debugging and responsive testing |
| Django Admin | Data administration |
| ADD_HOSTING_PLATFORM | Cloud deployment |
| ADD_WIREFRAME_TOOL | Wireframe creation |
| ADD_ERD_TOOL | Database diagram creation |

---

# Testing

Detailed testing documentation can be found in:

[TESTING.md](TESTING.md)

Testing includes:

- Manual feature testing.
- User-story testing.
- Authentication testing.
- CRUD testing.
- Authorisation testing.
- Responsive testing.
- Browser compatibility testing.
- Accessibility testing.
- HTML validation.
- CSS validation.
- JavaScript validation.
- Python linting.
- Lighthouse testing.
- Deployment testing.

---

# Bugs

## Fixed Bugs

The following issues were identified and resolved during development:

| Bug | Cause | Solution |
|---|---|---|
| Missing database columns | New fields were added to the `Recipe` model before the corresponding migrations had been created and applied. | Ran `python manage.py makemigrations` followed by `python manage.py migrate` to update the database schema. |
| Static CSS did not load | `home.html` was not extending `base.html`, so the stylesheet included in the base template was not applied. | Updated the template to extend `mealflow/base.html` and placed the page content inside the correct content block. |
| Recipe grid layout broke | Some recipe cards were placed outside the `.recipe-grid` container, causing them to display as full-width elements. | Moved all recipe cards inside the shared grid container so the CSS Grid layout applied consistently. |
| Hidden recipe cards remained visible | Existing CSS display rules overrode the browser's default behaviour for the HTML `hidden` attribute. | Added explicit CSS rules for `.recipe-card[hidden]` and `#load-more-recipes[hidden]` using `display: none`. |
| Duplicate saved-recipe feedback | The JavaScript contained repeated toast logic, causing the same feedback behaviour to run more than once. | Removed the duplicated logic and moved the saved-recipe functionality into a dedicated initialization function. |
| Django messages did not display | The message container was placed inside a template block that was replaced by child templates. | Moved the message container outside the replaceable content block while keeping it inside the main page structure. |
| Footer exceeded the viewport width | The footer used `width: 100%` together with padding, while the default box model added the padding outside the declared width. | Added a global `box-sizing: border-box` reset for all elements and pseudo-elements. |
| Page layout could not expand correctly | The `body` used `height: 100vh`, which restricted the layout as page content increased. | Replaced it with `min-height: 100vh` so the page could grow naturally. |
| HTML validator reported an empty form action | The search form included an unnecessary empty `action=""` attribute. | Removed the empty action attribute and allowed the form to submit to the current page by default. |
| HTML validator reported a section without a heading | A visual wrapper used a semantic `section` element without its own heading. | Replaced the `section` with a `div` because the element was used only for layout. |

## Known Issue

### Delete Confirmation May Occasionally Appear Twice

On some occasions, the delete confirmation dialog may appear twice before a recipe is deleted.
The deletion still completes correctly, and no data-integrity issues were observed. Cancelling the confirmation leaves the recipe unchanged.
This is considered a minor non-critical issue and would be investigated further in future development.

## Current Limitations

The following are intentional limitations rather than bugs:

- Recipe images are selected from static project files instead of being uploaded by users.
- The application does not currently include ratings, comments or nutritional information.
- The initial page load may occasionally be slower depending on the hosting service and current server response time.

# Deployment

MealFlow is deployed on [Heroku](https://www.heroku.com/) and uses a Heroku PostgreSQL database in production.

The deployed application uses:

- **Heroku** for cloud hosting.
- **PostgreSQL** as the production database.
- **Gunicorn** as the production web server.
- **WhiteNoise** for static-file serving.
- Environment variables for sensitive production settings.

The deployed application can be viewed here:

- [MealFlow Live Site](https://mealflow-c8de861cd143.herokuapp.com/)

---

## Version Control

Git was used for version control throughout development, with GitHub used as the remote repository.

The general workflow was:

1. Changes were made and tested locally.
2. Updated files were staged using:

   ```bash
   git add .
   ```

3. Changes were saved with descriptive commit messages:

   ```bash
   git commit -m "Commit message"
   ```

4. Commits were pushed to the main branch on GitHub:

   ```bash
   git push origin main
   ```

The Heroku application is connected to the GitHub repository, allowing new commits on the `main` branch to be deployed automatically.

---

## Deployment Preparation

The production dependencies were installed using:

```bash
pip install gunicorn psycopg2-binary dj-database-url whitenoise
```

The dependency file was then updated:

```bash
pip freeze > requirements.txt
```

A `Procfile` was added to the project root to tell Heroku how to start the application:

```text
web: gunicorn config.wsgi
```

A `.python-version` file was also added to define the Python version used during deployment:

```text
3.11
```

---

## Environment Variables

The following Config Vars were added through the Heroku application settings:

| Key | Purpose |
|---|---|
| `SECRET_KEY` | Stores the Django secret key securely |
| `DATABASE_URL` | Connects Django to the production PostgreSQL database |
| `DEBUG` | Controls Django debug mode and is set to `False` in production |

Sensitive values are stored in Heroku and are not committed to the GitHub repository.

A new Django secret key can be generated locally using:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

The generated value should be added directly to the Heroku Config Vars.

---

## Static Files

WhiteNoise is used to serve static files in production.

The middleware is placed directly after Django's security middleware in `settings.py`:

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # Remaining middleware
]
```

A static root is also configured so that Django can collect production assets:

```python
STATIC_ROOT = BASE_DIR / "staticfiles"
```

Static files are collected during deployment using:

```bash
python manage.py collectstatic
```

---

## Heroku Deployment Steps

The following process was used to deploy MealFlow:

1. Log in to Heroku and select **Create new app**.
2. Enter a unique application name and choose the appropriate region.
3. Add a Heroku PostgreSQL database to the application.
4. Open **Settings** and add the required Config Vars:
   - `SECRET_KEY`
   - `DATABASE_URL`
   - `DEBUG=False`
5. Confirm that the project contains:
   - `requirements.txt`
   - `Procfile`
   - `.python-version`
6. Open the **Deploy** tab.
7. Select **GitHub** as the deployment method.
8. Connect the Heroku application to the project repository.
9. Select the `main` branch.
10. Enable automatic deployment or select **Deploy Branch** manually.
11. Run the production database migrations:

    ```bash
    heroku run python manage.py migrate
    ```

12. Create an administrator account:

    ```bash
    heroku run python manage.py createsuperuser
    ```

13. Load the initial recipe data:

    ```bash
    heroku run python manage.py loaddata initial_recipes.json
    ```

14. Open the deployed application and verify that the database, static files and application features work correctly.

> The initial fixture should only be loaded once to avoid duplicate or conflicting database records.

---

## Local Development

To run MealFlow locally, Python and Git must be installed.

### Cloning

1. Open the [MealFlow GitHub repository](https://github.com/Fannyhenriques/milestone-project-3).
2. Select **Code**.
3. Copy the HTTPS, SSH or GitHub CLI URL.
4. Open a terminal and move to the directory where the project should be stored.
5. Clone the repository:

   ```bash
   git clone https://github.com/Fannyhenriques/milestone-project-3.git
   ```

6. Enter the project directory:

   ```bash
   cd milestone-project-3
   ```

7. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

8. Activate the virtual environment.

   On macOS or Linux:

   ```bash
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

9. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

10. Apply the database migrations:

    ```bash
    python manage.py migrate
    ```

11. Create a superuser if administrator access is required:

    ```bash
    python manage.py createsuperuser
    ```

12. Start the local development server:

    ```bash
    python manage.py runserver
    ```

13. Open the local application at:

    ```text
    http://127.0.0.1:8000/
    ```

The local version uses SQLite by default unless a different `DATABASE_URL` environment variable is supplied.

---

## Forking

To create an independent copy of the repository:

1. Log in to GitHub.
2. Open the MealFlow repository.
3. Select **Fork** near the top-right of the repository page.
4. Choose the account where the fork should be created.
5. GitHub will create a copy that can be changed without affecting the original repository.

---

## Local and Deployed Versions

The local and deployed versions provide the same core functionality.

The main infrastructure difference is the database:

- The local development environment uses SQLite by default.
- The deployed Heroku application uses PostgreSQL.

Production also runs with `DEBUG=False` and serves static files through WhiteNoise.

# Local Development

## Requirements

To run MealFlow locally, the following are required:

- Python.
- pip.
- Git.
- A code editor.
- The packages listed in `requirements.txt`.

## Installation

1. Clone or fork the repository.
2. Open the project directory.
3. Create a virtual environment:

```bash
python3 -m venv venv
```

4. Activate the virtual environment on macOS or Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

5. Install the project dependencies:

```bash
pip install -r requirements.txt
```

6. Add the required local environment variables.

7. Apply database migrations:

```bash
python manage.py migrate
```

8. Create a superuser if required:

```bash
python manage.py createsuperuser
```

9. Start the Django development server:

```bash
python manage.py runserver
```

10. Open the local application in a browser:

```text
http://127.0.0.1:8000/
```

