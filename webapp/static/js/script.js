document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.try-on-button');

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            // Find the parent .image-pair div
            const imagePairDiv = this.closest('.image-pair');
            // Find the generated image within this pair
            const generatedImg = imagePairDiv.querySelector('.generated-img');

            // Toggle visibility
            generatedImg.classList.toggle('hidden');

            // Change button text
            if (generatedImg.classList.contains('hidden')) {
                this.textContent = 'Show Virtual Try-On';
            } else {
                this.textContent = 'Hide Virtual Try-On';
            }
        });
    });
});