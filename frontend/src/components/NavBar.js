import React from "react";

const NavBar = () => {
  return (
    <div className="fixed top-0 left-[257px] w-[100%] bg-white border-b-[3px] h-[85px] text-white">
      <div className="flex justify-between items-center h-full mr-[20em]">
        <div className="text-black">search</div>
        <div className="flex">
          <div className="text-black p-2">notification</div>
          <div className="text-black p-2">user</div>
        </div>
      </div>
    </div>
  );
};

export default NavBar;
