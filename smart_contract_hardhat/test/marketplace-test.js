const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Marketplace", function () {

  let acc1, acc2;
  let marketplaceAddress;
  let nftAddress;
  let nft;
  let nftMarketplace;
  let listPrice = ethers.parseEther("0.01", "ether");

  beforeEach(async function () {

    [acc1, acc2, acc3] = await ethers.getSigners();
    
    const Marketplace = await ethers.getContractFactory("Marketplace");
    nftMarketplace = await Marketplace.deploy(acc1.address);
    await nftMarketplace.waitForDeployment();
    marketplaceAddress = await nftMarketplace.getAddress();

    const NFT = await ethers.getContractFactory("NFT");
    nft = await NFT.deploy(acc1.address);
    await nft.waitForDeployment();
    nftAddress = await nft.getAddress();
    
  });

  it("Should list an NFT onto the marketplace", async function () {
    
    // Mint a new NFT to acc2
    await nft.safeMint(acc2.address, "META_DATA_URI");
    tokenId = 0
    owner = await nft.ownerOf(tokenId);
    expect(owner).to.equal(acc2.address);

    // Give marketplace approval permission
    await nft.connect(acc2).approve(marketplaceAddress, tokenId);
    approval = await nft.getApproved(tokenId);
    expect(approval).to.equal(marketplaceAddress);

    // Listing NFT to marketplace
    await nftMarketplace.connect(acc2).createListing(tokenId, nftAddress, listPrice); //0.01 MATIC
    marketplaceItemId = 0
    item = await nftMarketplace.getMarketItem(marketplaceItemId)
    expect(item.marketplaceId).to.equal(marketplaceItemId);
    expect(item.nftAddress).to.equal(nftAddress);
    expect(item.tokenId).to.equal(tokenId);
    expect(item.seller).to.equal(acc2.address);
    expect(item.owner).to.equal("0x0000000000000000000000000000000000000000");
    expect(item.listPrice).to.equal(listPrice);
  });

  it("Should sell an active NFT listed on the marketplace ", async function () {

    // Create NFT in collections and listing it in marketplace
    await nft.safeMint(acc2.address, "META_DATA_URI");
    tokenId = 0
    await nft.connect(acc2).approve(marketplaceAddress, tokenId);
    await nftMarketplace.connect(acc2).createListing(tokenId, nftAddress, listPrice); //0.01 MATIC

    // Buy item
    marketplaceItemId = 0
    await expect(
      await nftMarketplace
        .connect(acc3)
        .buyListing(marketplaceItemId, nftAddress, { value: listPrice })
    )
    
    // Item was transfered from acc2 to acc3
    item = await nftMarketplace.getMarketItem(marketplaceItemId);
    expect(item.owner).to.equal(acc3.address);
  });

  it("Test a market sale that does not send sufficient funds", async function () {

    await nft.safeMint(acc2.address, "META_DATA_URI");
    tokenId = 0
    await nft.connect(acc2).approve(marketplaceAddress, tokenId);
    await nftMarketplace.connect(acc2).createListing(tokenId, nftAddress, listPrice);

    // Buy item
    marketplaceItemId = 0
    await expect(
        nftMarketplace
        .connect(acc3)
        .buyListing(marketplaceItemId, nftAddress, { value:  ethers.parseEther("0.02", "ether")})
    ).to.be.revertedWith(
      "Value sent does not meet list price for NFT"
    );

    item = await nftMarketplace.getMarketItem(marketplaceItemId);

    expect(item.owner).to.equal("0x0000000000000000000000000000000000000000");
  });
});