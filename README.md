# HarvestShare 🌱

A modern web platform that connects food donors with charities and individuals facing hunger, ensuring surplus food is shared with those in need. This came to light as a final project for one of my courses. The project is a frontend which delivers the main idea of what we came up with.

## 🌟 About

HarvestShare is a community-driven platform designed to reduce food waste and combat hunger by creating a bridge between food donors and those in need.

## ✨ Features

- **Responsive Design**: Mobile-first approach with Bootstrap framework
- **User Authentication**: Sign up and sign in functionality
- **Food Donation System**: Easy-to-use interface for food donors
- **Food Distribution**: Platform for those seeking food assistance
- **Contact System**: Built-in contact form with backend processing
- **Modern UI/UX**: Clean, professional design with smooth animations
- **Cross-browser Compatibility**: Works across all modern browsers

## 📄 Pages

### 1. **Home Page** (`index.html`)
- Hero section with compelling messaging
- Image slideshow showcasing the platform's mission
- Call-to-action buttons for donation and food requests
- Information about how the platform works

### 2. **Sign Up Page** (`sign-up.html`)
- User registration form
- Social login options (Google, Facebook)
- Password validation and confirmation
- Link to sign in for existing users

### 3. **Sign In Page** (`sign-in.html`)
- User authentication form
- Social login integration
- Password recovery options
- Link to sign up for new users

### 4. **Contact Page** (`contact.html`)
- Contact form with backend processing
- User-friendly form validation
- Professional contact information display

## 🛠️ Technologies Used

### Frontend
- **HTML5**: Semantic markup and structure
- **CSS3**: Custom styling and animations
- **Bootstrap 5**: Responsive framework and components
- **JavaScript**: Interactive functionality
- **jQuery**: DOM manipulation and AJAX requests

### Libraries & Frameworks
- **Bootstrap Icons**: Icon library
- **Slick Carousel**: Image slideshow functionality
- **Headroom.js**: Smart header behavior
- **Google Fonts**: Typography (Inter font family)

### Backend
- **Python**: Contact form processing (`contact1.py`)

## 📁 File Structure

```
website/
├── index.html              # Main homepage
├── sign-up.html            # User registration page
├── sign-in.html            # User authentication page
├── contact.html            # Contact form page
├── contact1.py             # Backend contact form processor
├── README.md               # Project documentation
│
├── css/                    # Stylesheets
│   ├── bootstrap.min.css   # Bootstrap framework
│   ├── bootstrap-icons.css # Bootstrap icons
│   ├── slick.css          # Slick carousel styles
│   └── tooplate-little-fashion.css # Custom theme
│
├── js/                     # JavaScript files
│   ├── bootstrap.bundle.min.js # Bootstrap JS
│   ├── custom.js          # Custom functionality
│   ├── Headroom.js        # Header behavior
│   ├── jQuery.headroom.js # jQuery Headroom plugin
│   ├── jquery.min.js      # jQuery library
│   └── slick.min.js       # Slick carousel
│
├── fonts/                  # Font files
│   ├── bootstrap-icons.woff
│   └── bootstrap-icons.woff2
│
└── images/                 # Image assets
    ├── header/            # Header images
    ├── people/            # Portrait images
    ├── product/           # Product showcase images
    ├── slideshow/         # Homepage slideshow images
    └── [other images]     # Various website images
```

## 🚀 Setup Instructions

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3.x (for contact form functionality)
- Web server (optional, for production deployment)

### Local Development Setup

1. **Clone or Download the Project**
   ```bash
   # If using git
   git clone [repository-url]
   cd website
   
   # Or simply download and extract the files
   ```

2. **Open in Browser**
   - Navigate to the project directory
   - Open `index.html` in your web browser
   - Or use a local server for better development experience

3. **Using a Local Server (Recommended)**
   ```bash
   # Using Python's built-in server
   python -m http.server 8000
   
   # Using Node.js (if you have it installed)
   npx serve .
   
   # Using PHP (if you have it installed)
   php -S localhost:8000
   ```

4. **Access the Website**
   - Open your browser and go to `http://localhost:8000`
   - The website should now be running locally

### Backend Setup (Contact Form)

1. **Python Environment**
   ```bash
   # Ensure Python is installed
   python --version
   
   # Install required packages (if any)
   pip install [required-packages]
   ```

2. **Configure Contact Form**
   - Edit `contact1.py` to configure email settings
   - Update form processing logic as needed



## 📄 License

This project is based on the "Little Fashion" template from Tooplate:
- **Template**: Tooplate 2127 Little Fashion
- **Source**: https://www.tooplate.com/view/2127-little-fashion

Please respect the original template's license and terms of use.

