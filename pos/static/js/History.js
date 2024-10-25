const clearSearch = () => {
    document.getElementById('order_id').value = ''; 
    document.getElementById('date').value = '';
    window.location.assign('/history?page=1');
};