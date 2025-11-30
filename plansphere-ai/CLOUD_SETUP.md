# Plansphere.ai Cloud Deployment Setup

## Quick Start: Connect to MongoDB Atlas (Cloud)

### Step 1: Create a MongoDB Atlas Cluster
1. Go to https://www.mongodb.com/cloud/atlas
2. Sign in or create a free account
3. Create a free cluster (M0 tier is free)
4. Choose a cloud provider and region (AWS, GCP, or Azure)

### Step 2: Create a Database User
1. In Atlas UI, go to **Database Access** → **Add New Database User**
2. Choose "Password" authentication method
3. Create a username and strong password
4. Set permissions to "Read and write to any database" (or create a custom role for your DB)
5. Click "Add User"

### Step 3: Whitelist Your IP (Network Access)
1. In Atlas UI, go to **Network Access** → **Add IP Address**
2. For **local testing**: add your current IP address (you can find it by running `curl ifconfig.me` or check your router)
3. For **production deployment on Vercel/cloud**: add `0.0.0.0/0` (allows all IPs; secure this in production by adding only your deployment service IPs)

### Step 4: Get Your Connection String
1. In Atlas, click **Connect** → **Connect your application**
2. Copy the connection string (it will look like):
   ```
   mongodb+srv://<user>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```
3. Replace `<user>` and `<password>` with your database user credentials from Step 2

### Step 5: Local Development (Set Environment Variables)

#### Option A: Using `.env` file (Recommended for local dev)
1. Copy `.env.example` to `.env`:
   ```powershell
   Copy-Item .env.example .env
   ```
2. Edit `.env` and fill in your values:
   ```
   MONGO_URI="mongodb+srv://myuser:mypassword@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
   MONGO_DBNAME="plansphere"
   SECRET_KEY="your-secret-key-here"
   PORT="5000"
   ```
3. Install `python-dotenv` (already added to `requirements.txt`):
   ```powershell
   pip install python-dotenv
   ```
4. The Flask app will automatically load `.env` on startup

#### Option B: Using PowerShell Environment Variables (Temporary)
```powershell
$env:MONGO_URI = 'mongodb+srv://myuser:mypassword@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority'
$env:MONGO_DBNAME = 'plansphere'
$env:SECRET_KEY = 'your-secret-key'
python app_with_navigation.py
```

### Step 6: Test Connection Locally
```powershell
# Set environment variables (see Step 5 above)
# Then run a quick Python test:
python -c "from models import get_db; db = get_db(); print('Connected!'); print(db.list_collection_names())"
```

### Step 7: Deploy to Vercel
1. Install Vercel CLI:
   ```powershell
   npm install -g vercel
   ```
2. Login to Vercel:
   ```powershell
   vercel login
   ```
3. Set environment variables in Vercel dashboard:
   - Go to your Vercel project → **Settings** → **Environment Variables**
   - Add:
     - `MONGO_URI` = your Atlas connection string
     - `MONGO_DBNAME` = plansphere
     - `SECRET_KEY` = your secret key
4. Deploy:
   ```powershell
   vercel --prod
   ```

## Troubleshooting

### "Connection refused" or "Cannot connect to MongoDB"
- Check your MongoDB URI is correct (copy from Atlas again)
- Confirm your IP is whitelisted in Atlas Network Access
- Check that database user credentials are correct

### "MONGO_URI is empty" error
- Make sure `.env` file exists and is in the project root (not in `plansphere-ai/`)
- Or set environment variables in Vercel dashboard for production

### Vercel deployment fails
- Check Vercel build logs for the exact error
- Ensure `requirements.txt` is in the project root (already in place)
- Ensure `vercel.json` is configured correctly (already in place)

## Security Checklist
- ✅ Never commit `.env` files with real credentials (it's in `.gitignore`)
- ✅ Use strong, unique passwords for database users
- ✅ Restrict IP access in production (don't use `0.0.0.0/0` permanently)
- ✅ Rotate credentials periodically
- ✅ Use environment variables in production, not hardcoded values

## Need Help?
- [MongoDB Atlas Docs](https://docs.atlas.mongodb.com/)
- [Vercel Python Deployment](https://vercel.com/docs/frameworks/python)
- [Flask-PyMongo Docs](https://flask-pymongo.readthedocs.io/)
