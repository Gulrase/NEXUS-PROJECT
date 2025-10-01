import React from "react";
import Chat from "./components/Chat";

export default function App(){
  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <header className="max-w-3xl mx-auto">
        <h1 className="text-2xl font-bold">Student Wellbeing Prototype</h1>
        <p className="text-sm text-gray-600">AI-based mental health support — demo prototype</p>
      </header>
      <main className="max-w-3xl mx-auto mt-6">
        <Chat />
      </main>
    </div>
  );
}
