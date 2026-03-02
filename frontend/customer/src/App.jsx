import React, { useState } from 'react'
import { healthCheck, registerUser, loginUser } from './api'

export default function App() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState('')

  return (
    <div className="container">
      <h1>WindowClean — Customer</h1>
      <div style={{display:'flex', gap:8}}>
        <button onClick={async () => { const r = await healthCheck(); setMessage(JSON.stringify(r)) }}>Health</button>
        <button onClick={async () => { const r = await getMe(); setMessage(JSON.stringify(r)) }}>Whoami</button>
      </div>

      <h2>Register</h2>
      <input placeholder="email" value={email} onChange={e => setEmail(e.target.value)} />
      <input placeholder="password" type="password" value={password} onChange={e => setPassword(e.target.value)} />
      <button onClick={async () => { const r = await registerUser(email, password); setMessage(JSON.stringify(r)) }}>Register</button>

      <h2>Login</h2>
      <div style={{display:'flex', gap:8}}>
        <button onClick={async () => { const r = await loginUser(email, password); setMessage(JSON.stringify(r)) }}>Login</button>
        <button onClick={() => { logout(); setMessage('logged out') }}>Logout</button>
      </div>

      <pre className="output">{message}</pre>
    </div>
  )
}
