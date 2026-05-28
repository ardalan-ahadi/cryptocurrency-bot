// plt
// plt
function plotPriceChart(CHRT, tcoin) {
    // update: CHRT
    if (tcoin !== chrt_coin && priceChart) { priceChart.destroy(); } 
    // CHRT: stats & config
    const xaxis = CHRT.map(entry => entry.tstmp); const nvol = CHRT.map(entry => entry.nvol);
    const sopn = CHRT.map(entry => entry.sopn); const scls = CHRT.map(entry => entry.scls);
    const shgh = CHRT.map(entry => entry.shgh); const slow = CHRT.map(entry => entry.slow);
    const sprm = new Array(scls.length).fill(scls[scls.length - 1]);
    const ymin = Math.min(...slow)*.9985; const ymax = Math.max(...shgh)*1.0015;
    const vmax = Math.max(...nvol)*10;
    const data = { labels: xaxis, datasets: [
            { label: 'sopn', data: sopn, backgroundColor: 'rgba(20, 20, 250, 0.1)', borderColor: 'rgba(20, 20, 250, .5)' },
            { label: 'shgh', data: shgh, backgroundColor: 'rgba(100, 200, 250, 0.5)', borderColor: 'rgba(100, 200, 250, 1)' },
            { label: 'slow', data: slow, backgroundColor: 'rgba(100, 200, 250, 0.5)', borderColor: 'rgba(100, 200, 250, 1)' },
            { label: 'scls', data: scls, backgroundColor: 'rgba(120, 120, 250, 0.1)', borderColor: 'rgba(120, 120, 250, .5)' },
            { label: 'sprm', data: sprm, backgroundColor: 'rgba(250, 250, 250, 0.5)', borderColor: 'rgba(250, 250, 250, 1)',
                borderWidth: 1, borderDash: [20, 20], pointRadius: 0 },
            { label: 'nvol', data: nvol, backgroundColor: 'rgba(50, 150, 250, 0.5)', borderColor: 'rgba(50, 150, 250, 1)',
                type: 'bar', yAxisID: 'v', borderWidth: 1, pointRadius: 0 }] };
    const options = { responsive: true, animation: false, plugins: { legend: { display: false }, 
        zoom: { zoom: { wheel: { enabled: true }, mode: 'x' }}}, maintainAspectRatio: false,
        scales: { x: { title: { display: true, text: 'Time' }}, 
                  y: { title: { display: true, text: 'Price ($)' }, beginAtZero: false,
                       ticks: { callback: function(value) { return (value >= ymin && value <= ymax) ? value : '' } }},
                  v: { title: { display: true, text: 'Volume', align: 'start' }, position: 'right', beginAtZero: false,
                       ticks: { stepSize: Math.round(Math.max(...nvol)/2), callback: function(value) { return value < Math.max(...nvol) ? value : '' }}}},
        onHover: function(event, chartElement) { event.native.target.style.cursor = event.native.x && event.native.y ? (chartElement.length ? 'pointer' : 'grab') : 'default'} };
    const config = { type: 'line', data: data, options: options }; const ctx = document.getElementById('CHRT');
    // master: remain (update CHRT)
    if (tcoin === chrt_coin) { priceChart.data = data; 
        priceChart.options.scales.y.min = ymin; priceChart.options.scales.y.max = ymax;
        priceChart.options.scales.v.max = Number.isFinite(vmax) && vmax > 0 ? vmax : undefined;
        // if you want fresh view after data shift when zoom plugin is used:
        // if (priceChart.resetZoom) { priceChart.resetZoom(); }
        priceChart.update(); }
    // master: change (new CHRT)
    if (tcoin !== chrt_coin) { chrt_coin = tcoin; priceChart = new Chart(ctx, config); 
        priceChart.options.scales.y.min = ymin; priceChart.options.scales.y.max = ymax;
        priceChart.options.scales.v.max = Number.isFinite(vmax) && vmax > 0 ? vmax : undefined;
        priceChart.update(); }
};
/*
function plotPriceChart(CHRT, tcoin) {
    // update: CHRT
    if (tcoin !== chrt_coin && priceChart) { priceChart.destroy(); } 
    // CHRT: stats & config
    const xaxis = CHRT.map(entry => entry.tstmp); const nvol = CHRT.map(entry => entry.nvol);
    const sopn = CHRT.map(entry => entry.sopn); const scls = CHRT.map(entry => entry.scls);
    const shgh = CHRT.map(entry => entry.shgh); const slow = CHRT.map(entry => entry.slow);
    const sprm = new Array(scls.length).fill(scls[scls.length - 1]);
    const data = { labels: xaxis, datasets: [
            { label: 'sopn', data: sopn, backgroundColor: 'rgba(20, 20, 250, 0.1)', borderColor: 'rgba(20, 20, 250, .5)' },
            { label: 'shgh', data: shgh, backgroundColor: 'rgba(100, 200, 250, 0.5)', borderColor: 'rgba(100, 200, 250, 1)' },
            { label: 'slow', data: slow, backgroundColor: 'rgba(100, 200, 250, 0.5)', borderColor: 'rgba(100, 200, 250, 1)' },
            { label: 'scls', data: scls, backgroundColor: 'rgba(120, 120, 250, 0.1)', borderColor: 'rgba(120, 120, 250, .5)' },
            { label: 'sprm', data: sprm, backgroundColor: 'rgba(250, 250, 250, 0.5)', borderColor: 'rgba(250, 250, 250, 1)',
                borderWidth: 1, borderDash: [20, 20], pointRadius: 0 },
            { label: 'nvol', data: nvol, backgroundColor: 'rgba(50, 150, 250, 0.5)', borderColor: 'rgba(50, 150, 250, 1)',
                type: 'bar', yAxisID: 'v', borderWidth: 1, pointRadius: 0 }] };
    const options = { responsive: true, animation: false, plugins: { legend: { display: false }, 
        zoom: { zoom: { wheel: { enabled: true }, mode: 'x' }}}, maintainAspectRatio: false,
        scales: { x: { title: { display: true, text: 'Time' }}, 
                  y: { title: { display: true, text: 'Price ($)' }, beginAtZero: false, max: Math.max(...shgh)*1.0015, min: Math.min(...slow)*.9985,
                       ticks: { callback: function(value) { return (value >= Math.min(...slow) && value <= Math.max(...shgh)) ? value : '' }}},
                  v: { title: { display: true, text: 'Volume', align: 'start' }, position: 'right', beginAtZero: false, max: Math.max(...nvol)*10,
                       ticks: { stepSize: Math.round(Math.max(...nvol)/2), callback: function(value) { return value < Math.max(...nvol) ? value : '' }}}},
        onHover: function(event, chartElement) { event.native.target.style.cursor = event.native.x && event.native.y ? (chartElement.length ? 'pointer' : 'grab') : 'default'} };
    const config = { type: 'line', data: data, options: options }; const ctx = document.getElementById('CHRT');
    // master: remain (update CHRT)
    if (tcoin === chrt_coin) { priceChart.data = data; priceChart.update(); }
    // master: change (new CHRT)
    if (tcoin !== chrt_coin) { chrt_coin = tcoin; priceChart = new Chart(ctx, config); }
};
*/