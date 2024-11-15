$(document).ready(function() {
    // Load existing data
    // loadDataIn();

    //////// Show initial message ////////

    var statusMessageContainer = $("header h5");

    displayMessage(
        statusMessageContainer,
        "App ready!"
    );

    //////// Input data validation ////////

    // Age must be 19 years or more
    var ageField = $("#input-age");
    var minAge = 19;
    var maxAge = 150;
    var ageErrorMessage = "Must be between 19 and 150";
    isBetween(
        ageField,
        minAge,
        maxAge,
        ageErrorMessage,
        statusMessageContainer
    );
    
    // Initial weight mus be 0 or more
    var weightField = $('#input-weight');
    var minWeight = 0;
    var weightErrorMessage = "Weight must be 0 or more";
    isGreaterThan(
        weightField,
        minWeight,
        weightErrorMessage,
        statusMessageContainer
    );

    // Height must be 0 or more
    var heightField = $('#input-height');
    var minHeight = 0;
    var heightErrorMessage = "Must be 0 or more";
    isGreaterThan(
        heightField,
        minHeight,
        heightErrorMessage,
        statusMessageContainer
    );

    // Time to Project must be 0 or more
    var timeField = $('#input-time');
    var minTime = 0;
    var timeErrorMessage = "Must be 0 or more";
    isGreaterThan(
        timeField,
        minTime,
        timeErrorMessage,
        statusMessageContainer
    );

    // Weight Loss Rate must be 0 or more
    var rateField = $('#input-rate');
    var minRate = 0;
    var rateErrorMessage = "Must be 0 or more";
    isGreaterThan(
        rateField,
        minRate,
        rateErrorMessage,
        statusMessageContainer
    );

    // Energy Deficit must be 0 or more
    var energyField = $('#input-energy');
    var minEnergy = 0;
    var energyErrorMessage = "Must be 0 or more";
    isGreaterThan(
        energyField,
        minEnergy,
        energyErrorMessage,
        statusMessageContainer
    );

    //////// Change units display based on selection ////////

    $('#select-units').on(
        'change',
        function() {
            // Code to execute when the select option changes
            var selectedValue = $(this).val();
            if (selectedValue == 'imperial') {
                $('#label-weight-unit').text("lbs")
                $('#label-rate-unit').text("lbs")
                $('#label-height-unit').text("inch")
            } else {
                $('#label-weight-unit').text("kg")
                $('#label-rate-unit').text("kg")
                $('#label-height-unit').text("cm")
            };
        }
    );

    //////// Handle form submission ////////

    $('#data-form').on(
        'submit',
        function(event) {
        event.preventDefault();
        var form_data = $('#data-form').serializeArray(); // Receive form data
        // Report input data to browser console
        console.log("Form input data:")
        console.log(form_data); 

        var formInputIsValid = {}; // To store field validation result
        // Trigger form input field validation check
        for (var input in form_data){
            var element=$("#input-"+form_data[input]['name']);
            var select_element=$("#select-"+form_data[input]['name']);

            if (element.hasClass("input-valid") || select_element.hasClass("input-valid")) {
                formInputIsValid[form_data[input]["name"]] = true;
            }
            else {
                formInputIsValid[form_data][input]["name"] = false;
            }
        };

        const sex = $('#select-sex').val();
        const age = $('#input-age').val();
        const weight = $('#input-weight').val();
        const height = $('#input-height').val();
        const units = $('#select-units').val();
        const weeks = $('#input-time').val();
        const weightLossRate = $('#input-rate').val();
        const energyDeficit = $('#input-energy').val();

        console.log("Form input data validation object:")
        console.log(formInputIsValid)

        // Check if form input data values are valid 
        const formIsValid = Object.values(formInputIsValid).every(value => value === true);
        console.log("Is form input data valid?")
        console.log(formIsValid)

        if (formIsValid) {
            $.ajax({
                url: '/submit',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({
                    sex: sex,
                    age: age,
                    weight: weight,
                    height: height,
                    units: units,
                    weeks: weeks,
                    weight_loss_rate: weightLossRate,
                    energy_deficit: energyDeficit
                }),
                success: function(response) {
                    console.log("Server response:");
                    console.log(response);
                    serverMessage = `${response.message}: ${response.status}`;
                    displayMessage(statusMessageContainer, serverMessage);
                }
            });
        }
        else {
            displayMessage(statusMessageContainer, "Data not valid")
        };
    });

    //////// Handle form clearing ////////

    $('.clear').on(
        'click',
        function(event) {
        event.preventDefault();
        $.ajax({
            url: '/clear',
            type: 'POST',
            contentType: 'application/json',
            success: function(response) {
                console.log("Server response");
                console.log(response);
                serverMessage = `${response.message}: ${response.status}`;
                displayMessage(statusMessageContainer, serverMessage);
                // Clear form fields
                $('#input-age').val('');
                $('#input-weight').val('');
                $('#input-height').val('');
                $('#input-time').val('');
                $('#input-rate').val('2');
                $('#input-energy').val('1000');
            }
        });
    });
});

//////// Utility functions ////////

// Input fields validatio function
function isGreaterThan (
    field,
    minValue,
    errorMessage,
    messageContainer) {
    field.on(
        'input',
        function() {
        var input = $(this);
        var inputValue = input.val();

        if(inputValue >= minValue) {
            input.removeClass("input-invalid").addClass("input-valid");
            messageContainer.removeClass("input-invalid");
            displayMessage(messageContainer, '');   
        }
        else {
            input.removeClass("input-valid").addClass("input-invalid");
            messageContainer.addClass("input-invalid");
            // Append the error message and show
            messageContainer.val('');
            messageContainer.text(errorMessage);
            messageContainer.animate(
                {"opacity": 100},
                700
            );
            // Remove the error message on focus
            input.on("focus", function() {
                messageContainer.removeClass("input-invalid");
                displayMessage(messageContainer, '');
            });
        };
    });
};

function isBetween (
    field,
    minValue,
    maxValue,
    errorMessage,
    messageContainer) {
    field.on(
        'input',
        function() {
        var input = $(this);
        var inputValue = input.val();

        if(inputValue >= minValue && inputValue <= maxValue) {
            input.removeClass("input-invalid").addClass("input-valid");
            messageContainer.removeClass("input-invalid");
            displayMessage(messageContainer, '');   
        }
        else {
            input.removeClass("input-valid").addClass("input-invalid");
            messageContainer.addClass("input-invalid");
            // Append the error message and show
            messageContainer.val('');
            messageContainer.text(errorMessage);
            messageContainer.animate(
                {"opacity": 100},
                700
            );
            // Remove the error message on focus
            input.on("focus", function() {
                messageContainer.removeClass("input-invalid");
                displayMessage(messageContainer, '');
            });
        };
    });
};

// Function to deisplay confirmation/error messages
function displayMessage (messageContainer, message) {
    messageContainer.val('');
    messageContainer.text(message);

    messageContainer.animate(
        {"opacity": 100},
        700
    );

    messageContainer.animate(
        {"opacity": 0},
        400
    );
};