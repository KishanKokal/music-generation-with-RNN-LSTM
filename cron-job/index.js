const cron = require("node-cron");
const axios = require("axios");

// Define your API endpoint URL
const apiUrl = "https://music-generation-with-rnn-lstm.onrender.com";

// Define the cron schedule to run every minute
cron.schedule("*/10 * * * * *", async () => {
  try {
    // Make a GET request to the API
    const response = await axios.get(apiUrl);

    // Process the response data
    console.log("API Response:", response.data);

    // You can add further processing here if needed
  } catch (error) {
    console.error("Error fetching data:", error.message);
  }
});
