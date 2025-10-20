document.addEventListener("DOMContentLoaded", function () {
    const textarea = document.getElementById('user-query-input');
    const queryLocation = document.querySelector('.query-location');

    const resizeTextarea = () => {
        textarea.style.height = "auto";
        const maxHeight = parseFloat(getComputedStyle(textarea).maxHeight);
        const newHeight = textarea.scrollHeight;
        const appliedHeight = Math.min(newHeight, maxHeight);
        textarea.style.height = `${appliedHeight}px`;

        if (newHeight > maxHeight) {
            textarea.style.overflowY = "auto";
            textarea.scrollTop = textarea.scrollHeight;
        } else {
            textarea.style.overflowY = "hidden";
        }

        // only apply upward "lift" after it's at the bottom
        if (queryLocation.classList.contains('moved')) {
            const lift = (appliedHeight - 40) / 10; // small upward nudge as it grows
            queryLocation.style.transform = `translateY(calc(40vh - ${Math.max(lift, 0)}vh))`;
        }
    };

    textarea.addEventListener("input", resizeTextarea);
    resizeTextarea();
});