export default function MetricsCard({ title, value }) {
  return (
    <div style={{
      border: "1px solid #ddd",
      padding: "16px",
      borderRadius: "8px",
      minWidth: "200px"
    }}>
      <h4>{title}</h4>
      <strong>{value}</strong>
    </div>
  );
}
