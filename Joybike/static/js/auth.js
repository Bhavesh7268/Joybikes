document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.getElementById('id_password1');
    const usernameInput = document.getElementById('id_username');
    const requirementItems = document.querySelectorAll('.requirement-list li');
    
    if (passwordInput) {
        passwordInput.addEventListener('input', function() {
            const password = this.value;
            
            // Check each requirement
            requirementItems.forEach(item => {
                const requirement = item.getAttribute('data-requirement');
                let isValid = false;
                
                switch(requirement) {
                    case 'length':
                        isValid = password.length >= 8;
                        break;
                    case 'common':
                        // Simple check - in real app use proper validation
                        isValid = !['password', '12345678'].includes(password.toLowerCase());
                        break;
                    case 'numeric':
                        isValid = !/^\d+$/.test(password);
                        break;
                    case 'similar':
                        const username = usernameInput ? usernameInput.value : '';
                        isValid = !username || password.toLowerCase() !== username.toLowerCase();
                        break;
                }
                
                if (isValid) {
                    item.classList.add('valid');
                } else {
                    item.classList.remove('valid');
                }
            });
        });
    }
    
    // Trigger validation if username changes
    if (usernameInput) {
        usernameInput.addEventListener('input', function() {
            if (passwordInput && passwordInput.value) {
                passwordInput.dispatchEvent(new Event('input'));
            }
        });
    }
});