import https from 'https';

const API_TOKEN = "7d563982e5e0be438575aae70773a4a60fce2d19";
const API_URL = "https://api.qualcomm.com/v1/models/riffusion";

export async function generateSpectrogram(prompt: string): Promise<string> {
  const data = JSON.stringify({
    prompt,
    style: "cartoon",
    intensity: 0.7,
  });

  const options = {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${API_TOKEN}`,
      'Content-Type': 'application/json',
    },
    timeout: 30000, // 30 second timeout
  };

  return new Promise((resolve, reject) => {
    const req = https.request(API_URL, options, (res) => {
      let responseData = '';

      res.on('data', (chunk) => {
        responseData += chunk;
      });

      res.on('end', () => {
        if (res.statusCode !== 200) {
          console.error(`API Error: ${res.statusCode} - ${responseData}`);
          reject(new Error(`API returned status code ${res.statusCode}`));
          return;
        }

        try {
          const data = JSON.parse(responseData);
          resolve(data.spectrogram);
        } catch (error) {
          console.error('Failed to parse API response:', error);
          reject(new Error('Invalid API response format'));
        }
      });
    });

    req.on('error', (error) => {
      console.error('Request error:', error);
      reject(error);
    });

    req.write(data);
    req.end();
  });
}