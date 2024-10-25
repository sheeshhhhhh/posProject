
const monthSelector = document.getElementById('month-selector');

let pieChart;
let barChart;

// ref: https://stackoverflow.com/questions/24875414/addeventlistener-change-and-option-selection
monthSelector.addEventListener('change', (e) => {
    pieChart.destroy();
    barChart.destroy();
    getData(monthSelector.value)
})

const getData = async (month=undefined) => {
    let url = '/api/dashboard/';

    if (month) {
        url = `/api/dashboard/?month=${month}`;
    }

    const response = await fetch(url);
    const data = await response.json().then((data) => {

        // PIE CHART
        const dashboard = data.dashboardmonth
        const piectx = document.getElementById('pieChart');
        const header = document.getElementById('month-dashboard');
        const total = document.getElementById('month-total')
        header.innerHTML = `Statistic for ${dashboard.month}`
        monthSelector.value = dashboard.month
        total.innerHTML = `Total: ${dashboard.total}`

        pieChart = new Chart(piectx, {
            type: 'pie',
            data: {
                labels: ['Tax', 'Sub Total'], 
                datasets: [{
                    label: 'Tax, Sub Total and Total',
                    data: [dashboard.totalTax, dashboard.totalSub],
                    backgroundColor: ['#3b82f6','#1e3a8a'],
                    borderColor: ['#3b82f6', '#1e3a8a'],
                    borderWidth: 1
                }]
            }
        })
    
    
        // BAR CHART
        const months = data.data.map((item) => item.month)
        const revenue = data.data.map((item) => item.totalRevenue)
        const tax = data.data.map((item) => item.totalTax)
        const barctx = document.getElementById('barChart');
        barChart = new Chart(barctx, {
          type: 'bar',
          data: {
            labels: months,
            datasets: [ {
                label: 'Revenue',
                data: revenue, 
                borderColor: '#1e3a8a', 
                backgroundColor: '#1e3a8a',
                fill: true, 
                tension: 0.1 
            },
            {
                label: 'Tax VAT(12%)',
                data: tax,
                borderColor: '#3b82f6', 
                backgroundColor: '#3b82f6', 
                fill: true, 
                tension: 0.1 
            }]
          },
          options: {
            scales: {
              y: {
                beginAtZero: true
              }
            }
          }
    });
    });
}

getData();