// Автоматичний сабміт форми при зміні чекбокса
document.querySelectorAll('input[type="checkbox"]').forEach(el => {
    el.addEventListener('change', () => el.form.submit());
});