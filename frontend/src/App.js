import { useMemo, useState } from "react";
import { Link, Route, Router, Routes } from "react-router-dom";
import "./App.css";
import { UserContext, useLocalStorage } from "./components/UserContext";
import Home from "./pages/Home";
import LoginPage from "./pages/LoginPage";

function App() {
  const [user, setUser] = useLocalStorage("name", "Bob");

  return (
    <div className="">
      <UserContext.Provider value={{ user, setUser }}>
        <Routes>
          <Route path="/login" element={<LoginPage />}></Route>
          <Route path="/home" element={<Home />}></Route>
        </Routes>
      </UserContext.Provider>
    </div>
  );
}

export default App;
