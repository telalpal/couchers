import { Divider, Hidden, makeStyles, Typography } from "@material-ui/core";
import React from "react";

const useStyles = makeStyles((theme) => ({
  divider: {
    border: "3px solid rgba(246, 138, 12, 0.7)",
    boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
    left: theme.spacing(1),
    position: "absolute",
    width: "100%",
  },
  header: {
    marginBottom: theme.spacing(4),
    position: "relative",
  },
  typography: {
    [theme.breakpoints.up("md")]: {
      marginTop: 0,
    },
  },
}));

export default function AuthHeader(props: { children: React.ReactNode }) {
  const classes = useStyles();

  return (
    <div className={classes.header}>
      <Typography variant="h1" className={classes.typography}>
        {props.children}
      </Typography>
      <Hidden mdUp>
        <Divider className={classes.divider} />
      </Hidden>
    </div>
  );
}
