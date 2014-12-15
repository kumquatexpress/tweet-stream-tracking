function initialize() {
  // Create the map.
  var mapOptions = {
    zoom: 4,
    center: new google.maps.LatLng(37.09024, -95.712891),
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };

  var map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
  var cityCircle;
  
  $.ajax({
    url: "/tweets",
    type: "GET",
    success: function(data){   
      $.each(data["tweets"], function(_, tweet){
        var tweetLoc = {
          strokeColor: '#FF0000',
          strokeOpacity: 0.8,
          strokeWeight: 2,
          fillColor: '#FF0000',
          fillOpacity: 0.35,
          map: map,
          center: new google.maps.LatLng(tweet["location"][1],tweet["location"][0]),
          radius: 400000/data["tweets"].length
        };
        // Add the circle for this city to the map.
        cityCircle = new google.maps.Circle(tweetLoc);
      });
    },
    error: function(){ console.log("failed to get tweets"); }
  });
}

google.maps.event.addDomListener(window, 'load', initialize);