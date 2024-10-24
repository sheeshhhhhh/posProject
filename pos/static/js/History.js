
const Url = new URL(window.location.href);
let page = Url.searchParams.get('page') 

if (!page) {
    window.location.assign('/history?page=1');
}

if (page == 1) {
    document.getElementById('prev').disabled = true;
}

const clearSearch = () => {
    document.getElementById('order_id').value = ''; 
    document.getElementById('date').value = '';
    window.location.assign('/history');
}


const nextPage = () => {

    window.location.assign('/history?page=' + (parseInt(page) + 1));
}

const prevPage = () => {

    if (page == 1) {
        return 
    }

    window.location.assign('/history?page=' + (parseInt(page) - 1));
}