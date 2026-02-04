import { useState } from "react";
import Login from "./pages/Login";
import Upload from "./pages/Upload";
import Dashboard from "./pages/Dashboard";
import { getUser } from "./utils/auth";

export default function App() {
  const [loggedIn, setLoggedIn] = useState(!!getUser());

  if (!loggedIn) {
    return <Login onLogin={() => setLoggedIn(true)} />;
  }

  return (
    <>
      <Upload />
      <Dashboard />
    </>
  );
}
