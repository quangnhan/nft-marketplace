const { buildModule } = require("@nomicfoundation/hardhat-ignition/modules");

const OWNER = "0x5BF421d1b035a7FC4cF9436CBC42AA122A05749B"

module.exports = buildModule ("NFTModules", (m) => {
    const nft = m.contract("NFT", [OWNER]);

    return { nft };
});