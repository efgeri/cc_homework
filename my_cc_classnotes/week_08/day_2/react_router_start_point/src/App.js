import { BrowserRouter, Routes, Route } from "react-router-dom";
import React, {useState} from "react";
import Home from "./components/Home";
import About from "./components/About";
import Pricing from "./components/Pricing";
import NavBar from "./components/NavBar";
import Tobyvore from "./components/Tobyvore";
import ErrorPage from "./components/ErrorPage";
import Choice from "./components/Choice";

let initialPricing = [
  { level: "Hobby", cost: 0 },
  { level: "Startup", cost: 10 },
  { level: "Enterprise", cost: 100 }
];


const App = () => {
  const [pricing, setPricing] = useState(initialPricing);
  return (
    <BrowserRouter>
    <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/pricing" element={<Pricing pricing={pricing}/>} />
        <Route path="/tobivore" element={<Tobyvore />} />
        <Route path="/choices/:choice" element={<Choice/>}/>
        <Route path="*" element={<ErrorPage/>}/>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
