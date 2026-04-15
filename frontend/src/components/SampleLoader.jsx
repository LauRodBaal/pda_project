import { useEffect, useState } from "react";
import { getSamples } from "../api/pdaApi";

export default function SampleLoader() {
  const [samples, setSamples] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchSamples() {
      try {
        const data = await getSamples();
        setSamples(data.samples || []);
      } catch (err) {
        setError("Failed to load samples from backend.");
      }
    }

    fetchSamples();
  }, []);

  return (
    <div>
      <h2>Available Samples</h2>

      {error && <p>{error}</p>}

      {samples.length === 0 && !error ? (
        <p>Loading samples...</p>
      ) : (
        <ul>
          {samples.map((sample) => (
            <li key={sample}>{sample}</li>
          ))}
        </ul>
      )}
    </div>
  );
}