import React from "react";
import axios from "axios";
import LoginPage from "../pages/LoginPage";

const getUsers = async () => {
  try {
    const url = "http://127.0.0.1:8000/api/users";
    const options = {
      auth: {
        username: "admin",
        password: "admin",
      },
    };
    const response = await axios.get(url, options);
    const data = await response.data;
    return data;
  } catch (err) {
    console.error(err);
  }
};

export { getUsers };
