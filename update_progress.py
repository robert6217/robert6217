import sys

# Option: PRE, MY, TH, NP, IN, AE, KE, EG, AM, GR, IT, FR, ES, DONE
CURRENT_CODE = "PRE" 

itinerary = [
	{"code": "MY", "name": "Malaysia", "flag": "🇲🇾"},
	{"code": "TH", "name": "Thailand", "flag": "🇹🇭"},
	{"code": "NP", "name": "Nepal",    "flag": "🇳🇵"},
	{"code": "IN", "name": "India",    "flag": "🇮🇳"},
	{"code": "AE", "name": "Dubai",    "flag": "🇦🇪"},
	{"code": "KE", "name": "Kenya",    "flag": "🇰🇪"},
	{"code": "EG", "name": "Egypt",    "flag": "🇪🇬"},
	{"code": "AM", "name": "Armenia",  "flag": "🇦🇲"},
	{"code": "GR", "name": "Greece",   "flag": "🇬🇷"},
	{"code": "IT", "name": "Italy",    "flag": "🇮🇹"},
	{"code": "FR", "name": "France",   "flag": "🇫🇷"},
	{"code": "ES", "name": "Spain",    "flag": "🇪🇸"},
	{"code": "CH", "name": "Switzerland",    "flag": "🇨🇭"},
]

def generate_progress_bar(current_idx, total):
	if current_idx < 0: return "[░░░░░░░░░░] 0%"
	if current_idx >= total: return "[▓▓▓▓▓▓▓▓▓▓] 100%"

	percent = ((current_idx + 1) / total) * 100
	bar_length = 10
	filled_length = int(bar_length * (current_idx + 1) // total)
	bar = '▓' * filled_length + '░' * (bar_length - filled_length)
	return f"[{bar}] {int(percent)}%"

def generate_readme_content():
	total_stops = len(itinerary)
	current_idx = -1

	for idx, stop in enumerate(itinerary):
		if stop["code"] == CURRENT_CODE:
			current_idx = idx
			break
			
	if CURRENT_CODE == "DONE":
		current_idx = total_stops

	if 0 <= current_idx < total_stops:
		curr = itinerary[current_idx]
		location_str = f"{curr['flag']} {curr['name']}"
	elif CURRENT_CODE == "DONE":
		location_str = "🏆 Santiago de Compostela, Spain (Mission Complete!)"
	else:
		location_str = "🏠 Taiwan (Preparing)"

	progress_bar = generate_progress_bar(current_idx, total_stops)

	path_visuals = []
	for idx, stop in enumerate(itinerary):
		code = stop["code"]
		if idx < current_idx:
			path_visuals.append(f"✅ {code}")
		elif idx == current_idx:
			path_visuals.append(f"**📍 {code}**")
		else:
			path_visuals.append(f"⚪ {code}")
			
	path_str = " ➝ ".join(path_visuals)

	markdown = f"""
> **Current Location:** {location_str} | **Trip Progress:** {progress_bar}

**The Path:**
{path_str}

"""
	return markdown

readme_path = 'README.md'
try:
	with open(readme_path, 'r', encoding='utf-8') as f:
		content = f.read()

	start_marker = '### 🌏 2026 The Great Backpacking Journey'
	end_marker = '*Last Updated: Automated by Python*'

	if start_marker in content and end_marker in content:
		new_content = generate_readme_content()
		before = content.split(start_marker)[0]
		after = content.split(end_marker)[1]
		
		final_output = before + start_marker + new_content + end_marker + after
		
		with open(readme_path, 'w', encoding='utf-8') as f:
			f.write(final_output)
		print("✅ Trip status updated successfully!")
	else:
		print("❌ Error: Couldn't find marks in README.md")

except FileNotFoundError:
	print("❌ Error: README.md not found.")
    