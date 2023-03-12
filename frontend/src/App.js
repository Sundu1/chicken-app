import "./App.css";
import "./components/NavBar";
import NavBar from "./components/NavBar";
import SideBar from "./components/SideBar";
import MainSecion from "./components/MainSecion";

function App() {
  return (
    <div className="">
      <SideBar />
      <NavBar />
      <MainSecion />
    </div>
  );
}

export default App;
