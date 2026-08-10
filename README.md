# 🚀 Daily GitHub Contribution Booster

Automatically generate between **12 and 50 contributions every day** to keep your GitHub contribution graph active and green! 🟩

---

## 🌟 How It Works

1. **GitHub Actions Cloud Scheduler**: Runs every day automatically at `03:00 UTC` (or whenever triggered manually).
2. **Commit Generator Script (`commit.js`)**: Selects a random count $N \in [12, 50]$, writes timestamped activity updates to `data/contributions.log`, and creates $N$ individual commits with realistic messages.
3. **Pushes to GitHub**: Updates your repository on GitHub, directly adding 12–50 commits to your daily contribution graph!

---

## 🛠️ Quick Setup Guide

### 1. Initialize Git Repository (if not already done)
Open your terminal in this folder (`d:\Program Files\Github-Up`) and run:

```bash
git init
git add .
git commit -m "feat: initial setup for daily contribution booster"
```

### 2. Create a Repository on GitHub & Push

1. Go to [GitHub - New Repository](https://github.new).
2. Name your repository (e.g., `github-contribution-booster` or `github-up`).
3. Set visibility to **Public** or **Private**.
   > 💡 *Note*: If you make the repo **Private**, make sure to enable **"Include private contributions on my profile"** in your GitHub profile settings:
   > Go to `GitHub Settings -> Profile -> Contributions -> Check "Include private contributions on my profile"`.
4. Run the remote setup commands shown by GitHub:

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/github-contribution-booster.git
git push -u origin main
```

---

### 3. Grant Write Permissions to GitHub Actions

For GitHub Actions to be able to push commits back to your repository:

1. Open your repository on GitHub.
2. Go to **Settings** -> **Actions** -> **General**.
3. Scroll down to **Workflow permissions**.
4. Select **Read and write permissions**.
5. Click **Save**.

---

## ⚡ Manual Execution & Custom Options

### Run Locally Anytime
You can test or run the script locally at any time:

```bash
# Default: Generates random commits between 12 and 50
npm start

# Custom commit count range (e.g., 20 to 30)
node commit.js --min=20 --max=30

# Force exact commit count (e.g., exactly 25 commits)
node commit.js --count=25

# Test mode (dry run - does not execute real git commits)
node commit.js --dry-run
```

### Manually Trigger on GitHub
1. Go to your GitHub Repository -> **Actions** tab.
2. Click **Daily GitHub Contributions Booster** on the left menu.
3. Click **Run workflow** -> **Run workflow**.

---

## 📅 Schedule Customization

To change the time when the daily automation runs, open [`.github/workflows/daily-contributions.yml`](.github/workflows/daily-contributions.yml) and adjust the `cron` string:

```yaml
schedule:
  - cron: '0 3 * * *'  # 03:00 UTC daily
```

---

## 📄 License
MIT License
