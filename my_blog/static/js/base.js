document.addEventListener("DOMContentLoaded", function () {
    
    // TOAST MESSAGE
    const toastEl = document.getElementById("toastMessage");
    if (toastEl) {
        const toast = new bootstrap.Toast(toastEl);
        toast.show();
    }
    
    // TOOL TIP
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
      new bootstrap.Tooltip(tooltipTriggerEl);
    });

    const tooltipTrigger = document.querySelectorAll('.custom-tooltip');
    const tooltip = new bootstrap.Tooltip(tooltipTrigger, {
    delay: { show: 100, hide: 2000 } // Show after 100ms, hide after 2000ms
    });
});



// ****DASHBOARDS SCRIPTS ****//

// ADMIN OFF-Canvass Sidebar Menu
document.addEventListener('DOMContentLoaded', function () {
    console.log('POGI AKO')

    const offcanvasEl = document.getElementById('offcanvasScrolling');
    const offcanvas = new bootstrap.Offcanvas(offcanvasEl);
    
    // Manually add class on initial load
    document.body.classList.add('sidebar-open');
    offcanvas.show();

    // Handle class when opened/closed via buttons
    offcanvasEl.addEventListener('show.bs.offcanvas', function () {
        document.body.classList.add('sidebar-open');
    });
    
    offcanvasEl.addEventListener('hidden.bs.offcanvas', function () {
        document.body.classList.remove('sidebar-open');
    });
});




