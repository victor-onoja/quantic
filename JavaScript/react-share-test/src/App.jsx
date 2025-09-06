import { useState } from "react";
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
import "./App.css";

function App() {
  // State for dynamic URL testing
  const [shareUrl, setShareUrl] = useState("https://example.com/your-page");
  const [shareTitle, setShareTitle] = useState(
    "Check out this amazing content!"
  );
  const [shareDescription, setShareDescription] = useState(
    "This is a test of react-share functionality with multiple social media platforms."
  );

  // Predefined test URLs
  const testUrls = [
    "https://example.com/your-page",
    "https://github.com/nygardk/react-share",
    "https://reactjs.org",
    "https://vitejs.dev",
  ];

  return (
    <div className="app">
      <header className="app-header">
        <h1>🚀 React Share Testing Ground</h1>
        <p>Test various social media sharing buttons and configurations</p>
      </header>

      <main className="main-content">
        {/* URL Configuration Section */}
        <section className="config-section">
          <h2>📝 Configure Share Content</h2>
          <div className="form-group">
            <label htmlFor="url-input">Share URL:</label>
            <input
              id="url-input"
              type="url"
              value={shareUrl}
              onChange={(e) => setShareUrl(e.target.value)}
              placeholder="Enter URL to share"
            />
          </div>
          <div className="form-group">
            <label htmlFor="title-input">Title:</label>
            <input
              id="title-input"
              type="text"
              value={shareTitle}
              onChange={(e) => setShareTitle(e.target.value)}
              placeholder="Share title"
            />
          </div>
          <div className="form-group">
            <label htmlFor="description-input">Description:</label>
            <textarea
              id="description-input"
              value={shareDescription}
              onChange={(e) => setShareDescription(e.target.value)}
              placeholder="Share description"
              rows="3"
            />
          </div>

          <div className="quick-urls">
            <h3>Quick Test URLs:</h3>
            <div className="url-buttons">
              {testUrls.map((url, index) => (
                <button
                  key={index}
                  onClick={() => setShareUrl(url)}
                  className="url-button"
                >
                  {url.replace("https://", "")}
                </button>
              ))}
            </div>
          </div>
        </section>

        {/* Share Buttons Section */}
        <section className="share-section">
          <h2>📱 Social Media Share Buttons</h2>

          {/* Basic Share Buttons */}
          <div className="share-group">
            <h3>Basic Share Buttons (Text Only)</h3>
            <div className="share-buttons">
              <FacebookShareButton
                url={shareUrl}
                quote={shareTitle}
                hashtag="#reactshare"
              >
                Share on Facebook
              </FacebookShareButton>

              <TwitterShareButton
                url={shareUrl}
                title={shareTitle}
                hashtags={["reactshare", "testing"]}
              >
                Share on Twitter
              </TwitterShareButton>

              <LinkedinShareButton
                url={shareUrl}
                title={shareTitle}
                summary={shareDescription}
              >
                Share on LinkedIn
              </LinkedinShareButton>

              <WhatsappShareButton
                url={shareUrl}
                title={shareTitle}
                separator=" - "
              >
                Share on WhatsApp
              </WhatsappShareButton>

              <TelegramShareButton url={shareUrl} title={shareTitle}>
                Share on Telegram
              </TelegramShareButton>

              <RedditShareButton url={shareUrl} title={shareTitle}>
                Share on Reddit
              </RedditShareButton>

              <EmailShareButton
                url={shareUrl}
                subject={shareTitle}
                body={shareDescription}
              >
                Share via Email
              </EmailShareButton>
            </div>
          </div>

          {/* Icon Share Buttons */}
          <div className="share-group">
            <h3>Icon Share Buttons</h3>
            <div className="share-icons">
              <FacebookShareButton
                url={shareUrl}
                quote={shareTitle}
                hashtag="#reactshare"
              >
                <FacebookIcon size={48} round />
              </FacebookShareButton>

              <TwitterShareButton
                url={shareUrl}
                title={shareTitle}
                hashtags={["reactshare", "testing"]}
              >
                <TwitterIcon size={48} round />
              </TwitterShareButton>

              <LinkedinShareButton
                url={shareUrl}
                title={shareTitle}
                summary={shareDescription}
              >
                <LinkedinIcon size={48} round />
              </LinkedinShareButton>

              <WhatsappShareButton
                url={shareUrl}
                title={shareTitle}
                separator=" - "
              >
                <WhatsappIcon size={48} round />
              </WhatsappShareButton>

              <TelegramShareButton url={shareUrl} title={shareTitle}>
                <TelegramIcon size={48} round />
              </TelegramShareButton>

              <RedditShareButton url={shareUrl} title={shareTitle}>
                <RedditIcon size={48} round />
              </RedditShareButton>

              <EmailShareButton
                url={shareUrl}
                subject={shareTitle}
                body={shareDescription}
              >
                <EmailIcon size={48} round />
              </EmailShareButton>
            </div>
          </div>

          {/* Custom Styled Buttons */}
          <div className="share-group">
            <h3>Custom Styled Icons</h3>
            <div className="custom-icons">
              <FacebookShareButton
                url={shareUrl}
                quote={shareTitle}
                hashtag="#reactshare"
              >
                <FacebookIcon size={64} round={false} borderRadius={12} />
              </FacebookShareButton>

              <TwitterShareButton
                url={shareUrl}
                title={shareTitle}
                hashtags={["reactshare", "testing"]}
              >
                <TwitterIcon size={64} round={false} borderRadius={12} />
              </TwitterShareButton>

              <LinkedinShareButton
                url={shareUrl}
                title={shareTitle}
                summary={shareDescription}
              >
                <LinkedinIcon size={64} round={false} borderRadius={12} />
              </LinkedinShareButton>
            </div>
          </div>
        </section>

        {/* Testing Information */}
        <section className="info-section">
          <h2>ℹ️ Testing Information</h2>
          <div className="info-content">
            <p>
              <strong>Current Share URL:</strong> {shareUrl}
            </p>
            <p>
              <strong>Share Title:</strong> {shareTitle}
            </p>
            <p>
              <strong>Share Description:</strong> {shareDescription}
            </p>

            <div className="tips">
              <h3>💡 Testing Tips:</h3>
              <ul>
                <li>
                  Try different URLs to see how each platform handles them
                </li>
                <li>Test with various titles and descriptions</li>
                <li>Click the buttons to see the actual sharing dialogs</li>
                <li>Note that some platforms may require authentication</li>
                <li>WhatsApp and Telegram work best on mobile devices</li>
                <li>Email button will open your default email client</li>
              </ul>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
