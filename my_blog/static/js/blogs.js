// import { openModal, closeModal, showToast} from './script.js';

// document.addEventListener('DOMContentLoaded', () => {

// const modal = document.querySelector('.modal-frame-blog');
// const overlay = document.querySelector('.modal-overlay-blog');
// const modalInset = document.querySelector('.modal-inset-blog');
// const modalBody = document.querySelector('.modal-body-blog');
// // const modal = document.querySelector('.modal-frame');
// // const overlay = document.querySelector('.modal-overlay');
// // const modalInset = document.querySelector('.modal-inset');
// // const modalBody = document.querySelector('.modal-body');


// console.log('modal:', modal);           // check if modal is null
// console.log('overlay:', overlay);       // check if overlay is null
// console.log('modalInset:', modalInset); // check if modalInset is null
// console.log('modalBody:', modalBody);   // check if modalBody is null

// // handle save/unsave button clicks directly
// document.addEventListener('click', e => {
    
//     const trigger = e.target.closest('.bookmark-btn');
//     if (!trigger) return;

//     e.preventDefault();

//     console.log('bookmark clicked');        // check if click is detected
//     console.log('modal:', modal);           // check if modal is null
//     console.log('overlay:', overlay);       // check if overlay is null
//     console.log('modalInset:', modalInset); // check if modalInset is null
//     console.log('modalBody:', modalBody);   // check if modalBody is null


//     const action = trigger.dataset.action;   // 'save' or 'unsave'
//     // const postId = trigger.dataset.postId;   // post id
//     const url = trigger.dataset.url
    
  
//     openModal(modal, overlay, modalInset);
//     renderSaveConfirm(action, url);


//     // Close modal
//     document.addEventListener('click', e => {
//     if (e.target.closest('.close') || e.target === overlay) {
//         closeModal(modal, overlay);
//     }
//     });
// });


// function openModal(modal, overlay, modalInset) {
//     console.log('Opening modal...');
  
//   // if (localStorage.getItem('darkMode') === 'enabled') {
//   //   modalInset.classList.add('dark');
//   // } else {
//   //   modalInset.classList.remove('dark');
//   // }
  
//   overlay.classList.add('state-show');
//   modal.classList.remove('state-leave');
//   modal.classList.add('state-appear');
//   modal.style.display = 'flex';
// }

// function closeModal(modal, overlay) {
//   overlay.classList.remove('state-show');
//   modal.classList.remove('state-appear');
//   modal.classList.add('state-leave');

//   modal.addEventListener('animationend', function handler() {
//     modal.classList.remove('state-leave');
//     modal.style.display = 'none';
//     modal.removeEventListener('animationend', handler);
//   });
// }

// function renderSaveConfirm(action, url) {
//     console.log(modalBody)
//     // modalBody.innerHTML = `
//     // <h1>POGI AKO</h1>
//     // `;

//     modalBody.innerHTML = `
//         <div style="text-align:center; padding: 20px;">
//             <h3>${action === 'save' ? 'Save this post?' : 'Remove from saved?'}</h3>
//             <p class="text-muted">${action === 'save'
//                 ? 'This post will be added to your saved library.'
//                 : 'This post will be removed from your saved library.'
//             }</p>
//             <div style="display:flex; gap:10px; justify-content:center; margin-top:20px;">
//                 <button class="btn-primary" id="confirmSave">
//                     ${action === 'save' ? 'Save' : 'Remove'}
//                 </button>
//                 <button class="btn-danger" id="cancelSave">Cancel</button>
//             </div>
//         </div>
//     `;

//     // confirm button
//     document.getElementById('confirmSave').addEventListener('click', () => {
//         fetch(`/save/${postId}/`, {
//             method: 'POST',
//             headers: {
//                 'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
//             }
//         })
//         .then(res => res.json())
//         .then(result => {
//             closeModal(modal, overlay);
//             showToast(result.message, 'success');
//             setTimeout(() => {
//                 window.location.reload();
//             }, 1000);
//         })
//         .catch(err => {
//             console.error(err);
//             showToast('Something went wrong', 'error');
//         });
//     });

//     // cancel button
//     document.getElementById('cancelSave').addEventListener('click', () => {
//         closeModal(modal, overlay);
//     });
//     }      
// });

document.addEventListener('DOMContentLoaded', () => {

    const modalElement = document.getElementById('staticBackdrop');
    const modalBody = document.querySelector('#staticBackdrop .modal-body');
    const modalTitle = document.querySelector('#staticBackdropLabel');

    const bootstrapModal = new bootstrap.Modal(modalElement);

    document.addEventListener('click', e => {

        const trigger = e.target.closest('.bookmark-btn');
        if (!trigger) return;

        e.preventDefault();

        const action = trigger.dataset.action;
        const url = trigger.dataset.url;
        const postId = trigger.dataset.postId;

        renderSaveConfirm(action, url, postId, modalBody, modalTitle, bootstrapModal);
    });
});


function renderSaveConfirm(action, url, postId, modalBody, modalTitle, bootstrapModal) {

    modalTitle.textContent =
        action === 'save' ? 'Save Post' : 'Remove Saved Post';

    modalBody.innerHTML = `
        <div class="text-center">
            <p>
                ${action === 'save'
                    ? 'Do you want to save this post?'
                    : 'Do you want to remove this post from saved?'}
            </p>
        </div>
    `;

    // IMPORTANT: replace footer buttons (clean control)
    const footer = document.querySelector('#staticBackdrop .modal-footer');
                  
    footer.innerHTML = `
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
            Cancel
        </button>
        <button type="button" class="btn btn-primary" id="confirmSave">
            ${action === 'save' ? 'Save' : 'Remove'}
        </button>
    `;

    bootstrapModal.show();

    document.getElementById('confirmSave').onclick = () => {

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            }
        })
        .then(res => res.json())
        .then(result => {

            bootstrapModal.hide();

            // optional toast
            if (typeof showToast === "function") {
                showToast(result.message, 'success');
            }

            setTimeout(() => {
                window.location.reload();
            }, 500);
        })
        .catch(err => {
            console.error(err);
            if (typeof showToast === "function") {
                showToast('Something went wrong', 'error');
            }
        });
    };
}












// import { openModal, closeModal, showLoader, showToast } from './script.js';

// document.addEventListener('DOMContentLoaded', () => {

//     const modal = document.querySelector('.modal-frame');
//     const overlay = document.querySelector('.modal-overlay');
//     const modalInset = document.querySelector('.modal-inset');
//     const modalBody = document.querySelector('.modal-body');

//     // debug
//     console.log('modal:', modal);
//     console.log('overlay:', overlay);
//     console.log('modalInset:', modalInset);
//     console.log('modalBody:', modalBody);

//     if (!modal || !overlay || !modalInset || !modalBody) {
//         console.warn('Modal elements not found.');
//         return;
//     }

//     document.addEventListener('click', e => {
//         const trigger = e.target.closest('.bookmark-btn');
//         if (!trigger) return;

//         e.preventDefault();

//         const action = trigger.dataset.action;
//         const url = trigger.dataset.url;

//         console.log('clicked action:', action);
//         console.log('clicked url:', url);

//         openModal(modal, overlay, modalInset);
//         renderSaveConfirm(action, url, modal, overlay, modalBody);
//     });

//     function renderSaveConfirm(action, url, modal, overlay, modalBody) {
//         modalBody.innerHTML = `
//             <div style="text-align:center; padding: 20px;">
//                 <h3>${action === 'save' ? 'Save this post?' : 'Remove from saved?'}</h3>
//                 <p>${action === 'save'
//                     ? 'This post will be added to your saved library.'
//                     : 'This post will be removed from your saved library.'
//                 }</p>
//                 <div style="display:flex; gap:10px; justify-content:center; margin-top:20px;">
//                     <button class="btn-primary" id="confirmSave">
//                         ${action === 'save' ? 'Save' : 'Remove'}
//                     </button>
//                     <button class="btn-danger" id="cancelSave">Cancel</button>
//                 </div>
//             </div>
//         `;

//         document.getElementById('confirmSave').addEventListener('click', () => {
//             fetch(url, {
//                 method: 'POST',
//                 headers: {
//                     'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
//                 }
//             })
//             .then(res => res.json())
//             .then(result => {
//                 closeModal(modal, overlay);
//                 showToast(result.message, 'success');
//                 setTimeout(() => {
//                     window.location.reload();
//                 }, 1000);
//             })
//             .catch(err => {
//                 console.error(err);
//                 showToast('Something went wrong', 'error');
//             });
//         });

//         document.getElementById('cancelSave').addEventListener('click', () => {
//             closeModal(modal, overlay);
//         });
//     }

// }); // end DOMContentLoaded