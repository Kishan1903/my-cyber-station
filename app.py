from flask import Flask, render_template_string, request, session
import hashlib, os, random, string, base64, platform, re

app = Flask(__name__)
app.secret_key = "station_v16_3_ultimate_prime"

CYBER_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>STATION_V16.3_ADVANCED</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Poppins:wght@300;400;500&display=swap');
        :root { --primary: #00ff41; --bg: #0a0a0c; --card: #121216; --weak: #ff4141; --medium: #ffb141; --strong: #00ff41; }

        body { background: var(--bg); margin: 0; height: 100vh; display: flex; justify-content: center; align-items: center; font-family: 'Poppins', sans-serif; color: var(--primary); overflow: hidden; }
        .terminal-box { background: var(--card); border: 1px solid rgba(0, 255, 65, 0.2); border-radius: 12px; width: 550px; padding: 25px; box-shadow: 0 15px 50px rgba(0,0,0,0.9); }
        h1 { text-align: center; color: #fff; letter-spacing: 2px; font-size: 1.1rem; margin-bottom: 20px; border-bottom: 1px solid #222; padding-bottom: 12px; font-family: 'Orbitron', sans-serif; }

        .tabs-container { display: flex; overflow-x: auto; white-space: nowrap; gap: 10px; padding-bottom: 12px; margin-bottom: 20px; }
        .tabs-container::-webkit-scrollbar { height: 10px; display: block; }
        .tabs-container::-webkit-scrollbar-track { background: #1a1a1f; border-radius: 10px; }
        .tabs-container::-webkit-scrollbar-thumb { background: var(--primary); border-radius: 10px; border: 2px solid #000; }

        .tab-btn { background: #1a1a1f; border: 1px solid #333; color: #555; padding: 10px 18px; cursor: pointer; font-size: 0.65rem; border-radius: 4px; font-family: 'Orbitron', sans-serif; flex: 0 0 auto; transition: 0.3s; }
        .tab-btn.active { color: var(--primary); border-color: var(--primary); background: rgba(0, 255, 65, 0.05); }

        input, select { width: 100%; padding: 12px; margin-bottom: 15px; background: #000; border: 1px solid #333; border-radius: 6px; color: var(--primary); font-family: 'Poppins', sans-serif; box-sizing: border-box; font-size: 0.9rem; }
        
        .main-btn { width: 100%; padding: 16px; background: var(--primary); color: #000; border: none; font-weight: bold; cursor: pointer; text-transform: uppercase; letter-spacing: 2px; border-radius: 6px; font-family: 'Orbitron', sans-serif; }
        
        .result-box { margin-top: 20px; padding: 15px; background: #000; border-left: 4px solid var(--primary); position: relative; border-radius: 0 6px 6px 0; }
        .copy-btn { position: absolute; right: 10px; top: 10px; background: var(--primary); border: none; color: #000; font-size: 0.6rem; font-weight: bold; cursor: pointer; padding: 4px 8px; border-radius: 3px; }
        .label { font-size: 0.6rem; font-weight: bold; margin-bottom: 5px; display: block; color: #888; font-family: 'Orbitron', sans-serif; }
        .history-item { font-size: 0.7rem; border-bottom: 1px solid #222; padding: 10px 0; color: #ccc; }

        .check-group { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 15px; }
        .check-item { font-size: 0.65rem; display: flex; align-items: center; gap: 6px; color: #aaa; cursor: pointer;}
        .check-item input { width: auto; margin: 0; }
    </style>
    <script>
        function setTab(mode) {
            // જો કિંમત ખાલી હોય અથવા 'None' હોય તો 'crypto' Default રાખો
            if (!mode || mode === 'None' || mode === '') mode = 'crypto';

            document.getElementById('main_action').value = mode;
            const sections = ['crypto_ui', 'base64_ui', 'generate_ui', 'strength_ui', 'identify_ui', 'history_ui', 'about_ui'];
            
            sections.forEach(s => {
                const el = document.getElementById(s);
                if (el) el.style.display = 'none';
            });
            
            if(document.getElementById(mode + '_ui')) document.getElementById(mode + '_ui').style.display = 'block';

            const inputTerminal = document.getElementById('input_terminal');
            const runBtn = document.getElementById('run_btn');
            const saltArea = document.getElementById('salt_area');

            if (mode === 'about' || mode === 'history') {
                if(inputTerminal) inputTerminal.style.display = 'none';
                if(runBtn) runBtn.style.display = 'none';
                if(saltArea) saltArea.style.display = 'none';
            } else {
                if(inputTerminal) inputTerminal.style.display = 'block';
                if(runBtn) runBtn.style.display = 'block';
                if(saltArea) saltArea.style.display = (mode === 'crypto') ? 'block' : 'none';
            }

            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            const activeBtn = document.getElementById('tab-' + mode);
            if(activeBtn) activeBtn.classList.add('active');
        }

        // પેજ લોડ થાય ત્યારે છેલ્લું એક્ટિવ ટેબ ફરી ખોલવા માટે
        window.onload = function() { 
            let currentTab = '{{ sel_action }}';
            setTab(currentTab); 
        };

        function copyToClipboard() {
            var text = document.getElementById("res_val").innerText;
            navigator.clipboard.writeText(text);
            alert("COPIED!");
        }
    </script>
</head>
<body>
    <div class="terminal-box">
        <h1>STATION V16.3 MASTER</h1>
        <div class="tabs-container">
            <button id="tab-crypto" class="tab-btn" type="button" onclick="setTab('crypto')">CRYPTO</button>
            <button id="tab-base64" class="tab-btn" type="button" onclick="setTab('base64')">BASE-XX</button>
            <button id="tab-generate" class="tab-btn" type="button" onclick="setTab('generate')">ENHANCER</button>
            <button id="tab-strength" class="tab-btn" type="button" onclick="setTab('strength')">STRENGTH</button>
            <button id="tab-identify" class="tab-btn" type="button" onclick="setTab('identify')">IDENTIFY</button>
            <button id="tab-history" class="tab-btn" type="button" onclick="setTab('history')">HISTORY</button>
            <button id="tab-about" class="tab-btn" type="button" onclick="setTab('about')">ABOUT</button>
        </div>

        <form method="POST">
            <input type="hidden" name="main_action" id="main_action" value="{{ sel_action }}">
            
            <div id="input_terminal">
                <span class="label">SEED WORD / INPUT:</span>
                <input type="text" name="data" value="{{ user_data }}" placeholder="Write_Here" autocomplete="off">
            </div>

            <div id="salt_area" style="display:none;">
                <span class="label">HASH SALT (OPTIONAL):</span>
                <input type="text" name="salt" value="{{ salt_val }}" placeholder="Secret salt..." autocomplete="off">
            </div>

            <div id="crypto_ui" style="display:none;">
                <span class="label">ADVANCED ALGORITHMS:</span>
                <select name="algo">
                    <optgroup label="Latest & Secure">
                        <option value="sha3_256" {% if sel_algo == 'sha3_256' %}selected{% endif %}>SHA3-256 (Keccak)</option>
                        <option value="sha3_512" {% if sel_algo == 'sha3_512' %}selected{% endif %}>SHA3-512</option>
                        <option value="blake2b" {% if sel_algo == 'blake2b' %}selected{% endif %}>BLAKE2b (64-bit)</option>
                        <option value="blake2s" {% if sel_algo == 'blake2s' %}selected{% endif %}>BLAKE2s (32-bit)</option>
                    </optgroup>
                    <optgroup label="Standard">
                        <option value="sha256" {% if sel_algo == 'sha256' %}selected{% endif %}>SHA-256</option>
                        <option value="sha512" {% if sel_algo == 'sha512' %}selected{% endif %}>SHA-512</option>
                        <option value="sha384" {% if sel_algo == 'sha384' %}selected{% endif %}>SHA-384</option>
                        <option value="md5" {% if sel_algo == 'md5' %}selected{% endif %}>MD5</option>
                        <option value="sha1" {% if sel_algo == 'sha1' %}selected{% endif %}>SHA-1</option>
                    </optgroup>
                </select>
            </div>

            <div id="generate_ui" style="display:none;">
                <span class="label">ENHANCEMENT OPTIONS:</span>
                <div class="check-group">
                    <label class="check-item"><input type="checkbox" name="smart_sub" checked> Smart Sub (a=@, s=$)</label>
                    <label class="check-item"><input type="checkbox" name="add_num" checked> Add Random Numbers</label>
                    <label class="check-item"><input type="checkbox" name="add_sym" checked> Add Extra Symbols</label>
                    <label class="check-item"><input type="checkbox" name="random_case" checked> Randomize Case</label>
                </div>
            </div>

            <div id="base64_ui" style="display:none;">
                <span class="label">BASE ENCODING:</span>
                <select name="b_mode">
                    <option value="b64_enc">BASE64 ENCODE</option>
                    <option value="b64_dec">BASE64 DECODE</option>
                    <option value="b32_enc">BASE32 ENCODE</option>
                    <option value="b32_dec">BASE32 DECODE</option>
                </select>
            </div>

            <div id="strength_ui" style="display:none;"><p class="label" style="text-align:center;">Analyzing password integrity...</p></div>
            <div id="identify_ui" style="display:none;"><p class="label" style="text-align:center;">Detecting hash signature...</p></div>
            <div id="about_ui" style="display:none;"><div class="history-item">STATION VERSION: V16.3 (ADVANCED)</div></div>
            
            <div id="history_ui" style="display:none;">
                {% for item in session.get('history', []) %}<div class="history-item">> {{ item }}</div>{% endfor %}
            </div>
            
            <button type="submit" id="run_btn" class="main-btn">_PROCESS_SEQUENCE_</button>
        </form>

        {% if r %}
        <div class="result-box">
            <button class="copy-btn" onclick="copyToClipboard()">COPY</button>
            <span class="label">SYSTEM RESULT:</span>
            <div id="res_val" style="color: #fff; font-size: 0.9rem; margin-top: 5px; word-break: break-all;">{{ r | safe }}</div>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

# (બાકીનું Python લોજિક સમાન રહેશે...)
def smart_enhance(word, subs, nums, syms, cases):
    if not word: return "ENTER A SEED WORD"
    res = word
    if subs:
        map = {'a': '@', 'A': '@', 's': '$', 'S': '$', 'i': '1', 'I': '1', 'o': '0', 'O': '0', 'e': '3', 'E': '3'}
        res = "".join(map.get(c, c) for c in res)
    if cases:
        res = "".join(c.upper() if random.random() > 0.5 else c.lower() for c in res)
    if syms:
        s_list = ["#", "!", "_", "*", "&", "%"]
        res = random.choice(s_list) + res + random.choice(s_list)
    if nums:
        res += str(random.randint(10, 999))
    return res

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'history' not in session: session['history'] = []
    r, sel_action, user_data, salt_val, sel_algo = None, "crypto", "", "", "sha256"
    
    if request.method == 'POST':
        sel_action = request.form.get('main_action', 'crypto')
        user_data = request.form.get('data', '').strip()
        salt_val = request.form.get('salt', '').strip()
        sel_algo = request.form.get('algo', 'sha256') 
        
        try:
            if sel_action == "generate":
                r = smart_enhance(user_data, request.form.get('smart_sub'), 
                                  request.form.get('add_num'), request.form.get('add_sym'), 
                                  request.form.get('random_case'))
            
            elif sel_action == "strength":
                score = 0
                if len(user_data) >= 12: score += 1
                if re.search("[A-Z]", user_data): score += 1
                if re.search("[0-9]", user_data): score += 1
                if re.search("[!@#$%^&*]", user_data): score += 1
                status = '<span style="color:var(--strong)">STRONG</span>' if score >= 3 else '<span style="color:var(--medium)">MEDIUM</span>' if score == 2 else '<span style="color:var(--weak)">WEAK</span>'
                r = f"LEVEL: {status}"
            
            elif sel_action == "crypto":
                r = hashlib.new(sel_algo, (user_data + salt_val).encode()).hexdigest()
            
            elif sel_action == "base64":
                m = request.form.get('b_mode')
                if m == "b64_enc": r = base64.b64encode(user_data.encode()).decode()
                elif m == "b64_dec": r = base64.b64decode(user_data.encode()).decode()
                elif m == "b32_enc": r = base64.b32encode(user_data.encode()).decode()
                elif m == "b32_dec": r = base64.b32decode(user_data.encode()).decode()
            
            elif sel_action == "identify":
                l = len(user_data)
                types = {32: "MD5", 40: "SHA-1", 64: "SHA-256 / SHA3-256", 96: "SHA-384", 128: "SHA-512 / SHA3-512"}
                r = f"LENGTH: {l} | TYPE: {types.get(l, 'UNKNOWN')}"

        except Exception as e:
            r = f"ERROR: {str(e)}"

        if r:
            h = session['history']
            h.insert(0, f"{sel_action.upper()}: {str(r)[:15]}...")
            session['history'] = h[:5]
            session.modified = True

    return render_template_string(CYBER_HTML, r=r, sel_action=sel_action, user_data=user_data, salt_val=salt_val, sel_algo=sel_algo)

if __name__ == '__main__':
    app.run(debug=True, port=5005)