
const clearSearch = () => {
    document.getElementById('order_id').value = ''; 
    document.getElementById('date').value = '';
    window.location.assign('/history');
}

const nextPage = () => {
    const Url = new URL(window.location.href);
    const page = Url.searchParams.get('page')

    window.location.assign('/history?page=' + (parseInt(page) + 1));
}