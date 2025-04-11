document.addEventListener('DOMContentLoaded', function() {
  // Get the sidebar elements
  const sidebar = document.querySelector('[role="dialog"]');
  const sidebarBackdrop = sidebar.querySelector('.fixed.inset-0.bg-gray-900\\/80');
  const sidebarPanel = sidebar.querySelector('.relative.mr-16.flex.w-full.max-w-xs.flex-1');
  const closeButton = sidebar.querySelector('button[aria-label="Close sidebar"]');
  const openButton = document.querySelector('button[aria-label="Open sidebar"]');
  
  // Function to open the sidebar
  function openSidebar() {
    // Show the sidebar
    sidebar.classList.remove('hidden');
    
    // Add transition classes
    sidebarBackdrop.classList.add('transition-opacity', 'ease-linear', 'duration-300', 'opacity-100');
    sidebarBackdrop.classList.remove('opacity-0');
    
    sidebarPanel.classList.add('transition', 'ease-in-out', 'duration-300', 'transform', 'translate-x-0');
    sidebarPanel.classList.remove('-translate-x-full');
    
    closeButton.classList.add('transition', 'ease-in-out', 'duration-300', 'opacity-100');
    closeButton.classList.remove('opacity-0');
    
    // Prevent scrolling on the body
    document.body.style.overflow = 'hidden';
  }
  
  // Function to close the sidebar
  function closeSidebar() {
    // Add transition classes for closing
    sidebarBackdrop.classList.add('transition-opacity', 'ease-linear', 'duration-300', 'opacity-0');
    sidebarBackdrop.classList.remove('opacity-100');
    
    sidebarPanel.classList.add('transition', 'ease-in-out', 'duration-300', 'transform', '-translate-x-full');
    sidebarPanel.classList.remove('translate-x-0');
    
    closeButton.classList.add('transition', 'ease-in-out', 'duration-300', 'opacity-0');
    closeButton.classList.remove('opacity-100');
    
    // Hide the sidebar after the transition completes
    setTimeout(() => {
      sidebar.classList.add('hidden');
      document.body.style.overflow = '';
    }, 300);
  }
  
  // Add event listeners
  openButton.addEventListener('click', openSidebar);
  closeButton.addEventListener('click', closeSidebar);
  sidebarBackdrop.addEventListener('click', closeSidebar);
  
  // Handle user menu dropdown
  const userMenuButton = document.getElementById('user-menu-button');
  const userMenu = userMenuButton.nextElementSibling;
  
  userMenuButton.addEventListener('click', function() {
    const expanded = userMenuButton.getAttribute('aria-expanded') === 'true';
    userMenuButton.setAttribute('aria-expanded', !expanded);
    userMenu.classList.toggle('hidden');
  });
  
  // Close the menu when clicking outside
  document.addEventListener('click', function(event) {
    if (!userMenuButton.contains(event.target) && !userMenu.contains(event.target)) {
      userMenuButton.setAttribute('aria-expanded', 'false');
      userMenu.classList.add('hidden');
    }
  });
}); 