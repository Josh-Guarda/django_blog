document.addEventListener('DOMContentLoaded', () => {

    const modalElement = document.getElementById('staticBackdrop');
    const modalBody = document.querySelector('#staticBackdrop .modal-body');
    const modalTitle = document.querySelector('#staticBackdropLabel');

    const bootstrapModal = new bootstrap.Modal(modalElement);

    document.addEventListener('click', e => {
        console.log('Modal trigger clicked');
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
    
    const isSave = action === 'save';

    modalTitle.textContent = isSave ? 'Save this post?' : 'Remove from saved?';

    modalBody.innerHTML = `
        <div class="save-post-icon mb-3 ${isSave ? 'icon-save' : 'icon-remove'}">
            <i class="fa-${isSave ? 'regular' : 'solid'} fa-bookmark"></i>
        </div>
        <p class="text-muted mb-0 px-3">
            ${isSave
                ? 'This post will be added to your saved library.'
                : 'This post will be removed from your saved library.'}
        </p>
    `;

    // IMPORTANT: replace footer buttons (clean control)
    const footer = document.querySelector('#staticBackdrop .modal-footer');

    footer.innerHTML = `
        <button type="button" class="btn btn-outline-secondary px-4" data-bs-dismiss="modal">
            Cancel
        </button>
        <button type="button" class="btn ${isSave ? 'btn-primary' : 'btn-danger'} px-4" id="confirmSave">
            ${isSave ? 'Save' : 'Remove'}
        </button>
    `;

    bootstrapModal.show();

    document.getElementById('confirmSave').onclick = () => {
        const confirmBtn = document.getElementById('confirmSave');
        confirmBtn.disabled = true;
        confirmBtn.innerHTML = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>Processing...`;

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
            confirmBtn.disabled = false;
            confirmBtn.textContent = 'Try Again';
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