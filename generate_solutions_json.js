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
            practiceCount: 0,
            filePath: filePath // Add file path for debugging
        };
    } catch (error) {
        console.error(`Error processing file ${filePath}:`, error.message);
        return null;
    }
}

// Function to remove duplicates based on title, keeping the best version
function removeDuplicates(snippets) {
    const titleMap = new Map();
    
    snippets.forEach(snippet => {
        const title = snippet.title;
        
        if (!titleMap.has(title)) {
            titleMap.set(title, snippet);
        } else {
            // Keep the version with more code (likely more complete)
            const existing = titleMap.get(title);
            if (snippet.code.length > existing.code.length) {
                console.log(`Replacing duplicate: ${title} (${existing.code.length} chars -> ${snippet.code.length} chars)`);
                titleMap.set(title, snippet);
            } else {
                console.log(`Skipping duplicate: ${title} (keeping ${existing.code.length} chars over ${snippet.code.length} chars)`);
            }
        }
    });
    
    // Convert back to array and remove filePath
    return Array.from(titleMap.values()).map(snippet => {
        const { filePath, ...cleanSnippet } = snippet;
        return cleanSnippet;
    });
}

// Function to create chunks and save separate files
function createChunkedFiles(snippets, chunkSize = 500) {
    const chunks = [];
    for (let i = 0; i < snippets.length; i += chunkSize) {
        chunks.push(snippets.slice(i, i + chunkSize));
    }
    
    const outputFiles = [];
    
    chunks.forEach((chunk, index) => {
        const startIndex = index * chunkSize + 1;
        const endIndex = Math.min(startIndex + chunkSize - 1, snippets.length);
        
        const fileName = `leetCode - ${startIndex} to ${endIndex}.json`;
        
        const result = {
            snippets: chunk
        };
        
        fs.writeFileSync(fileName, JSON.stringify(result, null, 2));
        outputFiles.push(fileName);
        
        console.log(`Created: ${fileName} (${chunk.length} snippets)`);
    });
    
    return outputFiles;
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
    const allSnippets = [];
    let processedCount = 0;
    
    for (const filePath of pythonFiles) {
        const snippet = processPythonFile(filePath);
        if (snippet) {
            allSnippets.push(snippet);
            processedCount++;
        }
        
        // Log progress every 100 files
        if (processedCount % 100 === 0) {
            console.log(`Processed ${processedCount} files...`);
        }
    }
    
    console.log(`\nTotal snippets before deduplication: ${allSnippets.length}`);
    
    // Remove duplicates based on title
    console.log('Removing duplicates...');
    const uniqueSnippets = removeDuplicates(allSnippets);
    
    console.log(`Total snippets after deduplication: ${uniqueSnippets.length}`);
    console.log(`Removed ${allSnippets.length - uniqueSnippets.length} duplicates`);
    
    // Sort snippets by title (problem number)
    uniqueSnippets.sort((a, b) => {
        const aNum = parseInt(a.title.match(/^\d+/)?.[0] || '0');
        const bNum = parseInt(b.title.match(/^\d+/)?.[0] || '0');
        return aNum - bNum;
    });
    
    console.log(`\nProcessing completed! Final unique snippets: ${uniqueSnippets.length}`);
    console.log('Creating chunked files...');
    
    // Create chunked files (500 items each)
    const outputFiles = createChunkedFiles(uniqueSnippets, 500);
    
    // Also create the original single file
    const singleFile = 'leetcode_solutions.json';
    const result = {
        snippets: uniqueSnippets
    };
    fs.writeFileSync(singleFile, JSON.stringify(result, null, 2));
    
    console.log(`\nAll files created successfully!`);
    console.log(`Total files created: ${outputFiles.length + 1}`);
    console.log(`Chunked files: ${outputFiles.length}`);
    console.log(`Single file: ${singleFile}`);
    
    // Show file sizes
    console.log('\nFile sizes:');
    outputFiles.forEach(file => {
        const size = (fs.statSync(file).size / 1024 / 1024).toFixed(2);
        console.log(`${file}: ${size} MB`);
    });
    
    const singleFileSize = (fs.statSync(singleFile).size / 1024 / 1024).toFixed(2);
    console.log(`${singleFile}: ${singleFileSize} MB`);
}

// Run the script
if (require.main === module) {
    generateSolutionsJSON();
}

module.exports = { generateSolutionsJSON }; 