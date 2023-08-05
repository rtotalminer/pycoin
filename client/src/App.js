import Header from "./components/Header";
import LatestBlocks from "./components/LatestBlocks";
import LatestTxs from "./components/LatestTxs";
import Overview from "./components/Overview";

import Grid from '@mui/material/Grid';

function App() {
  const styles = {
    content: {
      paddingLeft: "15em",
      paddingRight: "15em",
    }
  };

  return (
    <div>
      <Header/>
      <br></br>
      <div className="content" style={styles.content}>
        <Overview/>
        <br></br>
        <Grid container spacing={2}>
          <Grid item xs={6} md={6}>
            <LatestBlocks/>
          </Grid>
          <Grid item xs={6} md={6}>
            <LatestBlocks/>
          </Grid>
        </Grid>
      </div>
    </div>
  );
}

export default App;
