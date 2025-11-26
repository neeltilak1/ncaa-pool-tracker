# GitHub Pages Deployment Guide

## 🚀 Quick Deploy (5 Minutes)

### Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click the **"+"** in top right → **"New repository"**
3. Name it: `ncaa-pool-tracker` (or any name you like)
4. Make it **Public** (required for free GitHub Pages)
5. ✅ Check **"Add a README file"**
6. Click **"Create repository"**

### Step 2: Upload Files

**Option A: Web Upload (Easiest)**

1. In your new repo, click **"Add file"** → **"Upload files"**
2. Drag and drop ALL these files:
   ```
   index.html
   ncaa-pool-tracker-live.html
   ncaa-pool-tracker.html
   pool_data.json
   README.md
   LIVE-TRACKER-GUIDE.md
   TRACKER-GUIDE.md
   .gitignore
   ```
3. Scroll down, add commit message: "Initial commit"
4. Click **"Commit changes"**

**Option B: Git Command Line**

```bash
# Navigate to your folder with the files
cd /path/to/files

# Initialize git (if not already)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: NCAA Basketball Pool Tracker"

# Add remote (replace YOUR-USERNAME and REPO-NAME)
git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. In your repo, click **"Settings"** (top menu)
2. Scroll down left sidebar, click **"Pages"**
3. Under **"Source"**, select:
   - Branch: **main**
   - Folder: **/ (root)**
4. Click **"Save"**
5. Wait 1-2 minutes for deployment

### Step 4: Access Your Site

Your tracker will be live at:
```
https://YOUR-USERNAME.github.io/REPO-NAME/
```

Example:
```
https://neelaltitude.github.io/ncaa-pool-tracker/
```

---

## 🎯 What Happens Next?

### First Visit
- GitHub Pages builds your site (~1-2 minutes)
- Green checkmark appears when ready
- Link appears at top of Pages settings

### Updates
- Any commit to `main` branch auto-deploys
- Usually updates within 1 minute
- No need to do anything!

---

## 📝 Making Updates

### Update Team Records (Automatic)
1. Just visit your live site
2. Click "Fetch Latest Data"
3. Data updates from Sports Reference
4. No GitHub update needed!

### Update Draft Picks (Manual)

**Option 1: Edit on GitHub**
1. Go to your repo
2. Click on `pool_data.json`
3. Click pencil icon (Edit)
4. Make changes
5. Scroll down, click "Commit changes"
6. Site updates in ~1 minute

**Option 2: Upload New File**
1. Edit `pool_data.json` locally
2. Go to repo → "Add file" → "Upload files"
3. Upload the updated file
4. Check "Replace existing file"
5. Commit changes

### Update HTML/CSS
Same process - edit files in GitHub or upload new versions

---

## 🔗 Sharing Your Tracker

### Share the Link
```
https://YOUR-USERNAME.github.io/ncaa-pool-tracker/
```

### Custom Domain (Optional)

Want `pool.yourdomain.com` instead?

1. Buy a domain (Namecheap, Google Domains, etc.)
2. In GitHub repo → Settings → Pages
3. Enter your custom domain
4. Add DNS records (GitHub shows instructions)
5. Wait for DNS propagation (up to 24 hours)

---

## 🎨 Customization

### Change Pool Name
Edit `index.html` and HTML files, search for:
```html
<h1>🏀 NCAA Basketball Pool</h1>
```
Replace with your pool name!

### Change Colors
Search for color classes in HTML files:
- `from-purple-600` → Your color
- `bg-blue-600` → Your color
- Use Tailwind color names

### Add Your Logo
1. Upload logo image to repo (e.g., `logo.png`)
2. In HTML files, add:
   ```html
   <img src="logo.png" alt="Logo">
   ```

---

## 🔐 Security & Privacy

### Public Repository
- ✅ Code is visible to everyone
- ✅ No sensitive data exposed
- ✅ Player names are already public
- ✅ Win counts are public info

### Private Repository
- Requires GitHub Pro ($4/month)
- Site still public, but code is private
- Probably not necessary for this use case

---

## 📊 Analytics (Optional)

Want to see how many people visit?

### Google Analytics
1. Get tracking code from Google Analytics
2. Add to `<head>` of HTML files:
   ```html
   <!-- Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-ID"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'YOUR-ID');
   </script>
   ```

### GitHub Insights
- Free built-in analytics
- Repo → Insights → Traffic
- Shows page views, visitors, etc.

---

## 🐛 Troubleshooting

### Site Not Loading
1. Check Settings → Pages shows green checkmark
2. Make sure branch is set to `main`
3. Verify URL is correct
4. Wait 2-3 minutes after first deploy

### 404 Error
1. Check files are in root folder (not subfolder)
2. Verify `index.html` exists
3. Check file names are exact (case-sensitive)

### Data Not Fetching
1. This is a CORS issue, not GitHub Pages
2. Try the manual edit feature
3. Works better on some browsers than others

### Changes Not Showing
1. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
2. Clear browser cache
3. Wait 1-2 minutes for GitHub to rebuild
4. Check commit was successful

---

## 💡 Pro Tips

### Bookmark the Pages URL
Save this in your browser bookmarks:
```
https://YOUR-USERNAME.github.io/ncaa-pool-tracker/
```

### Mobile Home Screen
On mobile, "Add to Home Screen" for app-like experience

### Share with Everyone
Send the link to all participants - everyone sees same data!

### Regular Backups
Click "Export Data" weekly to save backup JSON files

### Monitor the Repo
"Watch" your repo to get notified of any changes

---

## 🔄 Updating the Tracker Code

If you want to update the tracker itself (new features, bug fixes):

1. Download updated HTML files
2. Go to your repo
3. Upload → Replace existing files
4. Commit changes
5. Done!

---

## 📞 Need Help?

### GitHub Pages Documentation
https://docs.github.com/en/pages

### GitHub Community
https://github.community/

### Common Issues
Check the README.md troubleshooting section

---

## ✅ Deployment Checklist

Before going live, verify:

- [ ] All 8 files uploaded to repo
- [ ] GitHub Pages enabled in Settings
- [ ] `index.html` redirects to live tracker
- [ ] Live tracker loads properly
- [ ] "Fetch Latest Data" button works
- [ ] All 10 participants appear
- [ ] Team logos loading
- [ ] Mobile view works
- [ ] Bookmark the URL
- [ ] Share with participants!

---

**🎉 Congratulations! Your tracker is now live!**

Your URL: `https://YOUR-USERNAME.github.io/ncaa-pool-tracker/`

---

**Last Updated:** November 25, 2025  
**Version:** 2.0