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

      buttonText.textContent = data.is_saved
        ? "Saved"
        : "Save recipe";

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
  initSiteMessages();
  initSaveRecipe();
});