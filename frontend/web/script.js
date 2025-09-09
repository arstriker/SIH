// Wait for the DOM to be fully loaded before attaching event listeners
document.addEventListener('DOMContentLoaded', () => {

    // --- 1. DOM Element Selection ---
    // Advice Section
    const getAdviceButton = document.getElementById('get-advice-button');
    const adviceContainer = document.getElementById('advice-container');

    // Diagnosis Section
    const imageInput = document.getElementById('image-input');
    const imagePreview = document.getElementById('image-preview');
    const diagnoseButton = document.getElementById('diagnose-button');
    const diagnosisResult = document.getElementById('diagnosis-result');

    // Diary Section
    const diaryInput = document.getElementById('diary-input');
    const logDiaryButton = document.getElementById('log-diary-button');
    const diaryConfirmation = document.getElementById('diary-confirmation');

    // --- 2. API Configuration ---
    // This should be the address of the running FastAPI backend.
    // For local development, this is typically the correct address.
    const API_BASE_URL = 'http://127.0.0.1:8000';

    // --- 3. Event Listeners ---
    getAdviceButton.addEventListener('click', fetchAdvice);
    diagnoseButton.addEventListener('click', submitDiagnosis);
    logDiaryButton.addEventListener('click', submitDiaryEntry);
    imageInput.addEventListener('change', previewSelectedImage);

    // --- 4. Functions ---

    /**
     * Reads the selected image file and displays it in the preview element.
     */
    function previewSelectedImage() {
        const file = imageInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.src = e.target.result;
                imagePreview.classList.remove('hidden');
            };
            reader.readAsDataURL(file);
        }
    }

    /**
     * Fetches and displays personalized farming advice from the backend.
     */
    async function fetchAdvice() {
        adviceContainer.innerHTML = '<p>Fetching advice...</p>';
        try {
            const response = await fetch(`${API_BASE_URL}/get_advice`);
            if (!response.ok) throw new Error(`Server responded with status: ${response.status}`);

            const data = await response.json();

            let adviceHTML = '<ul>';
            data.advice_list.forEach(item => {
                adviceHTML += `<li>${item.task}</li>`;
            });
            adviceHTML += '</ul>';
            adviceContainer.innerHTML = adviceHTML;

        } catch (error) {
            adviceContainer.innerHTML = `<p style="color: red;">Failed to fetch advice. Is the backend server running?</p><p style="font-size: 0.8em;">${error.message}</p>`;
        }
    }

    /**
     * Submits the selected image to the backend for diagnosis.
     */
    async function submitDiagnosis() {
        const file = imageInput.files[0];
        if (!file) {
            diagnosisResult.innerHTML = `<p style="color: orange;">Please select an image first.</p>`;
            return;
        }

        diagnosisResult.innerHTML = '<p>Analyzing image...</p>';

        const formData = new FormData();
        formData.append('image', file);

        try {
            const response = await fetch(`${API_BASE_URL}/diagnose`, {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) throw new Error(`Server responded with status: ${response.status}`);

            const data = await response.json();

            let remediesHTML = '<ul>';
            data.remedies.forEach(remedy => {
                remediesHTML += `<li><strong>${remedy.type}:</strong> ${remedy.description}</li>`;
            });
            remediesHTML += '</ul>';

            diagnosisResult.innerHTML = `
                <h3>${data.disease_name}</h3>
                <p><strong>Confidence:</strong> ${(data.confidence_score * 100).toFixed(0)}%</p>
                <p>${data.description}</p>
                <h4>Recommended Actions:</h4>
                ${remediesHTML}
            `;

        } catch (error) {
            diagnosisResult.innerHTML = `<p style="color: red;">Diagnosis failed. Is the backend server running?</p><p style="font-size: 0.8em;">${error.message}</p>`;
        }
    }

    /**
     * Submits the user's text input to the backend to be logged in the diary.
     */
    async function submitDiaryEntry() {
        const text = diaryInput.value.trim();
        if (!text) {
            diaryConfirmation.innerHTML = `<p style="color: orange;">Please enter an activity log.</p>`;
            return;
        }

        diaryConfirmation.innerHTML = '<p>Saving entry...</p>';

        const formData = new FormData();
        formData.append('text', text);

        try {
            const response = await fetch(`${API_BASE_URL}/log_diary`, {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) throw new Error(`Server responded with status: ${response.status}`);

            const data = await response.json();
            const entry = data.logged_entry;

            diaryConfirmation.innerHTML = `
                <p><strong>Diary Updated! (Simulated)</strong></p>
                <p>Action: <strong>${entry.action || 'N/A'}</strong>, Item: <strong>${entry.item || 'N/A'}</strong>, Quantity: <strong>${entry.quantity || 'N/A'}</strong>, Cost: <strong>${entry.cost || 'N/A'}</strong></p>
            `;
            diaryInput.value = ''; // Clear the textarea

        } catch (error) {
            diaryConfirmation.innerHTML = `<p style="color: red;">Failed to save diary entry. Is the backend server running?</p><p style="font-size: 0.8em;">${error.message}</p>`;
        }
    }
});
