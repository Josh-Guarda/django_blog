

"use strict";

function _createForOfIteratorHelper(o, allowArrayLike) { var it; if (typeof Symbol === "undefined" || o[Symbol.iterator] == null) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = o[Symbol.iterator](); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

document.addEventListener('DOMContentLoaded', function () {
  'use strict';
  /* function testWebP(callback) {
  var webP = new Image();
  webP.onload = webP.onerror = function () {
  callback(webP.height == 2);
  };
  webP.src = "data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA";
  }
  testWebP(function (support) {
  if (support == true) {
  document.querySelector('body').classList.add('webp');
  }else{
  document.querySelector('body').classList.add('no-webp');
  }
  });*/

  feather.replace();

  (function () {
    var sidebar = document.querySelector('.sidebar'),
        catSubMenu = document.querySelector('.cat-sub-menu'),
        sidebarBtns = document.querySelectorAll('.sidebar-toggle');

    var _iterator = _createForOfIteratorHelper(sidebarBtns),
        _step;

    try {
      for (_iterator.s(); !(_step = _iterator.n()).done;) {
        var sidebarBtn = _step.value;

        if (sidebarBtn && catSubMenu && sidebarBtn) {
          sidebarBtn.addEventListener('click', function () {
            var _iterator2 = _createForOfIteratorHelper(sidebarBtns),
                _step2;

            try {
              for (_iterator2.s(); !(_step2 = _iterator2.n()).done;) {
                var sdbrBtn = _step2.value;
                sdbrBtn.classList.toggle('rotated');
              }
            } catch (err) {
              _iterator2.e(err);
            } finally {
              _iterator2.f();
            }

            sidebar.classList.toggle('hidden');
            catSubMenu.classList.remove('visible');
          });
        }
      }
    } catch (err) {
      _iterator.e(err);
    } finally {
      _iterator.f();
    }
  })();

  

  (function () {
    var showCatBtns = document.querySelectorAll('.show-cat-btn');

    showCatBtns.forEach(function (showCatBtn) {
      var catSubMenu = showCatBtn.nextElementSibling;
      var arrowIcon = showCatBtn.querySelector('.category__btn .arrow-down');

      showCatBtn.addEventListener('click', function (e) {
        e.preventDefault();
        showCatBtn.blur();

        // Toggle submenu
        catSubMenu.classList.toggle('visible');

        // Rotate only THIS arrow
        arrowIcon.classList.toggle('rotated');
      });
    });
  })();





  

  (function () {
    var showMenu = document.querySelector('.lang-switcher');
    var langMenu = document.querySelector('.lang-menu');
    var layer = document.querySelector('.layer');

    if (showMenu) {
      showMenu.addEventListener('click', function () {
        langMenu.classList.add('active');
        layer.classList.add('active');
      });

      if (layer) {
        layer.addEventListener('click', function (e) {
          if (langMenu.classList.contains('active')) {
            langMenu.classList.remove('active');
            layer.classList.remove('active');
          }
        });
      }
    }
  })();

  (function () {
    var userDdBtnList = document.querySelectorAll('.dropdown-btn');

    var userDdList = document.querySelectorAll('.users-item-dropdown');
    var layer = document.querySelector('.layer');

    if (userDdList && userDdBtnList) {
      var _iterator3 = _createForOfIteratorHelper(userDdBtnList),
          _step3;

      try {
        for (_iterator3.s(); !(_step3 = _iterator3.n()).done;) {
          var userDdBtn = _step3.value;
          userDdBtn.addEventListener('click', function (e) {
            layer.classList.add('active');

            var _iterator4 = _createForOfIteratorHelper(userDdList),
                _step4;

            try {
              for (_iterator4.s(); !(_step4 = _iterator4.n()).done;) {
                var userDd = _step4.value;

                if (e.currentTarget.nextElementSibling == userDd) {
                  if (userDd.classList.contains('active')) {
                    userDd.classList.remove('active');
                  } else {
                    userDd.classList.add('active');
                  }
                } else {
                  userDd.classList.remove('active');
                }
              }
            } catch (err) {
              _iterator4.e(err);
            } finally {
              _iterator4.f();
            }
          });
        }
      } catch (err) {
        _iterator3.e(err);
      } finally {
        _iterator3.f();
      }
    }

    if (layer) {
      layer.addEventListener('click', function (e) {
        var _iterator5 = _createForOfIteratorHelper(userDdList),
            _step5;

        try {
          for (_iterator5.s(); !(_step5 = _iterator5.n()).done;) {
            var userDd = _step5.value;

            if (userDd.classList.contains('active')) {
              userDd.classList.remove('active');
              layer.classList.remove('active');
          
            }
          }
        } catch (err) {
          _iterator5.e(err);
        } finally {
          _iterator5.f();
        }
      });
    }
  })();

  /* Theme Switcher light/dark*/
  (function () {
    Chart.defaults.backgroundColor = '#000';
    var darkMode = localStorage.getItem('darkMode');
    var darkModeToggle = document.querySelector('.theme-switcher');

    var enableDarkMode = function enableDarkMode() {
      document.body.classList.add('darkmode');
      localStorage.setItem('darkMode', 'enabled');
    };

    var disableDarkMode = function disableDarkMode() {
      document.body.classList.remove('darkmode');
      localStorage.setItem('darkMode', null);
    };

    if (darkMode === 'enabled') {
      enableDarkMode();
    }

    if (darkModeToggle) {
      darkModeToggle.addEventListener('click', function () {
        darkMode = localStorage.getItem('darkMode');

        if (darkMode !== 'enabled') {
          enableDarkMode();
        } else {
          disableDarkMode();
        }

        addData();
      });
    }
  })();



  /* List Checker*/

  const ddDropdown = document.querySelector('.dd-button');

  function fetchCheckItems(urlParams){
    // console.log(urlParams)
    fetch(`${window.location.pathname}?${urlParams.toString()}`, {
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      }
    })
    .then(res => res.json())
    .then(data => {
      // console.log(data)
      if (data.checked === 0){
        ddDropdown.style.display = 'none';
        return;
      }

      ddDropdown.style.display = 'inline-block';
      ddDropdown.textContent =
      `Selected: ${data.checked} / ${data.total}`
      
    });
  }


  (function () {
    var ddDropdown = document.querySelector('.dd-dropdown')
    var checkAll = document.querySelector('.check-all');
    var checkers = document.querySelectorAll('.check');

    
    if (checkAll && checkers) {
      checkAll.addEventListener('change', function (e) {
        var _iterator6 = _createForOfIteratorHelper(checkers),
            _step6;
        e.preventDefault();
        const formData = new FormData(this.form);
        const urlParams = new URLSearchParams(formData);
        
        
        try {
          for (_iterator6.s(); !(_step6 = _iterator6.n()).done;) {
            var checker = _step6.value;

            if (checkAll.checked) {
              checker.checked = true;
              checker.parentElement.parentElement.parentElement.classList.add('active');

            //show dropdown counter when checkAll is True
              ddDropdown.style.display = "inline-block"
              console.log(checker.value)

            } else {
              checker.checked = false;
              checker.parentElement.parentElement.parentElement.classList.remove('active');
            //Hide dropdown counter when checkAll is False
              ddDropdown.style.display = "none"
            }
          }
          
          var totalCheckbox = document.querySelectorAll('.users-table .check').forEach(cb => urlParams.append('checksItems', cb.value));
          
          var totalChecked = document.querySelectorAll('.users-table .check:checked').forEach(cb => urlParams.append('checkers', cb.value));
          fetchCheckItems(urlParams)
          
          
        } catch (err) {
          _iterator6.e(err);
        } finally {
          _iterator6.f();
        }
      });

      var _iterator7 = _createForOfIteratorHelper(checkers),
          _step7;

      try {
        var _loop = function _loop() {
          var checker = _step7.value;
            checker.addEventListener('change', function (e) {
            
            e.preventDefault();
            const formData = new FormData(this.form);
            const urlParams = new URLSearchParams(formData);
            // console.log(urlParams)

            checker.parentElement.parentElement.parentElement.classList.toggle('active');
            
            //show dropdown counter
            ddDropdown.style.display = "inline-block"

            var totalCheckbox = document.querySelectorAll('.users-table .check');
            var totalChecked = document.querySelectorAll('.users-table .check:checked');
            
            //get total CheckBoxes
            totalCheckbox.forEach(cb => urlParams.append('checksItems', cb.value));
            
            //get total Checked
            totalChecked.forEach(cb => urlParams.append('checks', cb.value));

            fetchCheckItems(urlParams)
            
            
            if (checker.checked){
              console.log(checker.value)//return ID of the checked post
            
            }
            

            if (!checker.checked) {
              checkAll.checked = false;
              //put a function here to check the number of 
            }

            if (totalCheckbox && totalChecked) {
              if (totalCheckbox.length == totalChecked.length) {
                checkAll.checked = true;
              } else {
                checkAll.checked = false;
              }
            }
          });
        };

        for (_iterator7.s(); !(_step7 = _iterator7.n()).done;) {
          _loop();
        }
      } catch (err) {
        _iterator7.e(err);
      } finally {
        _iterator7.f();
      }
    }
  })();

  (function () {
    var checkAll = document.querySelector('.check-all');
    var checkers = document.querySelectorAll('.check');
    var checkedSum = document.querySelector('.checked-sum');

    if (checkedSum && checkAll && checkers) {
      checkAll.addEventListener('change', function (e) {
        var totalChecked = document.querySelectorAll('.users-table .check:checked');
        checkedSum.textContent = totalChecked.length;
        
      });

      var _iterator8 = _createForOfIteratorHelper(checkers),
          _step8;

      try {
        for (_iterator8.s(); !(_step8 = _iterator8.n()).done;) {
          var checker = _step8.value;
          checker.addEventListener('change', function (e) {
            var totalChecked = document.querySelectorAll('.users-table .check:checked');
            checkedSum.textContent = totalChecked.length;
            
          });
        }
      } catch (err) {
        _iterator8.e(err);
      } finally {
        _iterator8.f();
      }
    }
  })();

  var charts = {};
  var gridLine;
  var titleColor;

  (function () {
    /* Add gradient to chart */
    var width, height, gradient;

    function getGradient(ctx, chartArea) {
      var chartWidth = chartArea.right - chartArea.left;
      var chartHeight = chartArea.bottom - chartArea.top;

      if (gradient === null || width !== chartWidth || height !== chartHeight) {
        width = chartWidth;
        height = chartHeight;
        gradient = ctx.createLinearGradient(0, chartArea.bottom, 0, chartArea.top);
        gradient.addColorStop(0, 'rgba(255, 255, 255, 0)');
        gradient.addColorStop(1, 'rgba(255, 255, 255, 0.4)');
      }

      return gradient;
    }
    /* Visitors chart */


    var ctx = document.getElementById('myChart');

    if (ctx) {
      var myCanvas = ctx.getContext('2d');
      var myChart = new Chart(myCanvas, {
        type: 'line',
        data: {
          labels: ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
          datasets: [{
            label: 'Last 6 months',
            data: [35, 27, 40, 15, 30, 25, 45],
            cubicInterpolationMode: 'monotone',
            tension: 0.4,
            backgroundColor: ['rgba(95, 46, 234, 1)'],
            borderColor: ['rgba(95, 46, 234, 1)'],
            borderWidth: 2
          }, {
            label: 'Previous',
            data: [20, 36, 16, 45, 29, 32, 10],
            cubicInterpolationMode: 'monotone',
            tension: 0.4,
            backgroundColor: ['rgba(75, 222, 151, 1)'],
            borderColor: ['rgba(75, 222, 151, 1)'],
            borderWidth: 2
          }]
        },
        options: {
          scales: {
            y: {
              min: 0,
              max: 100,
              ticks: {
                stepSize: 25
              },
              grid: {
                display: false
              }
            },
            x: {
              grid: {
                color: gridLine
              }
            }
          },
          elements: {
            point: {
              radius: 2
            }
          },
          plugins: {
            legend: {
              position: 'top',
              align: 'end',
              labels: {
                boxWidth: 8,
                boxHeight: 8,
                usePointStyle: true,
                font: {
                  size: 12,
                  weight: '500'
                }
              }
            },
            title: {
              display: true,
              text: ['Visitor statistics', 'Nov - July'],
              align: 'start',
              color: '#171717',
              font: {
                size: 16,
                family: 'Inter',
                weight: '600',
                lineHeight: 1.4
              }
            }
          },
          tooltips: {
            mode: 'index',
            intersect: false
          },
          hover: {
            mode: 'nearest',
            intersect: true
          }
        }
      });
      charts.visitors = myChart;
    }
    /* Customers chart */

    var customersChart = document.getElementById('customersChart');

    if (customersChart) {
      var customersChartCanvas = customersChart.getContext('2d');
      var myCustomersChart = new Chart(customersChartCanvas, {
        type: 'line',
        data: {
          labels: ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
          datasets: [{
            label: '+958',
            data: [90, 10, 80, 20, 70, 30, 50],
            tension: 0.4,
            backgroundColor: function backgroundColor(context) {
              var chart = context.chart;
              var ctx = chart.ctx,
                  chartArea = chart.chartArea;

              if (!chartArea) {
                // This case happens on initial chart load
                return null;
              }

              return getGradient(ctx, chartArea);
            },
            borderColor: ['#fff'],
            borderWidth: 2,
            fill: true
          }]
        },
        options: {
          scales: {
            y: {
              display: false
            },
            x: {
              display: false
            }
          },
          elements: {
            point: {
              radius: 1
            }
          },
          plugins: {
            legend: {
              position: 'top',
              align: 'end',
              labels: {
                color: '#fff',
                size: 18,
                fontStyle: 800,
                boxWidth: 0
              }
            },
            title: {
              display: true,
              text: ['New Customers', '28 Daily Avg.'],
              align: 'start',
              color: '#fff',
              font: {
                size: 16,
                family: 'Inter',
                weight: '600',
                lineHeight: 1.4
              },
              padding: {
                top: 20
              }
            }
          },
          maintainAspectRatio: false
        }
      });
      customersChart.customers = myCustomersChart;
    }
  })();
  /* Change data of all charts */

  function addData() {
    var darkMode = localStorage.getItem('darkMode');

    if (darkMode === 'enabled') {
      gridLine = '#37374F';
      titleColor = '#EFF0F6';
    } else {
      gridLine = '#EEEEEE';
      titleColor = '#171717';
    }

    if (charts.hasOwnProperty('visitors')) {
      charts.visitors.options.scales.x.grid.color = gridLine;
      charts.visitors.options.plugins.title.color = titleColor;
      charts.visitors.options.scales.y.ticks.color = titleColor;
      charts.visitors.options.scales.x.ticks.color = titleColor;
      charts.visitors.update();
    }
  }

  addData();
});




/*HEADER/PROFILE*/

//LOAD PROFILE IMAGE
let dispImage = document.getElementById('display-image');
  let inputPicture = document.getElementById('avatar-upload');
  inputPicture.onchange = function () {
      console.log('POGI AKO')
      if (inputPicture.files && inputPicture.files[0]) {
          dispImage.src = URL.createObjectURL(inputPicture.files[0]);
      }
  };














/*POSTS*/


//Dropdown when select checkbox is check
document.addEventListener('click', function (e) {
    const dropdown = document.querySelector('.dd-dropdown');
    const checkbox = document.querySelector('#dd-toggle');

    // If click is outside the dropdown
    if (!dropdown.contains(e.target)) {
      checkbox.checked = false;
    }
  })



//MODAL SCRIPT
document.addEventListener('DOMContentLoaded', () => {
  initModal();
  initPostsList();
});

//Load PostList --> Read Pagination
function initPostsList(){
  const postQuant = document.getElementById('paginateQuant')
  // this.form.submit();
  postQuant.addEventListener("change", function () {    
        this.form.submit();
    });
}



function initModal() {
  const modal = document.querySelector('.modal-frame');
  const overlay = document.querySelector('.modal-overlay');
  const modalInset = document.querySelector('.modal-inset');
  const modalBody = document.querySelector('.modal-body');

  
  // Event delegation for View/Edit
  document.addEventListener('click', e => {
    const trigger = e.target.closest('.modal-trigger');
    if (!trigger) return;

    e.preventDefault();

    const url = trigger.dataset.url;
    const mode = trigger.dataset.mode;
    const action = trigger.dataset.action;

    openModal(modal, overlay, modalInset);
    showLoader(modalBody);
    
    if (mode === 'trash' && action === 'batch-delete') {
      renderBatchTrash();
      return;
    }

    fetchData(url, mode,overlay,modalInset);
  });

  // Close modal
  document.addEventListener('click', e => {
    if (e.target.closest('.close') || e.target === overlay) {
      closeModal(modal, overlay);
    }
  });
}


function openModal(modal, overlay, modalInset) {
  if (localStorage.getItem('darkMode') === 'enabled') {
    modalInset.classList.add('dark');
  } else {
    modalInset.classList.remove('dark');
  }
  


  overlay.classList.add('state-show');
  modal.classList.remove('state-leave');
  modal.classList.add('state-appear');
  modal.style.display = 'flex';
}

function closeModal(modal, overlay) {
  overlay.classList.remove('state-show');
  modal.classList.remove('state-appear');
  modal.classList.add('state-leave');

  modal.addEventListener('animationend', function handler() {
    modal.classList.remove('state-leave');
    modal.style.display = 'none';
    modal.removeEventListener('animationend', handler);
  });
}


function showLoader(container) {
  container.innerHTML = `
    <div class="loader-wrapper">
      <div class="spinner"></div>
      <p class="loader-text">Loading data...</p>
    </div>
  `;
}



 
  const toast = document.getElementById('dashboardToastMessage');
  const toastBody = document.getElementById('toastBody');
  const closeBtn = toast.querySelector('.toast-close');
  function showToast(message, type = 'success', delay = 3000) { 
    toastBody.textContent = message;
    toast.className = 'toast show';
    if (type) toast.classList.add(type);
    setTimeout(() => {
    hideToast();
    }, delay);
    }
    function hideToast() {
    toast.classList.remove('show');
    }
    closeBtn.addEventListener('click', hideToast);



function fetchData(url, mode,modalInset) {
  console.log(url)
  fetch(url)
  .then(res => {
    
    if (!res.ok){
      if (res.status===403){
          //Close Create Modal for Error 403
          const modal = document.querySelector('.modal-frame');
          const overlay = document.querySelector('.modal-overlay');
          closeModal(modal, overlay);
          // Trigger Toast
          showToast('You do not have permission to do this action', 'error');
      }   
    }
    return res.json()
  })
  .then(result => {
      // console.log(result)
      // const parsed = JSON.parse(result.data);
      const parsed = JSON.parse(result.data);
      // const post = parsed[0].fields;
      // console.log(parsed)
      const post = parsed
      const categories = result.categories;
      const authors = result.authors;
      
      if(mode ==='add'){
        renderCreate(categories,url);
      }
      if (mode === 'view') {
        renderView(post);
      }if (mode === 'edit') {
        renderEdit(post,categories,authors,url);
      }
      if (mode === 'trash'){
        modalInset.classList.add('trash-mode');
        renderTrash(post,url);
      }
    
  })
  .catch(err => console.error(err));
}




function renderCreate(categories,url) {
  const TOKEN_VALUE = window.CSRF_TOKEN;
  
  document.querySelector('.modal-body').innerHTML = `
  <form class="createPostsForm" action="${url}" method="POST" enctype="multipart/form-data">
    <input type="hidden" name="csrfmiddlewaretoken" value="${TOKEN_VALUE}">
    <div class="post-modal-content">

      <!-- TOP ROW -->
      <div class="editor-top">

        <!-- LEFT: Image -->
        <div class="editor-left">
          <div id="blog-image-container" class="image-uploader">
            <div class="image-preview">
              <img id="blog-image" src="/media/golden_burst.jpg" alt="featured_image">
            </div>
            
            <div class="image-actions">
              <label for="avatar-upload" class="upload-btn">Upload Image</label>
              <input type="file" id="avatar-upload" name="featured_image" accept="image/png,image/jpeg" hidden/>
              <small class="upload-hint">PNG or JPG • Max 5MB</small>
            </div>
          </div>
        </div>

        <!-- RIGHT: Title / Status / Description -->
        <div class="editor-right">
          <div class="field-group">
            <label>Title</label>
            <input type="text" name="postTitle" value="">
          </div>

          <div class="field-group">
            <label>Status</label>
            <select name="postStatus" class="status-select">
              <option value="Draft" selected>Draft</option>
              <option value="Published">Published</option>
            </select>
          </div>

          <div class="field-group">
            <label>Category</label>
            <select name="postCategory" class="status-select">
              ${categories.map(c => `<option value="${c.id}">${c.category_name}</option>`).join('')}
            </select>
          </div>

          <div class="field-group">
            <label>Feature this Post?</label>
            <select name="isFeatured" class="status-select">
              <option value="True" >True</option>
              <option value="False" selected>False</option>
              
            </select>
          </div>

          

        </div>
      </div>

      <!-- BOTTOM ROW -->
      <div class="field-group description-group">
        <label>Description</label>
        <textarea class="blog-desc" name="postDesc"></textarea>
      </div>

      <div class="field-group">
        <label>Content</label>
        <textarea class="content" name="postBody"></textarea>
      </div>

      <div class="create-actions">
        <input type="submit" value="Create Post" class="create"/>
        <input type="button" value="Cancel" class="cancel-create"/>
      </div>

    </div>
  </form>
  `;

  // Handle image preview
  const BlogImage = document.getElementById('blog-image');
  const inputPicture = document.getElementById('avatar-upload');
  inputPicture.onchange = function() {
    if (inputPicture.files && inputPicture.files[0]) {
      BlogImage.src = URL.createObjectURL(inputPicture.files[0]);
    }
  };
  
  // Handle form submission
  document.querySelector('.createPostsForm').addEventListener('submit', function(e){
    e.preventDefault();
    const form = this;
    const url = form.action;
    const formData = new FormData(form);

    fetch(url, {
      method: 'POST',
      body: formData
    })
    .then(res => {
      if (!res.ok) {
        console.error('Fetch failed');
      }
      return res.json();
    })
    .then(result => {
      console.log(result); // DEBUG: ensure result.data exists

      // Close modal
      const modal = document.querySelector('.modal-frame');
      const overlay = document.querySelector('.modal-overlay');
      closeModal(modal, overlay);

      
      //reloads the page
      setTimeout(() => window.location.reload(), 1000);

      // SweetAlert success
      Swal.fire({
        title: 'Success',
        text: 'Post Created Successfully!',
        icon: 'success',
        confirmButtonText: 'Confirm'
      });
    })
    .catch(err => console.error(err));
  });

  
  //Handle Cancel
  const cancel = document.querySelector('.cancel-create').addEventListener('click',(e) =>{
    const modal = document.querySelector('.modal-frame');
    const overlay = document.querySelector('.modal-overlay');
    closeModal(modal,overlay); //Closing the Modal

    Swal.fire({
      title: 'Create Post Cancelled',
      text: 'Your post is not created',
      icon: 'error',
      confirmButtonText: 'Confirm'
    })
  });
}


function renderView(post) {
  // console.log(post)
  document.querySelector('.modal-body').innerHTML = `
    <div class="post-modal-content view-mode">
    
      <!-- TOP ROW -->
      <div class="editor-top">

          <!-- LEFT: Image -->
          <div class="editor-left">
              <div class="image-preview">
                  <img src="/media/${post.featured_image}" alt="${post.title}">
              </div>
          </div>

          <!-- RIGHT: Title / Status -->
          <div class="editor-right">

              <header class="post-header view-header">
                  <h3>${post.title}</h3>

                  <span class="post-status ${post.status.toLowerCase()}">
                      ${post.status}
                  </span>
                  <p>
                      <strong>Category:</strong> <br /> <br />
                       ${post.category__category_name}
                  </p>

                  <p>
                      <strong>Posted By:</strong> <br /> <br />
                      ${post.author__first_name} ${post.author__last_name}
                  </p>
              </header>

          </div>
      </div>

      <!-- DESCRIPTION (ABOVE CONTENT) -->
      <div class="editor-bottom view-section">
          <h4>Description</h4>
          <br />
          <p class="view-text">${post.short_description}</p>
      </div>

      <!-- CONTENT -->
      <div class="editor-bottom view-section">
          <h4>Content</h4>
          <br />
          <p class="view-text content-text">${post.blog_body}</p>
      </div>
  </div>
  `;
}


function renderEdit(post,categories,authors,url) {
  var TOKEN_VALUE = window.CSRF_TOKEN
  document.querySelector('.modal-body').innerHTML = `
  <form class="editPostsForm" action= "${url}" method="POST" enctype="multipart/form-data">
  <input type="hidden" name="csrfmiddlewaretoken" value=${TOKEN_VALUE}>
    <div class="post-modal-content">

      <!-- TOP ROW -->
      <div class="editor-top">

        <!-- LEFT: Image -->
        <div class="editor-left">
          <div id="blog-image-container" class="image-uploader">
            <div class="image-preview">
              <img id="blog-image" src="/media/${post.featured_image}" alt="${post.title}">
            </div>

            <div class="image-actions">
              <label for="avatar-upload" class="upload-btn">Change Image</label>

              <input
                type="file"
                id="avatar-upload"
                name="featured_image"
                accept="image/png,image/jpeg"
                hidden
              />
              <small class="upload-hint">PNG or JPG • Max 5MB</small>
            </div>
          </div>
        </div>

        <!-- RIGHT: Title / Status / Description -->
        <div class="editor-right">

          <header class="post-header">
            <div class="field-group">
              <label>(Edit Title)</label>
              <input type="text" name="postTitle" value="${post.title}">
            </div>

            <div class="field-group">
              <label for="status-select">(Select Status)</label>
              <select id="status-select" name="postStatus" class="status-select">
                <option value="Draft" ${post.status === 'Draft' ? 'selected' : ''
                 }>Draft</option>
                <option value="Published" ${post.status === 'Published' ? 'selected' : ''}>Published</option>
              </select>
            </div>

            
            <!--
            !!!!!NOTE:!!!!! 
            To render currentSeleted data for current category_id as post.category and currentSeleted data for current author User_id include the category and author to the blog object that will be fetch so that we can get its ids.

            see dashboard/views.py def get_data() for reference of qs object.
            -->


            <div class="field-group">
              <label>(Select Category)</label>
              <select name="postCategory" class="status-select">
                ${categories.map(c => `
                  <option value="${c.id}" ${c.id === post.category ? 'selected' : `${post.category}`}>${c.category_name}</option>
                `).join('')}
              </select>
            </div>
                  
            <div class="field-group">
              <label>(Select Author)</label>
              <select name="postAuthor" class="status-select">
                ${authors.map(a => `
                  <option value="${a.id}" ${a.id === post.author ? 'selected' : `${post.author}`}>${a.first_name} ${a.last_name}</option>
                `).join('')}
              </select>
            </div>

          </header>

          <div class="field-group description-group">
            
          </div>

        </div>
      </div>

      <!-- BOTTOM ROW -->
      <div class="editor-bottom field-group">
        <label>(Edit Description)</label>
            <textarea class="blog-desc" name="postDesc">${post.short_description}</textarea>
      </div>

      <div class="editor-bottom field-group">
        <label>(Edit Content)</label>
        <textarea class="content" name="postBody">${post.blog_body}</textarea>
      </div>


      

      <div class="create-actions">
        <input type="submit" value="Save Changes"/class="create"/>
        <input type="button" value="Cancel" class="cancel-create"/>
      </div>
    </div>
  </form>
  `;

  // Avatar Picture Loading and Update 
  let BlogImage = document.getElementById('blog-image');
  let inputPicture = document.getElementById('avatar-upload');
  inputPicture.onchange = function () {
      if (inputPicture.files && inputPicture.files[0]) {
          BlogImage.src = URL.createObjectURL(inputPicture.files[0]);
      }
  };


  /*Handle Form Submission*/ 
  document.querySelector('.editPostsForm').addEventListener('submit',function(e){
    e.preventDefault();
    
    
    // IMPORTANT NOTE:
    /* for POST form Submission action is very crucial and it should hold the url-<Id> of the payload destination to the backend so that the backend should get the specific ID where the POST/PUT/DELETE/UPDATE will APPLY 
    
    Follow Form composition above for POST request

    BUG ENCOUNTERED: IF the action= "<url-id>" is not specified correctly there is a tendency that the update will not applied to correct target ID

    e.g POST for ID-5 
    the POST will be applied by backend the PK-1


    🔑 Key principle (THIS is the rule)
    - Django determines pk ONLY from the URL.
    - NOT from POST data.
    - NOT from JavaScript variables.

    */ 
    const form = this
    const url = form.action;
    const formData = new FormData(this)

    fetch(url, {
                method: "POST",
                body: formData
            })
            // .then(res =>res.json())  //NOTE: instead of direct conversion of json to javascript readable object that expects a promise output that is why we have a follow up .then line to fetch the promised output which is the data --> USE THE GUARD CLAUSE METHOD

            //(THIS IS A MUST: GUARD CLAUSE)
            .then(res => {
              if (!res.ok){
                if (res.status===403){
                  //Close Create Modal for Error 403
                  const modal = document.querySelector('.modal-frame');
                  const overlay = document.querySelector('.modal-overlay');
                  closeModal(modal, overlay);
                  // Trigger Toast
                  showToast('You do not have permission to do this action', 'error');
              }   
              } // NOTE: IF THE FETCH is not ok for example 404 or 500 the fetch is still completed but the address is unreachable this process stops here and return the console.log()

              return res.json() // if the address is reachable it return the res.json() which is the JS readable object
            })
            
            .then(result =>{
              // Close modal -- CALL DEFINE  closeModal(modal,overlay) ABOVE
              const modal = document.querySelector('.modal-frame');
              const overlay = document.querySelector('.modal-overlay');
              
              closeModal(modal,overlay);//CLosing the Modal
              

              setTimeout(() => {
                  window.location.reload();
              }, 1000);// Wait 2 seconds to show the message and reload the page


              //SWEET ALERT UPDATE CONFIRMATION
              Swal.fire({
                title: 'Success',
                text: 'Post Successfully Updated!',
                icon: 'success',
                confirmButtonText: 'Confirm'
              })
            })
            
            .catch(error =>{
              console.error(error)
            })
  });

  //Handle Cancel
  const cancel = document.querySelector('.cancel-create').addEventListener('click',(e) =>{
    const modal = document.querySelector('.modal-frame');
    const overlay = document.querySelector('.modal-overlay');
    closeModal(modal,overlay); //Closing the Modal

    Swal.fire({
      title: 'Edit Post Cancelled',
      text: 'No changes applied to the post',
      icon: 'error',
      confirmButtonText: 'Confirm'
    })
  });

}


function renderTrash(post,url){
  document.querySelector('.modal-body').innerHTML = `
    <div class="delete-modal-content">

    <div class="delete-header">
      <h3>Delete Post??</h3>
    </div>

    <div class="delete-body">
      <p>
        Are you sure you want to delete this post?
        <br>
        <strong><span class="reminder">Reminder :</span> This action cannot be undone.</strong>
      </p>
    </div>

    <div class="delete-actions">
      <button id="DeletePost" class="btn btn-danger">
        Delete
      </button>

      <button class="btn btn-secondary cancel-delete">
        Cancel 
      </button>
    </div>
  </div>
  `

  /*Tried to refactor this as function base but in this layout is not possible since we are only creating the modal content when the renderTrash is initialize. If we do a stand alone function that selects the 'cancel-delete' to trigger an event listener it will return an Error as
  
  ERROR: 
  script.js:904 Uncaught TypeError: Cannot read properties of null (reading 'addEventListener')
  
  Solution: include the EventListener to the template so that if the templates loaded it will read the class cancel-delete since it is now present.
  */

  //Handle Deletion
  var TOKEN_VALUE = window.CSRF_TOKEN
  const deleteAction = document.getElementById('DeletePost').addEventListener ('click',(e) =>{
      
      fetch(`${url}`, {
          method: "DELETE",
          headers: {
          'X-CSRFToken': TOKEN_VALUE,
          'Content-Type': 'application/json'}

      })
      .then(res => {
        if(!res.ok){
          if (res.status===403){
          //Close Create Modal for Error 403
          const modal = document.querySelector('.modal-frame');
          const overlay = document.querySelector('.modal-overlay');
          closeModal(modal, overlay);
          // Trigger Toast
          showToast('You do not have permission to do this action', 'error');
          }   
        }
        return res.json()
      })
      .then(data => {
        console.log(data)
        const modal = document.querySelector('.modal-frame');
        const overlay = document.querySelector('.modal-overlay');
        closeModal(modal,overlay);//CLosing the Modal


        //RELOAD PAGE
        setTimeout(() => {
            window.location.reload();
        }, 1000);// Wait 2 seconds to show the message and reload the page

        //SWEET ALERT CONFIRMATION
        Swal.fire({
        title: 'Successful',
        text: 'Delete Post Successfully',
        icon: 'success',
        confirmButtonText: 'Confirm'
      })
    });
  });

  //Handle Cancel
  const cancel = document.querySelector('.cancel-delete').addEventListener('click',(e) =>{
    const modal = document.querySelector('.modal-frame');
    const overlay = document.querySelector('.modal-overlay');
    closeModal(modal,overlay);//CLosing the Modal

    Swal.fire({
      title: 'Delete Action Cancelled',
      text: 'No changes applied to the post',
      icon: 'error',
      confirmButtonText: 'Confirm'
    })
  });
}


//Batch Delete
function renderBatchTrash(){
  console.log()
  const selectedIds = [...document.querySelectorAll('.check:checked')]
    .map(cb => cb.value);

  document.querySelector('.modal-body').innerHTML = `
    <div class="delete-modal-content">

    <div class="delete-header">
      <h3>Delete ${selectedIds.length} posts?</h3>
    </div>
  
    <div class="delete-body">
      <p>
        Are you sure you want to delete this post?
        <br>
        <strong><span class="reminder">Reminder :</span> This action cannot be undone.</strong>
      </p>
    </div>

    <div class="delete-actions">
      <button id="DeletePost" class="btn btn-danger">
        Delete
      </button>

      <button class="btn btn-secondary cancel-delete">
        Cancel 
      </button>
    </div>
  </div>
  `

  
  var TOKEN_VALUE = window.CSRF_TOKEN
  const deleteAction = document.getElementById('DeletePost');
  const deleteTrigger = document.querySelector('.modal-trigger');
  const url = deleteTrigger.dataset.url

  deleteAction.addEventListener ('click',(e) =>{
    
    const selectedIds = [...document.querySelectorAll('.check:checked')]
      .map(cb => cb.value);

    if (!selectedIds.length) return;

    
    fetch(url, {
        method: 'POST',
        headers: {
          'X-CSRFToken': TOKEN_VALUE,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ids: selectedIds })
    })
    .then(res =>{
      if(!res.ok){
          if (res.status===403){
          //Close Create Modal for Error 403
          const modal = document.querySelector('.modal-frame');
          const overlay = document.querySelector('.modal-overlay');
          closeModal(modal, overlay);
          // Trigger Toast
          showToast('You do not have permission to do this action', 'error');
          }   
        }
        return res.json()
      })
  
    .then(data => {
      // remove rows from DOM
      selectedIds.forEach(id => {
        document.querySelector(`[data-row-id="${id}"]`)?.remove();
      });

      const modal = document.querySelector('.modal-frame');
        const overlay = document.querySelector('.modal-overlay');
        closeModal(modal,overlay);//CLosing the Modal


        //RELOAD PAGE
        setTimeout(() => {
            window.location.reload();
        }, 1000);// Wait 2 seconds to show the message and reload the page

        //SWEET ALERT CONFIRMATION
        Swal.fire({
        title: 'Successful',
        text: 'Delete Post Successfully',
        icon: 'success',
        confirmButtonText: 'Confirm'
      })
    });
  });

  //Handle Cancel
  const cancel = document.querySelector('.cancel-delete').addEventListener('click',(e) =>{
    const modal = document.querySelector('.modal-frame');
    const overlay = document.querySelector('.modal-overlay');
    closeModal(modal,overlay);//CLosing the Modal

    Swal.fire({
      title: 'Delete Action Cancelled',
      text: 'No changes applied to the selected posts',
      icon: 'error',
      confirmButtonText: 'Confirm'
    })
  });
};


