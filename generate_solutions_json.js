const fs = require('fs');
const path = require('path');
const { v4: uuidv4 } = require('uuid');

// Function to recursively find all Python files
function findPythonFiles(dir) {
    const files = [];
    
    function traverse(currentDir) {
        const items = fs.readdirSync(currentDir);
        
        for (const item of items) {
            const fullPath = path.join(currentDir, item);
            const stat = fs.statSync(fullPath);
            
            if (stat.isDirectory()) {
                traverse(fullPath);
            } else if (item.endsWith('.py')) {
                files.push(fullPath);
            }
        }
    }
    
    traverse(dir);
    return files;
}

// Function to extract problem title from filename or directory
function extractTitle(filePath) {
    const fileName = path.basename(filePath, '.py');
    const dirName = path.basename(path.dirname(filePath));
    
    // If the file is in a numbered directory, use the directory name
    if (dirName.match(/^\d+\./)) {
        return dirName;
    }
    
    // Otherwise use the filename
    return fileName;
}

// Function to clean and format the title
function formatTitle(title) {
    // Remove file extensions and clean up
    title = title.replace(/\.py$/, '');
    
    // If title starts with a number and dot, keep it as is
    if (title.match(/^\d+\./)) {
        return title;
    }
    
    // Otherwise, try to extract from directory structure
    return title;
}

// Function to read and process a Python file
function processPythonFile(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf8');
        
        // Skip empty files or files without class Solution
        if (!content.trim() || !content.includes('class Solution')) {
            return null;
        }
        
        const title = formatTitle(extractTitle(filePath));
        
        return {
            id: uuidv4(),
            code: content.trim(),
            title: title,
            language: "python",
            notes: "",
            practiceCount: 0
        };
    } catch (error) {
        console.error(`Error processing file ${filePath}:`, error.message);
        return null;
    }
}

// Main function
function generateSolutionsJSON() {
    console.log('Starting to process Python solution files...');
    
    const solutionsDir = './solutions';
    
    if (!fs.existsSync(solutionsDir)) {
        console.error('Solutions directory not found!');
        return;
    }
    
    // Find all Python files
    console.log('Finding Python files...');
    const pythonFiles = findPythonFiles(solutionsDir);
    console.log(`Found ${pythonFiles.length} Python files`);
    
    // Process each file
    const snippets = [];
    let processedCount = 0;
    
    for (const filePath of pythonFiles) {
        const snippet = processPythonFile(filePath);
        if (snippet) {
            snippets.push(snippet);
            processedCount++;
        }
        
        // Log progress every 100 files
        if (processedCount % 100 === 0) {
            console.log(`Processed ${processedCount} files...`);
        }
    }
    
    // Sort snippets by title (problem number)
    snippets.sort((a, b) => {
        const aNum = parseInt(a.title.match(/^\d+/)?.[0] || '0');
        const bNum = parseInt(b.title.match(/^\d+/)?.[0] || '0');
        return aNum - bNum;
    });
    
    // Create the final JSON structure
    const result = {
        snippets: snippets
    };
    
    // Write to file
    const outputFile = 'leetcode_solutions.json';
    fs.writeFileSync(outputFile, JSON.stringify(result, null, 2));
    
    console.log(`\nCompleted! Generated ${snippets.length} snippets`);
    console.log(`Output saved to: ${outputFile}`);
    console.log(`File size: ${(fs.statSync(outputFile).size / 1024 / 1024).toFixed(2)} MB`);
}

// Run the script
if (require.main === module) {
    generateSolutionsJSON();
}

module.exports = { generateSolutionsJSON }; 