$(document).ready(function () {
    // Default values for sex and units
    let sex = "female";
    let units = "imperial";

    // Fix chart container dimensions same as parent
    const context = $("#chartContext");
    context.attr('width', $(".chart-container").width());
    context.attr('height', $(".chart-container").height()*2); // Adjust height as needed

    // Initial data transmission to server with default settings
    sendData(sex, units);

    // Event listener for the Units toggle switch (changes between 'imperial' and 'si')
    $(".checkbox-units").click(function () {
        // Toggle units based on checkbox state
        units = $(this).is(":checked") ? "si" : "imperial";
        console.log("Units", units)
        updateUnits(units);  // Update UI with new units
        sendData(sex, units);  // Send updated data to server
    });

    // Event listener for the Sex toggle switch (changes between 'male' and 'female')
    $(".checkbox-sex").click(function () {
        // Toggle sex based on checkbox state
        sex = $(this).is(":checked") ? "male" : "female";
        sendData(sex, units);  // Send updated data to server
    });

    // Event listener for changes in range sliders (weight, height, rate)
    $(".level").on("change", function () {
        sendData(sex, units);  // Send updated data to server whenever a slider value changes
    });
});

/**
 * Updates the UI and form values based on the selected system of units (SI or Imperial)
 * @param {string} units - The current system of units ('si' or 'imperial')
 */
function updateUnits(units) {
    // Determine if SI (metric) units are selected
    const isSI = units === "si";

    // Conversion factors for weight, height, and rate between units
    const weightFactor = isSI ? 1 / 2.20462262185 : 2.20462262185;
    const heightFactor = isSI ? 1 / 39.3701 : 39.3701;
    const rateFactor = isSI ? 1 / 2.20462262185 : 2.20462262185;

    // Limits for weight, height, and rate input fields, depending on selected units
    const weightLimits = isSI ? { min: 45, max: 204, step: 1 } : { min: 100, max: 450, step: 1 };
    const heightLimits = isSI ? { min: 1.27, max: 5.08, step: 0.01 } : { min: 50, max: 200, step: 1 };
    const rateLimits = isSI ? { min: 0, max: 10, step: 0.5 } : { min: 0, max: 20, step: 1 };

    // Textual representation of units for weight, height, and rate
    const unitsText = {
        weight: isSI ? "kg" : "lbs",
        height: isSI ? "m" : "inch",
        rate: isSI ? "kg" : "lbs",
    };

    // Descriptions for activity levels, depending on selected units
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

    // Update UI elements for weight, height, rate, and activity levels
    updateField(".level.weight", ".weight", weightFactor, weightLimits, unitsText.weight);
    updateField(".level.height", ".height", heightFactor, heightLimits, unitsText.height);
    updateField(".level.rate", ".rate", rateFactor, rateLimits, unitsText.rate);

    // Update activity level descriptions in UI
    $(".low-active-text").text(activityDescriptions.lowActive);
    $(".active-text").text(activityDescriptions.active);
    $(".very-active-text").text(activityDescriptions.veryActive);
}

/**
 * Updates a specific input field's value, attributes, and unit text based on the selected system of units
 * @param {string} valueSelector - The class of the input field to update
 * @param {string} valueLabel - The class of the input field label to update
 * @param {number} factor - The conversion factor (based on selected units)
 * @param {object} limits - The min, max, and step attributes for the field
 * @param {string} unit - The unit text to display (e.g., 'kg', 'lbs', 'm', 'inch')
 */
function updateField(valueSelector, valueLabel, factor, limits, unit) {
    // Calculate new value based on factor (conversion from imperial to SI or vice versa)
    const newValue = Math.round($(valueSelector).val() * factor * 100) / 100;

    // Update input field value and attributes (min, max, step)
    $(valueSelector)
        .attr(limits)
        .val(newValue);

    // Update value label and unit text in the UI
    $(`.level-value${valueLabel}`).text(newValue);
    $(`.unit${valueLabel}`).text(unit);
}

/**
 * Sends the form data, including sex and units, to the server via AJAX
 * @param {string} sex - The user's sex ('male' or 'female')
 * @param {string} units - The current system of units ('si' or 'imperial')
 */
function sendData(sex, units) {
    var formData = $("form").serialize(); // Serialize the form data: (URL-encoded notation)
    formData += `&sex=${sex}&units=${units}`;  // Append sex and units to the data

    // Convert height if necessary
    // If units = SI: height in meters -> height in centimeters
    if (units == "si") {
        let formDataArray = formData.split("&"); // Store URL as an array; e. g. ["units=imperial", ...]
        let formDataNew = "";
        for (let i = 0; i < formDataArray.length; i++) {
            // Split array entry into [label, value]; e. g. ["units", "imperial"]
            // If label = height -> convert height
            if ("height" == formDataArray[i].split("=")[0]) {
                let heightM = $(".level-value.height").val();
                let heightCM = heightM * 100;  // Convert meters to centimeters
                formDataNew += `height=${heightCM}&`;
            } else {
                formDataNew += formDataArray[i] + "&";
            }
        }
        formData = formDataNew;  // Update formData with converted height
    }

    // Send data to server via POST request
    $.ajax({
        url: "/submit",
        type: "POST",
        data: formData,
        success: function (response) {
            console.log(Math.floor(response.output.rmr[0]))
            renderChart(response.output.time_projection, response.output.rmr);  // Render the RMR chart
        },
    });
}

/**
 * Renders a line chart with the provided data for resting metabolic rate (RMR) over time
 * @param {Array} labels - The labels for the x-axis (e.g., weeks)
 * @param {Array} data - The RMR data for the y-axis (e.g., calories/day)
 */
function renderChart(labels, data) {
    const context = $("#chartContext");
    // context.attr('width', $(".chart-container").width());
    // context.attr('height', $(".chart-container").height() * 2); // Adjust height as needed
    // Destroy any existing chart before rendering a new one
    const existingChart = Chart.getChart("chartContext");
    if (existingChart) {
        existingChart.destroy();
    }

    // Create a new chart using the Chart.js library
    new Chart(context, {
        type: "line",  // Line chart type
        data: {
            labels: labels,  // Set x-axis labels (weeks)
            datasets: [
                {
                    label: "Sedentary",
                    data: data,  // Set y-axis data (RMR values)
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
                        text: "Weeks",  // X-axis title
                    },
                },
                y: {
                    title: {
                        display: true,
                        text: "RMR (calories/day)",  // Y-axis title
                    },
                },
            },
        },
    });
}