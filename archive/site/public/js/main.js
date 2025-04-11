
document.addEventListener("DOMContentLoaded", function() {
    console.log("Document is fully loaded");

    document.getElementById("sidebar-close").addEventListener("click", function() {
        document.getElementById('sidebar-mobile').style.visibility = 'hidden';
    });
    document.getElementById("sidebar-open").addEventListener("click", function() {
        document.getElementById('sidebar-mobile').style.visibility = 'visible';
    });

    document.getElementById("menu-toggle").addEventListener("click", function() {
        const menuPopup = document.getElementById('menu-popup');
        //console.log(menuPopup);
        menuPopup.classList.toggle('hidden');
    });

    // Your code here
  });