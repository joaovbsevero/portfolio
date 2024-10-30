document.querySelectorAll(".collapsible-arrow").forEach((arrow) => {
    arrow.addEventListener("click", () => {
        const content = arrow.parentNode.previousElementSibling; // Get the corresponding content div
        if (content.style.maxHeight) {
            // If the content is already expanded
            content.style.maxHeight = null; // Collapse it
            arrow.classList.remove("expanded");
            arrow.classList.add("collapsed");
            content.style.opacity = "0"; // Make it fully transparent
        } else {
            // If the content is collapsed
            content.style.maxHeight = content.scrollHeight + "px"; // Expand it
            arrow.classList.remove("collapsed");
            arrow.classList.add("expanded");
            content.style.opacity = "1"; // Make it fully visible
        }
    });
});
