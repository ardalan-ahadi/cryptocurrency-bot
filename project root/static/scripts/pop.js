// pop
function populateCoinBox(box_coin, PERPS, SRTR, VBSY, RBSY, VLTD_none, RLTD_none) {
    const saved1 = JSON.parse(localStorage.getItem('bscan')); if (saved1 !== null) {bscan = JSON.parse(saved1);}
    // choose: PERPS & SRTR
    if (!bscan) { PERPS_SRTR = PERPS } else { PERPS_SRTR = SRTR };
    // get: VBSY & RBSY
    // const vbsytcoin = new Set(VBSY.map(item => item.tcoin)); const rbsytcoin = new Set(RBSY.map(item => item.tcoin));
    // pop: PERPS
    PERPS_SRTR.forEach((item, index) => {
        const ticonElement = document.createElement('img'); ticonElement.src = item.ticon;
        ticonElement.style.marginRight = '10px'; ticonElement.style.width = '27px'; ticonElement.style.height = '27px';
        const tcoinElement = document.createElement('span'); tcoinElement.textContent = item.tcoin+'/'+item.tcola
        tcoinElement.style.color = 'white'; tcoinElement.style.fontSize = '16px'; tcoinElement.style.fontWeight = 'bold';
        // if (vbsytcoin.has(item.tcoin)) { tcoinElement.textContent += ' Ⓥ'; } if (rbsytcoin.has(item.tcoin)) { tcoinElement.textContent += ' ℛ'; }
        if (VLTD_none.includes(item.tcoin)) { tcoinElement.textContent += ' Ⓥ'; } if (RLTD_none.includes(item.tcoin)) { tcoinElement.textContent += ' ℛ'; }
        const leftContainer = document.createElement('div'); leftContainer.style.display = 'flex';
        leftContainer.style.alignItems = 'center'; leftContainer.appendChild(tcoinElement); leftContainer.appendChild(ticonElement);
        const snowElement = document.createElement('span'); snowElement.textContent = item.snow;
        snowElement.style.color = 'white'; snowElement.style.fontSize = '16px'; snowElement.style.fontWeight = 'bold';
        const coinItem = document.createElement('div'); coinItem.style.padding = '10px';  
        coinItem.style.display = 'flex'; coinItem.style.justifyContent = 'space-between'; coinItem.style.alignItems = 'center'; 
        coinItem.style.marginLeft = '10px'; coinItem.style.marginRight = '10px'; coinItem.style.marginTop = index === 0 ? '10px' : '10px'; // '50px'
        coinItem.style.backgroundColor = '#2E2E2E'; coinItem.style.border= "1px solid white"; coinItem.style.borderRadius= "5px";
        coinItem.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)'; coinItem.style.transition = 'background-color 0.25s';
        coinItem.style.cursor = 'pointer'; coinItem.appendChild(snowElement); coinItem.appendChild(leftContainer);
        coinItem.addEventListener('click', () => { hndl_btn_coin(item.tcoin, item.tcola, item.ticon, false);
            coinItem.style.transform = 'scale(1.02)'; coinItem.style.transform = 'translate(2px, 2px)'; coinItem.style.backgroundColor = '#696969';
            setTimeout(() => { coinItem.style.transform = 'scale(1)'; coinItem.style.transform = 'translate(0, 0)'; coinItem.style.backgroundColor = '#2E2E2E'; }, 200); });
        coinItem.addEventListener('mouseover', () => { coinItem.style.transform = 'scale(1.02)'; coinItem.style.backgroundColor = '#969696'; });
        coinItem.addEventListener('mouseout', () => { coinItem.style.transform = 'scale(1)'; coinItem.style.backgroundColor = '#2E2E2E'; });
        box_coin.appendChild(coinItem);
    });
};