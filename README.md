# NCAA Basketball Pool Tracker 🏀

Live tracking dashboard for NCAA Division I Men's Basketball draft pool - 2025-26 Season

**Live Demo:** [View Tracker](https://yourusername.github.io/ncaa-pool-tracker/ncaa-pool-tracker-live.html)

---

## 🎯 Features

- **Real-Time Updates** - Auto-fetch team records from Sports Reference
- **Live Leaderboard** - See rankings update instantly
- **Auto-Refresh** - Optional 5-minute auto-updates
- **Team Logos** - ESPN team logos for major programs
- **Mobile Responsive** - Works on all devices
- **Offline Capable** - Data cached in browser
- **Manual Override** - Edit records if needed
- **Export Data** - Download backups as JSON

---

## 🚀 Quick Start

### Option 1: GitHub Pages (Recommended)

1. Fork this repository
2. Go to Settings → Pages
3. Set Source to "main" branch
4. Your tracker will be live at: `https://yourusername.github.io/ncaa-pool-tracker/`

### Option 2: Download & Run Locally

1. Download `ncaa-pool-tracker-live.html`
2. Open in any web browser
3. Click "Fetch Latest Data"
4. Done!

---

## 📊 Current Standings

### 2025-26 Season

| Rank | Name | Wins | Teams |
|------|------|------|-------|
| 🥇 | Tom | 71 | 14 |
| 🥈 | Brian | 70 | 14 |
| 🥉 | Ryan | 67 | 14 |
| 4 | Kevin | 63 | 14 |
| 5 | Andrew | 62 | 14 |
| 6 | Jake | 56 | 14 |
| 7 | Neel | 54 | 14 |
| 8 | Matt | 54 | 14 |
| 9 | Pete | 51 | 14 |
| 10 | Stan | 49 | 14 |

**Last Updated:** November 25, 2025  
**Total Teams:** 140 (14 per person)

---

## 🎮 How to Use

### Automatic Updates

1. Open `ncaa-pool-tracker-live.html`
2. Click **"Fetch Latest Data"** button
3. Wait 5-10 seconds for data to load
4. Leaderboard updates automatically!

**Optional:** Turn on "Auto-Refresh" for updates every 5 minutes

### Manual Updates

1. Click **"Manual Edit"** button
2. Click on any participant's name
3. Update win-loss records
4. Click **"Done Editing"**

### View Team Rosters

- Click on any participant's name in the leaderboard
- See all 14 teams with logos and records
- Teams sorted by wins (highest first)

---

## 📁 Files

### Main Files

- **`ncaa-pool-tracker-live.html`** - Auto-updating version (recommended)
- **`ncaa-pool-tracker.html`** - Manual-only version (backup)
- **`index.html`** - Redirects to live version
- **`README.md`** - This file

### Documentation

- **`LIVE-TRACKER-GUIDE.md`** - Comprehensive usage guide
- **`TRACKER-GUIDE.md`** - Manual tracker guide

### Data

- **`pool_data.json`** - Initial draft data (backup)

---

## 🔧 Technical Details

### Data Source

Real-time data fetched from:
```
https://www.sports-reference.com/cbb/seasons/men/2026-school-stats.html
```

### Technology Stack

- **Frontend:** React 18 (via CDN)
- **Styling:** Tailwind CSS
- **Data Storage:** Browser localStorage
- **CORS Proxy:** allorigins.win
- **Logos:** ESPN CDN

### Browser Support

- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers

### Data Privacy

- All data stored locally in browser
- No server-side storage
- No tracking or analytics
- Export your own backups

---

## 🏆 Draft Details

### Participants (10)

Andrew • Brian • Jake • Kevin • Matt • Pete • Ryan • Stan • Tom • Neel

### Draft Format

- **Snake Draft** - Order reverses each round
- **14 Rounds** - 14 teams per person
- **140 Total Teams** - Across all NCAA Division I

### Scoring

- **1 point** per win
- Regular season + Conference tournaments
- NCAA Tournament games **NOT** included

---

## 🛠️ Customization

### Update Participant Rosters

Edit the `pool_data.json` file or use the tracker's manual edit feature.

### Add Team Logos

Add ESPN IDs to the `teamLogoMap` object in the HTML:

```javascript
const teamLogoMap = {
    'Team Name': ESPN_ID,
    // Example:
    'Duke': 150,
    'Kentucky': 96
};
```

Find ESPN IDs at: `https://www.espn.com/mens-college-basketball/teams`

### Customize Styling

The tracker uses Tailwind CSS. Modify classes in the HTML to change appearance.

---

## 📱 Mobile Usage

The tracker is fully responsive:

- **Portrait mode:** Single column layout
- **Landscape mode:** Multi-column grid
- **Touch-friendly:** Large tap targets
- **Fast loading:** Minimal assets

---

## 🔄 Update Frequency

### Recommended

- **Game Days:** Check 1-2 times (morning & evening)
- **Off Days:** Once per day or every few days
- **March:** Multiple times daily!

### Auto-Refresh

- Turn ON during game days
- Turn OFF to save data/battery
- Updates every 5 minutes when ON

---

## 🐛 Troubleshooting

### "Failed to fetch" Error

**Solutions:**
1. Wait 1-2 minutes and try again
2. Check internet connection
3. Try different browser
4. Use manual edit as backup

### Data Not Updating

**Checks:**
1. Status message shows success?
2. Last updated time changed?
3. Clear browser cache (Ctrl+Shift+R)

### Team Names Don't Match

Some teams may have different names on Sports Reference. Use manual edit for those teams.

---

## 📊 Statistics

- **Total Teams Tracked:** 140
- **Conferences Covered:** All 32 Division I
- **Update Frequency:** Real-time (when fetched)
- **Data Points:** ~2,000+ (teams × games)

---

## 🤝 Contributing

Found a bug or have a suggestion?

1. Open an issue
2. Submit a pull request
3. Share your improvements!

---

## 📄 License

MIT License - Feel free to use and modify!

---

## 🙏 Acknowledgments

- **Sports Reference** - Data source
- **ESPN** - Team logos
- **Tailwind CSS** - Styling framework
- **React** - UI framework

---

## 📞 Contact

**Questions?** Open an issue or contact the pool organizer.

---

## 🎯 Roadmap

### Potential Future Features

- [ ] Historical data & trends
- [ ] Head-to-head comparisons
- [ ] Weekly win leaders
- [ ] Conference breakdowns
- [ ] Playoff predictions
- [ ] Mobile app version

---

**Built for the 2025-26 NCAA Men's Basketball Season**  
**Last Updated:** November 25, 2025  
**Version:** 2.0