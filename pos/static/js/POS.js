async function printDiv(divId) {
    const printContents = document.getElementById(divId).innerHTML;
    let printWindow = window.open('', '', 'height=1000, width=1000');
    printWindow.document.open();
    printWindow.document.write(`
        <html>
        <head>  
            <style>
                body { font-family: Arial, sans-serif; }
                h1 { color: #333; }
                #cartItems {
                    height: auto;
                    margin: 15px 0px;
                }
            </style>
            <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body>
            ${printContents}
        </body>
        </html>
    `);

    await new Promise(resolve => setTimeout(resolve, 500));
    printWindow.print();
    printWindow.document.close();
}