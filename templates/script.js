// Simple JavaScript for cart functionality
document.addEventListener('DOMContentLoaded', function() {
    // Add to cart buttons
    const addToCartButtons = document.querySelectorAll('.btn-add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            alert('Mahsulot savatchaga qo\'shildi!');
        });
    });
    
    // Quantity buttons
    const quantityButtons = document.querySelectorAll('.quantity-btn');
    quantityButtons.forEach(button => {
        button.addEventListener('click', function() {
            const input = this.parentElement.querySelector('.quantity-input');
            let value = parseInt(input.value);
            
            if (this.textContent === '+') {
                value++;
            } else if (this.textContent === '-' && value > 1) {
                value--;
            }
            
            input.value = value;
        });
    });
    
    // Remove buttons
    const removeButtons = document.querySelectorAll('.remove-btn');
    removeButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.closest('.cart-item').remove();
            updateCartTotal();
        });
    });
    
    // Form submissions
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Form muvaffaqiyatli yuborildi!');
        });
    });
    
    // Auth form switching
    const urlParams = new URLSearchParams(window.location.search);
    const action = urlParams.get('action');
    const formTitle = document.getElementById('form-title');
    const submitBtn = document.getElementById('submit-btn');
    const switchText = document.getElementById('switch-text');
    const switchLink = document.getElementById('switch-link');
    const authForm = document.getElementById('auth-form');
    
    if (authForm) {
        if (action === 'login') {
            showLoginForm();
        }
        
        switchLink.addEventListener('click', function(e) {
            e.preventDefault();
            if (formTitle.textContent === 'Ro\'yxatdan o\'tish') {
                showLoginForm();
            } else {
                showRegisterForm();
            }
        });
    }
    
    function showLoginForm() {
        formTitle.textContent = 'Kirish';
        submitBtn.textContent = 'Kirish';
        switchText.innerHTML = 'Hisobingiz yo\'qmi? <a href="#" id="switch-link">Ro\'yxatdan o\'tish</a>';
        
        // Remove name and surname fields for login
        const nameField = document.getElementById('reg-name').closest('.form-group');
        const surnameField = document.getElementById('reg-surname').closest('.form-group');
        const confirmField = document.getElementById('reg-confirm-password').closest('.form-group');
        
        if (nameField) nameField.style.display = 'none';
        if (surnameField) surnameField.style.display = 'none';
        if (confirmField) confirmField.style.display = 'none';
        
        // Re-attach event listener to the new switch link
        document.getElementById('switch-link').addEventListener('click', function(e) {
            e.preventDefault();
            showRegisterForm();
        });
    }
    
    function showRegisterForm() {
        formTitle.textContent = 'Ro\'yxatdan o\'tish';
        submitBtn.textContent = 'Ro\'yxatdan o\'tish';
        switchText.innerHTML = 'Allaqachon hisobingiz bormi? <a href="#" id="switch-link">Kirish</a>';
        
        // Show all fields for registration
        const nameField = document.getElementById('reg-name').closest('.form-group');
        const surnameField = document.getElementById('reg-surname').closest('.form-group');
        const confirmField = document.getElementById('reg-confirm-password').closest('.form-group');
        
        if (nameField) nameField.style.display = 'block';
        if (surnameField) surnameField.style.display = 'block';
        if (confirmField) confirmField.style.display = 'block';
        
        // Re-attach event listener to the new switch link
        document.getElementById('switch-link').addEventListener('click', function(e) {
            e.preventDefault();
            showLoginForm();
        });
    }
    
    // Update cart total
    function updateCartTotal() {
        // This would normally calculate the total based on items in cart
        // For demo purposes, we'll just show a static total
    }
});