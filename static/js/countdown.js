// Set the date we're counting down to
var countDownDate = new Date("Aug 16, 2025 14:30:30").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();
    
  // Find the distance between now and the count down date
  var distance = countDownDate - now;
    
  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
  
  // If value is 0, change it to '00' and change class to countdown-zero
  if (days <= 0) {
    days = "00";
    document.getElementById("countdown-days").className = "zero";

    if (hours <= 0) {
      hours = "00";
      document.getElementById("countdown-hours").className = "zero";

      if (minutes <= 0) {
        minutes = "00";
        document.getElementById("countdown-minutes").className = "zero";

        if (seconds <= 0) {
          seconds = "00";
          document.getElementById("countdown-seconds").className = "zero";
        }
      }
    }
  }

  // Output the result in an element with id="demo"
  document.getElementById("countdown-days").innerHTML = days;
  document.getElementById("countdown-hours").innerHTML = hours;
  document.getElementById("countdown-minutes").innerHTML = minutes;
  document.getElementById("countdown-seconds").innerHTML = seconds;
    
}, 1000);