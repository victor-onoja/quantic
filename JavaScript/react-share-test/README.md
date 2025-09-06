# 🚀 React Share Testing Ground

A comprehensive testing environment for the `react-share` library, allowing you to experiment with various social media sharing buttons and configurations.

## 🎯 Purpose

This project serves as a testing playground to:

- Test different social media sharing buttons
- Experiment with various URLs and content
- See how different platforms handle sharing
- Learn about react-share configuration options

## 🚀 Getting Started

1. **Clone and Install**

   ```bash
   cd react-share-test
   npm install
   ```

2. **Start Development Server**

   ```bash
   npm run dev
   ```

3. **Open Browser**
   Navigate to `http://localhost:5173` (or the URL shown in terminal)

## 📱 Features

### Configuration Section

- **Dynamic URL Testing**: Change the URL to share in real-time
- **Custom Titles & Descriptions**: Test how different content appears
- **Quick Test URLs**: Pre-configured URLs for common testing scenarios

### Share Button Types

1. **Text-Based Buttons**: Simple buttons with platform names
2. **Icon Buttons**: Round social media icons (48px)
3. **Custom Styled Icons**: Square icons with custom styling (64px)

### Supported Platforms

- 📘 **Facebook**: With quote and hashtag support
- 🐦 **Twitter**: With title and hashtags
- 💼 **LinkedIn**: With title and summary
- 💬 **WhatsApp**: With custom separator
- ✈️ **Telegram**: Simple URL and title sharing
- 🔴 **Reddit**: With title for post
- 📧 **Email**: With subject and body

## 🧪 Testing Tips

### URL Testing

- Try different types of URLs (websites, GitHub repos, documentation)
- Test with URLs that have rich metadata vs. simple pages
- Experiment with local URLs (though they won't work in actual sharing)

### Content Testing

- Test with different title lengths
- Try special characters and emojis
- Test multilingual content

### Platform-Specific Notes

- **WhatsApp & Telegram**: Work best on mobile devices
- **Email**: Opens your default email client
- **Facebook**: May require authentication for some features
- **LinkedIn**: Best for professional content sharing

## 🔧 Technical Details

### Dependencies

- **React**: UI framework
- **Vite**: Build tool and dev server
- **react-share**: Social sharing library

### Key Components Used

```javascript
import {
  FacebookShareButton,
  TwitterShareButton,
  LinkedinShareButton,
  WhatsappShareButton,
  TelegramShareButton,
  RedditShareButton,
  EmailShareButton,
  FacebookIcon,
  TwitterIcon,
  LinkedinIcon,
  WhatsappIcon,
  TelegramIcon,
  RedditIcon,
  EmailIcon,
} from "react-share";
```

### Props Available

- `url`: The URL to share (required)
- `title`: Title for the shared content
- `quote`: Quote for Facebook sharing
- `hashtag`: Hashtag for Facebook
- `hashtags`: Array of hashtags for Twitter
- `summary`: Description for LinkedIn
- `subject`: Subject for email
- `body`: Body content for email
- `separator`: Custom separator for WhatsApp

## 🎨 Customisation

### Icon Styling

```javascript
// Round icons
<FacebookIcon size={48} round />

// Square icons with border radius
<FacebookIcon size={64} round={false} borderRadius={12} />
```

### Button Styling

The CSS includes platform-specific colours and hover effects. Customise in `App.css`:

- `.share-buttons button`: Text button styling
- `.share-icons button`: Icon button styling
- Platform-specific colours using nth-child selectors

## 🌐 Real-World Usage

After testing, you can implement react-share in your projects:

```javascript
import { FacebookShareButton, FacebookIcon } from "react-share";

function ShareComponent({ url, title }) {
  return (
    <FacebookShareButton url={url} quote={title}>
      <FacebookIcon size={32} round />
    </FacebookShareButton>
  );
}
```

## 📚 Resources

- [react-share Documentation](https://github.com/nygardk/react-share)
- [Social Media Sharing Best Practices](https://developers.facebook.com/docs/sharing/web/)
- [Open Graph Protocol](https://ogp.me/)

## 🐛 Troubleshooting

### Common Issues

1. **Buttons not working**: Check browser console for errors
2. **WhatsApp not opening**: Ensure you're on a mobile device or have WhatsApp Web
3. **Email not opening**: Check your default email client settings
4. **Share dialog not appearing**: Some platforms require user authentication

### Development Issues

- **Module not found**: Run `npm install` to ensure all dependencies are installed
- **Port already in use**: Vite will automatically find an available port
- **Hot reload not working**: Check if files are being saved properly

Happy testing! 🎉
