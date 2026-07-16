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
        src="documentation/images/home-mobile-wireframe.png"
        alt="Initial MealFlow Home page mobile wireframe"
        width="200"
      >
    </td>
    <td>
      <img
        src="documentation/images/home-tablet-wireframe.png"
        alt="Initial MealFlow Home page tablet wireframe"
        width="280"
      >
    </td>
    <td>
      <img
        src="documentation/images/home-desktop-wireframe.png"
        alt="Initial MealFlow Home page desktop wireframe"
        width="400"
      >
    </td>
  </tr>
</table>

---
