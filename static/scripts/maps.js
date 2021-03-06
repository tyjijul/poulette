function initialize() {
  var mapCanvas = document.getElementById('map');
  var mapOptions = {
    zoom: 12,
    center: {
      lat: 52.237442,
      lng: 21.003692
    },
    mapTypeControl: false,
    zoomControl: true,
    zoomControlOptions: {
      position: google.maps.ControlPosition.RIGHT_BOTTOM
    },
    scaleControl: false,
    streetViewControl: true,
    streetViewControlOptions: {
      position: google.maps.ControlPosition.RIGHT_BOTTOM
    }
  };

  var map = new google.maps.Map(mapCanvas, mapOptions);

  var locations = [
    ['palace', 52.231871, 21.005841],
    ['arkadia', 52.257305, 20.984481],
    ['stadium', 52.215147, 21.035074]
  ];

  var marker, i;
  var infowindow = new google.maps.InfoWindow();


  for (i = 0; i < locations.length; i++) {
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(locations[i][1], locations[i][2]),
      map: map
    });

    google.maps.event.addListener(marker, 'click', (function(marker, i) {
      return function() {
        infowindow.setContent(locations[i][0]);
        infowindow.open(map, marker);
        map.setZoom(14);
        map.setCenter(marker.getPosition());
      }
    })(marker, i));
  }

  var controlText = [
    ['N', google.maps.ControlPosition.TOP_CENTER],
    ['W', google.maps.ControlPosition.LEFT_CENTER],
    ['E', google.maps.ControlPosition.RIGHT_CENTER],
    ['S', google.maps.ControlPosition.BOTTOM_CENTER],
  ];

  for (var i = 0; i < controlText.length; i++) {
    var divLabel = controlText[i][0];
    var divName = document.createElement('div');
    var newDiv = new MakeControl(divName, divLabel, map);
    map.controls[controlText[i][1]].push(divName);
    google.maps.event.addDomListener(divName, 'click', function() {
      alert(controlText[i][0]);
    });
  }

}
google.maps.event.addDomListener(window, 'load', initialize);
/**
 * Creates a series of custom controls to demonstrate positioning
 * of controls within a map.
 */

/**
 * MakeControl adds a control to the map.
 * This constructor takes the controlDIV name and label text as arguments.
 * @constructor
 * @param {!Element} controlDiv  The name of the DIV element for the control.
 * @param {string} label  Text to display within the DIV element.
 */
function MakeControl(controlDiv, label, map) {

  // Set up the control border.
  var controlUI = document.createElement('div');
  controlUI.title = label;
  controlUI.className = 'controlUI';
  controlUI.style.cursor = 'pointer';
  controlDiv.appendChild(controlUI);

  // Set up the inner control.
  var controlText = document.createElement('div');
  controlText.innerHTML = label;
  controlText.className = 'controlText';
  controlUI.appendChild(controlText);
  // Setup the click event listeners: simply set the map to Chicago.
  controlUI.addEventListener('click', function() {
    var bounds = map.getBounds();
    var span = bounds.toSpan();
    switch (label) {
      case "N":
        map.setCenter(new google.maps.LatLng(map.getCenter().lat() + span.lat() / 2, map.getCenter().lng()));
        break;
      case "S":
        map.setCenter(new google.maps.LatLng(map.getCenter().lat() - span.lat() / 2, map.getCenter().lng()));
        break;
      case "E":
        map.setCenter(new google.maps.LatLng(map.getCenter().lat(), map.getCenter().lng() + span.lng() / 2));
        break;
      case "W":
        map.setCenter(new google.maps.LatLng(map.getCenter().lat(), map.getCenter().lng() - span.lng() / 2));
        break;
    }
  });
}