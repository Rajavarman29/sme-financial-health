import { useEffect, useState } from "react";
import { fetchMetrics } from "../api/metrics";
import { getUser } from "../utils/auth";
import MetricsCard from "../components/MetricsCard";

export default function Dashboard() {
  const [metrics, setMetrics] = useState(null);

  useEffect(() => {
    fetchMetrics(getUser()).then(setMetrics);
  }, []);

  if (!metrics) return <p>Loading...</p>;

  return (
    <div>
      <h2>Financial Dashboard</h2>

      <div style={{ display: "flex", gap: "16px", flexWrap: "wrap" }}>
        <MetricsCard title="Net Cash Flow" value={metrics.net_cash_flow} />
        <MetricsCard title="Outstanding Receivables" value={metrics.outstanding_receivables} />
        <MetricsCard title="Outstanding Payables" value={metrics.outstanding_payables} />
      </div>

      <h3>Monthly Revenue</h3>
      <ul>
        {metrics.monthly_revenue.map(m => (
          <li key={m.month}>{m.month}: {m.total}</li>
        ))}
      </ul>

      <h3>Monthly Expenses</h3>
      <ul>
        {metrics.monthly_expenses.map(m => (
          <li key={m.month}>{m.month}: {m.total}</li>
        ))}
      </ul>
    </div>
  );
}
