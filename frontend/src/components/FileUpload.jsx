import { useState } from "react";
import { uploadFile } from "../api/upload";
import { getUser } from "../utils/auth";

export default function FileUpload() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const handleUpload = async () => {
    if (!file) return;
    try {
      await uploadFile(file, getUser());
      setStatus("Upload successful");
    } catch {
      setStatus("Upload failed");
    }
  };

  return (
    <div>
      <input
        type="file"
        accept=".csv,.xlsx"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button onClick={handleUpload}>Upload</button>
      <p>{status}</p>
    </div>
  );
}
