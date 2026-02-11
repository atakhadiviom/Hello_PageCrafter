# Hello PageCrafter Theme

A minimalist Odoo theme designed specifically for use with [PageCrafter](https://github.com/atakhadivi/PageCrafter).

Inspired by "Hello Elementor" for WordPress, this theme provides a clean, blank canvas that lets PageCrafter's page builder shine without theme conflicts or styling interference.

## Features

- **Minimal Styling**: Lightweight base that won't conflict with your designs
- **Clean Canvas**: Removes unnecessary theme constraints for full design freedom
- **PageCrafter Optimized**: Designed to work seamlessly with PageCrafter module
- **Responsive Foundation**: Mobile-first approach with proper breakpoints
- **Full-Width Ready**: Supports modern full-width layouts out of the box

## Installation

### Requirements

- Odoo 19.0 or higher
- [PageCrafter](https://github.com/atakhadivi/PageCrafter) module installed

### Install from Source

1. Clone this repository to your Odoo addons path:
   ```bash
   cd /path/to/odoo/addons
   git clone https://github.com/atakhadivi/Hello_PageCrafter.git hello_pagecrafter
   ```

2. Update the addons list in Odoo:
   - Go to **Apps** > **Update Apps List**

3. Install the theme:
   - Go to **Apps**
   - Search for "Hello PageCrafter"
   - Click **Install**

### Install via Symlink (Development)

For development, you can symlink the module:

```bash
ln -s /path/to/Hello_PageCrafter /path/to/odoo/local-addons/hello_pagecrafter
```

## Usage

1. Install both **PageCrafter** and **Hello PageCrafter Theme**
2. Go to your website
3. Edit with PageCrafter - the theme provides a clean base for your designs
4. Enjoy full creative freedom without theme constraints!

## Philosophy

Like "Hello Elementor" for WordPress, this theme follows the philosophy that:

> A page builder theme should be invisible - it should provide structure without imposing design decisions.

This theme:
- ✅ Provides structure and layout hooks
- ✅ Ensures compatibility with PageCrafter
- ✅ Removes conflicts and constraints
- ❌ Does NOT impose colors, fonts, or styling
- ❌ Does NOT limit your creative options

## File Structure

```
hello_pagecrafter/
├── __init__.py
├── __manifest__.py
├── models/
│   └── __init__.py
├── static/
│   └── src/
│       ├── scss/
│       │   └── main.scss          # Main theme styles
│       └── js/                    # (if needed)
└── views/
    ├── assets.xml                 # Asset declarations
    └── layout.xml                 # Layout templates
```

## Customization

Since this is a minimal theme, most styling will come from PageCrafter itself. However, you can customize the base styles in:

- `static/src/scss/main.scss` - Base theme styles
- `views/layout.xml` - Template modifications

## Compatibility

- **Odoo Version**: 19.0+
- **Required Modules**: `website`, `pagecrafter`
- **Browser Support**: All modern browsers

## License

LGPL-3

## Credits

- **Author**: Ata Khadivi
- **Inspired by**: [Hello Elementor](https://elementor.com/hello-theme/) for WordPress
- **Built for**: [PageCrafter](https://github.com/atakhadivi/PageCrafter)

## Support

For issues, feature requests, or contributions, please visit the [GitHub repository](https://github.com/atakhadivi/Hello_PageCrafter).

---

**Note**: This theme is designed to work with PageCrafter. For the full page building experience, make sure to install the [PageCrafter module](https://github.com/atakhadivi/PageCrafter) first.
