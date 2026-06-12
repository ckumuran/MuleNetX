import SystemOverview from "./components/SystemOverview";
import RiskLeaderboard from "./components/RiskLeaderboard";
import CommunityExplorer from "./components/CommunityExplorer";
import GraphCanvas from "./components/GraphCanvas";
import InvestigationWorkspace from "./components/InvestigationWorkspace";

export default function App() {

    return (

        <div>

            <SystemOverview />

            <RiskLeaderboard />

            <CommunityExplorer />

            <GraphCanvas />

            <InvestigationWorkspace />

        </div>

    );
}
