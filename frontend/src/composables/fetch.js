// fetch.js
import { ref } from 'vue'

// Base URL of Flask backend, defined in .env file
const base_url = import.meta.env.VITE_BACKEND_BASE_URL;

const httpHeaders = new Headers( {
  'Content-Type': 'application/json'
})

//fetch wrapper composable for reuse in components
export function useFetch(url, method, body) {

  console.log(url)

  // Request object to be passed to fetch()
  const req = new Request(base_url + url, {
    method: method,
    headers: httpHeaders,
    credentials: 'include',
    body: JSON.stringify(body),
  })

  const data = ref(null)
  const error = ref(null)

  fetch(req)
    .then((res) => res.json())
    .then((json) => (data.value = json))
    .catch((err) => (error.value = err))

  return { data, error }
}


