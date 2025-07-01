<script>
// Configuration
const API_BASE_URL = window.location.origin;

async function fetchEmails() {
  const fetchBtn = document.getElementById('fetch-btn');
  const btnText = document.getElementById('btn-text');
  const loading = document.getElementById('loading');
  const emailResultsDiv = document.getElementById('email-results');
  const emailStatsDiv = document.getElementById('email-stats');

  try {
    // Show loading state
    fetchBtn.disabled = true;
    btnText.textContent = 'Fetching Emails...';
    loading.style.display = 'inline-block';
    emailResultsDiv.innerHTML = '<div class="loading-message">Loading emails...</div>';

    // Fetch sorted emails from the backend
    const response = await fetch(`${API_BASE_URL}/api/emails/gmail`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    const sortedEmails = data.sorted_emails;

    // Clear previous results
    emailResultsDiv.innerHTML = '';
    
    // Calculate and display stats
    displayEmailStats(sortedEmails, emailStatsDiv);
    
    // Display sorted emails
    displaySortedEmails(sortedEmails, emailResultsDiv);

  } catch (error) {
    console.error('Error fetching emails:', error);
    emailResultsDiv.innerHTML = `
      <div class="error-message">
        <h3>❌ Error Loading Emails</h3>
        <p>${error.message}</p>
        <p>Please check your server connection and try again.</p>
      </div>
    `;
  } finally {
    // Reset button state
    fetchBtn.disabled = false;
    btnText.textContent = 'Fetch and Sort Emails';
    loading.style.display = 'none';
  }
}

function displayEmailStats(sortedEmails, statsDiv) {
  const totalEmails = Object.values(sortedEmails).reduce((total, emails) => total + emails.length, 0);
  
  if (totalEmails === 0) {
    statsDiv.style.display = 'none';
    return;
  }

  const statsHtml = `
    <div class="stats-container">
      <h3>📊 Email Statistics</h3>
      <div class="stats-grid">
        <div class="stat-item">
          <span class="stat-number">${totalEmails}</span>
          <span class="stat-label">Total Emails</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">${sortedEmails.high_priority?.length || 0}</span>
          <span class="stat-label">High Priority</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">${sortedEmails.work_emails?.length || 0}</span>
          <span class="stat-label">Work Emails</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">${sortedEmails.spam_emails?.length || 0}</span>
          <span class="stat-label">Spam Detected</span>
        </div>
      </div>
    </div>
  `;
  
  statsDiv.innerHTML = statsHtml;
  statsDiv.style.display = 'block';
}

function displaySortedEmails(sortedEmails, resultsDiv) {
  const categoryOrder = ['high_priority', 'work_emails', 'personal_emails', 'low_priority', 'spam_emails'];
  const categoryIcons = {
    high_priority: '🔥',
    work_emails: '💼',
    personal_emails: '👤',
    low_priority: '📧',
    spam_emails: '🗑️'
  };
  
  const categoryNames = {
    high_priority: 'High Priority',
    work_emails: 'Work Emails',
    personal_emails: 'Personal Emails',
    low_priority: 'Low Priority',
    spam_emails: 'Spam Emails'
  };

  categoryOrder.forEach(category => {
    if (sortedEmails[category] && sortedEmails[category].length > 0) {
      const categoryDiv = document.createElement('div');
      categoryDiv.classList.add('email-category');
      
      const icon = categoryIcons[category] || '📁';
      const name = categoryNames[category] || category.replace('_', ' ').toUpperCase();
      
      categoryDiv.innerHTML = `
        <div class="category-header">
          <h3>${icon} ${name}</h3>
          <span class="email-count">${sortedEmails[category].length} emails</span>
        </div>
      `;

      const emailsList = document.createElement('div');
      emailsList.classList.add('emails-list');
      
      sortedEmails[category].forEach((email, index) => {
        const emailItem = document.createElement('div');
        emailItem.classList.add('email-item');
        
        emailItem.innerHTML = `
          <div class="email-header">
            <span class="email-sender">${email.sender || 'Unknown Sender'}</span>
            <span class="email-number">#${index + 1}</span>
          </div>
          <div class="email-subject">${email.subject || 'No Subject'}</div>
          ${email.category ? `<div class="email-category-tag">${email.category}</div>` : ''}
        `;
        
        emailsList.appendChild(emailItem);
      });
      
      categoryDiv.appendChild(emailsList);
      resultsDiv.appendChild(categoryDiv);
    }
  });
  
  // Show message if no emails
  if (resultsDiv.children.length === 0) {
    resultsDiv.innerHTML = `
      <div class="no-emails-message">
        <h3>📭 No Emails Found</h3>
        <p>No emails were retrieved. This might be because:</p>
        <ul>
          <li>Gmail API is not properly configured</li>
          <li>No emails match the current filters</li>
          <li>Authentication is required</li>
        </ul>
      </div>
    `;
  }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
  console.log('Email Organizer initialized');
});
</script>
