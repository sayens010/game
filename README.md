<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Suki Family</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: green;
            margin: 0;
        }
        .game-container {
            text-align: center;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input[type="text"] {
            padding: 10px;
            width: 200px;
            margin: 10px 0;
            border: 1px solid grey;
            border-radius: 5px;
        }
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: #007BFF;
            color: black;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>Game Kuis Suki</h1>
        <p id="question"></p>
        <input type="text" id="answer" placeholder="Masukkan jawabanmu">
        <button onclick="checkAnswer()">Submit</button>
        <p id="feedback"></p>
        <p>Skor: <span id="score">0</span></p>
        <p>Total Benar: <span id="correct">0</span></p>
        <p>Total Salah: <span id="wrong">0</span></p>
    </div>

    <script>
        const questions = [
            { question: "Siapa menteri kominfo saat ini?", answer: "Gak ada" },
            { question: "Matahari termasuk?", answer: "Bintang" },
            { question: "Siapa penulis Harry Potter?", answer: "J.k Rowling" },
            { question: "Siapa penemu teori Black Hole?", answer: "Htephen Hawking" },
            { question: "Benda apa yang bisa terbang tanpa mesin?", answer: "Burung" },
            { question: "Negara dengan populasi unta terbanyak?", answer: "Australia" },
            { question: "Sebutkan hewan mamalia terbesar?", answer: "Paus biru" },
            { question: "Apa hasil dari 7 x 8?", answer: "56" },
            { question: "Wakil prisiden ke 5?", answer: "Soedharmono" },
            { question: "Apa ibu kota turki?", answer: "Ankara" }
        ];

        let currentQuestionIndex = 0;
        let score = 0;
        let correctAnswers = 0;
        let wrongAnswers = 0;

        function loadQuestion() {
            const questionElement = document.getElementById("question");
            questionElement.textContent = questions[currentQuestionIndex].question;
        }

        function checkAnswer() {
            const answerInput = document.getElementById("answer");
            const feedbackElement = document.getElementById("feedback");
            const scoreElement = document.getElementById("score");
            const correctElement = document.getElementById("correct");
            const wrongElement = document.getElementById("wrong");

            if (answerInput.value.toLowerCase() === questions[currentQuestionIndex].answer.toLowerCase()) {
                feedbackElement.textContent = "Jawaban benar!";
                feedbackElement.style.color = "green";
                score += 100;
                correctAnswers++;
            } else {
                feedbackElement.textContent = "Jawaban salah.";
                feedbackElement.style.color = "red";
                score -=50;
                wrongAnswers++;
            }

            scoreElement.textContent = score;
            correctElement.textContent = correctAnswers;
            wrongElement.textContent = wrongAnswers;

            answerInput.value = "";
            currentQuestionIndex = (currentQuestionIndex + 1) % questions.length;
            loadQuestion();
        }

        window.onload = loadQuestion;
    </script>
</body>
</html>
