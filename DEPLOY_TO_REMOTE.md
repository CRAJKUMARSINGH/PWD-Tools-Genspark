# Deploy PWD Tools to Remote Repository

This guide explains how to deploy the PWD Tools application to a remote Git repository and then to Streamlit Cloud.

## Prerequisites

1. Git installed on your system
2. A GitHub/GitLab/Bitbucket account
3. The PWD Tools repository locally

## Step 1: Create a Remote Repository

### GitHub
1. Go to https://github.com/new
2. Create a new repository named `pwd-tools`
3. Don't initialize with README, .gitignore, or license
4. Copy the repository URL

### GitLab
1. Go to https://gitlab.com/projects/new
2. Create a new project named `pwd-tools`
3. Copy the repository URL

### Bitbucket
1. Go to https://bitbucket.org/repo/create
2. Create a new repository named `pwd-tools`
3. Copy the repository URL

## Step 2: Add Remote and Push

1. Open terminal/command prompt in the PWD Tools directory
2. Add the remote repository:
   ```bash
   git remote add origin <repository-url>
   ```
   
3. Push the code:
   ```bash
   git push -u origin master
   ```

## Step 3: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Sign in with your GitHub/GitLab/Bitbucket account
3. Click "New app"
4. Select your `pwd-tools` repository
5. Set these options:
   - Branch: `master` (or `main`)
   - Main file: `app.py`
6. Click "Deploy!"

## Step 4: Verify Deployment

1. Wait for the deployment to complete (usually 1-2 minutes)
2. Click "View app" to see your deployed application
3. Test all tools to ensure they work correctly

## Troubleshooting

### Common Issues

1. **Push rejected**:
   ```bash
   git pull origin master --allow-unrelated-histories
   git push -u origin master
   ```

2. **Streamlit Cloud deployment fails**:
   - Check that `requirements.txt` lists all dependencies
   - Ensure `runtime.txt` specifies the correct Python version
   - Verify that `app.py` is the correct entry point

3. **Missing files**:
   - Check `.gitignore` to ensure important files aren't excluded
   - Use `git add <filename>` to add missing files

### Updating the Deployment

To update your deployed application:

1. Make changes to your local code
2. Commit the changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```
   
3. Push to remote:
   ```bash
   git push origin master
   ```
   
4. On Streamlit Cloud, click "Reboot app" or wait for automatic redeployment

## Repository Structure

The deployed repository includes:

- `app.py` - Main Streamlit application
- `streamlit_landing.py` - Core tool implementations
- `pages/` - Individual tool pages
- `.streamlit/config.toml` - Streamlit configuration
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python runtime version
- `comprehensive_test.py` - Automated testing script
- Documentation files (README.md, etc.)

## Support

For deployment issues:
1. Check the Streamlit Cloud documentation
2. Review error logs in the Streamlit Cloud dashboard
3. Verify all required files are in the repository
4. Ensure `requirements.txt` lists all dependencies

## Next Steps

After successful deployment:
1. Share the application URL with users
2. Monitor usage and feedback
3. Regularly update and maintain the application
4. Add new tools as needed