const API = "http://localhost:8000";

export async function login(email, password) {
  const res = await fetch(`${API}/auth/login?email=${email}&password=${password}`, {
    method: "POST"
  });

  if (!res.ok) throw new Error("Invalid credentials");
  return res.json();
}
