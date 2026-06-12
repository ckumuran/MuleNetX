import SystemOverview from "./components/SystemOverview";
import RiskLeaderboard from "./components/RiskLeaderboard";
import CommunityExplorer from "./components/CommunityExplorer";
import GraphInvestigation from "./components/GraphInvestigation";
import InvestigationWorkspace from "./components/InvestigationWorkspace";

export default function App() {

    return (

        <div>

            <SystemOverview />

            <RiskLeaderboard />

            <CommunityExplorer />

            <GraphInvestigation />

            <InvestigationWorkspace />

        </div>

    );
}
