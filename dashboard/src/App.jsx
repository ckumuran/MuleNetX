import { useEffect, useState } from "react";

import BootSequence from "./components/BootSequence";
import GraphCanvas from "./components/GraphCanvas";
import SystemPanel from "./components/SystemPanel";
import EventFeed from "./components/EventFeed";

export default function App() {

  const [loading, setLoading] = useState(true);

  const graph = {
    nodes: [
      { id: "ACC-8842", risk: 94 },
      { id: "ACC-3371", risk: 82 },
      { id: "ACC-5519", risk: 71 },
      { id: "KNOWN-BAD", risk: 99 }
    ],

    edges: [
      {
        source: "ACC-8842",
        target: "KNOWN-BAD"
      },

      {
        source: "ACC-3371",
        target: "ACC-8842"
      },

      {
        source: "ACC-5519",
        target: "ACC-3371"
      }
    ]
  };

  if (loading) {
    return (
      <BootSequence
        onComplete={() => setLoading(false)}
      />
    );
  }

  return (
    <div
      style={{
        width: "100%",
        height: "100vh",
        background: "#000",
        position: "relative",
        overflow: "hidden"
      }}
    >
      <GraphCanvas data={graph} />

      <SystemPanel />

      <EventFeed />

      <div className="scanlines" />
    </div>
  );
}
