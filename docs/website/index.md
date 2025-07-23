# MHS Seals Website Documentation

Author: Alec Jensen

The website is available at [mhsroboboat.com](https://mhsroboboat.com).

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/MHSeals/website2025.git
cd website2025
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to `http://localhost:4321` to view the site.

## Pushing Changes

The website is (as of me writing this) hosted on Cloudflare Pages (on my account, I need to move it to the organization's account), which automatically deploys changes pushed to the `main` branch of this repository.
Because of this, the main branch is protected and requires pull requests to be merged. So you must either fork the repository or create a branch to make changes.

1. Create a new branch:
```bash
git checkout -b my-feature-branch
```

2. Make your changes and commit them:
```bash
git add .
git commit -m "Description of my changes"
```

3. Push your branch to the remote repository:
```bash
git push origin my-feature-branch
```

4. Open a pull request on GitHub to merge your changes into the `main` branch.
5. Once the pull request is approved and merged, your changes will be automatically deployed to the live site.

## Previous Year Pages

The website contains pages for previous years, so you can go back and look at the history of the team. These previous year pages are separate deployments on Cloudflare Pages, and are based on specific branches in this repository. The branches are named `2025`, `2025`, etc., and the deployments are available at [2025.mhsroboboat.com](https://2025.mhsroboboat.com), [2024.mhsroboboat.com](https://2024.mhsroboboat.com), etc.

### Adding a New Year Page to the Website

1. In GitHub, after competition season ends, create a new branch for the next year, e.g., `2025`.
2. In Cloudflare Pages, create a new application
    1. Select `Import a repository`
    2. Select the repository `MHSeals/website2025`
    3. Go to the application settings
    4. Set the production branch to the new branch you created, e.g., `2025`
3. Make sure the DNS is set up correctly for the new year page (Cloudflare Pages should handle this automatically).
4. Navigate to `src\pages\year\[year].astro`
5. Find `export function getStaticPaths()`
6. Add an object to the return, like this: `{ params: { year: "2025" }},`
   replacing `2025` with the year you want to add.

   Example:
```javascript
export function getStaticPaths() {
   return [
         { params: { year: "2025" }},
         { params: { year: "2024" }},
         // Add more years as needed
   ];
}
```
7. Follow the steps in the "Pushing Changes" section to create a pull request and deploy the changes.