
// JavaScript code to handle the button click event
        const colors = ["#FF5733", "#33FF57", "#5733FF", "#33FFFF", "#FFFF33"];
        let currentIndex = 0;

        const changeBackgroundColor = () => {
            // Get the body element
            const body = document.body;

            // Change the background color to the next color in the array
            body.style.backgroundColor = colors[currentIndex];

            // Increment the index or reset it to 0 if it exceeds the array length
            currentIndex = (currentIndex + 1) % colors.length;
        };

        // Add a click event listener to the button
        const button = document.getElementById("changeColorButton");
        button.addEventListener("click", changeBackgroundColor);
