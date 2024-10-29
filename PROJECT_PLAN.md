# CrypNoToad NFT Project Plan

## Immediate Tasks

### Domain Setup (@chrypnotoad)
1. Log into Squarespace
2. Go to Settings > Domains
3. Add custom subdomain:
   - Create CNAME record for 'nft'
   - Point to: thewebusai.github.io
   - TTL: 3600 (or default)

### Infrastructure
- [x] Set up GitHub repository
- [x] Create basic project structure
- [x] Create coming soon page
- [ ] Enable GitHub Pages
- [ ] Configure DNS
- [ ] Set up monitoring

## Development Tracks

### 1. NFT Asset Processing
- [ ] Optimize 536 images for web (target ~500KB)
- [ ] Generate consistent naming scheme
- [ ] Create metadata JSON for each NFT
- [ ] Upload to IPFS/Arweave
- [ ] Create mapping database
- [ ] Generate rarity scores
- [ ] Create trait distribution analysis

### 2. Smart Contract Development
- [ ] Create NFT contract using Metaplex
- [ ] Implement minting logic with whitelist
- [ ] Add $TOAD token integration
- [ ] Implement LP pool mechanics
- [ ] Add treasury split logic
- [ ] Set up test environment
- [ ] Create deployment scripts

Contract References:
- $TOAD: G4tUJwQbbMen99WBGHxEmj1xPn2RdssBTN2Hdd71jteQ
- Raydium Pool: G4tUJwQbbMen99WBGHxEmj1xPn2RdssBTN2Hdd71jteQ

### 3. Website Development
Phase 1 - Coming Soon:
- [x] Create basic coming soon page
- [ ] Deploy to GitHub Pages
- [ ] Add analytics
- [ ] Add mailing list signup

Phase 2 - Main Website:
- [ ] Design main layout
- [ ] Implement wallet connection
- [ ] Create minting interface
- [ ] Add collection gallery
- [ ] Add rarity guide
- [ ] Implement minting status tracking
- [ ] Add tokenomics information

### 4. Documentation & Marketing
- [ ] Technical documentation
- [ ] Smart contract audit report
- [ ] Tokenomics explanation
- [ ] Minting guide
- [ ] FAQ
- [ ] Social media assets
- [ ] Press kit
- [ ] Collection story

### 5. Testing & Security
- [ ] Smart contract tests
- [ ] Security audit
- [ ] Load testing
- [ ] Cross-browser testing
- [ ] Mobile responsiveness
- [ ] Wallet connection testing

## Notes
- Using KISS principle: Simple static HTML/CSS for frontend
- Python environment already set up for backend tasks
- 536 total images, need to select best 500
- Average image size currently ~1.5MB