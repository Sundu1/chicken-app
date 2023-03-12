import { useMemo, useState } from "react";
import { Link, Route, Router, Routes } from "react-router-dom";
import "./App.css";
import { UserContext } from "./components/UserContext";
import Home from "./pages/Home";
import LoginPage from "./pages/LoginPage";

function App() {
  const [user, setUser] = useState(null);

  const providerValue = useMemo(
    () => ({
      user,
      setUser,
    }),
    [user, setUser]
  );

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
