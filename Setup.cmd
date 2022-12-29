echo "# BranchTest" >> README.md
git init
git add README.md
git commit -m "setup commit"
git branch -M main
git remote add origin https://github.com/nikhilleo07/Python.git
git push -u origin main