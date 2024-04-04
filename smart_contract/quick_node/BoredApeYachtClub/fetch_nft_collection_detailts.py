from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('https://silent-powerful-sunset.quiknode.pro/1b4b2ca8e8106b992d01400a71e0ba35810091e2/'))
resp = w3.provider.make_request('qn_fetchNFTCollectionDetails', {
  "contracts": [
    "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D",
  ]
})
print(resp)
