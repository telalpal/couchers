import { Divider, Hidden, makeStyles, Typography } from "@material-ui/core";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import classnames from "classnames";
import Button from "components/Button";
import {
  ABOUT_US,
  INTRODUCTION_SUBTITLE,
  INTRODUCTION_TITLE,
  LOGIN,
  SIGN_UP,
} from "features/auth/constants";
import DesktopAuthBg from "features/auth/resources/desktop-auth-bg.png";
import MobileAuthBg from "features/auth/resources/mobile-auth-bg.png";
import useAuthStyles from "features/auth/useAuthStyles";
import React from "react";
import { Link } from "react-router-dom";
import { loginRoute, signupRoute } from "routes";

const useStyles = makeStyles((theme) => ({
  aboutUs: {
    color: "#2a2a2a",
    marginTop: "auto",
  },
  aboutUsLink: {
    color: "#2a2a2a",
    display: "block",
    textDecoration: "none",
    [theme.breakpoints.up("md")]: {
      color: theme.palette.common.white,
      fontWeight: 500,
      fontSize: "1.25rem",
      marginRight: theme.spacing(3),
      padding: theme.spacing(1),
    },
  },
  authPage: {
    alignItems: "flex-end",
    backgroundColor: "#f3f3f3",
    backgroundImage: `url(${MobileAuthBg})`,
    backgroundPosition: "top center",
    backgroundRepeat: "no-repeat",
    backgroundSize: "contain",
    boxSizing: "border-box",
    display: "flex",
    height: "100vh",
    justifyContent: "center",
    padding: `${theme.spacing(1, 4)}`,
    [theme.breakpoints.up("md")]: {
      alignItems: "flex-start",
      backgroundImage: `url(${DesktopAuthBg})`,
      backgroundSize: "cover",
      flexDirection: "column",
      padding: 0,
      width: "100%",
    },
  },
  button: {
    width: "45%",
  },
  content: {
    display: "flex",
    flexDirection: "column",
    height: "50vh",
    justifyContent: "center",
    textAlign: "center",
    [theme.breakpoints.up("md")]: {
      height: "100%",
      margin: "0 auto",
      width: theme.breakpoints.values.md,
    },
  },
  desktopNavigation: {
    display: "flex",
  },
  introduction: {
    color: theme.palette.common.white,
    textAlign: "left",
    width: "72%",
  },
  link: {
    borderRadius: theme.shape.borderRadius / 3,
    color: theme.palette.common.white,
    fontSize: "1.25rem",
    fontWeight: 500,
    textAlign: "center",
    textDecoration: "none",
    padding: theme.spacing(1, 2),
  },
  loginLink: {
    border: `1px solid ${theme.palette.primary.main}`,
    marginRight: theme.spacing(3),
  },
  mobileNavigation: {
    display: "flex",
    justifyContent: "space-around",
    marginTop: theme.spacing(3),
  },
  signupLink: {
    backgroundColor: theme.palette.primary.main,
  },
  subtitle: {
    marginTop: theme.spacing(1),
    [theme.breakpoints.up("md")]: {
      display: "inline-block",
      marginTop: theme.spacing(4),
      position: "relative",
    },
  },
  title: {
    ...theme.typography.h1,
    [theme.breakpoints.up("md")]: {
      fontSize: "4rem",
      lineHeight: "1.15",
      textAlign: "left",
    },
  },
  underline: {
    borderTop: `5px solid ${theme.palette.primary.main}`,
    boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
    left: theme.spacing(1),
    position: "absolute",
    width: "100%",
  },
}));

export default function AuthPage() {
  const classes = useStyles();
  const authClasses = useAuthStyles();

  return (
    <div className={classes.authPage}>
      {/***** MOBILE ******/}
      <Hidden mdUp>
        <div className={classes.content}>
          <Typography variant="h1">{INTRODUCTION_TITLE}</Typography>
          <Typography className={classes.subtitle}>
            {INTRODUCTION_SUBTITLE}
          </Typography>
          <Divider classes={{ root: authClasses.divider }} flexItem />
          <div className={classes.mobileNavigation}>
            <Button
              classes={{
                label: authClasses.buttonText,
              }}
              className={classnames(authClasses.button, classes.button)}
              color="secondary"
              component={Link}
              to={loginRoute}
            >
              {LOGIN}
            </Button>
            <Button
              classes={{
                label: authClasses.buttonText,
              }}
              className={classnames(authClasses.button, classes.button)}
              color="secondary"
              component={Link}
              to={signupRoute}
            >
              {SIGN_UP}
            </Button>
          </div>
          <div className={classes.aboutUs}>
            <Typography className={classes.aboutUsLink} component={Link} to="#">
              {ABOUT_US}
            </Typography>
            <ExpandMoreIcon />
          </div>
        </div>
      </Hidden>

      {/***** DESKTOP ******/}
      <Hidden smDown>
        <header className={authClasses.header}>
          <div className={authClasses.logo}>Couchers.org</div>
          <nav className={classes.desktopNavigation}>
            <Link to="#" className={classes.aboutUsLink}>
              {ABOUT_US}
            </Link>
            <Link
              to={loginRoute}
              className={`${classes.link} ${classes.loginLink}`}
            >
              {LOGIN}
            </Link>
            <Link
              to={signupRoute}
              className={`${classes.link} ${classes.signupLink}`}
            >
              {SIGN_UP}
            </Link>
          </nav>
        </header>
        <div className={classes.content}>
          <div className={classes.introduction}>
            <Typography className={classes.title} variant="h1">
              {INTRODUCTION_TITLE}
            </Typography>
            <Typography className={classes.subtitle} variant="h2">
              {INTRODUCTION_SUBTITLE}
              <Divider className={classes.underline}></Divider>
            </Typography>
          </div>
        </div>
      </Hidden>
    </div>
  );
}
