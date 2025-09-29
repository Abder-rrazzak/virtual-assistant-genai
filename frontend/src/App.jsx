import Chat from "./components/Chat";

function App() {
  return (
    <div className="flex items-center justify-center h-screen bg-gray-50">
      <div className="w-full max-w-2xl shadow-lg rounded-lg bg-white">
        <Chat />
      </div>
    </div>
  );
}

export default App;
