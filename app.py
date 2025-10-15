from flask import Flask, jsonify, request
from datetime import datetime, timezone

app = Flask(__name__)

@app.get("/u")
def hallo():
    # FinTech-themed demo payload for demonstration purposes
    payload = {
        "service": "snowball-Finance API",
        "message": "Willkommen bei snowball-Finance – FinTech Demo",
        "customer": {
            "name": request.args.get("name", "Max Mustermann")
        },
        "account": {
            "iban": "DE89370400440532013000",
            "currency": request.args.get("currency", "EUR"),
            "balance": {
                "amount": 1024.55,
                "currency": request.args.get("currency", "EUR")
            },
            "available_credit": 5000.00,
            "masked_card": "5355 **** **** 1234"
        },
        "features": ["instant_payments", "open_banking", "fraud_monitoring"],
        "server_time": datetime.now(timezone.utc).isoformat()
    }
    return jsonify(payload), 200


@app.get("/")
def index():
    # Simple FinTech-styled UI that consumes /u
    return (
        """
        <!doctype html>
        <html lang=\"de\">
        <head>
            <meta charset=\"utf-8\" />
            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
            <title>snowball-Finance Dashboard</title>
            <style>
                :root { --bg:#0b1020; --panel:#121a33; --accent:#4fd1c5; --text:#e8eef9; --muted:#9fb3c8; --danger:#ff7b7b; }
                * { box-sizing: border-box; }
                body { margin:0; font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Arial; background: linear-gradient(180deg, #0b1020 0%, #0e1530 100%); color: var(--text); }
                header { padding: 24px 16px; border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(0,0,0,0.2); backdrop-filter: blur(6px); position: sticky; top:0; }
                .container { max-width: 980px; margin: 0 auto; padding: 0 16px; }
                .brand { display:flex; align-items:center; gap:12px; font-weight:700; letter-spacing:0.4px; }
                .brand-badge { width:28px; height:28px; border-radius:8px; background: radial-gradient(120% 120% at 20% 20%, var(--accent) 0%, #1e90ff 60%, #7c3aed 120%); box-shadow: 0 0 24px rgba(79,209,197,0.5); }
                main { padding: 28px 0 60px; }
                .panel { background: linear-gradient(180deg, rgba(18,26,51,0.9), rgba(18,26,51,0.7)); border:1px solid rgba(255,255,255,0.06); border-radius: 14px; padding: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
                .grid { display:grid; grid-template-columns: 1.2fr 1fr; gap: 20px; }
                .controls { display:flex; gap: 10px; flex-wrap:wrap; margin: 12px 0 6px; }
                label { font-size: 12px; color: var(--muted); }
                input, select, button { height: 40px; border-radius: 10px; border:1px solid rgba(255,255,255,0.08); background:#0c1427; color:var(--text); padding:0 12px; }
                input, select { flex: 1 1 180px; min-width: 160px; }
                button { background: linear-gradient(180deg, var(--accent), #2bb3a7); color: #04131a; font-weight: 700; cursor:pointer; box-shadow: 0 8px 20px rgba(79,209,197,0.25); }
                button:hover { filter: brightness(1.05); }
                .cards { display:grid; grid-template-columns: repeat(2, 1fr); gap:12px; margin-top: 12px; }
                .card { background: #0c1427; border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 14px; }
                .muted { color: var(--muted); font-size: 12px; }
                .amount { font-size: 28px; font-weight: 800; letter-spacing: -0.5px; }
                .features { display:flex; flex-wrap:wrap; gap:8px; margin-top: 6px; }
                .chip { font-size: 12px; border:1px solid rgba(255,255,255,0.08); padding:6px 10px; border-radius: 999px; background:#0c1427; }
                footer { text-align:center; color:var(--muted); font-size: 12px; margin-top: 24px; }
                .error { color: var(--danger); margin-top: 8px; }
                @media (max-width: 820px) { .grid { grid-template-columns: 1fr; } .cards { grid-template-columns: 1fr; } }
            </style>
        </head>
        <body>
            <header>
                <div class=\"container\">
                    <div class=\"brand\">
                        <div class=\"brand-badge\"></div>
                        <div>snowball-Finance · Demo Dashboard</div>
                    </div>
                </div>
            </header>
            <main>
                <div class=\"container\">
                    <div class=\"panel\">
                        <div class=\"controls\">
                            <div>
                                <label>Kunde</label><br/>
                                <input id=\"name\" value=\"Max Mustermann\" />
                            </div>
                            <div>
                                <label>Währung</label><br/>
                                <select id=\"currency\">
                                    <option>EUR</option>
                                    <option>USD</option>
                                    <option>CHF</option>
                                    <option>GBP</option>
                                </select>
                            </div>
                            <div style=\"align-self:end\">
                                <button id=\"loadBtn\">Aktualisieren</button>
                            </div>
                        </div>
                        <div id=\"error\" class=\"error\"></div>
                        <div class=\"grid\">
                            <div>
                                <div class=\"card\">
                                    <div class=\"muted\">Kontoinhaber</div>
                                    <div id=\"customerName\"></div>
                                </div>
                                <div class=\"cards\">
                                    <div class=\"card\">
                                        <div class=\"muted\">IBAN</div>
                                        <div id=\"iban\"></div>
                                    </div>
                                    <div class=\"card\">
                                        <div class=\"muted\">Karte</div>
                                        <div id=\"maskedCard\"></div>
                                    </div>
                                </div>
                                <div class=\"card\" style=\"margin-top:12px\">
                                    <div class=\"muted\">Features</div>
                                    <div id=\"features\" class=\"features\"></div>
                                </div>
                            </div>
                            <div>
                                <div class=\"card\">
                                    <div class=\"muted\">Kontostand</div>
                                    <div class=\"amount\" id=\"balance\"></div>
                                </div>
                                <div class=\"cards\">
                                    <div class=\"card\">
                                        <div class=\"muted\">Verfügbarer Kredit</div>
                                        <div id=\"credit\"></div>
                                    </div>
                                    <div class=\"card\">
                                        <div class=\"muted\">Serverzeit (UTC)</div>
                                        <div id=\"serverTime\"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <footer>snowball-Finance</footer>
                </div>
            </main>
            <script>
                const $ = (id) => document.getElementById(id);
                function fmt(n, c) { try { return new Intl.NumberFormat('de-DE', { style: 'currency', currency: c }).format(n); } catch(e) { return n + ' ' + c; } }
                async function load() {
                    const name = $("name").value || "Max Mustermann";
                    const currency = $("currency").value || "EUR";
                    $("error").textContent = "";
                    try {
                        const res = await fetch(`/u?name=${encodeURIComponent(name)}&currency=${encodeURIComponent(currency)}`);
                        if (!res.ok) throw new Error(`HTTP ${res.status}`);
                        const data = await res.json();
                        $("customerName").textContent = data.customer?.name ?? name;
                        $("iban").textContent = data.account?.iban ?? "-";
                        $("maskedCard").textContent = data.account?.masked_card ?? "-";
                        const bal = data.account?.balance?.amount ?? 0;
                        const cur = data.account?.balance?.currency ?? currency;
                        $("balance").textContent = fmt(bal, cur);
                        $("credit").textContent = fmt(data.account?.available_credit ?? 0, cur);
                        $("serverTime").textContent = data.server_time ?? "-";
                        const features = data.features ?? [];
                        $("features").innerHTML = features.map(f => `<span class=\"chip\">${f}</span>`).join(" ");
                    } catch (err) {
                        $("error").textContent = `Fehler beim Laden: ${err.message}`;
                    }
                }
                $("loadBtn").addEventListener("click", load);
                window.addEventListener("DOMContentLoaded", load);
            </script>
        </body>
        </html>
        """,
        200,
        {"Content-Type": "text/html; charset=utf-8"}
    )


if __name__ == "__main__":
    # Intentionally enable debug mode to keep the app simple for demo purposes
    # Do NOT use debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)
