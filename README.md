# SafeRoute-AI
### An AI-Powered Automated Safety Check-In Agent for Women, sends real-time notifications to family when you enter/exit metro or college.
  
  Built for Kaggle x Google 5-Day AI Agent Intensive

---

## 🧠 Problem Statement  
As a college student traveling through unsafe or high-risk routes, I often forget to update my parents when I check in/out of metro stations.  
This small delay creates **panic, anxiety, and uncertainty** — especially during late travel hours.

Millions of students, working women, and commuters face this same problem:
- Forgetting to notify family  
- No automatic alert system  
- Safety uncertainty during solo travel  

**SafeRoute AI** solves this by sending **automatic, real-time safety notifications** to trusted contacts whenever the user enters or exits the metro.

---

## 🤖 Why Agents?  
Agents are ideal because:
- They automate repetitive human actions  
- They follow rules and trigger automatically (no manual messaging)  
- They integrate AI + Webhooks + Messaging channels  
- They work autonomously in the background  

SafeRoute AI uses an AI Agent to:
1. Receive metro check-in event  
2. Understand the context (check-in or check-out)  
3. Format it into a clear alert  
4. Send it to family email or WhatsApp automatically  

---

## 🏗️ What I Built — Architecture Overview  
SafeRoute AI is a **no-code/low-code agent** built using:

- **Make.com** (automation workflow)  
- **Google Gemini 1.5 Flash** (AI reasoning + message generation)  
- **Webhook Triggers** (simulate metro check-in/check-out event)  
- **Email Notifications** (default output channel)  
- Optional: WhatsApp Business Cloud API  

### High-Level Architecture


You can view the full architecture in `architecture.png`.

---

## 🎥 Demo  
The agent can be tested by sending any event to the webhook URL generated in Make.com.

Example demo event:

{
"event": "check_in",
"location": "Kashmere Gate Metro Station",
"timestamp": "2025-11-29T10:13:00Z"
}

Resulting output:
User has safely checked IN at Kashmere Gate Metro Station (10:13 AM).
Notification sent to family.


Demo details available in `demo.md`.

---

## 🛠️ The Build — Tools & Technologies  
| Component | Purpose |
|----------|---------|
| **Make.com** | No-code workflow automation |
| **Google Gemini Flash 1.5** | AI reasoning + message creation |
| **Custom Webhook** | Metro event trigger |
| **Email Module** | Sends alerts to trusted contacts |
| **JSON + Pseudocode** | Technical documentation for reproducibility |

Files included:
- `agent_workflow.json` — JSON representation of the Make workflow  
- `pseudocode.py` — Logic representation of the agent  
- `demo.md` — Live demo instructions  

---

## ⏳ If I Had More Time  
I would extend SafeRoute AI into a full civic-tech safety tool:
- Add **GPS-based auto-detection** instead of manual punching  
- Enable **WhatsApp push notifications**  
- Add **panic button alerts**  
- Integrate **Delhi Metro API** for real-time station logs  
- Add **location-sharing timeline** for families  
- Deploy as a **mobile app** with background activity  

---

## 📎 Project Links  
- Kaggle Submission Page: kaggle.com/competitions/agents-intensive-capstone-project/writeups/new-writeup-1764318230701

## 📌 Demo Video
Watch the full project demo here: https://youtu.be/DFq5ZWTmiDY?feature=shared

---

