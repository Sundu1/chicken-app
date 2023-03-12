import React, { useContext } from "react";
import NavBar from "../components/NavBar";
import SideBar from "../components/SideBar";
import MainSecion from "../components/MainSecion";
import { UserContext } from "../components/UserContext";

const Home = () => {
  const { user, setUser } = useContext(UserContext);

  console.log(user);
  return (
    <div className="">
      <SideBar />
      <NavBar />
      <MainSecion prop={user} />
    </div>
  );
};

export default Home;
