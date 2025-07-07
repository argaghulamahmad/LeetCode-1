const fs = require('fs');
const path = require('path');

const SOLUTIONS_DIR = path.join(__dirname);

function isTargetFile(file) {
  return file.endsWith('.py') || file.endsWith('.sql');
}

function main() {
  const entries = fs.readdirSync(SOLUTIONS_DIR, { withFileTypes: true });
  for (const entry of entries) {
    if (entry.isDirectory()) {
      const folderName = entry.name;
      const folderPath = path.join(SOLUTIONS_DIR, folderName);
      const files = fs.readdirSync(folderPath);
      const targetFiles = files.filter(isTargetFile);
      
      for (let i = 0; i < targetFiles.length; i++) {
        const file = targetFiles[i];
        const ext = path.extname(file);
        let newFileName = folderName + ext;
        
        // If there are multiple files, add suffix starting from 2
        if (targetFiles.length > 1) {
          const suffix = i === 0 ? '' : `_${i + 1}`;
          newFileName = folderName + suffix + ext;
        }
        
        const destPath = path.join(SOLUTIONS_DIR, newFileName);
        const srcPath = path.join(folderPath, file);
        
        if (fs.existsSync(destPath)) {
          console.warn(`SKIP: ${destPath} already exists.`);
          continue;
        }
        
        fs.renameSync(srcPath, destPath);
        console.log(`Moved: ${srcPath} -> ${destPath}`);
      }
    }
  }
}

main(); 