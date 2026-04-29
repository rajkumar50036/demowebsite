const axios = require('axios');
const schedule = require('node-schedule');

// --- Configuration ---
const ANTISPACE_API_KEY = 'your_antispace_api_key_here';
const ANTISPACE_API_URL = 'https://api.antispace.com/v1/tasks'; // Replace with actual URL
const SHEET_NAME = 'OxyCare_Patient_Leads';

let processedLeads = new Set();
let leadsToday = 0;

/**
 * Mock function to fetch new leads from your sheet.
 * In a real app, use the 'googleapis' or 'google-spreadsheet' npm package to connect to Google Sheets.
 */
async function fetchNewLeads() {
    console.log(`[${new Date().toISOString()}] Checking for new leads in ${SHEET_NAME}...`);
    
    // TODO: Connect to Google Sheets and fetch rows
    // Return mock data for now
    return []; 
}

/**
 * Creates a high-priority task in the Antispace dashboard.
 */
async function createAntispaceTask(lead) {
    console.log(`Creating high-priority Antispace task for lead: ${lead.name || 'Unknown'}`);
    
    const payload = {
        title: `Verify Notification for New Lead: ${lead.name || 'Unknown'}`,
        priority: 'High',
        description: `A new lead was added. Please verify their notification was sent.\nDetails: ${JSON.stringify(lead)}`
    };

    try {
        // Uncomment below to actually make the API call to Antispace
        /*
        const response = await axios.post(ANTISPACE_API_URL, payload, {
            headers: {
                'Authorization': `Bearer ${ANTISPACE_API_KEY}`,
                'Content-Type': 'application/json'
            }
        });
        console.log('Task created successfully.');
        */
    } catch (error) {
        console.error('Failed to create task:', error.message);
    }
}

/**
 * Sends the 8 PM daily summary of leads.
 */
function sendDailySummary() {
    console.log('\n--- 8 PM DAILY SUMMARY ---');
    console.log(`Total leads received today: ${leadsToday}`);
    console.log('Sending summary notification (You can integrate SendGrid for email or Twilio for SMS here)...');
    
    // Reset counter for the next day
    leadsToday = 0;
}

/**
 * Main monitoring loop
 */
async function monitorLeads() {
    try {
        const newLeads = await fetchNewLeads();
        
        for (const lead of newLeads) {
            // Assume each lead has a unique 'id' or use row number
            if (!processedLeads.has(lead.id)) {
                await createAntispaceTask(lead);
                processedLeads.add(lead.id);
                leadsToday++;
            }
        }
    } catch (error) {
        console.error('Error monitoring leads:', error);
    }
}

// 1. Run the lead monitor every 5 minutes
console.log('Starting Lead Automation Monitor...');
monitorLeads(); // Run once immediately
setInterval(monitorLeads, 5 * 60 * 1000);

// 2. Schedule the daily summary for 8:00 PM every day (using node-schedule cron syntax)
schedule.scheduleJob('0 20 * * *', () => {
    sendDailySummary();
});
