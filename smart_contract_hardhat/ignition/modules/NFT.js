const { buildModule } = require("@nomicfoundation/hardhat-ignition/modules");

const OWNER = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"

module.exports = buildModule ("NFTModules", (m) => {
    const nft = m.contract("NFT", [OWNER]);

    return { nft };
});