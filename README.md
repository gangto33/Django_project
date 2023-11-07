# Django_project

## 파일트리

___
```
C:.
├─accounts
│  ├─migrations
│  │  └─__pycache__
│  └─__pycache__
├─blog
│  ├─migrations
│  │  └─__pycache__
│  └─__pycache__
├─main
│  ├─migrations
│  │  └─__pycache__
│  └─__pycache__
├─media
│  └─blog
│      ├─files
│      │  └─2023
│      │      └─11
│      │          └─06
│      └─images
│          └─2023
│              └─11
│                  ├─01
│                  ├─05
│                  ├─06
│                  └─07
├─projectblog
│  └─__pycache__
├─static
│  ├─bootstrap
│  │  ├─.github
│  │  │  ├─codeql
│  │  │  ├─ISSUE_TEMPLATE
│  │  │  └─workflows
│  │  ├─build
│  │  ├─dist
│  │  │  ├─css
│  │  │  └─js
│  │  ├─js
│  │  │  ├─dist
│  │  │  │  ├─dom
│  │  │  │  └─util
│  │  │  ├─src
│  │  │  │  ├─dom
│  │  │  │  └─util
│  │  │  └─tests
│  │  │      ├─helpers
│  │  │      ├─integration
│  │  │      ├─unit
│  │  │      │  ├─dom
│  │  │      │  └─util
│  │  │      └─visual
│  │  ├─nuget
│  │  ├─scss
│  │  │  ├─forms
│  │  │  ├─helpers
│  │  │  ├─mixins
│  │  │  ├─tests
│  │  │  │  ├─mixins
│  │  │  │  ├─sass-true
│  │  │  │  └─utilities
│  │  │  ├─utilities
│  │  │  └─vendor
│  │  └─site
│  │      ├─assets
│  │      │  ├─js
│  │      │  │  └─vendor
│  │      │  └─scss
│  │      ├─content
│  │      │  └─docs
│  │      │      └─5.3
│  │      │          ├─about
│  │      │          ├─components
│  │      │          ├─content
│  │      │          ├─customize
│  │      │          ├─examples
│  │      │          │  ├─album
│  │      │          │  ├─album-rtl
│  │      │          │  ├─badges
│  │      │          │  ├─blog
│  │      │          │  ├─blog-rtl
│  │      │          │  ├─breadcrumbs
│  │      │          │  ├─buttons
│  │      │          │  ├─carousel
│  │      │          │  ├─carousel-rtl
│  │      │          │  ├─cheatsheet
│  │      │          │  ├─cheatsheet-rtl
│  │      │          │  ├─checkout
│  │      │          │  ├─checkout-rtl
│  │      │          │  ├─cover
│  │      │          │  ├─dashboard
│  │      │          │  ├─dashboard-rtl
│  │      │          │  ├─dropdowns
│  │      │          │  ├─features
│  │      │          │  ├─footers
│  │      │          │  ├─grid
│  │      │          │  ├─headers
│  │      │          │  ├─heroes
│  │      │          │  ├─jumbotron
│  │      │          │  ├─jumbotrons
│  │      │          │  ├─list-groups
│  │      │          │  ├─masonry
│  │      │          │  ├─modals
│  │      │          │  ├─navbar-bottom
│  │      │          │  ├─navbar-fixed
│  │      │          │  ├─navbar-static
│  │      │          │  ├─navbars
│  │      │          │  ├─navbars-offcanvas
│  │      │          │  ├─offcanvas-navbar
│  │      │          │  ├─pricing
│  │      │          │  ├─product
│  │      │          │  ├─sidebars
│  │      │          │  ├─sign-in
│  │      │          │  ├─starter-template
│  │      │          │  ├─sticky-footer
│  │      │          │  └─sticky-footer-navbar
│  │      │          ├─extend
│  │      │          ├─forms
│  │      │          ├─getting-started
│  │      │          ├─helpers
│  │      │          ├─layout
│  │      │          └─utilities
│  │      ├─data
│  │      ├─layouts
│  │      │  ├─partials
│  │      │  │  ├─callouts
│  │      │  │  ├─home
│  │      │  │  └─icons
│  │      │  ├─shortcodes
│  │      │  └─_default
│  │      │      └─_markup
│  │      └─static
│  │          └─docs
│  │              └─5.3
│  │                  └─assets
│  │                      ├─brand
│  │                      ├─img
│  │                      │  ├─examples
│  │                      │  ├─favicons
│  │                      │  └─guides
│  │                      └─js
│  └─bootstrap-5.3.2-examples
│      ├─album
│      ├─album-rtl
│      ├─assets
│      │  ├─brand
│      │  ├─dist
│      │  │  ├─css
│      │  │  └─js
│      │  └─js
│      ├─badges
│      ├─blog
│      ├─blog-rtl
│      ├─breadcrumbs
│      ├─buttons
│      ├─carousel
│      ├─carousel-rtl
│      ├─cheatsheet
│      ├─cheatsheet-rtl
│      ├─checkout
│      ├─checkout-rtl
│      ├─cover
│      ├─dashboard
│      ├─dashboard-rtl
│      ├─dropdowns
│      ├─features
│      ├─footers
│      ├─grid
│      ├─headers
│      ├─heroes
│      ├─jumbotron
│      ├─jumbotrons
│      ├─list-groups
│      ├─masonry
│      ├─modals
│      ├─navbar-bottom
│      ├─navbar-fixed
│      ├─navbar-static
│      ├─navbars
│      ├─navbars-offcanvas
│      ├─offcanvas
│      ├─offcanvas-navbar
│      ├─pricing
│      ├─product
│      ├─sidebars
│      ├─sign-in
│      ├─starter-template
│      ├─sticky-footer
│      └─sticky-footer-navbar
└─templates
    ├─accounts
    ├─blog
    └─main
```
