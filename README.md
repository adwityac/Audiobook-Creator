<h1>Audiobook Creator</h1>

<p>Welcome to the <strong>Audiobook Creator</strong> application! This Python-based tool allows you to convert PDF documents into audio files using text-to-speech technology.</p>

<h2>Features</h2>
<ul>
    <li><strong>PDF to Audio Conversion</strong>: Easily convert any PDF file to an audio format (MP3).</li>
    <li><strong>Voice Selection</strong>: Choose between a male or female voice for the audio.</li>
    <li><strong>User-Friendly Interface</strong>: Simple and intuitive GUI built with Tkinter.</li>
</ul>

<h2>Requirements</h2>
<p>To run this application, you need the following Python libraries:</p>
<ul>
    <li><code>tkinter</code></li>
    <li><code>PyPDF2</code></li>
    <li><code>pyttsx3</code></li>
</ul>
<p>You can install the required libraries using pip:</p>
<pre><code>pip install PyPDF2 pyttsx3</code></pre>

<h2>How to Use</h2>
<ol>
    <li><strong>Run the Application</strong>: Execute the script to launch the Audiobook Creator GUI.</li>
    <li><strong>Select a PDF File</strong>: 
        <ul>
            <li>Click the <strong>Browse a File</strong> button to choose a PDF document from your system.</li>
        </ul>
    </li>
    <li><strong>Choose Voice</strong>: 
        <ul>
            <li>Select either <strong>Male Voice</strong> or <strong>Female Voice</strong> using the checkboxes.</li>
        </ul>
    </li>
    <li><strong>Create and Save Audio File</strong>: 
        <ul>
            <li>Click the <strong>Create and Save the Audio File</strong> button.</li>
            <li>Choose a location to save your audio file (default is MP3 format).</li>
        </ul>
    </li>
    <li><strong>Audio Generation</strong>: 
        <ul>
            <li>The application will generate the audio file. A message will confirm when the audio file is saved.</li>
        </ul>
    </li>
</ol>

<h2>Notes</h2>
<ul>
    <li>Ensure that the PDF file you select contains extractable text; otherwise, the audio generation may not work as expected.</li>
    <li>The application supports basic error handling, informing you if a PDF file is not selected or if an issue occurs during processing.</li>
</ul>

<h2>License</h2>
<p>This project is open source and available for anyone to use and modify. Contributions are welcome!</p>

<h2>Acknowledgments</h2>
<p>Thanks to the creators of the libraries used in this project: <a href="https://pypi.org/project/PyPDF2/">PyPDF2</a> and <a href="https://pypi.org/project/pyttsx3/">pyttsx3</a>.</p>
