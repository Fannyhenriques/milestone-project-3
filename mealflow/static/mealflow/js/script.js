function initHamburgerMenu() {
  const menuButton = document.querySelector(".nav-toggle");
  const navLinks = document.querySelector("#nav-links");

  if (!menuButton || !navLinks) {
    return;
  }

  menuButton.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("nav-open");

    menuButton.setAttribute("aria-expanded", isOpen);
    menuButton.setAttribute(
      "aria-label",
      isOpen ? "Close navigation menu" : "Open navigation menu"
    );

    menuButton.textContent = isOpen ? "✕" : "☰";
  });
}


function initDeleteConfirmation() {
  const deleteRecipeForm = document.querySelector(
    "#delete-recipe-form"
  );

  if (!deleteRecipeForm) {
    return;
  }

  deleteRecipeForm.addEventListener("submit", (event) => {
    const confirmed = window.confirm(
      "Are you sure you want to delete this recipe?"
    );

    if (!confirmed) {
      event.preventDefault();
    }
  });
}

function initRecipeFilters() {
  const searchForm = document.querySelector(".recipe-search-form");
  const searchInput = document.querySelector("#recipe-search");
  const recipeCards = Array.from(
    document.querySelectorAll(".recipe-card")
  );
  const noResultsMessage = document.querySelector(
    "#no-filter-results"
  );
  const loadMoreButton = document.querySelector(
    "#load-more-recipes"
  );

  if (
    !searchForm ||
    !searchInput ||
    recipeCards.length === 0 ||
    !loadMoreButton
  ) {
    return;
  }

  const recipesPerLoad = 16;
  let visibleRecipeLimit = recipesPerLoad;

  function filterRecipes() {
    const searchTerm = searchInput.value
      .trim()
      .toLowerCase();

    const selectedMealTypes = Array.from(
      searchForm.querySelectorAll(
        'input[name="meal_type"]:checked'
      )
    ).map((checkbox) => checkbox.value);

    const selectedCategories = Array.from(
      searchForm.querySelectorAll(
        'input[name="food_category"]:checked'
      )
    ).map((checkbox) => checkbox.value);

    const matchingRecipes = recipeCards.filter((card) => {
      const title = card.dataset.title || "";
      const mealType = card.dataset.mealType || "";
      const category = card.dataset.foodCategory || "";

      const matchesSearch =
        !searchTerm ||
        title.includes(searchTerm);

      const matchesMealType =
        selectedMealTypes.length === 0 ||
        selectedMealTypes.includes(mealType);

      const matchesCategory =
        selectedCategories.length === 0 ||
        selectedCategories.includes(category);

      return (
        matchesSearch &&
        matchesMealType &&
        matchesCategory
      );
    });

    recipeCards.forEach((card) => {
      card.hidden = true;
    });

    matchingRecipes
      .slice(0, visibleRecipeLimit)
      .forEach((card) => {
        card.hidden = false;
      });

    if (noResultsMessage) {
      noResultsMessage.hidden =
        matchingRecipes.length !== 0;
    }

    loadMoreButton.hidden =
      matchingRecipes.length <= visibleRecipeLimit;
  }

  function resetVisibleLimit() {
    visibleRecipeLimit = recipesPerLoad;
    filterRecipes();
  }

  searchForm.addEventListener("submit", (event) => {
    event.preventDefault();
    resetVisibleLimit();
  });

  searchForm.addEventListener("change", (event) => {
    if (
      event.target.matches(
        'input[name="meal_type"], ' +
        'input[name="food_category"]'
      )
    ) {
      resetVisibleLimit();
    }
  });

  searchForm.addEventListener("reset", () => {
    visibleRecipeLimit = recipesPerLoad;
    requestAnimationFrame(filterRecipes);
  });

  loadMoreButton.addEventListener("click", () => {
    visibleRecipeLimit += recipesPerLoad;
    filterRecipes();
  });

  filterRecipes();
}


function initSiteMessages() {
  const siteMessages = document.querySelectorAll(".site-message");

  siteMessages.forEach((message) => {
    setTimeout(() => {
      message.classList.remove("show");
    }, 3000);
  });
}


function initSaveRecipe() {
  const saveForm = document.querySelector("#save-recipe-form");

  if (!saveForm) {
    return;
  }

  const saveButton = saveForm.querySelector(
    "#save-recipe-button"
  );
  const buttonText = saveButton.querySelector(
    ".save-button-text"
  );
  const heart = saveButton.querySelector(".save-heart");
  const feedback = document.querySelector("#save-feedback");

  if (!saveButton || !buttonText || !heart || !feedback) {
    return;
  }

  saveForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    saveButton.disabled = true;
    feedback.textContent = "";

    try {
      const response = await fetch(saveForm.action, {
        method: "POST",
        body: new FormData(saveForm),
      });

      if (!response.ok) {
        throw new Error(
          "The recipe could not be updated."
        );
      }

      const data = await response.json();

      buttonText.textContent = data.is_saved ? "Saved" : "Save recipe";

      heart.textContent = data.is_saved ? "♥" : "♡";
      feedback.textContent = data.message;
      feedback.classList.add("show");

      setTimeout(() => {
        feedback.classList.remove("show");
      }, 3000);
    } catch (error) {
      feedback.textContent =
        "Something went wrong. Please try again.";

      feedback.classList.add("show");

      setTimeout(() => {
        feedback.classList.remove("show");
      }, 3000);
    } finally {
      saveButton.disabled = false;
    }
  });
}


document.addEventListener("DOMContentLoaded", () => {
  initHamburgerMenu();
  initDeleteConfirmation();
  initRecipeFilters();
  initSiteMessages();
  initSaveRecipe();
});