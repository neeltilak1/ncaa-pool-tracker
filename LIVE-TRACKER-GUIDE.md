# NCAA Basketball Pool Tracker - LIVE VERSION

## 🚀 NEW: Auto-Updating from Sports Reference!

I've created TWO versions of the tracker:

### Version 1: Manual Tracker (`ncaa-pool-tracker.html`)
- Manual updates only
- Edit records yourself
- Lightweight and simple
- **Best for: Offline use or full control**

### Version 2: LIVE Tracker (`ncaa-pool-tracker-live.html`) ⭐ RECOMMENDED
- **Auto-fetches** data from Sports Reference
- One-click refresh button
- Auto-refresh every 5 minutes (optional)
- Manual edit as backup
- **Best for: Real-time updates with minimal effort**

---

## 🎯 How the LIVE Version Works

### Data Source
The tracker pulls real-time data from:
**https://www.sports-reference.com/cbb/seasons/men/2026-school-stats.html**

This page has ALL Division I team records updated after each game!

### New Features

#### 1. **"Fetch Latest Data" Button** 🔄
- Click to instantly update all team records
- Fetches from Sports Reference in real-time
- Matches your drafted teams automatically
- Shows success/error messages

#### 2. **Auto-Refresh Toggle** ⏰
- Turn ON to auto-update every 5 minutes
- Perfect for keeping it open during game days
- Turn OFF to save data/battery

#### 3. **Status Messages**
- "✓ Updated 140 teams successfully!" = Data fetched
- "🔄 Fetching latest data..." = In progress
- "⚠️ Failed to fetch..." = Use manual edit

#### 4. **Fallback to Manual**
- If auto-fetch fails, use "Manual Edit" button
- Same functionality as Version 1
- Your changes persist

---

## 📝 Step-by-Step Usage

### First Time Setup

1. **Open** `ncaa-pool-tracker-live.html` in your browser
2. **Bookmark** the page for easy access
3. Your draft picks are already loaded!

### During the Season

#### Option A: Automatic Updates (Recommended)
1. Click **"Fetch Latest Data"** button
2. Wait 5-10 seconds for fetch to complete
3. See leaderboard update automatically!
4. (Optional) Turn on **"Auto-Refresh"** toggle

#### Option B: Manual Updates
1. Click **"Manual Edit"** button
2. Click on a participant's name
3. Update win-loss records in the input fields
4. Click **"Done Editing"** when finished

### Best Practices

**🏀 Game Day Strategy:**
1. Open tracker in the morning
2. Turn ON "Auto-Refresh"
3. Leave tab open
4. Check throughout the day!

**📊 Weekly Updates:**
1. Open tracker once a week
2. Click "Fetch Latest Data"
3. Check leaderboard
4. Close when done

**💾 Backups:**
- Click "Export" to download data
- Save before major updates
- Restore if needed

---

## 🔧 Technical Details

### How It Fetches Data

The tracker uses a **CORS proxy** to fetch from Sports Reference:
```
allorigins.win → Sports Reference → Parse HTML → Match Teams → Update
```

### Data Matching

Teams are matched by name. The tracker tries:
1. **Exact match**: "Alabama" → "Alabama"
2. **Normalized match**: "Saint Mary's (CA)" → "Saint Mary's"
3. **Abbreviations**: "UConn" → "Connecticut"

### Data Storage

- Fetched data saves to **browser localStorage**
- Persists between sessions
- Survives browser restart
- Cleared if you clear browser data

### Fetch Frequency

- **Manual**: Only when you click "Fetch"
- **Auto-Refresh ON**: Every 5 minutes
- **Recommended**: Check 1-2 times per day

---

## ❓ Troubleshooting

### "Failed to fetch" Error

**Causes:**
- Sports Reference is down temporarily
- CORS proxy is busy
- Internet connection issue

**Solutions:**
1. Wait 1-2 minutes and try again
2. Use "Manual Edit" as backup
3. Check your internet connection
4. Try a different browser

### Team Names Don't Match

**Problem:** Your drafted team name differs from Sports Reference

**Solution:**
1. Note the exact name on Sports Reference
2. Use "Manual Edit" to update that team
3. Next fetch will work better

### Data Not Updating

**Check:**
- ✓ Status message shows success?
- ✓ Last Updated time changed?
- ✓ Browser console for errors (F12)

**Fix:**
1. Click "Fetch Latest Data" again
2. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
3. Clear browser cache

### Auto-Refresh Not Working

- ✓ Make sure toggle shows "Auto-Refresh ON"
- ✓ Keep browser tab active (not sleeping)
- ✓ Check if browser allows background scripts

---

## 🏆 Current Standings

As of last update in your Excel file:

| Rank | Name | Wins |
|------|------|------|
| 🥇 | Tom | 71 |
| 🥈 | Brian | 70 |
| 🥉 | Ryan | 67 |
| 4 | Kevin | 63 |
| 5 | Andrew | 62 |
| 6 | Jake | 56 |
| 7 | Neel | 54 |
| 8 | Matt | 54 |
| 9 | Pete | 51 |
| 10 | Stan | 49 |

**Total Teams:** 140 (14 per person)
**Total Wins Tracked:** 597

---

## 💡 Pro Tips

1. **Bookmark BOTH versions** - Live for updates, Manual as backup
2. **Check after big game days** - Conference rivalries, ranked matchups
3. **Enable notifications** - Set phone reminder to check tracker
4. **Share the link** - Everyone can see same real-time data
5. **Export regularly** - Weekly backups recommended

---

## 🚨 Important Notes

### Data Privacy
- All data stored **locally** in your browser
- No server-side storage
- No tracking or analytics
- Export to keep your own backup

### Browser Compatibility
- ✓ Chrome/Edge (Recommended)
- ✓ Firefox
- ✓ Safari
- ✓ Mobile browsers work too!

### Network Requirements
- Internet needed for auto-fetch
- Works offline for viewing
- Mobile data usage: ~100KB per fetch

---

## 📞 Support

**Questions?** Contact Neel at Altitude Consulting!

**Found a bug?** 
1. Note what you were doing
2. Check browser console (F12)
3. Try the Manual version
4. Send screenshot if possible

---

## 🎮 Quick Start Guide

### For Beginners:
1. Open `ncaa-pool-tracker-live.html`
2. Click "Fetch Latest Data"
3. View leaderboard!

### For Power Users:
1. Open tracker, turn on Auto-Refresh
2. Bookmark page
3. Check throughout game days
4. Export weekly backups

---

**Last Updated:** November 25, 2025  
**Pool Season:** 2025-26 NCAA Basketball  
**Data Source:** Sports-Reference.com (Real-Time)  
**Version:** 2.0 (Live Auto-Update)