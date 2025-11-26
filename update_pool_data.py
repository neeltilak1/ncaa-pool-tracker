#!/usr/bin/env python3
"""
NCAA Basketball Pool Data Updater
Fetches current team records from Sports Reference and updates pool_data.json
"""

import json
import re
import sys
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

def normalize_team_name(name):
    """Normalize team names for matching"""
    if not name:
        return ''
    
    # Common name mappings
    mappings = {
        'Connecticut': 'UConn',
        'Brigham Young': 'BYU',
        'Southern California': 'USC',
        'Louisiana State': 'LSU',
        'Southern Methodist': 'SMU',
        'University of California': 'UCLA',
        'North Carolina State': 'NC State',
    }
    
    # Check direct mappings
    for key, value in mappings.items():
        if key in name:
            return value
    
    # Remove common suffixes and normalize
    normalized = name.strip()
    normalized = re.sub(r'\s+State$', ' St.', normalized)
    normalized = re.sub(r'\(.*?\)', '', normalized)  # Remove parentheses
    normalized = normalized.strip()
    
    return normalized

def fetch_sports_reference_data():
    """Fetch team data from Sports Reference"""
    url = 'https://www.sports-reference.com/cbb/seasons/men/2026-school-stats.html'
    
    print("Fetching data from Sports Reference...")
    print(f"URL: {url}")
    
    try:
        # Add headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        req = Request(url, headers=headers)
        response = urlopen(req, timeout=30)
        html = response.read().decode('utf-8')
        
        print("✓ Successfully fetched data")
        return html
        
    except HTTPError as e:
        print(f"✗ HTTP Error: {e.code} - {e.reason}")
        return None
    except URLError as e:
        print(f"✗ URL Error: {e.reason}")
        return None
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return None

def parse_team_records(html):
    """Parse team records from HTML"""
    print("\nParsing team records...")
    
    team_records = {}
    
    # Find the stats table using regex
    # Look for table rows with school name, wins, and losses
    pattern = r'<tr[^>]*>.*?data-stat="school_name"[^>]*>.*?<a[^>]*>([^<]+)</a>.*?data-stat="wins"[^>]*>(\d+)</td>.*?data-stat="losses"[^>]*>(\d+)</td>'
    
    matches = re.finditer(pattern, html, re.DOTALL)
    
    for match in matches:
        school_name = match.group(1).strip()
        wins = int(match.group(2))
        losses = int(match.group(3))
        
        team_records[school_name] = {
            'wins': wins,
            'losses': losses,
            'games': wins + losses
        }
    
    print(f"✓ Parsed {len(team_records)} teams")
    return team_records

def update_pool_data(pool_data_file, sports_ref_data):
    """Update pool_data.json with new records"""
    print(f"\nReading pool data from {pool_data_file}...")
    
    try:
        with open(pool_data_file, 'r') as f:
            pool_data = json.load(f)
    except FileNotFoundError:
        print(f"✗ Error: {pool_data_file} not found!")
        return False
    except json.JSONDecodeError:
        print(f"✗ Error: {pool_data_file} is not valid JSON!")
        return False
    
    print("✓ Pool data loaded")
    
    # Track updates
    updated_count = 0
    not_found = []
    
    print("\nUpdating team records...")
    
    for team_name in pool_data['team_records'].keys():
        # Try exact match first
        if team_name in sports_ref_data:
            pool_data['team_records'][team_name] = sports_ref_data[team_name]
            updated_count += 1
            continue
        
        # Try normalized matching
        normalized = normalize_team_name(team_name)
        found = False
        
        for sr_name, sr_data in sports_ref_data.items():
            if normalize_team_name(sr_name) == normalized:
                pool_data['team_records'][team_name] = sr_data
                updated_count += 1
                found = True
                break
        
        if not found:
            not_found.append(team_name)
    
    # Save updated data
    print(f"\nWriting updated data to {pool_data_file}...")
    
    with open(pool_data_file, 'w') as f:
        json.dump(pool_data, f, indent=2)
    
    print(f"✓ Successfully updated {updated_count} teams")
    
    if not_found:
        print(f"\n⚠ Could not find matches for {len(not_found)} teams:")
        for team in not_found[:10]:  # Show first 10
            print(f"  - {team}")
        if len(not_found) > 10:
            print(f"  ... and {len(not_found) - 10} more")
    
    return True

def main():
    """Main function"""
    print("=" * 70)
    print("NCAA BASKETBALL POOL DATA UPDATER")
    print("=" * 70)
    
    # Default file name
    pool_data_file = 'pool_data.json'
    
    # Allow custom file path
    if len(sys.argv) > 1:
        pool_data_file = sys.argv[1]
    
    # Step 1: Fetch data from Sports Reference
    html = fetch_sports_reference_data()
    if not html:
        print("\n✗ Failed to fetch data from Sports Reference")
        print("Please check your internet connection and try again.")
        return 1
    
    # Step 2: Parse team records
    sports_ref_data = parse_team_records(html)
    if not sports_ref_data:
        print("\n✗ Failed to parse team records")
        return 1
    
    # Step 3: Update pool data
    success = update_pool_data(pool_data_file, sports_ref_data)
    
    if success:
        print("\n" + "=" * 70)
        print("✓ UPDATE COMPLETE!")
        print("=" * 70)
        print(f"\nNext steps:")
        print(f"1. Upload updated {pool_data_file} to GitHub")
        print(f"2. Or refresh your local tracker in the browser")
        return 0
    else:
        print("\n✗ Update failed")
        return 1

if __name__ == '__main__':
    sys.exit(main())
