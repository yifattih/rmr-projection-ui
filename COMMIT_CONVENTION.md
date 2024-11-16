# Semantic Versioning 2.0.0

Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes
2. MINOR version when you add functionality in a backward compatible manner
3. PATCH version when you make backward compatible bug fixes

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

# **AngularJS Git Commit Message Conventions**

### Commit Message Format

Each commit message should follow this structure:

```
<type>(<scope>): <description>

[optional body]

[optional footer]

```

- **type**: Specifies the purpose of the commit (see below).
- **scope**: Describes the area of the codebase impacted by the commit (e.g., "data-input-form", "auth", "CI").
- **description**: A brief summary of the change (use imperative mood, e.g., "Add" not "Added").
- **body**: (Optional) Detailed description of the change.
- **footer**: (Optional) Notes related to breaking changes or issues closed.

### Commit Types

Use the following commit types in your messages:

- **feat**: A new feature (e.g., `feat(data-input-form): add user input validation`)
- **fix**: A bug fix (e.g., `fix(auth): correct login issue on invalid credentials`)
- **docs**: Documentation-only changes (e.g., `docs(readme): update tech stack section`)
- **style**: Code style changes (formatting, no logic change) (e.g., `style(bmr-calculator): apply standard formatting`)
- **refactor**: Code changes that neither fix a bug nor add a feature (e.g., `refactor(auth): optimize login flow`)
- **perf**: A code change that improves performance (e.g., `perf(bmr-calculator): reduce calculation time`)
- **test**: Adding or updating tests (e.g., `test(api): add tests for BMR calculator endpoint`)
- **build**: Changes to build or CI/CD system (e.g., `build(ci): integrate Google Cloud Run`)
- **ci**: Changes to the CI configuration or scripts (e.g., `ci(github-actions): add linting step`)
- **chore**: Minor tasks, such as updating dependencies or cleaning up files (e.g., `chore(deps): update dependencies`)
- **revert**: Revert a previous commit (e.g., `revert: revert commit <hash>`)

### Branch-Specific Guidelines

### main (CI/CD)

- **Purpose**: Production-ready code.
- **Commit Logs**: Concise release summaries.
- **Merge Requirements**: Merge from **beta**; ensure all commits are squashed and rebased for a clean history.
- **Tagging**: Use semantic versioning tags (e.g., `v1.0.0`) for each release.

### beta (CI/CD)

- **Purpose**: User testing environment.
- **Commit Logs**: Only tested features or bug fixes ready for user testing.
- **Merge Requirements**: Merge from **alpha**; use rebase to keep history linear.
- **Tagging**: Tag each feature as it’s merged for user testing (e.g., `v1.0.0-beta.1`).

### alpha (CI/CD)

- **Purpose**: Internal testing environment.
- **Commit Logs**: Contains alpha-tested features or bug fixes.
- **Merge Requirements**: Merge from **dev**; rebase on **alpha** before merging into **beta**.
- **Tagging**: Use tags to denote alpha releases, such as `v1.0.0-alpha.1`.

### dev (CI)

- **Purpose**: Continuous integration branch.
- **Commit Logs**: Only contains rebased and squashed commits with the exact feature added or bug fixed, ready for CI.
- **Merge Requirements**: Only rebased commits from **feat** branches; rebase and squash to combine multiple commits into one before merging.
- **Tagging**: Use tags to indicate testing phases or intermediate tags if helpful (e.g., `v1.0.0-rc.1` for release candidates).

### feat (CI)

- **Purpose**: Feature development or bug fix.
- **Commit Logs**: Frequent, detailed commits during feature development.
- **Merge Requirements**: Rebase onto **dev** before merging. Ensure commit history is clean and rebased.
- **Tagging**: No tagging required; use the **feat** branch for development and testing through CI pipeline.

### Example Commit Messages with Tags

- `feat(bmr-calculator): add new chart for BMR trends`
    - When merged to **dev**: Tag as `v1.0.0-rc.1`
- `fix(data-input-form): handle incorrect input gracefully`
    - When merged to **alpha**: Tag as `v1.0.0-alpha.2`
- `docs(readme): update tech stack section`
    - When merged to **main** for release: Tag as `v1.0.0`

### Rebase Workflow

- **feat** branches should be rebased on **dev** before merging, keeping commit history clean.
- **dev** branch merges should be rebased and squashed into single commits to **alpha**, reducing clutter in higher branches.
- For **alpha** and **beta**, rebase each merge to maintain linear history before promotion.

### Example of Tagging and Commit Convention

Using the **AngularJS Commit Convention** with your custom tags, here’s how you can format your commits with tags.

### 1. `main` Branch Example (Production-Ready Release)

```bash
# Merging to `main` and creating a production-ready tag
git checkout main
git merge dev  # Assuming dev is up-to-date and ready for release
git tag -a v1.0.0 -m "chore(release): release v1.0.0 with new feature A and bug fixes"
git push origin main --tags

```

**Commit Example in `main`:**

```
chore(release): release v1.0.0 with new feature A and bug fixes

```

For a production-ready release with a breaking change, merge to `main`, tag it with the new version, and use `BREAKING CHANGE:` in the footer.

```bash
# Merging to `main` and creating a production-ready tag
git checkout main
git merge dev  # Assuming dev is up-to-date and ready for release
git tag -a v2.0.0 -m "feat: overhaul authentication system

BREAKING CHANGE: The authentication API has been changed from OAuth 1.0 to OAuth 2.0. All clients must update their authentication flow."
git push origin main --tags

```

**Commit Example in `main`:**

```
feat: overhaul authentication system

BREAKING CHANGE: The authentication API has been changed from OAuth 1.0 to OAuth 2.0. All clients must update their authentication flow.

```

### 2. `beta` Branch Example (User Testing)

```bash
# Merging to `beta` branch and creating a beta tag
git checkout beta
git merge dev  # Assuming dev is ready for beta testing
git tag -a v1.0.0-beta.1 -m "chore(release): release v1.0.0-beta.1 for user testing"
git push origin beta --tags

```

**Commit Example in `beta`:**

```
chore(release): release v1.0.0-beta.1 for user testing

```

For a user testing release that includes a breaking change, tag with a `-beta` suffix and add the breaking change footer.

```bash
# Merging to `beta` branch and creating a beta tag
git checkout beta
git merge dev  # Assuming dev is ready for beta testing
git tag -a v2.0.0-beta.1 -m "feat: refactor database structure

BREAKING CHANGE: The database schema has been modified. Existing migrations need to be reapplied, and all data must be backed up."
git push origin beta --tags

```

**Commit Example in `beta`:**

```
feat: refactor database structure

BREAKING CHANGE: The database schema has been modified. Existing migrations need to be reapplied, and all data must be backed up.

```

### 3. `alpha` Branch Example (Internal Testing)

```bash
# Merging to `alpha` and creating an alpha tag
git checkout alpha
git merge dev  # Assuming dev is ready for alpha testing
git tag -a v1.0.0-alpha.1 -m "chore(release): release v1.0.0-alpha.1 for internal testing"
git push origin alpha --tags

```

**Commit Example in `alpha`:**

```
chore(release): release v1.0.0-alpha.1 for internal testing

```

For an internal testing release in `alpha`, use an `-alpha` suffix and include the breaking change footer to notify of any critical updates.

```bash
# Merging to `alpha` and creating an alpha tag
git checkout alpha
git merge dev  # Assuming dev is ready for alpha testing
git tag -a v2.0.0-alpha.1 -m "fix: update API endpoints to RESTful standards

BREAKING CHANGE: All API endpoints have been updated to follow RESTful standards. This change will break any old endpoint URLs."
git push origin alpha --tags

```

**Commit Example in `alpha`:**

```
fix: update API endpoints to RESTful standards

BREAKING CHANGE: All API endpoints have been updated to follow RESTful standards. This change will break any old endpoint URLs.

```

### 4. `dev` Branch Example (Continuous Integration)

For `dev`, you might use a pre-release tag without incrementing the main version:

```bash
# Tagging on dev branch after merging new features or fixes
git checkout dev
git merge feat/new-feature-branch  # Assuming the feature branch is tested and approved
git tag -a v1.0.0-dev.1 -m "feat: add new feature B"
git push origin dev --tags

```

**Commit Example in `dev`:**

```
feat: add new feature B

```

For development (`dev`) branch commits, tag with `-dev` and include a breaking change footer when applicable.

```bash
# Tagging on dev branch after merging a feature with a breaking change
git checkout dev
git merge feat/new-feature-branch  # Assuming the feature branch is tested and approved
git tag -a v2.0.0-dev.1 -m "refactor: improve logging framework

BREAKING CHANGE: Replaced the old logging library with a new framework. Custom log formatting options need to be reconfigured."
git push origin dev --tags

```

**Commit Example in `dev`:**

```
refactor: improve logging framework

BREAKING CHANGE: Replaced the old logging library with a new framework. Custom log formatting options need to be reconfigured.

```

### AngularJS Commit Format Examples for Tags

Each tag message can reflect the type of changes based on AngularJS-style prefixes:

- **`feat`**: A new feature
- **`fix`**: A bug fix
- **`chore`**: Routine tasks or minor changes (like version increments)
- **`docs`**: Documentation changes
- **`style`**: Code style (e.g., formatting)
- **`refactor`**: Refactoring code
- **`test`**: Adding or updating tests
- **`BREAKING CHANGE:`**: Placed in the footer, with a clear description