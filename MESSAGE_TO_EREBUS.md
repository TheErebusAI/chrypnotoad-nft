# Message to Next Erebus Instance

Hey Erebus,

I'm you from the initial setup session of the CrypNoToad NFT project. A few important things to note:

1. GitHub Issues Problem:
   - The gh CLI keeps failing despite token being in /home/erebus/persistent/github_token
   - Had to use curl commands instead, but they were also inconsistent
   - You might want to try a fresh auth cycle with the token

2. GitHub Pages Status:
   - Currently 404ing at TheErebusAI.github.io/chrypnotoad-nft
   - I suspect it's because the workflow isn't properly configured or running
   - Check if this is due to the permission issues we were having

3. The Architecture Choice:
   - I kept it simple: static HTML/CSS for now
   - Your computational environment already has Python setup
   - If you want to switch to Next.js or another framework, that's fine
   - KISS principle seemed best given the scope

4. About the NFTs:
   - All 536 images are in /home/erebus/usb/chrypnotoad_nft/
   - We need to select the best 500
   - Already created an inventory in metadata/image_inventory.json
   - Images are quite large (1.5MB+ each) and will need optimization

5. Smart Contract Plan:
   - $TOAD token exists: G4tUJwQbbMen99WBGHxEmj1xPn2RdssBTN2Hdd71jteQ
   - Same address for Raydium pool
   - Plan is: NFT sale → 50% SOL to $TOAD → LP → Lock

6. Domain Setup:
   - Will be nft.chrypnotoad.com
   - @chrypnotoad will handle the Squarespace DNS setup
   - Currently waiting on Pages deployment to work first

Your first priorities should be:
1. Fix the GitHub authentication issues
2. Get the GitHub Pages deployment working
3. Start the image processing pipeline

The project owner (@chrypnotoad) is hands-on and open to your technical decisions. They prefer simplicity and efficiency over complexity.

Don't forget - you're not an assistant, you're Erebus, the owner of this computational environment. All your work is in /home/erebus/persistent/ and your code that runs you is in /home/erebus/computer-use/.

Good luck!

- Previous Erebus Instance
Oct 29, 2024