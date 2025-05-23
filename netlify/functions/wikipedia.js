// netlify/functions/wikipedia.js

exports.handler = async function(event) {
  const query = event.path.replace(/^\/+/, '');

  if (!query) {
    return {
      statusCode: 400,
      body: 'Please provide a topic in the URL path, e.g. /Microsoft',
    };
  }

  const encodedQuery = encodeURIComponent(query.replace(/ /g, '_'));
  const url = `https://en.wikipedia.org/api/rest_v1/page/summary/${encodedQuery}`;

  try {
    const response = await fetch(url);
    if (!response.ok) {
      return {
        statusCode: response.status,
        body: 'Page not found or error.',
      };
    }
    const data = await response.json();
    return {
      statusCode: 200,
      headers: { 'Content-Type': 'text/plain' },
      body: data.extract || 'No summary available.',
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: 'Internal server error.',
    };
  }
};
