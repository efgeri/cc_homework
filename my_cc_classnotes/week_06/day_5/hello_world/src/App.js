import React from "react"; // 1️⃣
import "./App.css"; // 2️⃣

function App() {
  const age = 32;              
  const name = "Geri";        
  // 3️⃣
  // we can write JS here :)  // 4️⃣

  return (
    // 5️⃣
    <div>
    <h1 className="title">Hello World!</h1>
    <p> This is a paragraph of text</p>
    <p> My name is {name} and I'm {age} years old</p>
  </div>  // 6️⃣
  ); // 7️⃣
} // 8️⃣

export default App; // 9️⃣
