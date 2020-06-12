datax = d3.json('http://127.0.0.1:5000/data');
console.log(datax);

data2 = d3.json('http://127.0.0.1:5000/data/ab_c');
console.log(data2);


// const svg = d3.select("svg"), 
// margin = {top: 20, right: 20, bottom: 30, left: 40}, 
// width = +svg.attr("width") - margin.left - margin.right, 
// height = +svg.attr("height") - margin.top - margin.bottom, 
// x = d3.scaleBand().rangeRound([0, width]).padding(0.2), 
// y = d3.scaleLinear().rangeRound([height, 0]), 
// g = svg.append("g") 
// .attr("transform", `translate(${margin.left},${margin.top})`); 

// d3.json(data2).then( data2 => { 
//     data2 = data2.RECORDS; 
     
//     x.domain(data2.map(d => d.Age_Group)); 
//     y.domain([0, d3.max(data2, d => d.Count)]); 
     
//     g.append("g") 
//     .attr("class", "axis axis-x") 
//     .attr("transform", `translate(0,${height})`) 
//     .call(d3.axisBottom(x)); 
     
//     g.append("g") 
//     .attr("class", "axis axis-y") 
//     .call(d3.axisLeft(y).ticks(10)); 
//     }); 






// console.log("Hi world");

// call_api();