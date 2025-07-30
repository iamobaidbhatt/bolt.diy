# 🌟 Hotstar Cookie Validator

A comprehensive tool to validate Hotstar cookies from files or folders on your computer. This application helps you identify valid Hotstar cookies and filter out expired or invalid ones with proper validation logic.

## 🚀 Features

- **File & Folder Support**: Select individual cookie files or entire folders
- **Comprehensive Validation**: Validates cookie format, expiry, domains, and Hotstar-specific requirements
- **Beautiful GUI**: Modern dark theme with intuitive interface
- **Real-time Progress**: Progress bar and status updates during validation
- **Detailed Results**: Separate tabs for valid and invalid cookies with detailed information
- **Export Functionality**: Export valid cookies to a new file
- **JWT Validation**: Special validation for Hotstar JWT tokens (userUP, sessionUserUP)
- **CloudFront Support**: Validates CloudFront cookies for video streaming

## 📋 Supported Cookie Format

The tool supports Netscape cookie format (tab-separated values):
```
domain    domain_flag    path    secure    expires    name    value
```

Example from your provided format:
```
www.hotstar.com	FALSE	/	FALSE	1753802789	deviceId	bfbdeb5a-0edd-4e57-8693-1c3564f18925
```

## 🔍 Validation Logic

### Hotstar Cookie Detection
- **Domains**: `hotstar.com`, `.hotstar.com`, `www.hotstar.com`, CloudFront CDN domains
- **Cookie Names**: `deviceId`, `userHID`, `userPID`, `userUP`, `sessionUserUP`, CloudFront cookies, analytics cookies

### Validation Checks
1. **Domain Validation**: Ensures cookie belongs to Hotstar domains
2. **Expiry Check**: Validates if cookies are not expired
3. **Essential Cookies**: Checks for required Hotstar authentication cookies
4. **JWT Format**: Validates JWT token structure for user authentication
5. **Security Flags**: Ensures CloudFront cookies have proper security settings
6. **Value Validation**: Checks for empty or malformed cookie values

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.6 or higher
- No additional dependencies required (uses Python standard library)

### Running the Application

1. **Download the script**:
   ```bash
   python hotstar_cookie_validator.py
   ```

2. **Using the GUI**:
   - Click "📁 Select Cookie File" to choose a single cookie file
   - Click "📂 Select Folder" to scan an entire folder for cookie files
   - Click "✅ Validate Cookies" to start the validation process
   - View results in the "Valid Cookies" and "Invalid Cookies" tabs
   - Click "💾 Export Valid Cookies" to save valid cookies to a new file

### Command Line Alternative
You can also run the script directly:
```bash
python3 hotstar_cookie_validator.py
```

## 📁 File Support

The tool automatically detects and processes:
- `.txt` files
- `.cookies` files
- `.dat` files
- Any text file containing Netscape-format cookies

## 🎯 Cookie Categories Validated

### Essential Hotstar Cookies
- `deviceId`: Device identification
- `userHID`: User hash ID
- `userPID`: User profile ID
- `userUP`: User profile JWT token
- `sessionUserUP`: Session user JWT token

### CloudFront Cookies (Video Streaming)
- `CloudFront-Key-Pair-Id`: CDN key pair identification
- `CloudFront-Policy`: Access policy for video content
- `CloudFront-Signature`: Security signature for content access

### Analytics & Tracking
- `_ga`, `_gid`: Google Analytics cookies
- `_fbp`: Facebook pixel tracking
- `loc`: Location information
- `geo`: Geographical data

### Preferences
- `SELECTED__LANGUAGE`: User language preference
- Various other tracking and preference cookies

## 🔧 Validation Results

### Valid Cookies Display
- Cookie name and domain
- Expiration date (if applicable)
- Source file information
- Raw cookie line for easy copying

### Invalid Cookies Display
- Cookie details
- Specific validation issues
- Reasons for rejection (expired, invalid format, etc.)

### Statistics
- Total cookies processed
- Count of valid cookies
- Count of invalid cookies

## 🚨 Common Validation Issues

1. **Expired Cookies**: Cookies past their expiration date
2. **Invalid Domain**: Cookies not belonging to Hotstar domains
3. **Empty Values**: Essential cookies with missing values
4. **Malformed JWT**: Invalid JWT token structure
5. **Security Issues**: CloudFront cookies missing security flags

## 💾 Export Features

- Export only valid cookies to a new file
- Includes metadata (export date, count)
- Maintains original Netscape format
- Easy to import into browsers or other tools

## 🎨 Interface Features

- **Dark Theme**: Easy on the eyes for extended use
- **Progress Tracking**: Real-time progress during validation
- **Tabbed Results**: Organized display of valid/invalid cookies
- **Status Updates**: Continuous feedback on current operations
- **File Information**: Shows source file for each cookie

## 🔒 Privacy & Security

- **Local Processing**: All validation happens locally on your computer
- **No Network Calls**: Tool doesn't send data anywhere
- **File Safety**: Only reads files, doesn't modify original files
- **Export Control**: You choose where to save results

## 🐛 Troubleshooting

### Common Issues
1. **No GUI appears**: Ensure Python has tkinter support
2. **File reading errors**: Check file permissions and encoding
3. **Empty results**: Verify cookie file format matches Netscape standard

### File Format Requirements
- Tab-separated values (not spaces)
- Minimum 6 columns per line
- Proper Unix timestamp for expiry field
- No special characters in essential fields

## 📝 Example Usage Workflow

1. **Collect Cookies**: Export cookies from browser or obtain cookie files
2. **Select Input**: Choose individual files or entire folders
3. **Validate**: Run validation to identify working cookies
4. **Review Results**: Check valid/invalid tabs for detailed information
5. **Export**: Save valid cookies for use in other applications

## 🔄 Future Enhancements

- Browser integration for direct cookie import
- Bulk cookie testing with Hotstar API
- Cookie refresh/renewal suggestions
- Advanced filtering and sorting options
- Backup and restore functionality

## ⚠️ Disclaimer

This tool is for educational and personal use only. Ensure you have proper authorization to use any cookies you validate. Respect Hotstar's terms of service and applicable laws regarding cookie usage.

## 🤝 Contributing

Feel free to submit issues, feature requests, or improvements to enhance this tool's functionality.

---

**Note**: This tool validates cookie format and basic properties but cannot guarantee that valid cookies will work with Hotstar services, as that depends on various factors including account status, subscription validity, and Hotstar's current authentication requirements.
