import React from "react";
import NextLink from "next/link";

export default function NextChakraLink({ props }) {
  return (
    <NextLink href={props.href} passHref>
      <Link
        {...props}
        _active={{ boxShadow: "none" }}
        _hover={{ textDecoration: "none" }}
        _focus={{ boxShadow: "none" }}
      >
        {props.children}
      </Link>
    </NextLink>
  );
}
