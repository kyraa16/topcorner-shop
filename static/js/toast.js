// Toast configuration
const ToastStyles = {
    success: {
        icon: '✅',
        background: 'bg-white border-green-200',
        iconColor: 'text-green-500'
    },
    error: {
        icon: '❌',
        background: 'bg-white border-red-200',
        iconColor: 'text-red-500'
    },
    warning: {
        icon: '⚠️',
        background: 'bg-white border-yellow-200',
        iconColor: 'text-yellow-500'
    },
    info: {
        icon: '💡',
        background: 'bg-white border-blue-200',
        iconColor: 'text-blue-500'
    }
};

let toastTimeout;

function showToast(title, message = '', type = 'info', duration = 4000) {
    const toast = document.getElementById('toast-component');
    const toastIcon = document.getElementById('toast-icon');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    // Clear any existing timeout
    if (toastTimeout) {
        clearTimeout(toastTimeout);
    }
    
    // Set content
    toastTitle.textContent = title;
    toastMessage.textContent = message;
    toastIcon.textContent = ToastStyles[type].icon;
    
    // Apply styles
    toast.className = `fixed bottom-6 right-6 p-4 rounded-2xl shadow-lg z-50 transition-all duration-500 transform flex items-start gap-3 min-w-80 max-w-md backdrop-blur-sm ${ToastStyles[type].background} border ${ToastStyles[type].iconColor}`;
    
    // Show toast with slide-in animation
    setTimeout(() => {
        toast.classList.remove('opacity-0', 'translate-y-32');
        toast.classList.add('opacity-100', 'translate-y-0');
    }, 50);
    
    // Auto hide after duration
    toastTimeout = setTimeout(() => {
        hideToast();
    }, duration);
}

function hideToast() {
    const toast = document.getElementById('toast-component');
    
    toast.classList.remove('opacity-100', 'translate-x-0');
    toast.classList.add('opacity-0', 'translate-x-32');
    
    if (toastTimeout) {
        clearTimeout(toastTimeout);
    }
}

// Optional: Add hover pause functionality
document.getElementById('toast-component').addEventListener('mouseenter', () => {
    if (toastTimeout) {
        clearTimeout(toastTimeout);
    }
});

document.getElementById('toast-component').addEventListener('mouseleave', () => {
    const toast = document.getElementById('toast-component');
    if (!toast.classList.contains('opacity-0')) {
        toastTimeout = setTimeout(() => {
            hideToast();
        }, 2000);
    }
});