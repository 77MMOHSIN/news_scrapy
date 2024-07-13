// time changing

function displayTime() {
    // Create a new Date object
    var now = new Date();
    
    // Get hours, minutes, and seconds
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();
    
    // Add leading zero if hours, minutes, or seconds are less than 10
    hours = hours < 10 ? '0' + hours : hours;
    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;
    
    // Build the time string
    var timeString = hours + ':' + minutes + ':' + seconds;
    
    // Update the content of the element with id="time"
    document.getElementById('time').textContent = timeString;
    
    // Refresh time every second
    setTimeout(displayTime, 1000);
  }
  
  // Call the function to display time when the page loads
  window.onload = displayTime;
//   slider
  
$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

// scroll down
function scrollToDetail() {
    // Get the position of the detail element
    const detailElement = document.getElementById('detail');
    const detailPosition = detailElement.getBoundingClientRect().top;

    // Scroll to the detail element
    window.scrollTo({
        top: window.scrollY + detailPosition,
        behavior: 'smooth' // Smooth scrolling
    });
}
function scrollToDetail1() {
    // Get the position of the detail element
    const detailElement = document.getElementById('detail1');
    const detailPosition = detailElement.getBoundingClientRect().top;

    // Scroll to the detail element
    window.scrollTo({
        top: window.scrollY + detailPosition,
        behavior: 'smooth' // Smooth scrolling
    });
}
function scrollToDetail2() {
    // Get the position of the detail element
    const detailElement = document.getElementById('detail2');
    const detailPosition = detailElement.getBoundingClientRect().top;

    // Scroll to the detail element
    window.scrollTo({
        top: window.scrollY + detailPosition,
        behavior: 'smooth' // Smooth scrolling
    });
}
function scrollToDetail3() {
    // Get the position of the detail element
    const detailElement = document.getElementById('detail3');
    const detailPosition = detailElement.getBoundingClientRect().top;

    // Scroll to the detail element
    window.scrollTo({
        top: window.scrollY + detailPosition,
        behavior: 'smooth' // Smooth scrolling
    });
}
function scrollToDetail4() {
    // Get the position of the detail element
    const detailElement = document.getElementById('detail4');
    const detailPosition = detailElement.getBoundingClientRect().top;

    // Scroll to the detail element
    window.scrollTo({
        top: window.scrollY + detailPosition,
        behavior: 'smooth' // Smooth scrolling
    });
}
function scrollToDetail5() {
    // Get the position of the detail element
    const detailElement = document.getElementById('detail5');
    const detailPosition = detailElement.getBoundingClientRect().top;

    // Scroll to the detail element
    window.scrollTo({
        top: window.scrollY + detailPosition,
        behavior: 'smooth' // Smooth scrolling
    });
}






