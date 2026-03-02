const BASE = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:8000'

let _token = localStorage.getItem('wc_token') || null

function setToken(t) {
  _token = t
  if (t) localStorage.setItem('wc_token', t)
  else localStorage.removeItem('wc_token')
}

function authHeaders() {
  return _token ? { Authorization: `Bearer ${_token}` } : {}
}

export async function healthCheck() {
  const res = await fetch(`${BASE}/health`)
  return await res.json().catch(() => ({ status: res.status }))
}

export async function registerUser(email, password) {
  const res = await fetch(`${BASE}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  })
  return await res.json().catch(() => ({ status: res.status }))
}

export async function loginUser(email, password) {
  const res = await fetch(`${BASE}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  })
  const j = await res.json().catch(() => ({ status: res.status }))
  if (j && j.access_token) setToken(j.access_token)
  return j
}

export function logout() { setToken(null) }

export async function getMe() {
  const res = await fetch(`${BASE}/auth/me`, { headers: { ...authHeaders() } })
  return await res.json().catch(() => ({ status: res.status }))
}

export function getToken() { return _token }
