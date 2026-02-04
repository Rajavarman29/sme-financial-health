const API = "http://localhost:8000";

export async function fetchMetrics(userId) {
  const res = await fetch(`${API}/metrics/?user_id=${userId}`);
  if (!res.ok) throw new Error("Failed to fetch metrics");
  return res.json();
}
