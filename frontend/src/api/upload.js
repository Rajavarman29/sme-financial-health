const API = "http://localhost:8000";

export async function uploadFile(file, userId) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API}/upload/?user_id=${userId}`, {
    method: "POST",
    body: formData
  });

  if (!res.ok) throw new Error("Upload failed");
  return res.json();
}
