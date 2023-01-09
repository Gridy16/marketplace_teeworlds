const { ethers } = require("hardhat");
const hre = require("hardhat");
const fs = require("fs");

async function main() {
  //get the signer that we will use to deploy
  const [deployer] = await ethers.getSigners();
  
  //Get the NFTMarketplace smart contract object and deploy it
  const NFT_Teeworlds = await hre.ethers.getContractFactory("NFT_Teeworlds");

  const nft_teeworlds = await NFT_Teeworlds.deploy();

  await nft_teeworlds.deployed();

  console.log("Smart contract address ", nft_teeworlds.address)
  
  //Pull the address and ABI out while you deploy, since that will be key in interacting with the smart contract later
  const data = {
    address: nft_teeworlds.address,
    abi: JSON.parse(nft_teeworlds.interface.format('json'))
  }

  //This writes the ABI and address to the nft_teeworlds.json
  //This data is then used by frontend files to connect with the smart contract
  fs.writeFileSync('./src/abis/nft_teeworlds.json', JSON.stringify(data))
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });