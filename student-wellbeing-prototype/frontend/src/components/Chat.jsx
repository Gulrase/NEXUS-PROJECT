import React, { useState } from "react";

export default function Chat() {
  const [text, setText] = useState("");
  const [msgs, setMsgs] = useState([]);

  async function send() {
    if (!text) return;
    const userMsg = { from: "user", text };
    setMsgs((m) => [...m, userMsg]);
    setText("");
    try {
      const res = await fetch("http://localhost:8000/chat/message", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({user_id: "demo-user", message: text})
      });
      const j = await res.json();
      setMsgs((m) => [...m, { from: "bot", text: j.reply }]);
    } catch (err) {
      setMsgs((m) => [...m, { from: "bot", text: "Error contacting backend." }]);
    }
  }

  return (
    <div className="bg-white p-4 shadow rounded">
      <div className="h-80 overflow-auto border p-2">
        {msgs.map((m,i) => (
          <div key={i} className={`my-2 ${m.from==="user" ? "text-right" : "text-left"}`}>
            <div className={`inline-block px-3 py-2 rounded ${m.from==="user" ? "bg-blue-500 text-white" : "bg-gray-100 text-gray-800"}`}>
              {m.text}
            </div>
          </div>
        ))}
      </div>
      <div className="mt-2 flex gap-2">
        <input className="flex-1 p-2 border rounded" value={text} onChange={e=>setText(e.target.value)} placeholder="Say something..." />
        <button className="px-4 py-2 bg-blue-600 text-white rounded" onClick={send}>Send</button>
      </div>
    </div>
  );
}
