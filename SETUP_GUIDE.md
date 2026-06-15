# Campus Voice - Setup Guide

## Quick Start for GitHub Upload

Your project is now ready to push to GitHub! Follow these steps:

### Step 1: Create a GitHub Repository
1. Go to [GitHub.com](https://github.com/new)
2. Click "New repository"
3. Name it: `campus-voice` (or your preferred name)
4. Add description: "Smart Complaint Management System with Rewards"
5. Choose Public or Private
6. **Do NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

### Step 2: Add Remote and Push to GitHub
Copy and run these commands in PowerShell:

```powershell
cd "c:\Users\Priyanshu Rajpurohit\Downloads\campus-voice-with-rewards\campus-voice"

# Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual GitHub username and repo name
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Rename branch to main if needed
git branch -M main

# Push your code
git push -u origin main
```

### Alternative: Using SSH (if you have SSH keys configured)
```powershell
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

---

## Project Structure

```
campus-voice/
├── app.py                 # Main Flask application
├── init_db.py             # Database initialization script
├── migrate_rewards.py      # Rewards migration script
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
├── static/
│   ├── css/style.css      # Styling
│   ├── js/main.js         # JavaScript functionality
│   └── uploads/           # User uploads (not tracked)
└── templates/
    ├── base.html          # Base template
    ├── admin.html         # Admin dashboard
    ├── complaint.html      # New complaint form
    ├── dashboard.html      # Student dashboard
    ├── home.html          # Home page
    ├── leaderboard.html   # Leaderboard
    ├── login.html         # Login page
    ├── my_complaints.html # User complaints
    └── register.html      # Registration
```

---

## Installation & Running

### Prerequisites
- Python 3.8+
- pip

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_db.py

# Run application
python app.py
```

The app will be available at: `http://127.0.0.1:5000`

### Admin Credentials
- Email: `admin@campus.edu`
- Password: `Admin@123`

---

## Features

✨ **Smart Complaint Management**
- Submit complaints with photos and descriptions
- Real-time status tracking (Pending → Assigned → In Progress → Resolved)
- 9 complaint categories
- Priority levels (Low, Medium, High)

🏆 **Reward System**
- Students earn 50 points when complaint is assigned by admin
- Leaderboard ranking system
- Track earned rewards on dashboard

👨‍💼 **Admin Dashboard**
- View all complaints with filters
- Update status and priority
- Assign complaints to students
- Analytics and top contributors

📱 **Responsive Design**
- Works on desktop, tablet, and mobile
- Modern UI with Tailwind CSS
- Bootstrap components

---

## Latest Update

**Reward System Change**: Points are now awarded when admin assigns a complaint (status = "Assigned"), not when it's resolved. This encourages faster issue reporting.

---

## Future Enhancements

- Email notifications
- Complaint attachments (multiple files)
- Department-wise assignments
- SMS alerts
- Mobile app integration

---

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, create a GitHub issue or contact the development team.
