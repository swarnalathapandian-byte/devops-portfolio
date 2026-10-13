# DevOps GitHub Portfolio Starter Kit

Tailored for a DevOps Engineer with MBRDI experience. **This is a starter kit, not an already-published GitHub profile.**

## Contents

- `profile/README.md` — GitHub profile introduction
- `website/` — responsive static portfolio for GitHub Pages
- `projects/python-ci-validator/` — Python CI demo with unit tests
- `projects/terraform-aws-starter/` — safe Terraform AWS starter
- `projects/kubernetes-deployment/` — Docker + Kubernetes demo
- `.github/workflows/python-tests.yml` — example GitHub Actions workflow

## Publish your GitHub profile

1. Create a public GitHub repository named **exactly your GitHub username**.
2. Copy `profile/README.md` into the repository root as `README.md`.
3. Replace `YOUR_USERNAME`, `YOUR_LINKEDIN`, and `YOUR_EMAIL@example.com`.
4. Remove any skills or accomplishments you don't want to claim publicly.

## Publish your portfolio website

1. Create a public repository named `devops-portfolio`.
2. Copy the contents of `website/` into its root.
3. Replace placeholder GitHub, LinkedIn and email links in `index.html`.
4. In GitHub, go to **Settings → Pages → Build and deployment**, choose **Deploy from a branch**, select `main` and `/ (root)`, and save.
5. Your site should be available at `https://YOUR_USERNAME.github.io/devops-portfolio/` once deployment finishes.

## Publish the sample projects

Create public repos named `python-ci-validator`, `terraform-aws-starter` and `kubernetes-deployment`; copy each matching directory into its repository. To enable the Python test workflow in its standalone repository, copy `.github/workflows/python-tests.yml` and remove the `working-directory` setting because the files will be at the repo root.

**Important:** Run, test, and customize each project before calling it a completed personal project. Never upload proprietary MBRDI source, credentials, internal URLs, or confidential architecture diagrams.
