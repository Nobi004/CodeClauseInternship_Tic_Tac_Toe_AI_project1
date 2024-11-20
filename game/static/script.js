document.addEventListener("DOMContentLoaded", function () {
    const boardElement = document.getElementById("game-board");
    const restartButton = document.getElementById("restart");

    // Function to render the game board
    function renderBoard(board) {
        boardElement.innerHTML = "";
        board.forEach((row, rowIndex) => {
            row.forEach((cell, colIndex) => {
                const cellDiv = document.createElement("div");
                cellDiv.classList.add("cell");
                cellDiv.dataset.row = rowIndex;
                cellDiv.dataset.col = colIndex;
                cellDiv.textContent = cell || "";
                boardElement.appendChild(cellDiv);
            });
        });
    }

    // Handle cell click
    boardElement.addEventListener("click", function (event) {
        if (event.target.classList.contains("cell")) {
            const row = event.target.dataset.row;
            const col = event.target.dataset.col;

            fetch("/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken, // Include CSRF token in the header
                },
                body: JSON.stringify({ row: parseInt(row), col: parseInt(col) }),
            })
                .then((response) => response.json())
                .then((data) => {
                    renderBoard(data.board);
                    if (data.winner || data.draw) {
                        alert(data.winner ? `${data.winner} Wins!` : "It's a draw!");
                    }
                });
        }
    });

    // Handle restart button click
    restartButton.addEventListener("click", function () {
        fetch("/reset/", {
            method: "POST",
            headers: { "X-CSRFToken": csrfToken }, // Include CSRF token in the header
        }).then(() => {
            renderBoard([
                [null, null, null],
                [null, null, null],
                [null, null, null],
            ]);
        });
    });
});
