$(document).ready(function () {
    let sex = "female";
    let units = "imperial";

    // Initial data transmission
    sendData(sex, units);

    // Event Listener for Units Toggle
    $(".checkbox-units").click(function () {
        units = $(this).is(":checked") ? "si" : "imperial";
        console.log(`System of Units: ${units.toUpperCase()}`);
        updateUnits(units);
        sendData(sex, units);
    });

    // Event Listener for Sex Toggle
    $(".checkbox-sex").click(function () {
        sex = $(this).is(":checked") ? "male" : "female";
        console.log(`Sex at Birth: ${sex.charAt(0).toUpperCase() + sex.slice(1)}`);
        sendData(sex, units);
    });

    // Event Listener for Range Sliders
    $(".level").on("change", function () {
        sendData(sex, units);
    });
});

/**
 * Updates the UI and values based on the selected system of units
 * @param {string} units - The current system of units ('si' or 'imperial')
 */
function updateUnits(units) {
    const isSI = units === "si";

    const weightFactor = isSI ? 1 / 2.20462262185 : 2.20462262185;
    const heightFactor = isSI ? 1 / 39.3701 : 39.3701;
    const rateFactor = isSI ? 1 / 2.20462262185 : 2.20462262185;

    const weightLimits = isSI ? { min: 22, max: 453 } : { min: 50, max: 999 };
    const heightLimits = isSI
        ? { min: 1.27, max: 5.08, step: 0.01 }
        : { min: 50, max: 200, step: 1 };
    const rateLimits = isSI
        ? { min: 0, max: 9.1, step: 0.1 }
        : { min: 0, max: 20, step: 1 };

    const unitsText = {
        weight: isSI ? "kg" : "lbs",
        height: isSI ? "m" : "inch",
        rate: isSI ? "kg" : "lbs",
    };

    const activityDescriptions = isSI
        ? {
              lowActive: "2.4–5 km at 5–6 km/h",
              active: "5+ km at 5–6 km/h",
              veryActive: "12+ km at 5–6 km/h",
          }
        : {
              lowActive: "1.5–3 m at 3–4 mph",
              active: "3+ m at 3–4 mph",
              veryActive: "7.5+ m at 3–4 mph",
          };

    // Update weight
    updateField(".weight", weightFactor, weightLimits, unitsText.weight);
    // Update height
    updateField(".height", heightFactor, heightLimits, unitsText.height);
    // Update rate
    updateField(".rate", rateFactor, rateLimits, unitsText.rate);

    // Update activity level descriptions
    $(".low-active-text").text(activityDescriptions.lowActive);
    $(".active-text").text(activityDescriptions.active);
    $(".very-active-text").text(activityDescriptions.veryActive);
}

/**
 * Updates a specific input field's value, attributes, and unit text
 * @param {string} selector - The class of the input field to update
 * @param {number} factor - The conversion factor
 * @param {object} limits - The min, max, and step attributes for the field
 * @param {string} unit - The unit text to display
 */
function updateField(selector, factor, limits, unit) {
    const newValue = Math.round($(selector).val() * factor * 100) / 100;
    $(selector)
        .attr(limits)
        .val(newValue);
    $(`.level-value${selector}`).text(newValue);
    $(`.unit${selector}`).text(unit);
}

/**
 * Sends form data along with additional parameters (sex and units) to the server
 * @param {string} sex - The user's sex ('male' or 'female')
 * @param {string} units - The current system of units ('si' or 'imperial')
 */
function sendData(sex, units) {
    let formData = $("form").serialize();
    formData += `&sex=${sex}&units=${units}`;
    console.log("Data Sent:", formData);

    $.ajax({
        url: "/submit",
        type: "POST",
        data: formData,
        success: function (response) {
            console.log("Server response:", response.output.rmr);
            $(".plots-text").text(response.output.rmr);

            // Render Chart
            renderChart(response.output.time_projection, response.output.rmr);
        },
    });
}

/**
 * Renders a line chart with the provided data
 * @param {Array} labels - The labels for the x-axis
 * @param {Array} data - The RMR data for the y-axis
 */
function renderChart(labels, data) {
    const ctx = document.getElementById("myChart");

    // Destroy existing chart instance if present
    const existingChart = Chart.getChart("myChart");
    if (existingChart) {
        existingChart.destroy();
    }

    new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Resting Metabolic Rate (RMR)",
                    data: data,
                    borderWidth: 1,
                },
            ],
        },
        options: {
            scales: {
                x: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: "Weeks",
                    },
                },
                y: {
                    title: {
                        display: true,
                        text: "RMR (kcal/day)",
                    },
                },
            },
        },
    });
}