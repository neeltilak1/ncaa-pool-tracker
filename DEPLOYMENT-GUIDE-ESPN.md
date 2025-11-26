# 🚀 GitHub Pages Deployment Guide - ESPN Live Tracker

## Complete Step-by-Step Instructions

---

## 📦 Files to Upload (ONLY 4 Required!)

### ✅ REQUIRED FILES

1. **`index.html`** (2.1 KB)
   - Landing page with auto-redirect
   - First page visitors see

2. **`ncaa-pool-tracker-espn-live.html`** (55 KB) ⭐ **MAIN FILE**
   - Live ESPN tracker
   - All functionality in one file!

3. **`README-ESPN.md`** (8 KB)
   - Rename to `README.md` when uploading
   - Repository documentation

4. **`.gitignore`** (522 bytes)
   - Git configuration

### 📚 OPTIONAL FILES (For Reference)

- `DEPLOYMENT-GUIDE-ESPN.md` (this file)
- `LIVE-TRACKER-GUIDE.md`
- `ESPN-API-GUIDE.md`

---

## 🎯 Quick Deploy (5 Minutes)

### Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click **"+"** in top right → **"New repository"**
3. **Repository name:** `ncaa-pool-tracker`
4. **Description:** "NCAA Basketball Pool 2025-26 - Live ESPN Tracker"
5. **Visibility:** PUBLIC (required for free Pages)
6. ✅ **Check:** "Add a README file"
7. Click **"Create repository"**

### Step 2: Upload Files

1. In your new repo, click **"Add file"** → **"Upload files"**

2. **Drag and drop these 4 files:**
   ```
   ✓ index.html
   ✓ ncaa-pool-tracker-espn-live.html
   ✓ README-ESPN.md (will rename in step 3)
   ✓ .gitignore
   ```

3. **Commit message:** "Initial commit: Live ESPN tracker"

4. Click **"Commit changes"**

5. **Rename README:**
   - Click on `README-ESPN.md`
   - Click pencil icon (Edit)
   - Change filename to `README.md`
   - Scroll down, click "Commit changes"

### Step 3: Enable GitHub Pages

1. Click **"Settings"** tab (top of repository)

2. Scroll down left sidebar, click **"Pages"**

3. Under **"Build and deployment":**
   - **Source:** Deploy from a branch
   - **Branch:** `main`
   - **Folder:** `/ (root)`

4. Click **"Save"**

5. **Wait 1-2 minutes** for deployment

6. **Refresh** the Pages settings page

7. **Your site is live!** Green checkmark appears with URL:
   ```
   https://YOUR-USERNAME.github.io/ncaa-pool-tracker/
   ```

### Step 4: Test Your Tracker

1. **Click the URL** or open it in browser

2. **Should see:** Loading screen with basketball emoji

3. **Click:** "🔄 Refresh from ESPN" button

4. **Watch:** Data loads in 2-3 seconds

5. **Verify:** Leaderboard appears with all 10 participants

6. **Test:** Click on participant names to see rosters

7. **Test:** Enable "Auto-Refresh ON"

8. **Success!** 🎉

---

## 📋 Detailed Instructions

### Creating the Repository

**Why Public?**
- GitHub Pages is free for public repositories
- Anyone with the link can view
- Code is visible (but it's just HTML, no secrets!)

**Repository Settings:**
- **Name:** Can be anything, but `ncaa-pool-tracker` is clear
- **Description:** Helps identify the project
- **README:** Will be replaced with your README-ESPN.md

### Uploading Files

**Drag and Drop Method** (Easiest):
1. Open File Explorer/Finder
2. Select all 4 required files
3. Drag into GitHub upload area
4. Release to upload

**Individual Upload Method:**
1. Click "Add file" → "Upload files"
2. Click "choose your files"
3. Select files one by one
4. Click "Commit changes"

**Important Notes:**
- Make sure filenames are exact (case-sensitive)
- `.gitignore` starts with a dot
- Don't change file extensions

### Enabling Pages

**Settings Location:**
- Must be in repository Settings
- Not your personal GitHub settings
- Left sidebar has "Pages" option

**Branch Selection:**
- `main` is the default branch name
- If your branch is called `master`, select that
- Folder must be `/ (root)` not `/docs`

**Deployment Time:**
- Usually 1-2 minutes
- Can take up to 5 minutes on first deploy
- Subsequent updates are faster (30-60 seconds)

---

## 🔧 Troubleshooting

### Site Not Loading

**Problem:** 404 error when visiting URL

**Solutions:**
1. **Wait longer** - First deploy can take 5 minutes
2. **Check Settings → Pages** - Green checkmark should appear
3. **Verify branch** - Make sure it's set to `main`
4. **Check files** - Ensure `index.html` is in root folder
5. **Refresh hard** - Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

### Blank Page

**Problem:** Page loads but nothing appears

**Solutions:**
1. **Check browser console** - Press F12, look for errors
2. **Verify file names** - Must be exact (case-sensitive)
3. **Try different browser** - Test in Chrome/Firefox
4. **Clear cache** - Full refresh with Ctrl+Shift+R

### "Fetch Failed" Error

**Problem:** ESPN data doesn't load

**Solutions:**
1. **Check internet** - Must be connected
2. **Try different network** - Mobile hotspot, different WiFi
3. **Wait and retry** - ESPN API very rarely has issues
4. **Check browser console** - Look for CORS or network errors

### Wrong Data Showing

**Problem:** Records don't match ESPN.com

**Solutions:**
1. **Click refresh again** - Might have been cached
2. **Clear browser cache** - Hard refresh
3. **Compare team names** - Ensure exact matches
4. **Check ESPN.com** - Verify their data is correct

### Changes Not Appearing

**Problem:** Updated file but site shows old version

**Solutions:**
1. **Wait 30-60 seconds** - GitHub Pages takes time to rebuild
2. **Hard refresh** - Ctrl+Shift+R to bypass cache
3. **Check commit** - Verify changes were saved in GitHub
4. **Clear browser cache** - Settings → Clear browsing data

---

## 🎨 Customization After Deployment

### Change Pool Name

1. Go to repository on GitHub
2. Click `ncaa-pool-tracker-espn-live.html`
3. Click pencil icon (Edit)
4. Find line: `<h1 className="text-4xl font-black mb-1">🏀 NCAA Basketball Pool</h1>`
5. Change "NCAA Basketball Pool" to your pool name
6. Scroll down, click "Commit changes"
7. Wait 30 seconds, refresh your site

### Update Participants

1. Edit `ncaa-pool-tracker-espn-live.html`
2. Find `const DRAFT_DATA = {`
3. Add/remove/modify participants and their teams
4. Commit changes
5. Site updates automatically!

### Change Auto-Refresh Time

1. Edit `ncaa-pool-tracker-espn-live.html`
2. Find `300000` (= 5 minutes)
3. Change to desired milliseconds:
   - 3 min = `180000`
   - 10 min = `600000`
4. Commit changes

---

## 📱 Sharing Your Tracker

### Get Your URL

**Format:**
```
https://YOUR-USERNAME.github.io/ncaa-pool-tracker/
```

**Example:**
```
https://neelaltitude.github.io/ncaa-pool-tracker/
```

### Share With Participants

**Email Template:**
```
Hey everyone!

Our NCAA Basketball Pool tracker is now live:
https://YOUR-USERNAME.github.io/ncaa-pool-tracker/

Click "Refresh from ESPN" to see latest standings!
Updates in real-time throughout the season.

Good luck! 🏀
```

**Group Chat:**
```
🏀 Pool tracker is live!
https://YOUR-USERNAME.github.io/ncaa-pool-tracker/
```

**Social Media:**
```
Our NCAA pool is tracking live on GitHub Pages!
Real-time updates from ESPN. Check the leaderboard:
[your-url]
```

---

## 🔄 Making Updates

### Update Participant Rosters

**Option 1: GitHub Web Interface**
1. Click file in repository
2. Click pencil icon
3. Make changes
4. Commit changes
5. Site updates in 30-60 seconds

**Option 2: Git Command Line**
```bash
git clone https://github.com/YOUR-USERNAME/ncaa-pool-tracker.git
cd ncaa-pool-tracker
# Edit files locally
git add .
git commit -m "Updated rosters"
git push origin main
```

### No Data Updates Needed!

**Best part:** The tracker fetches live data from ESPN, so you NEVER need to manually update team records! Just click "Refresh from ESPN" and it's always current.

---

## 🌐 Custom Domain (Optional)

### Want Your Own Domain?

**Example:** `pool.yourdomain.com` instead of GitHub URL

**Steps:**
1. **Buy domain** (Namecheap, Google Domains, etc.)
2. **In GitHub:** Settings → Pages → Custom domain
3. **Enter your domain:** `pool.yourdomain.com`
4. **In domain registrar:** Add DNS records (GitHub shows instructions)
5. **Wait:** DNS propagation (up to 24 hours)
6. **Done!** Your tracker is at your domain

**DNS Records Needed:**
```
Type: CNAME
Name: pool (or @)
Value: YOUR-USERNAME.github.io
```

---

## 📊 Analytics (Optional)

### Want to Track Visitors?

**Google Analytics:**

1. Get tracking code from analytics.google.com
2. Edit `ncaa-pool-tracker-espn-live.html`
3. Add to `<head>` section:
   ```html
   <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-ID"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'YOUR-ID');
   </script>
   ```
4. Commit changes

**GitHub Insights:**
- Free built-in analytics
- Repository → Insights → Traffic
- Shows page views, visitors, referring sites

---

## ✅ Pre-Launch Checklist

Before sharing with participants:

- [ ] All 4 files uploaded to GitHub
- [ ] GitHub Pages enabled (green checkmark)
- [ ] Site loads at your URL
- [ ] "Refresh from ESPN" button works
- [ ] Data loads (all 10 participants visible)
- [ ] Leaderboard shows correct order
- [ ] Can click participant names
- [ ] Rosters display with logos
- [ ] Auto-refresh toggle works
- [ ] Tested on mobile device
- [ ] Tested on different browser
- [ ] Bookmarked the URL
- [ ] URL copied for sharing
- [ ] Ready to announce! 🎉

---

## 🎯 Common Questions

**Q: Do I need to know coding?**  
A: Nope! Just upload files and enable Pages.

**Q: Is GitHub Pages free?**  
A: Yes! Completely free for public repositories.

**Q: Can I make the repo private?**  
A: Yes, but requires GitHub Pro ($4/month).

**Q: How often does ESPN API update?**  
A: Updates as games finish, typically within minutes.

**Q: What if ESPN API goes down?**  
A: Very rare! Just try again later or wait for ESPN to fix.

**Q: Can I edit participant teams mid-season?**  
A: Yes! Just edit the DRAFT_DATA in the HTML file.

**Q: Do I need to keep updating data files?**  
A: No! It fetches live from ESPN automatically.

**Q: Can multiple people view at once?**  
A: Yes! Share the link with everyone.

**Q: Will it work on mobile?**  
A: Perfectly! Fully responsive design.

**Q: How do I delete files in GitHub?**  
A: Click file → Trash icon → Commit changes

---

## 🎉 Success Checklist

You're done when:

✅ Repository created  
✅ Files uploaded  
✅ GitHub Pages enabled  
✅ Site loads successfully  
✅ ESPN data fetches correctly  
✅ Tested on desktop  
✅ Tested on mobile  
✅ URL bookmarked  
✅ Link shared with participants  
✅ Everyone can access  

**Congratulations! Your live ESPN tracker is running!** 🏀🏆

---

## 📞 Need Help?

**Still stuck?** 

1. Check [GitHub Pages documentation](https://docs.github.com/en/pages)
2. Review this guide again carefully
3. Open an issue in your repository
4. Ask in pool group chat
5. Contact pool organizer

---

## 💡 Pro Tips

1. **Bookmark GitHub repo** - Easy access to edit files
2. **Enable notifications** - Get alerts when someone commits
3. **Star your repo** - Show it in your GitHub profile
4. **Watch the repo** - Track all activity
5. **Add collaborators** - Let others help manage

---

**Last Updated:** November 26, 2025  
**Deploy Time:** 5 minutes  
**Difficulty:** Beginner-friendly  
**Cost:** $0 (FREE!)  
**Maintenance:** Zero - ESPN API updates automatically  

---

**Ready to deploy? Let's go!** 🚀

Your live tracker awaits at:  
`https://YOUR-USERNAME.github.io/ncaa-pool-tracker/`

**Good luck with your pool!** 🏀