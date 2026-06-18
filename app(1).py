import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ML in the Cloud – Présentation du Devoir",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS global ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600;700&family=Share+Tech+Mono&display=swap');

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'Rajdhani', sans-serif;
    background-color: #080d14;
    color: #cdd9e8;
}
.stApp { background: #080d14; }
.block-container { padding: 0 2rem 4rem 2rem !important; max-width: 1200px; margin: auto; }

/* ── Scanline overlay ── */
.stApp::before {
    content: '';
    position: fixed; top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(0,200,255,0.015) 2px,
        rgba(0,200,255,0.015) 4px
    );
    pointer-events: none;
    z-index: 9999;
}

/* ── HERO ── */
.hero {
    text-align: center;
    padding: 4rem 1rem 3rem;
    position: relative;
}
.hero-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.35em;
    color: #00c8ff;
    text-transform: uppercase;
    margin-bottom: 1rem;
    display: flex; align-items: center; justify-content: center; gap: 0.8rem;
}
.hero-label::before, .hero-label::after {
    content: '◆';
    color: #00c8ff;
    opacity: 0.7;
}
.hero-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(2.2rem, 5vw, 4rem);
    font-weight: 900;
    color: #ffffff;
    letter-spacing: 0.04em;
    line-height: 1.1;
    margin-bottom: 0.5rem;
    text-shadow: 0 0 40px rgba(0,200,255,0.35);
}
.hero-subtitle {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.85rem;
    letter-spacing: 0.25em;
    color: #4ecdc4;
    text-transform: uppercase;
    margin-bottom: 2rem;
}
.hero-desc {
    font-size: 1.15rem;
    color: #8aa0b8;
    margin: 0 auto 0.5rem;
    line-height: 1.7;
    text-align: center;
}
.hero-divider {
    width: 180px;
    height: 1px;
    background: linear-gradient(90deg, transparent, #00c8ff, transparent);
    margin: 2.5rem auto;
}

/* ── Section title ── */
.section-title {
    font-family: 'Orbitron', monospace;
    font-size: 1.3rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
    display: flex; align-items: center; gap: 0.75rem;
}
.section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, #00c8ff33, transparent);
}

/* ── Info Card ── */
.info-card {
    background: linear-gradient(135deg, #0d1721 0%, #101a26 100%);
    border: 1px solid #1a2d42;
    border-left: 3px solid #00c8ff;
    border-radius: 8px;
    padding: 1.6rem 2rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.info-card::before {
    content: '';
    position: absolute; top: 0; right: 0;
    width: 120px; height: 120px;
    background: radial-gradient(circle, rgba(0,200,255,0.06) 0%, transparent 70%);
}
.info-card h4 {
    font-family: 'Orbitron', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    color: #00c8ff;
    text-transform: uppercase;
    margin: 0 0 0.5rem;
}
.info-card p {
    font-size: 1.05rem;
    color: #cdd9e8;
    margin: 0;
    line-height: 1.6;
}
.info-card .value-big {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: #e8f1fb;
}

/* ── Supervisor card ── */
.supervisor-card {
    background: linear-gradient(135deg, #0d1e2e 0%, #0a1520 100%);
    border: 1px solid #1a3a52;
    border-top: 3px solid #4ecdc4;
    border-radius: 8px;
    padding: 1.6rem 2rem;
    text-align: center;
}
.supervisor-card .badge {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    color: #4ecdc4;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.supervisor-card .name {
    font-family: 'Orbitron', monospace;
    font-size: 1.1rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 0.3rem;
}
.supervisor-card .role {
    font-size: 0.95rem;
    color: #7fa8c8;
    font-style: italic;
}

/* ── Part cards ── */
.part-card {
    border-radius: 10px;
    padding: 2rem;
    height: 100%;
    position: relative;
    overflow: hidden;
}
.part-card-1 {
    background: linear-gradient(145deg, #0d1b2e 0%, #0f2035 100%);
    border: 1px solid #1e3a58;
    border-top: 4px solid #00c8ff;
}
.part-card-2 {
    background: linear-gradient(145deg, #0d2218 0%, #0f2b1e 100%);
    border: 1px solid #1e4832;
    border-top: 4px solid #4ecdc4;
}
.part-number {
    font-family: 'Orbitron', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}
.part-card-1 .part-number { color: #00c8ff; }
.part-card-2 .part-number { color: #4ecdc4; }
.part-title {
    font-family: 'Orbitron', monospace;
    font-size: 1.15rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 1rem;
    line-height: 1.3;
}
.part-desc {
    font-size: 0.98rem;
    color: #8aa0b8;
    line-height: 1.65;
    margin-bottom: 1.2rem;
}
.part-tasks {
    list-style: none;
    padding: 0;
    margin: 0 0 1.5rem 0;
}
.part-tasks li {
    font-size: 0.92rem;
    color: #b0c4d8;
    padding: 0.3rem 0 0.3rem 1.2rem;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    position: relative;
    line-height: 1.4;
}
.part-tasks li::before {
    content: '→';
    position: absolute; left: 0;
    color: #00c8ff;
    font-family: 'Share Tech Mono', monospace;
}
.part-card-2 .part-tasks li::before { color: #4ecdc4; }
.part-members {
    background: rgba(0,0,0,0.2);
    border-radius: 6px;
    padding: 0.9rem 1rem;
    margin-bottom: 1.2rem;
}
.part-members .label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    color: #00c8ff;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.part-card-2 .part-members .label { color: #4ecdc4; }
.part-members .names {
    font-size: 0.95rem;
    font-weight: 600;
    color: #e8f1fb;
    line-height: 1.5;
}

/* ── Link button ── */
.link-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.6rem 1.2rem;
    border-radius: 4px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    text-decoration: none !important;
    font-weight: 600;
    transition: all 0.2s;
}
.link-btn-1 {
    background: linear-gradient(135deg, #00c8ff22, #00c8ff11);
    border: 1px solid #00c8ff55;
    color: #00c8ff !important;
}
.link-btn-1:hover {
    background: linear-gradient(135deg, #00c8ff44, #00c8ff22);
    border-color: #00c8ff;
    box-shadow: 0 0 20px rgba(0,200,255,0.3);
}
.link-btn-2 {
    background: linear-gradient(135deg, #4ecdc422, #4ecdc411);
    border: 1px solid #4ecdc455;
    color: #4ecdc4 !important;
}
.link-btn-2:hover {
    background: linear-gradient(135deg, #4ecdc444, #4ecdc422);
    border-color: #4ecdc4;
    box-shadow: 0 0 20px rgba(78,205,196,0.3);
}

/* ── Team grid ── */
.team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}
.team-member {
    background: linear-gradient(135deg, #0d1721 0%, #101a26 100%);
    border: 1px solid #1a2d42;
    border-radius: 8px;
    padding: 1.2rem 1.4rem;
    text-align: center;
}
.team-member .avatar {
    width: 48px; height: 48px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Orbitron', monospace;
    font-size: 1.1rem;
    font-weight: 700;
    margin: 0 auto 0.7rem;
}
.team-member.p1 .avatar {
    background: linear-gradient(135deg, #00c8ff33, #00c8ff11);
    border: 1px solid #00c8ff55;
    color: #00c8ff;
}
.team-member.p2 .avatar {
    background: linear-gradient(135deg, #4ecdc433, #4ecdc411);
    border: 1px solid #4ecdc455;
    color: #4ecdc4;
}
.team-member .mname {
    font-size: 0.9rem;
    font-weight: 700;
    color: #e8f1fb;
    margin-bottom: 0.2rem;
    line-height: 1.3;
}
.team-member .mpart {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
}
.team-member.p1 .mpart { color: #00c8ff; }
.team-member.p2 .mpart { color: #4ecdc4; }

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 2rem;
    border-top: 1px solid #1a2d42;
    margin-top: 3rem;
}
.footer-text {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    color: #3a5570;
}

/* ── Streamlit hide default ── */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
div[data-testid="stDecoration"] { display: none; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero">
    <div class="hero-label">Machine Learning in the Cloud</div>
    <div class="hero-title">Devoir de CC</div>
    <div class="hero-subtitle">Intelligence Artificielle · Prédiction · Monitoring</div>
    <p class="hero-desc">
        Une solution complète combinant vision par ordinateur, traitement du langage naturel,
        séries temporelles et monitoring cloud — articulée en deux applications déployées.
    </p>
    <div class="hero-divider"></div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# INFOS GÉNÉRALES
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">📋 Informations Générales</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h4>Matière</h4>
        <p class="value-big">Machine Learning in the Cloud</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h4>Type d'évaluation</h4>
        <p class="value-big">Contrôle Continu (CC)</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="supervisor-card">
        <div class="badge">◆ Supervisé par</div>
        <div class="name">Mr Dalil Abdouraman</div>
        <div class="role">ING DATA – Specialist IA</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# INTITULÉ DU DEVOIR
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">📌 Ce qu\'il était question de faire</div>', unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
    <h4>Objectif global du devoir</h4>
    <p>
        Concevoir et déployer un système ML complet en deux modules distincts :
        <strong style="color:#e8f1fb"> (1)</strong> un CNN de classification de maladies rénales enrichi d'un chatbot intelligent, de traduction automatique, de synthèse vocale et de monitoring LangSmith ;
        <strong style="color:#e8f1fb"> (2)</strong> un système de prédiction des cours boursiers des entreprises NVIDIA, Oracle, IBM et Cisco
        exploitant trois modèles — LSTM, Facebook Prophet et NeuralProphet — avec un horizon de prédiction
        configurable de 3 à 12 mois et un chatbot d'analyse financière.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# LES DEUX PARTIES
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">🔬 Répartition du Travail</div>', unsafe_allow_html=True)

col_p1, col_p2 = st.columns(2, gap="large")

with col_p1:
    st.markdown("""
    <div class="part-card part-card-1">
        <div class="part-number">◆ Partie 01</div>
        <div class="part-title">Prédiction des Maladies Rénales<br>avec Monitoring</div>
        <p class="part-desc">
            Système de diagnostic assisté par CNN sur des images CT-Scan rénales,
            enrichi d'un pipeline NLP complet et d'un monitoring de production.
        </p>
        <ul class="part-tasks">
            <li>CNN de classification (Normal / Kyste / Tumeur / Pierre) sur le dataset CT-Kidney Kaggle</li>
            <li>Chatbot intelligent intégré (résultat de classification → input chatbot)</li>
            <li>Traduction automatique du résumé en Allemand</li>
            <li>Conversion texte → audio du résultat du chatbot</li>
            <li>Monitoring de bout-en-bout avec LangSmith</li>
        </ul>
        <div class="part-members">
            <div class="label">👥 Membres</div>
            <div class="names">Aimé Thierry MBOG<br>Hamad RASSEM</div>
        </div>
        <a class="link-btn link-btn-1" href="https://aimethmbog1-medicalscan-ai-app-kidney-5-eeferc.streamlit.app/" target="_blank">
            🚀 Voir l'application déployée
        </a>
    </div>
    """, unsafe_allow_html=True)

with col_p2:
    st.markdown("""
    <div class="part-card part-card-2">
        <div class="part-number">◆ Partie 02</div>
        <div class="part-title">Prédiction des Cours<br>d'Actions Boursières</div>
        <p class="part-desc">
            Plateforme de forecasting financier multi-modèles pour quatre entreprises tech,
            avec horizon de prédiction configurable et analyse conversationnelle.
        </p>
        <ul class="part-tasks">
            <li>Modèle LSTM pour la prédiction des séries temporelles boursières</li>
            <li>Sélecteur d'horizon : de 3 à 12 mois (~63 à 252 jours de bourse)</li>
            <li>Actions supportées : NVIDIA (NVDA), Oracle (ORCL), IBM, Cisco (CSCO)</li>
            <li>Facebook Prophet &amp; NeuralProphet pour la prévision temporelle additive</li>
            <li>Sélecteur d'actions: NVIDIA (NVDA), Oracle (ORCL), IBM, Cisco (CSCO) </li>
        </ul>
        <div class="part-members">
            <div class="label">👥 Membres</div>
            <div class="names">Kamno Kamche RUTH<br>Manuella EFEMBA</div>
        </div>
        <a class="link-btn link-btn-2" href="https://stocksightaistockprediction-rrceguvir9vxa9tmappwkps.streamlit.app/" target="_blank">
            🚀 Voir l'application déployée
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# ÉQUIPE
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">👥 L\'Équipe</div>', unsafe_allow_html=True)

st.markdown("""
<div class="team-grid">
    <div class="team-member p1">
        <div class="avatar">AT</div>
        <div class="mname">Aimé Thierry MBOG</div>
        <div class="mpart">Partie 1 · Maladies Rénales</div>
    </div>
    <div class="team-member p1">
        <div class="avatar">HR</div>
        <div class="mname">Hamad RASSEM</div>
        <div class="mpart">Partie 1 · Maladies Rénales</div>
    </div>
    <div class="team-member p2">
        <div class="avatar">KR</div>
        <div class="mname">Kamno Kamche RUTH</div>
        <div class="mpart">Partie 2 · Prédiction Boursière</div>
    </div>
    <div class="team-member p2">
        <div class="avatar">ME</div>
        <div class="mname">Manuella EFEMBA</div>
        <div class="mpart">Partie 2 · Prédiction Boursière</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TECH STACK
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">⚙️ Technologies Utilisées</div>', unsafe_allow_html=True)

tc1, tc2, tc3, tc4 = st.columns(4)

techs = [
    ("🧠", "Deep Learning", "CNN · LSTM · NeuralProphet"),
    ("📊", "Time Series", "Facebook Prophet · NeuralProphet"),
    ("💬", "NLP & Chatbot", "LangChain · LangSmith · TTS"),
    ("☁️", "Déploiement", "Streamlit Cloud · Python"),
]

for col, (icon, title, stack) in zip([tc1, tc2, tc3, tc4], techs):
    with col:
        st.markdown(f"""
        <div class="info-card" style="text-align:center; border-left-color: #4ecdc4;">
            <div style="font-size:1.8rem; margin-bottom:0.4rem;">{icon}</div>
            <h4 style="color:#4ecdc4;">{title}</h4>
            <p style="font-size:0.9rem; color:#8aa0b8;">{stack}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# LIENS RAPIDES
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">🔗 Accès Rapide aux Applications</div>', unsafe_allow_html=True)

lc1, lc2 = st.columns(2, gap="large")

with lc1:
    st.markdown("""
    <div class="info-card" style="border-left-color:#00c8ff;">
        <h4>🏥 Application — Partie 1</h4>
        <p style="margin-bottom:1rem; color:#8aa0b8;">Diagnostic CNN · Chatbot · Audio · Monitoring LangSmith</p>
        <a class="link-btn link-btn-1" href="https://aimethmbog1-medicalscan-ai-app-kidney-5-eeferc.streamlit.app/" target="_blank">
            Ouvrir MedicalScan AI →
        </a>
    </div>
    """, unsafe_allow_html=True)

with lc2:
    st.markdown("""
    <div class="info-card" style="border-left-color:#4ecdc4;">
        <h4>📈 Application — Partie 2</h4>
        <p style="margin-bottom:1rem; color:#8aa0b8;">LSTM · Prophet · NeuralProphet · Chatbot Financier</p>
        <a class="link-btn link-btn-2" href="https://stocksightaistockprediction-rrceguvir9vxa9tmappwkps.streamlit.app/" target="_blank">
            Ouvrir StockSight AI →
        </a>
    </div>
    """, unsafe_allow_html=True)


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-text">
        ◆ &nbsp; Machine Learning in the Cloud · CC; ◆ &nbsp;
        Supervisé par Mr Dalil Abdouraman (ING DATA – Specialist IA) &nbsp; ◆ &nbsp;
        MBOG · RASSEM · RUTH · EFEMBA &nbsp; ◆
    </div>
</div>
""", unsafe_allow_html=True)
