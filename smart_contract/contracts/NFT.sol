// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

import {ERC721} from "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract NatNFT is ERC721 {
    constructor() ERC721("NATSolutions", "NAT") {
    }
}
