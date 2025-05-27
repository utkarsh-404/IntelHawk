document.addEventListener('DOMContentLoaded', () => {
    let currentModule = null;

    // Module click handler
     document.querySelectorAll('.module-card').forEach(card => {
        card.addEventListener('click', () => {
            currentModule = card.dataset.module;
            const container = document.getElementById('moduleContainer');
            const title = card.querySelector('h3').textContent;
            
            // Update UI
            document.getElementById('moduleTitle').textContent = title;
            document.getElementById('targetInput').placeholder = getPlaceholder(currentModule);
            container.classList.remove('hidden');
            
            // Reset previous state
            document.getElementById('targetInput').value = '';
            document.getElementById('resultsSection').classList.add('hidden');
        });
    });

    // Scan handler
    document.getElementById('startScan').addEventListener('click', async () => {
        const target = document.getElementById('targetInput').value.trim();
        const output = document.getElementById('resultsOutput');
        const resultsSection = document.getElementById('resultsSection');

        if (!target) {
            output.textContent = 'Please enter a target first!';
            output.style.color = '#ff4444';
            resultsSection.classList.remove('hidden');
            return;
        }

        try {
            output.textContent = 'Scanning...';
            output.style.color = '#ffffff';
            resultsSection.classList.remove('hidden');

            const response = await fetch(`/scan/${currentModule}`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ target })
            });

            const data = await response.json();
            output.textContent = JSON.stringify(data, null, 2);
            output.style.color = data.error ? '#ff4444' : '#00ff00';

        } catch (error) {
            output.textContent = `Error: ${error.message}`;
            output.style.color = '#ff4444';
        }
    });

    document.addEventListener('DOMContentLoaded', () => {
    let currentModule = null;


    // Scan handler
    document.getElementById('startScan').addEventListener('click', async () => {
        const target = document.getElementById('targetInput').value.trim();
        const output = document.getElementById('resultsOutput');
        const resultsSection = document.getElementById('resultsSection');

        if (!target) {
            output.textContent = 'Please enter a target first!';
            output.style.color = '#ff4444';
            resultsSection.classList.remove('hidden');
            return;
        }

        try {
            output.textContent = 'Scanning...';
            output.style.color = '#ffffff';
            resultsSection.classList.remove('hidden');

            const response = await fetch(`/scan/${currentModule}`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ target })
            });

            if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
            
            const data = await response.json();
            output.textContent = JSON.stringify(data, null, 2);
            output.style.color = data.error ? '#ff4444' : '#00ff00';

        } catch (error) {
            output.textContent = `Error: ${error.message}`;
            output.style.color = '#ff4444';
            console.error('Scan Error:', error);
        }
    });

    // Helper function for placeholders
    function getPlaceholder(module) {
        const placeholders = {
            nmap: 'Enter IP/Domain (e.g. 192.168.1.1 or scanme.nmap.org)',
            breach: 'Enter email address',
            whois: 'Enter domain name (e.g. example.com)',
            subdomains: 'Enter domain name (e.g. example.com)',
            email: 'Enter domain to harvest emails from',
            tech: 'Enter website URL (e.g. https://example.com)',
            virustotal: 'Enter URL/IP/Domain to scan',
            geoip: 'Enter IP address'
        };
        return placeholders[module] || 'Enter target';
    }
});

// Update download handler
// static/js/app.js
document.getElementById('downloadReport').addEventListener('click', () => {
    const content = document.getElementById('resultsOutput').textContent;
    
    if (!content || content.includes('Scanning...')) {
        alert('No results available to download!');
        return;
    }

    try {
        const blob = new Blob([content], { type: 'text/plain' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        
        a.href = url;
        a.download = `IntelHawk-Report-${currentModule}-${new Date().toISOString()}.txt`;
        document.body.appendChild(a);
        a.click();
        
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
        
    } catch (error) {
        console.error('Download failed:', error);
        alert('Download failed. Check console for details.');
    }
});

    // Close handler
    document.querySelector('.close-module').addEventListener('click', () => {
        document.getElementById('moduleContainer').classList.add('hidden');
    });
});