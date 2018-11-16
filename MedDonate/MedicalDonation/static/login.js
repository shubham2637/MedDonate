$(function() {
  var nightsky = ["#280F36", "#632B6C", "#BE6590", "#FFC1A0", "#FE9C7F"];

  var star0 =
    "<div class='star star-0' style='top:{{top}}vh;left:{{left}}vw;animation-duration:{{duration}}s;'></div>";

  var star1 =
    "<div class='star star-1 blink' style='top:{{top}}vh;left:{{left}}vw;animation-duration:{{duration}}s;'></div>";

  var star2 =
    "<div class='star star-2 blink' style='top:{{top}}vh;left:{{left}}vw;animation-duration:{{duration}}s;'></div>";

  var star3 =
    "<div class='star star-3' style='top:{{top}}vh;left:{{left}}vw;animation-duration:{{duration}}s;'></div>";

    var star4 =
    "<div class='star star-4' style='top:{{top}}vh;left:{{left}}vw;animation-duration:{{duration}}s;'></div>";
  
    var star5 =
    "<div class='star star-5' style='top:{{top}}vh;left:{{left}}vw;animation-duration:{{duration}}s;background-color:{{color}}'></div>";


  
  var star1pt =
    "<div class='star star-1 blink' style='top:{{top}}%;left:{{left}}%;animation-duration:{{duration}}s;background-color:{{color}};box-shadow:0px 0px 6px 1px {{shadow}}'></div>";

  var star2pt =
    "<div class='star star-2' style='top:{{top}}%;left:{{left}}%;animation-duration:{{duration}}s;background-color:{{color}};box-shadow:0px 0px 10px 1px {{shadow}};opacity:0.7'></div>";

  var blur =
    "<div class='blur' style='top:{{top}}%;left:{{left}}%;background-color:{{color}}'></div>";

  for (i = 0; i < 1000; i++) {
    $(".stars").append(
      star1
        .replace("{{top}}", getRandomInt(0, 40))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(4, 10))
    );

    $(".stars").append(
      star2
        .replace("{{top}}", getRandomInt(20, 70))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(8, 16))
    );
  }

  for (i = 0; i < 300; i++) {
    $(".stars").append(
      star0
        .replace("{{top}}", getRandomInt(0, 50))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(2, 5))
    );

    $(".stars").append(
      star1
        .replace("{{top}}", getRandomInt(0, 50))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(5, 8))
    );

    $(".stars").append(
      star2
        .replace("{{top}}", getRandomInt(0, 50))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(8, 11))
    );
  }

  for (i = 0; i < 200; i++) {
    $(".stars").append(
      star0
        .replace("{{top}}", getRandomInt(40, 75))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(2, 6))
    );

    $(".stars").append(
      star1
        .replace("{{top}}", getRandomInt(40, 75))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(5, 8))
    );
  }

  for (i = 0; i < 500; i++) {
    $(".stars").append(
      star0
        .replace("{{top}}", getRandomInt(0, 100))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(2, 5))
    );

    $(".stars").append(
      star1
        .replace("{{top}}", getRandomInt(0, 100))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(2, 5))
    );

    $(".stars").append(
      star2
        .replace("{{top}}", getRandomInt(0, 100))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(3, 8))
    );

    $(".stars").append(
      star4
        .replace("{{top}}", getRandomInt(0, 70))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(11, 14))
    );
  }

  for (i = 0; i < 150; i++) {
    
        $(".stars").append(
      star4
        .replace("{{top}}", getRandomInt(0, 100))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(11, 14))
    );
    
    $(".stars-cross").append(
      blur
        .replace("{{top}}", getRandomInt(0, 100))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace(
          "{{color}}",
          nightsky[Math.ceil(getRandomInt(0, nightsky.length - 1))]
        )
    );
    
        $(".stars-cross").append(
      star1pt
        .replace("{{top}}", getRandomInt(0, 100))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(6, 12)).replace(
          "{{color}}",
          nightsky[Math.ceil(getRandomInt(0, nightsky.length - 1))]
        ).
          replace(
          "{{shadow}}",
          nightsky[Math.ceil(getRandomInt(0, nightsky.length - 1))]
        )
    );
  }

  for (i = 0; i < 100; i++) {
    
    if(i%2 == 0){
            $(".stars").append(
      star5
        .replace("{{top}}", getRandomInt(0, 50))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(11, 14))
              .replace(
          "{{color}}",
          nightsky[Math.ceil(getRandomInt(0, nightsky.length - 1))]
        )
    );
              }
    
    $(".stars-cross-aux").append(
      blur
        .replace("{{top}}", getRandomInt(0, 100))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace(
          "{{color}}",
          nightsky[Math.ceil(getRandomInt(0, nightsky.length - 1))]
        )
    );
    
            $(".stars-cross-aux").append(
      star2pt
        .replace("{{top}}", getRandomInt(0, 100))
        .replace("{{left}}", getRandomInt(0, 100))
        .replace("{{duration}}", getRandomInt(4, 10)).replace(
          "{{color}}",
          nightsky[Math.ceil(getRandomInt(0, nightsky.length - 1))]
        ).
              replace(
          "{{shadow}}",
          nightsky[Math.ceil(getRandomInt(0, nightsky.length - 1))]
        )
    );
  }

});

function getRandomInt(min, max) {
  return Math.random() * (max - min) + min;
}
