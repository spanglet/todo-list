// fetch.js

// Base URL of Flask backend, defined in .env file
const base_url = import.meta.env.VITE_BACKEND_BASE_URL;

// Backend API uses only JSON payload type
const httpHeaders = new Headers( {
  'Content-Type': 'application/json'
})


// fetch() wrapper for communicating with backend API
async function doFetch(url, method, body) {

  // Request object to be passed to fetch()
  const req = new Request(base_url + url, {
    method: method,
    headers: httpHeaders,
    credentials: 'include',
    body: JSON.stringify(body),
  })

  var data = await fetch(req)
    .then((res) => res.json())
    .catch((err) => alert(err))

  return data

}


// class containing all custom fetch() methods (for axios-style method use)
export default { 

  get(url) {
    return doFetch(url, 'GET')
  },
  post(url, body) {
    return doFetch(url, 'POST', body)
  },
  put(url, body) {
    return doFetch(url, 'PUT', body)
  },
  delete(url) {
    return Fetch(url, 'POST', body)
  }
}
