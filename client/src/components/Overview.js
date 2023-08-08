import React, { useState, useEffect } from 'react';

import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import { styled } from '@mui/material/styles';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(2),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));

export default function Overview() {
  
  const [pycoinVersion, setPycoinVersion] = useState([]);
  const [supply, setSupply] = useState([]);
  const [maxSupply, setMaxSupply] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/blockchain')
       .then((response) => response.json())
       .then((data) => {
          console.log(data.curr_supply);
          setSupply(data.curr_supply);
          setMaxSupply(data.max_supply);
       })
       .catch((err) => {
       });
 }, []);


  return (
    <Card sx={{ minWidth: 275 }}>
      <CardContent>
        <Grid container spacing={2}>
          <Grid item md={3} sm={12}>
            <Item>{supply} / {maxSupply}</Item>
          </Grid>
          <Grid item xs={3}>
            <Item>Blocks</Item>
          </Grid>
          <Grid item xs={3}>
            <Item>Transactions</Item>
          </Grid>
          <Grid item xs={3}>
            <Item>Nodes</Item>
          </Grid>
          
        </Grid>
      </CardContent>
    </Card>
  );
}