// Gets Max Profit from an array of prices (Interview Cake)
function getMaxProfit(stockPrices) {

  let c = stockPrices[0]
  let opt = stockPrices[1] - stockPrices[0]
  
  for(let v of stockPrices) {
    if(v <= c) {
      c = v;
      continue;
    }
    let tryOpt = v - c;
    if(tryOpt > opt) {
      opt = tryOpt;
    }
  }
  return opt;
}
