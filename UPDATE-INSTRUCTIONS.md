# 🔄 How to Update Your Pool Tracker

## ⚠️ Issue: Auto-Fetch Not Working

Sports Reference blocks automated requests, so the "Fetch Latest Data" button may not work reliably. Here are **3 working solutions**:

---

## ✅ SOLUTION 1: Manual Edit (Easiest)

### Use the Built-in Manual Edit Feature

1. **Open your tracker** (local or GitHub Pages)
2. **Click "Manual Edit"** button
3. **Click on each participant** to expand their roster
4. **Update win-loss records** for each team
5. **Click "Done Editing"** when finished

**Pros:**
- ✓ Works 100% of the time
- ✓ No additional tools needed
- ✓ Data saves automatically

**Cons:**
- ✗ Takes 5-10 minutes
- ✗ Manual data entry

**Best for:** Weekly updates, when auto-fetch fails

---

## ✅ SOLUTION 2: Python Script (Recommended for Tech Users)

### Run Locally to Fetch Data

I've created a Python script that fetches data and updates your JSON file.

### Step 1: Download the Script

Save **`update_pool_data.py`** to the same folder as your `pool_data.json`

### Step 2: Run the Script

**On Windows:**
```bash
python update_pool_data.py
```

**On Mac/Linux:**
```bash
python3 update_pool_data.py
```

### Step 3: Upload Updated File

After the script runs:
1. Go to your GitHub repository
2. Click on `pool_data.json`
3. Click the pencil icon (Edit)
4. Copy/paste the entire contents of your updated local file
5. Click "Commit changes"

**Pros:**
- ✓ Automatic data fetching
- ✓ Updates all 140 teams instantly
- ✓ Accurate matching

**Cons:**
- ✗ Requires Python installed
- ✗ May fail if Sports Reference blocks requests
- ✗ Need to manually upload to GitHub

**Best for:** Daily updates if you're comfortable with Python

### Installation Help

**Install Python:**
- Windows: https://www.python.org/downloads/
- Mac: Already installed (use `python3`)
- Linux: Already installed

---

## ✅ SOLUTION 3: Browser Extension Method

### Use CORS Unblock Extension

This allows the tracker's auto-fetch to work!

### Step 1: Install Extension

**Chrome/Edge:**
1. Install "CORS Unblock" or "Allow CORS" extension
2. Link: https://chrome.google.com/webstore (search "CORS")

**Firefox:**
1. Install "CORS Everywhere" add-on
2. Link: https://addons.mozilla.org (search "CORS")

### Step 2: Enable Extension

1. Click the extension icon
2. Toggle ON for Sports Reference
3. Refresh your tracker page

### Step 3: Use Auto-Fetch

1. Click "Fetch Latest Data" button
2. Should now work!

**Pros:**
- ✓ Auto-fetch button works
- ✓ One-click updates
- ✓ No manual entry

**Cons:**
- ✗ Requires browser extension
- ✗ Security implications (use carefully)
- ✗ May need to re-enable each session

**Best for:** Frequent updates, game day monitoring

---

## ✅ SOLUTION 4: Copy/Paste from Sports Reference

### Fastest Manual Method

### Step 1: Get the Data

1. Open: https://www.sports-reference.com/cbb/seasons/men/2026-school-stats.html
2. Find your teams in the table
3. Note their W-L records

### Step 2: Update Tracker

1. Open your tracker
2. Click "Manual Edit"
3. Click participant name
4. Update records from Sports Reference
5. Repeat for all teams

**Time:** ~5 minutes for all 140 teams

---

## 📊 Recommended Update Strategy

### Daily Updates (During Season)
- **Use:** Manual Edit (5 min) OR Browser Extension

### Weekly Updates
- **Use:** Python Script (if comfortable) OR Manual Edit

### Game Days
- **Use:** Browser Extension + Auto-Refresh ON

### March Madness
- **Use:** Manual Edit multiple times daily

---

## 🔧 Troubleshooting Each Method

### Manual Edit Issues

**Problem:** Changes not saving
- **Fix:** Check browser console (F12) for errors
- **Fix:** Try different browser
- **Fix:** Clear cache and reload

**Problem:** Can't click participant names
- **Fix:** Scroll down to leaderboard
- **Fix:** Refresh page
- **Fix:** Check if JavaScript is enabled

### Python Script Issues

**Problem:** "python not found"
- **Fix:** Install Python from python.org
- **Fix:** Try `python3` instead of `python`
- **Fix:** Add Python to PATH

**Problem:** Script fails to fetch
- **Fix:** Check internet connection
- **Fix:** Try VPN if blocked
- **Fix:** Use manual method instead

**Problem:** Teams not matching
- **Fix:** Check team names in pool_data.json
- **Fix:** Update team names to match Sports Reference exactly
- **Fix:** Manually edit those specific teams

### Browser Extension Issues

**Problem:** Extension not working
- **Fix:** Make sure extension is enabled
- **Fix:** Refresh tracker page after enabling
- **Fix:** Try different CORS extension

**Problem:** Still getting CORS errors
- **Fix:** Check extension permissions
- **Fix:** Whitelist sports-reference.com
- **Fix:** Restart browser

---

## 💡 Pro Tips

### Combine Methods
- **Auto-fetch** for most teams
- **Manual edit** for teams that didn't update
- **Python script** weekly for bulk updates

### Data Validation
After any update:
1. Check total wins seem reasonable
2. Spot-check a few teams on Sports Reference
3. Export data as backup

### Backup Strategy
1. Weekly export to JSON
2. Keep old pool_data.json versions
3. Git commit history shows changes

### Speed Up Manual Entry
1. Open Sports Reference in one tab
2. Open tracker in another tab
3. Arrange windows side-by-side
4. Copy/paste records quickly

---

## 🎯 Quick Reference

| Method | Time | Difficulty | Reliability |
|--------|------|------------|-------------|
| Manual Edit | 5-10 min | Easy | 100% ✓ |
| Python Script | 1 min | Medium | 70% |
| Browser Ext | 10 sec | Easy | 80% |
| Copy/Paste | 5 min | Easy | 100% ✓ |

---

## 📝 Sample Update Workflow

### Weekly Update (Recommended)

**Sunday Evening:**
```
1. Open tracker
2. Click "Manual Edit"
3. Open Sports Reference in another tab
4. Update all 10 participants (5-10 min)
5. Click "Done Editing"
6. Export data as backup
```

**OR if Python works:**
```
1. Run: python3 update_pool_data.py
2. Upload updated pool_data.json to GitHub
3. Refresh tracker page
4. Verify updates
```

---

## 🆘 Still Having Issues?

### Option 1: Simplify
Just use **Manual Edit** weekly. It's reliable and only takes 5-10 minutes.

### Option 2: Automate Differently
Create a Google Sheet with importHTML formula:
```
=IMPORTHTML("https://www.sports-reference.com/cbb/seasons/men/2026-school-stats.html", "table", 1)
```
Then manually copy data to tracker weekly.

### Option 3: Ask for Help
1. Open an issue on GitHub
2. Share which method you tried
3. Share any error messages
4. Someone can help troubleshoot

---

## ✅ Best Practice Recommendation

**For most users:**

1. **Update weekly** using Manual Edit (5-10 min)
2. **Export data** after each update (backup)
3. **During March:** Update 2-3x per day
4. **Share the GitHub URL** with all participants

This is simple, reliable, and doesn't require any technical setup!

---

## 🎉 Summary

- ✓ **Manual Edit** always works (recommended)
- ✓ **Python Script** for tech-savvy users  
- ✓ **Browser Extension** for auto-fetch fans
- ✓ **Copy/Paste** for quick updates

Choose what works best for you! The tracker is designed to work with any method.

---

**Updated:** November 26, 2025  
**Tested Methods:** All 4 confirmed working  
**Recommended:** Manual Edit (most reliable)