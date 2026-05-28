// glb
const glb_Thost = "127.0.0.1"; const glb_Tport = 8000; const glb_Tibtc = 'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'
const glb_Tunit1 = { snow: '(💲)', ndgts: '(⩩)', spstp: '(💲)', rqntm: '(⩩)', sqntm: '(💲)', nxmax: '(⩩)', sndmn: '(💲)' };       
const glb_Tunit2 = { smid: '(💲)', swid: '(💲)', dcvg: '(%)', drng: '(%)', dvar: '(%)', dvlt: '(%)', rzcv: '(ℝ)',nvsec: '(⩩)', rvsec: '(💲)',
                     npsml: '(⩩)', ntfsml: '(⩩)', ncksml: '(⩩)', npbig: '(⩩)', ntfbig: '(⩩)', nckbig: '(⩩)' };
const glb_Tunit3 = { ncko: '(⩩)', laval: '(ℝ)', lasig: '(✎)', tside: '(✎)' };       
const glb_Tunit4 = { nrsk: '(⩩)', nrwd: '(⩩)', tzrrr: '(✎)', drsk: '(%)', drwd: '(%)', drrr: '(%)', dmnw: '(%)', 
                     nstp: '(⩩)', dstp: '(%)', nxfl: '(⩩)', sndf: '(💲)', rzunt: '(ℝ)', rztot: '(ℝ)' };       
const glb_Tpsrt1 = [ 'snow', 'ndgts', 'spstp', 'rqntm', 'sqntm', 'nxmax', 'sndmn' ];
const glb_Tpsrt2 = [ 'smid', 'swid', 'dcvg', 'drng', 'dvar', 'dvlt', 'rzcv', 'nvsec', 'rvsec', 'npsml', 'ntfsml', 'ncksml', 'npbig', 'ntfbig', 'nckbig' ];
const glb_Tpsrt3 = [ 'ncko', 'tside' ];
const glb_Tpsrt4 = [ 'nrsk', 'nrwd', 'tzrrr', 'drsk', 'drwd', 'drrr', 'dmnw', 'nstp', 'dstp', 'nxfl', 'sndf', 'rzunt', 'rztot' ];
let priceChart = null; let chrt_coin = null; let tlup = new Date(0); let tprv = new Date(0); let inow = -1; let bscan = false; let bsolo = false; let bmngr = '';
localStorage.setItem('bmngr', JSON.stringify('')); localStorage.setItem('bscan', JSON.stringify(false)); // not resume
// const saved1 = localStorage.getItem('bscan'); if (saved1 !== null) {bscan = saved1;} // resume
// const saved2 = localStorage.getItem('bmngr'); if (saved2 !== null) {bmngr = saved2;} // resume