import express from "express";
import cors from "cors";
import fs from "fs";

const app = express();

app.use(cors());

const graph = JSON.parse(
  fs.readFileSync("./data/graph.json", "utf-8")
);

app.get("/api/graph", (req, res) => {
  res.json(graph);
});

app.get("/api/status", (req, res) => {

  res.json({
    topology: "ONLINE",
    anomalyEngine: "ACTIVE",
    propagation: "RUNNING",
    graphNodes: graph.nodes.length,
    graphEdges: graph.edges.length
  });

});

app.listen(5000, () => {
  console.log("MuleNetX API running on port 5000");
});
