document.addEventListener('DOMContentLoaded', () => {
    console.log('Website loaded');

    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (event) => {
            event.preventDefault();
            alert('Thank you for your message!');
            contactForm.reset();
        });
    }
});