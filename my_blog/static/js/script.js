

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
  (function () {
    var checkAll = document.querySelector('.check-all');
    var checkers = document.querySelectorAll('.check');

    if (checkAll && checkers) {
      checkAll.addEventListener('change', function (e) {
        var _iterator6 = _createForOfIteratorHelper(checkers),
            _step6;

        try {
          for (_iterator6.s(); !(_step6 = _iterator6.n()).done;) {
            var checker = _step6.value;

            if (checkAll.checked) {
              checker.checked = true;
              checker.parentElement.parentElement.parentElement.classList.add('active');
            } else {
              checker.checked = false;
              checker.parentElement.parentElement.parentElement.classList.remove('active');
            }
          }
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
            checker.parentElement.parentElement.parentElement.classList.toggle('active');

            if (!checker.checked) {
              checkAll.checked = false;
            }

            var totalCheckbox = document.querySelectorAll('.users-table .check');
            var totalChecked = document.querySelectorAll('.users-table .check:checked');

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


//MODAL SCRIPT
// document.addEventListener('DOMContentLoaded', function () {
  
//   const OpenView = document.querySelectorAll('.openView');
//   const OpenEditView = document.querySelectorAll('.openEditView');

//   // Open View modal
  
//   TriggerModal(OpenView)
  
//   });


// function TriggerModal(Trigger){
//   const modal = document.querySelector('.modal-frame');
//   const overlay = document.querySelector('.modal-overlay');
//   const modalInset = document.querySelector('.modal-inset');

//   Trigger.forEach(openBtn => {
//     openBtn.addEventListener('click', e => {
//       e.preventDefault();
//         const postUrl = openBtn.dataset.url;
//         const modalBody = document.querySelector('.modal-body');
//         // Show loader
//         modalBody.innerHTML = `
//           <div class="loader-wrapper">
//             <div class="spinner"></div>
//             <p class="loader-text">Loading user data...</p>
//           </div>
//         `;

//         //Initialize Fetch
//         fetch_data(postUrl)
//         // Apply theme to modal
//         if (localStorage.getItem('darkMode') === 'enabled') {
//           modalInset.classList.add('dark');
//         } else {
//           modalInset.classList.remove('dark');
//         }
//         overlay.classList.add('state-show');
//         modal.classList.remove('state-leave');
//         modal.classList.add('state-appear');
//         modal.style.display = 'flex'; // show modal container
//     });
//   });

//     // Close modal
//   document.querySelectorAll('.close').forEach(closeBtn => {
//     closeBtn.addEventListener('click', () => {
//     overlay.classList.remove('state-show');
//     modal.classList.remove('state-appear');
//     modal.classList.add('state-leave');

        

//       // Wait for animation to finish before hiding the container
//     modal.addEventListener('animationend', function handler() {
//       if (modal.classList.contains('state-leave')) {
//         modal.classList.remove('state-leave');
//         modal.style.display = 'none'; // hide modal container completely
//       }
//       modal.removeEventListener('animationend', handler);
//       });
//     });
//   });
// }


// function fetch_data(postUrl){
//   fetch(postUrl)
//     .then(res => res.json())
//     .then(result =>{
//       console.log(result)
//       // document.querySelector('.modal-body').innerHTML = res;
//       const parsedData = JSON.parse(result.data); // SECOND parse
//       const post = parsedData[0].fields;

//       //Creating html element to load in Modal
//       renderPostToModal(post);
//     })
//     .catch(err => console.error(err));
//   };


//   function renderPostToModal(post) {
//     const modalBody = document.querySelector('.modal-body');
//     modalBody.innerHTML = `

//       <div class="post-modal-content">
//         <header class="post-header">
//           <h3 class="post-title">${post.title}</h3>
//           <span class="post-status ${post.status.toLowerCase()}">
//             ${post.status}
//           </span>
//         </header>

//         <div class="post-image">
//           <img 
//             src="/media/${post.featured_image}" 
//             alt="${post.title}"
//           >
//         </div>

//         <section class="post-section">
//           <h4>Description</h4>
//           <p>${post.short_description}</p>
//         </section>

//         <hr>

//         <section class="post-section">
//           <h4>Content</h4>
//           <p>${post.blog_body}</p>
//         </section>

//       </div>
//     `;
//   };







document.addEventListener('DOMContentLoaded', () => {
  initModal();
});


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

    openModal(modal, overlay, modalInset);
    showLoader(modalBody);
    fetchData(url, mode);
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


function fetchData(url, mode) {
  fetch(url)
    .then(res => res.json())
    .then(result => {
      const parsed = JSON.parse(result.data);
      const post = parsed[0].fields;

      if (mode === 'view') {
        renderView(post);
      } else if (mode === 'edit') {
        renderEdit(post);
      }
    })
    .catch(err => console.error(err));
}



function renderView(post) {
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

          <!-- RIGHT: Title / Status / Description -->
          <div class="editor-right">

              <header class="post-header view-header">
                  <h3>${post.title}</h3>
                  <span class="post-status ${post.status.toLowerCase()}">
                      ${post.status}
                  </span>
              </header>

              <div class="view-section">
                  <h4>Description</h4>
                  <br />
                  <p class="view-text">${post.short_description}</p>
              </div>

          </div>
      </div>

      <!-- BOTTOM ROW -->
      <div class="editor-bottom view-section">
          <h4>Content</h4>
          <br />
          <p class="view-text content-text">${post.blog_body}</p>
      </div>
  </div>

  `;
}


function renderEdit(post) {
  var TOKEN_VALUE = window.CSRF_TOKEN
  // console.log(window.CSRF_TOKEN)
  document.querySelector('.modal-body').innerHTML = `
  <form class="editPostsForm" method="POST" enctype="multipart/form-data">
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
                name="featuredImage"
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
              <input type="text" value="${post.title}">
            </div>

            <div class="field-group">
              <label for="status-select">(Select Status)</label>
              <select id="status-select" class="status-select">
                <option value="Draft" ${post.status === 'Draft' ? 'selected' : ''}>Draft</option>
                <option value="Published" ${post.status === 'Published' ? 'selected' : ''}>Published</option>
              </select>
            </div>
          </header>

          <div class="field-group description-group">
            <label>(Edit Description)</label>
            <textarea class="blog-desc">${post.short_description}</textarea>
          </div>

        </div>
      </div>

      <!-- BOTTOM ROW -->
      <div class="editor-bottom field-group">
        <label>(Edit Content)</label>
        <textarea class="content">${post.blog_body}</textarea>
      </div>


      <input type="submit" value="Save Changes"/>
    </div>
  </form>
  `;

  // Avatar Picture Loading and Update 
  let BlogImage = document.getElementById('blog-image');
  // set initial src
  // BlogImage.src = data.profile_picture
      // ? `/static/uploads/avatars/${data.BlogImage}`
      // : `/static/builtin/icons/person.png`;
  let inputPicture = document.getElementById('avatar-upload');

  inputPicture.onchange = function () {
      if (inputPicture.files && inputPicture.files[0]) {
          BlogImage.src = URL.createObjectURL(inputPicture.files[0]);
      }
  };


  /*Handle Form Submission*/ 
  document.querySelector('.editPostsForm').addEventListener('submit',function(e){
    e.preventDefault();
    console.log()
    const formData = new FormData(this)
    console.log(formData)

    const trigger = document.querySelector('.modal-trigger');
    const url = trigger.dataset.url;
    console.log(url)
    fetch(url, {
                method: "POST",
                body: formData
            })
            .then(res => res.json())  
            .then(result => {
                console.log(result);
             })
  })
}

