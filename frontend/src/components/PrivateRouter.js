import React from "react";
import { Navigate } from "react-router-dom";

const PrivateRouter = ({ children }) => {
  const test = false;

  return test ? children : <Navigate to="/" />;
};

export default PrivateRouter;
