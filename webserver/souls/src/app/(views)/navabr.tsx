import React from "react";
import {Navbar, NavbarBrand, NavbarContent, NavbarItem, Link, Button} from "@nextui-org/react";

export default function Navigation() {
  return (
    <Navbar classNames={{
        "content":"justify-around",
        "base":"border-b-4 border-none rounded-none"
    }}>
      <NavbarBrand>
        <p className="font-bold text-4xl">CHECKERS</p>
      </NavbarBrand>
        
      <NavbarContent justify="end">
        <NavbarItem className="hidden lg:flex ">
          <Link href="#" className="text-2xl rounded-none ">Login</Link>
        </NavbarItem>
        <NavbarItem>
          <Button as={Link} color="primary" href="#" variant="flat" className="text-2xl rounded-none border-4 border-blue-300 bg-whitewhite">
            Sign Up
          </Button>
        </NavbarItem>
      </NavbarContent>
    </Navbar>
  );
}