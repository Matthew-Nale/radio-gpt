document.addEventListener("DOMContentLoaded", function () {
    const textarea = document.getElementById('user-query-input');

    const resizeTextarea = () => {
        textarea.style.height = "auto";
        const maxHeight = parseFloat(getComputedStyle(textarea).maxHeight);
        const newHeight = textarea.scrollHeight;
        textarea.style.height = `${Math.min(newHeight, maxHeight)}px`;

        textarea.style.height = `${textarea.scrollHeight}px`;

        if (newHeight > maxHeight) {
            textarea.style.overflowY = "auto";
        } else {
            textarea.style.overflowY = "hidden";
        }
    };

    textarea.addEventListener("input", resizeTextarea);
    resizeTextarea();
});