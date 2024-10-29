# CrypNoToad NFT Collection

A Solana-based NFT collection with innovative tokenomics that builds $TOAD token liquidity through NFT sales.

## Project Structure

```
├── assets/
│   ├── raw/         # Original NFT images
│   └── processed/   # Processed and optimized images
├── contracts/
│   ├── nft/         # Solana NFT contract
│   └── token/       # $TOAD token and LP contracts
├── website/
│   ├── frontend/    # React-based minting website
│   └── backend/     # API and server components
├── metadata/        # NFT metadata and collection info
└── scripts/         # Utility scripts for processing
```

## Tokenomics

- 500 unique NFTs
- Each NFT sale:
  - 50% of SOL → $TOAD token buy
  - Bought $TOAD → Added to LP
  - LP tokens locked
