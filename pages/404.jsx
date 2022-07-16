import React from "react";
import { Heading } from "@chakra-ui/react";
import NextChakraLink from "../components/NextChakraLink";

export default function fourOfour() {
  return (
    <>
      <Heading as="h1">404 Page is not Found. RIP</Heading>
      <Heading as="h3">BEEP BOOP BKSBFAKJBSKDJABJKSD</Heading>
      <NextChakraLink href="/">
        Go back to where you came from lol
      </NextChakraLink>
    </>
  );
}
