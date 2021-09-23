var w = 300;
var h = 300;
var svg = d3.select("body").append("svg").attr("width", w).attr("height", h);
    
var stat = {}

// Set our map from physical to device coordinates, flipping y because SVG uses upper-left as O.
var xS = d3.scaleLinear().domain([0, 1]).range([10, 290]);
var yS = d3.scaleLinear().domain([0, 1]).range([290, 10]);
// Set our axis scales
var xA = d3.axisBottom(xS).ticks(5);

d3.json("test.json", function(error, x) {
    keys = Object.keys(x)
    for (var i = 0; i < keys.length; i++) {
        stat[keys[i]] = x[keys[i]]
    }
    drawScatter();
});

function drawScatter(){
    svg.selectAll("circle").data(Object.keys(stat)).enter().append("circle")
        .attr("cx", function(d) {return xS(stat[d][0]);})
        .attr("cy", function(d) {return yS(stat[d][1]);})
        .attr("r", 5)
        .attr("fill", "red");
    svg.selectAll("text").data(Object.keys(stat)).enter().append("text")
        .text(function (d) {return d;})
        .attr("x", function(d) {return xS(stat[d][0]);})
        .attr("y", function(d) {return yS(stat[d][1]);})
        .attr("font-family", "arial")
        .attr("font-size", "12px")
        .attr("fill", "blue");
    svg.append("g").attr("transform", "translate(0," + (h-10) + ")").call(xA);
}
