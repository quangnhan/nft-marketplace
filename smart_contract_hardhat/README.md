# Sample Hardhat Project

This project demonstrates a basic Hardhat use case. It comes with a sample contract, a test for that contract, and a Hardhat Ignition module that deploys that contract.

Try running some of the following tasks:

```shell
npx hardhat help
npx hardhat test
npx hardhat compile
REPORT_GAS=true npx hardhat test
npx hardhat node

# Set env
npx hardhat vars set INFURA_API_KEY
npx hardhat vars set SEPOLIA_PRIVATE_KEY

npx hardhat vars get INFURA_API_KEY
npx hardhat vars list
# Deploy
npx hardhat ignition deploy ./ignition/modules/NFT.js --network localhost
npx hardhat ignition deploy ./ignition/modules/NFT.js --network sepolia
```
