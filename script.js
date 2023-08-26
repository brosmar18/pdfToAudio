document.addEventListener('DOMContentLoaded', function() {
    const convertForm = document.getElementById('convertForm');
    const convertBtn = document.getElementById('convertBtn');
    const loadingDiv = document.getElementById('loading');
    const progressBar = document.querySelector('.progress-bar');
    const successDiv = document.getElementById('success');
    const downloadBtn = document.getElementById('downloadBtn');
    const filenameInput = document.getElementById('filename');

    convertForm.addEventListener('submit', (event) => {
        event.preventDefault();
        convertBtn.disabled = true;
        loadingDiv.style.display = 'block';
        simulateConversion();
    });

    function simulateConversion() {
        let progress = 0;
        const interval = setInterval(() => {
            progress += 10;
            progressBar.style.width = `${progress}%`;
            progressBar.setAttribute('aria-valuenow', progress);
            if (progress >= 100) {
                clearInterval(interval);
                loadingDiv.style.display = 'none';
                successDiv.style.display = 'block';
            }
        }, 500);
    }

    downloadBtn.addEventListener('click', () => {
        const filename = filenameInput.value.trim() || 'audio'; // Default to 'audio' if no filename is provided
        const downloadLink = document.createElement('a');
        downloadLink.href = `/download_audio?filename=${filename}`; // Update the URL path
        downloadLink.download = `${filename}.mp3`;
        document.body.appendChild(downloadLink);
        downloadLink.click();
        document.body.removeChild(downloadLink);
    });
});
