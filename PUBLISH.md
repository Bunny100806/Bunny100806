# SAI GitHub — Cinematic Motion Edition

This ZIP is for your **existing** profile repository: `Bunny100806/Bunny100806`. It is NOT a new repository.

## What's new

- Large editorial SVG hero with independent moving rings, animated text entrance, glow, and sliding light.
- Animated AegisTwin and ArchAgent-R showcase graphics, HackYeah award, experience, technologies, Kaggle, and footer.
- `scripts/build_activity.py` and `.github/workflows/contribution-flight.yml` generate the activity SVG **from real GitHub contributions**, then show a decorative moving aircraft across it.
- The initial `activity-flight.svg` is intentionally labeled decorative until the first successful workflow run.
- All artwork is original and self-contained SVG; no JavaScript is required to play it on GitHub.

## Recommended publishing method (GitHub Desktop)

1. Download and extract this ZIP.
2. **Clone your existing** `Bunny100806/Bunny100806` repository in GitHub Desktop, if not already cloned.
3. Copy `README.md`, `assets/`, `scripts/`, and `.github/` from this ZIP into the cloned folder.
4. Keep your old root SVG files for now; the new README references `./assets/` so no old path conflicts matter.
5. Review changes in GitHub Desktop. **Do not include the preview PNG images** in a commit; only `.svg` files are needed from `assets/`.
6. Commit: `Introduce cinematic SVG motion and real contribution flight`. Push origin.
7. In GitHub, open your repository's **Actions** tab, choose **Refresh real contribution flight**, then **Run workflow**. GitHub may require you to enable Actions first.
8. If the workflow fails with `403 Resource not accessible by integration`, go to Settings → Actions → General → Workflow permissions and permit **Read and write permissions** if your repository policy allows it. Rerun workflow.
9. Open `https://github.com/Bunny100806` and check that SVGs actually animate in your browser. GitHub image caching and reduced-motion settings may affect playback.

## Important

- This recreates the reference's **technique and editorial feel** with original graphics; it does not copy her images/source or pretend to be the same person.
- This is a GitHub README, not an interactive website: arbitrary JavaScript, scroll triggers, clickable embedded SVG controls, video backgrounds, and page CSS are not available.
- All contribution counts displayed by the finished workflow derive from the GitHub GraphQL API. Private activity may not be included in the public GraphQL response.
- Never commit a token, personal phone number, or private resume details.
- The user-provided Kaggle link is displayed without invented medals or rankings.
- A headshot was not supplied, so the hero uses an original typographic SCN monogram instead of guessing a portrait.
