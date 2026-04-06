async function detectEmotion(event) {

    if (event) {
        event.preventDefault();
    }

    console.log("Sending file...");

    const fileInput = document.getElementById("audioFile");

    if (!fileInput || fileInput.files.length === 0) {
        alert("Please select an audio file");
        return;
    }

    const formData = new FormData();
    formData.append("audio", fileInput.files[0]);

    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Analyzing emotion...";

    try {

        const response = await fetch("/detect-emotion" , {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        console.log(data);

        resultDiv.innerHTML = "🎧 Detected Emotion: " + data.emotion;

    } catch (error) {

        console.error(error);
        resultDiv.innerHTML = "Error detecting emotion";

    }
}


// lyrics_analysis code 

let mediaRecorder
let audioChunks = []

async function startRecording() {

    const stream = await navigator.mediaDevices.getUserMedia({ audio: true })

    mediaRecorder = new MediaRecorder(stream)

    audioChunks = []

    mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data)
    }

    mediaRecorder.start()

    document.getElementById("recordingStatus").innerHTML = "Recording..."
}

function stopRecording() {

    mediaRecorder.stop()

    mediaRecorder.onstop = async () => {

        const audioBlob = new Blob(audioChunks, { type: "audio/webm" })

        const formData = new FormData()

        formData.append("audio", audioBlob, "recording.webm")

        document.getElementById("recordingStatus").innerHTML = "Processing..."

        const response = await fetch("/analyze-audio", {
            method: "POST",
            body: formData
        });
        
        const data = await response.json();

        document.getElementById("recordingStatus").innerHTML = "";

        // playlist variable
        let playlistHTML = "<b>Recommended Playlist:</b><br>";

        data.playlist.forEach(song => {

        playlistHTML += "<a style='color:black;font-family:serif;font-weight:bold;font-style:italic;' href='" 
        + song.youtube + 
        "' target='_blank'>" + 
        song.title + 
        "</a><br>";

        });

        document.getElementById("textResult").innerHTML =
        "<b>Transcript:</b> " + data.transcript + "<br>" +
        "<b>Emotion:</b> " + data.emotion;

        document.getElementById("playlistBox").innerHTML = playlistHTML;
        }}

// plagiarism detection code

async function checkPlagiarism(){

const fileInput = document.getElementById("plagiarismFile")

if(!fileInput.files.length){
alert("Upload a song")
return
}

const formData = new FormData()
formData.append("audio", fileInput.files[0])

document.getElementById("plagiarismResult").innerHTML="Analyzing melody..."

const response = await fetch("/check-plagiarism",{
method:"POST",
body:formData
})

const data = await response.json()

document.getElementById("plagiarismResult").innerHTML =
"Most similar song: "+data.match_song+"<br>"+
"Similarity: "+data.similarity+"%"
}


// ============== Regional music genre detection =============

function detectRegion(){

let file = document.getElementById("regionAudio").files[0]

let formData = new FormData()

formData.append("audio", file)

document.getElementById("regionResult").innerHTML = "Detecting region..."

fetch("/detect-region",{
method:"POST",
body:formData
})
.then(res=>res.json())
.then(data=>{

document.getElementById("regionResult").innerHTML =
"<b>Language:</b> " + data.language + "<br>" +
"<b>Region:</b> " + data.region

})
}

// ================= MUSIC GENRE IDENTIFICATION =================

function detectGenre(){

let file = document.getElementById("genreAudio").files[0]

if(!file){
alert("Please upload an audio file")
return
}

let formData = new FormData()

formData.append("audio", file)

fetch("/detect-genre",{
method:"POST",
body:formData
})
.then(res=>res.json())
.then(data=>{

document.getElementById("genreResult").innerHTML =
"<b>Detected Genre:</b> " + data.genre

})
.catch(err=>{
console.log(err)
})

}