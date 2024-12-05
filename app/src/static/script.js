$(document).ready(function() {
    var sex = "female";
    var units = "imperial";
    senddata(sex, units)
    // System of Units Checkbox
    $(".checkbox-units").click(function () {
        if ($(this).is(":checked")) {
            console.log("System of Units: SI");
            units = "si"

            // Handle and transmit data
            senddata(sex, units)

            // Weight
            var new_weight = Math.round($(".level.weight").val() / 2.20462262185);
            $(".level.weight").attr({min: 22, max: 453});
            $(".level.weight").val(new_weight);
            $(".level-value.weight").text(new_weight);
            $(".unit.weight").text("kg");
            
            // Height
            var new_height = Math.round(($(".level.height").val() / 39.3701)*100)/100;
            $(".unit.height").text("m");
            $(".level.height").attr({min: 1.27, max: 5.08, step: 0.01});
            $(".level.height").val(new_height);
            $(".level-value.height").text(new_height);
            
            // Rate
            var new_rate = Math.round(($(".level.rate").val() / 2.20462262185)*10)/10;
            $(".unit.rate").text("kg");
            $(".level.rate").attr({min: 0, max: 9.1, step: 0.1});
            $(".level.rate").val(new_rate);
            $(".level-value.rate").text(new_rate);

            // Cards
            $(".low-active-text").text("2.4–5 km at 5–6 km/h")
            $(".active-text").text("5+ km at 5–6 km/h")
            $(".very-active-text").text("12+ km at 5–6 km/h")
        } else {
            console.log("System of Units: Imperial");
            units = "imperial"

            // Handle and transmit data
            senddata(sex, units)

            // Weight
            var new_weight = Math.round($(".level.weight").val() * 2.20462262185);
            $(".unit.weight").text("lbs");
            $(".level.weight").attr({min: 50, max: 999});
            $(".level.weight").val(new_weight);
            $(".level-value.weight").text(new_weight);

            // Height
            var new_height = Math.round($(".level.height").val() * 39.3701);
            $(".unit.height").text("inch");
            $(".level.height").attr({min: 50, max: 200, step: 1});
            $(".level.height").val(new_height);
            $(".level-value.height").text(new_height);

            // Rate
            var new_rate = Math.round($(".level.rate").val() * 2.20462262185);
            $(".unit.rate").text("lbs");
            $(".level.rate").attr({min: 0, max: 20, step: 1});
            $(".level.rate").val(new_rate);
            $(".level-value.rate").text(new_rate);

            // Cards
            $(".low-active-text").text("1.5–3 m at 3–4 mph")
            $(".active-text").text("3+ m at 3–4 mph")
            $(".very-active-text").text("7.5+ m at 3–4 mph")
        };
    });
    // Birth Sex Checkbox
    $(".checkbox-sex").click(function () {
        if ($(this).is(":checked")) {
            console.log("Sex at Birth: Male");
            sex = "male";
        } else {
            console.log("Sex at Birth: Female");
            sex = "female";
        };
        
        // Handle and transmit data
        senddata(sex, units)

    });

    // Range Sliders
    $(".level").on("change", function() {
        senddata(sex, units)
    });
});

//  Function to handle and transmit form data
function senddata(sex, units) {
    let form_data = $("form").serialize();
    form_data += "&sex=" + sex;
    form_data += "&units=" + units;
    console.log("Data Sent:", form_data);
    $.ajax({
        url: '/submit',
        type: 'POST',
        data: form_data,
        success: function(response) {
            console.log("Server response:");
            console.log(response.output.rmr);
            $(".plots-text").text(response.output.rmr)
            
            let chartStatus = Chart.getChart("myChart"); // <canvas> id
            if (chartStatus != undefined) {
                chartStatus.destroy();
            }

            var ctx = document.getElementById('myChart');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                  labels: response.output.time_projection,
                  datasets: [{
                    label: 'Resting Metabolic Rate (RMR)',
                    data: response.output.rmr,
                    borderWidth: 1
                  }]
                },
                options: {
                    scales: {
                        x: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: "Weeks"
                        }
                        },
                        y: {
                            title: {
                                display: true,
                                text: "RMR (kcal/day)"
                            }
                        }
                    }
                }
            });
        }
    });
}