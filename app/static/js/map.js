var mymap = L.map('mapid').setView([51.505, -0.09], 2);

L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoicmV0c2VkaXYiLCJhIjoiY2oyeWtycGR6MDBhNDJxcnRwcXBxaHJjayJ9.F2M35qbg_B31hwxTi4JCCQ', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 20,
    id: 'mapbox.mapbox-terrain-v2'
}).addTo(mymap);

function set_points(year, month) {
    clearMap();

    $("#arrow-text").text(year + "-" + month);

    $.get("/data/" + year + "/" + month, function (data, status, obj) {
        var points = JSON.parse(data);

        points.forEach(function (item) {
            var lng = item[0][0];
            var lat = item[0][1];
            // L.marker([lng, lat]).addTo(mymap);

            var myStyle = {
                radius: item[1] * 1500,
                fillColor: "red",
                color: "red",
                weight: 5,
                opacity: 0.25,
                fillOpacity: 0.55
            };

            L.circle([lng, lat], myStyle).addTo(mymap);
        });


    });

}

function clearMap() {
    for (i in mymap._layers) {
        if (mymap._layers[i]._path != undefined) {
            try {
                mymap.removeLayer(mymap._layers[i]);
            }
            catch (e) {
                console.log("problem with " + e + mymap._layers[i]);
            }
        }
    }
}

var monthes = [[2005, 1], [2006, 1], [2006, 2], [2006, 3]],
    currentMonth = monthes[0];


function nextMonth() {
    var index = monthes.indexOf(currentMonth);

    currentMonth = monthes[(index + 1) % monthes.length];

    set_points(currentMonth[0], currentMonth[1]);
}

function prevMonth() {
    var index = monthes.indexOf(currentMonth);

    var newIndex = index - 1;
    if(newIndex < 0) {
        newIndex = monthes.length - 1;
    }

    currentMonth = monthes[newIndex];

    set_points(currentMonth[0], currentMonth[1])
}

$("#arrow-left").click(prevMonth);
$("#arrow-right").click(nextMonth);

set_points(currentMonth[0], currentMonth[1]);

