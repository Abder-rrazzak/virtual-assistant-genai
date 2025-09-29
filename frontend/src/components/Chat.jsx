import { useState } from "react";

function Chat() {
  const [messages, setMessages] = useState([]);
  const [query, setQuery] = useState("");

  const sendMessage = async () => {
    if (!query) return;

    // Ajoute le message utilisateur
    setMessages([...messages, { role: "user", content: query }]);

    // Appel API FastAPI
    const res = await fetch("http://localhost:8000/api/v1/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    });
    const data = await res.json();

    // Ajoute la réponse de l'assistant
    setMessages((prev) => [
      ...prev,
      { role: "assistant", content: data.response },
    ]);

    setQuery("");
  };

  return (
    <div className="flex flex-col h-[80vh] p-4">
      <div className="flex-1 overflow-y-auto space-y-2 mb-4">
        {messages.map((m, i) => (
          <div
            key={i}
            className={`p-2 rounded-lg max-w-lg ${
              m.role === "user"
                ? "bg-blue-100 self-end text-right"
                : "bg-gray-200 self-start text-left"
            }`}
          >
            {m.content}
          </div>
        ))}
      </div>

      <div className="flex gap-2">
        <input
          className="flex-1 border rounded-lg p-2"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Écris ton message..."
        />
        <button
          onClick={sendMessage}
          className="bg-blue-500 text-white px-4 py-2 rounded-lg"
        >
          Envoyer
        </button>
      </div>
    </div>
  );
}

export default Chat;
