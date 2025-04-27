document.addEventListener('DOMContentLoaded', function() {
    const clienteTable = document.querySelector('#cliente-table');
    
    if (clienteTable) {
        clienteTable.addEventListener('click', async function(e) {
            // Delete functionality
            if (e.target.classList.contains('btn-danger')) {
                const row = e.target.closest('tr');
                const clienteId = row.dataset.id;
                
                if (confirm('¿Está seguro de eliminar este cliente?')) {
                    const deleted = await deleteRecord('/clientes/', clienteId);
                    if (deleted) {
                        row.remove();
                        const alert = document.createElement('div');
                        alert.className = 'alert alert-success alert-dismissible fade show';
                        alert.innerHTML = `
                            Cliente eliminado exitosamente
                            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                        `;
                        document.querySelector('.container').insertBefore(alert, clienteTable);
                    }
                }
            }
            
            // Edit functionality
            if (e.target.classList.contains('btn-warning')) {
                e.preventDefault();
                const row = e.target.closest('tr');
                const clienteId = row.dataset.id;
                const editUrl = e.target.href;

                try {
                    const response = await fetch(editUrl, {
                        headers: {
                            'X-Requested-With': 'XMLHttpRequest'
                        }
                    });
                    
                    if (!response.ok) throw new Error('Error al cargar el formulario');
                    
                    const data = await response.json();
                    const modal = document.querySelector('#clienteModal');
                    modal.querySelector('.modal-title').textContent = 'Editar Cliente';
                    modal.querySelector('form').action = editUrl;
                    modal.querySelector('.modal-body').innerHTML = data.form;
                    
                    const bsModal = new bootstrap.Modal(modal);
                    bsModal.show();
                } catch (error) {
                    console.error('Error:', error);
                    window.location.href = editUrl;
                }
            }
        });

        // Form submission handler
        const modalForm = document.querySelector('#clienteModal form');
        if (modalForm) {
            const modalElement = document.querySelector('#clienteModal');
            const modal = new bootstrap.Modal(modalElement);
            let hasValidationErrors = false;

            const emailInput = modalForm.querySelector('[name="email"]');
            const telefonoInput = modalForm.querySelector('[name="telefono"]');
            
            // Función para validar campo
            async function validateField(field, value) {
                try {
                    const response = await fetch(`/clientes/validate/?field=${field}&value=${value}`);
                    const data = await response.json();
                    
                    const input = modalForm.querySelector(`[name="${field}"]`);
                    const feedbackDiv = input.nextElementSibling || document.createElement('div');
                    
                    if (!input.nextElementSibling) {
                        feedbackDiv.className = 'invalid-feedback';
                        input.parentNode.appendChild(feedbackDiv);
                    }
                    
                    if (!data.valid) {
                        input.classList.add('is-invalid');
                        input.classList.remove('is-valid');
                        feedbackDiv.textContent = data.message;
                    } else {
                        input.classList.remove('is-invalid');
                        input.classList.add('is-valid');
                        feedbackDiv.textContent = '';
                    }
                    
                    return data.valid;
                } catch (error) {
                    console.error('Error:', error);
                    return true; // En caso de error, permitimos continuar
                }
            }
            
            // Validar email mientras se escribe
            let emailTimeout;
            emailInput.addEventListener('input', function() {
                clearTimeout(emailTimeout);
                emailTimeout = setTimeout(() => {
                    if (this.value) {
                        validateField('email', this.value);
                    }
                }, 500); // Esperar 500ms después de que el usuario deje de escribir
            });
            
            // Validar teléfono mientras se escribe
            let telefonoTimeout;
            telefonoInput.addEventListener('input', function() {
                clearTimeout(telefonoTimeout);
                telefonoTimeout = setTimeout(() => {
                    if (this.value) {
                        validateField('telefono', this.value);
                    }
                }, 500);
            });
            
            // Validar antes de enviar
            modalForm.addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const emailValid = await validateField('email', emailInput.value);
                const telefonoValid = await validateField('telefono', telefonoInput.value);
                
                // Mostrar alerta de error si hay campos inválidos
                const alertDiv = modalForm.querySelector('.alert') || document.createElement('div');
                alertDiv.className = 'alert alert-danger mt-3';
                
                if (!emailValid || !telefonoValid) {
                    alertDiv.textContent = 'Por favor, corrija los errores antes de continuar.';
                    if (!modalForm.querySelector('.alert')) {
                        modalForm.insertBefore(alertDiv, modalForm.firstChild);
                    }
                    return false; // Prevenir el envío del formulario
                }
                
                // Remover alerta si todo está bien
                if (modalForm.querySelector('.alert')) {
                    modalForm.querySelector('.alert').remove();
                }
                
                const formData = new FormData(modalForm);
                
                try {
                    const response = await fetch(modalForm.action, {
                        method: 'POST',
                        body: formData,
                        headers: {
                            'X-CSRFToken': csrftoken
                        }
                    });
                    
                    const data = await response.json();
                    
                    if (data.status === 'success') {
                        window.location.reload();
                    } else {
                        alertDiv.textContent = 'Hubo un error al guardar los datos. Por favor, intente nuevamente.';
                        if (!modalForm.querySelector('.alert')) {
                            modalForm.insertBefore(alertDiv, modalForm.firstChild);
                        }
                    }
                } catch (error) {
                    console.error('Error:', error);
                    alertDiv.textContent = 'Error de conexión. Por favor, intente nuevamente.';
                    if (!modalForm.querySelector('.alert')) {
                        modalForm.insertBefore(alertDiv, modalForm.firstChild);
                    }
                }
                
                return false; // Prevenir el envío del formulario
            });

            // Prevenir que el modal se cierre si hay errores
            modalElement.addEventListener('hide.bs.modal', function(e) {
                const hasErrors = modalForm.querySelectorAll('.is-invalid').length > 0 || 
                                 modalForm.querySelector('.alert');
                if (hasErrors) {
                    e.preventDefault();
                    e.stopPropagation();
                }
            });

            // Limpiar errores cuando se abre el modal
            modalElement.addEventListener('show.bs.modal', function() {
                const invalidInputs = modalForm.querySelectorAll('.is-invalid');
                invalidInputs.forEach(input => {
                    input.classList.remove('is-invalid');
                    const feedback = input.nextElementSibling;
                    if (feedback && feedback.classList.contains('invalid-feedback')) {
                        feedback.textContent = '';
                    }
                });
                
                const alert = modalForm.querySelector('.alert');
                if (alert) {
                    alert.remove();
                }
            });
        }
    }
}); 