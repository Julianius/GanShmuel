fetch('open_ports.txt')
  .then(response => response.text())
  .then(data => {
        for(let i=0 ; i<=12 ; i+=2) {
            let port = 8080 + (i/2);
            if(data[i] == "1") {
                document.getElementById(port).querySelector("h3").innerHTML = "Port is on";
                document.getElementById(port).querySelector(".image").innerHTML = "<div class='green'></div>";
            } else {
                document.getElementById(port).querySelector("h3").innerHTML = "Port is off";
                document.getElementById(port).querySelector(".image").innerHTML = "<div class='red'></div>";
            }
        }
    }
  );