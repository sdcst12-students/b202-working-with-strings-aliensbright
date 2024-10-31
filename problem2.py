#!python3
import urllib.request
"""
##### Problem 2
Retrieve the contents of the sd.deltasd.bc.ca webpage.
Remove all of the HTML and display just the real contents of the page.
"""

import requests, time


x = requests.get("https://sd.deltasd.bc.ca")
time.sleep(1)
print(x.text)


"""
                <title>Home - South Delta</title>

                                <meta name="HandheldFriendly" content="True">
                <meta name="MobileOptimized" content="320">
                <meta name="viewport" content="width=device-width, initial-scale=1"/>
                                        <meta http-equiv="X-XSS-Protection" content="1; mode=block">
                        <meta http-equiv="X-Frame-Options" content="SAMEORIGIN">
                        <meta http-equiv="X-Content-Type-Options" content="nosniff">
                        <meta http-equiv="Strict-Transport-Security" content="max-age=63072000; includeSubDomains">
                        <meta http-equiv="Referrer-Policy" content="same-origin">
                        <meta http-equiv="Content-Security-Policy" content="default-src 'self' data: blob: *.public.deltasd.bc.ca *.googleapis.com *.gstatic.com *.typekit.net *.google.com *.vimeo.com deltapolice.ca unpkg.com *.vimeocdn.com yoast.com *.gravatar.com 'unsafe-inline' 'unsafe-eval';">
                                                <link rel="apple-touch-icon" href="https://sd.deltasd.bc.ca/wp-content/themes/school/library/images/apple-touch-icon.png">
                <link rel="icon" href="https://sd.deltasd.bc.ca/wp-content/themes/school/favicon.png">
                <!--[if IE]>
                        <link rel="shortcut icon" href="https://sd.deltasd.bc.ca/wp-content/themes/school/favicon.ico">
                <![endif]-->
                                <meta name="msapplication-TileColor" content="#f01d4f">
                <meta name="msapplication-TileImage" content="https://sd.deltasd.bc.ca/wp-content/themes/school/library/images/win8-tile-icon.png">
            <meta name="theme-color" content="#121212">

                <link rel="pingback" href="https://sd.deltasd.bc.ca/xmlrpc.php">

                                <meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

        <!-- This site is optimized with the Yoast SEO plugin v23.1 - https://yoast.com/wordpress/plugins/seo/ -->
        <link rel="canonical" href="https://sd.deltasd.bc.ca/" />
        <meta property="og:locale" content="en_US" />
        <meta property="og:type" content="website" />
        <meta property="og:title" content="Home - South Delta" />
        <meta property="og:description" content="... Read more &raquo;" />
        <meta property="og:url" content="https://sd.deltasd.bc.ca/" />
        <meta property="og:site_name" content="South Delta" />
        <meta property="article:modified_time" content="2023-06-15T16:23:15+00:00" />
        <meta name="twitter:card" content="summary_large_image" />
        <script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://sd.deltasd.bc.ca/","url":"https://sd.deltasd.bc.ca/","name":"Home - South Delta","isPartOf":{"@id":"https://sd.deltasd.bc.ca/#website"},"datePublished":"2017-07-28T21:42:07+00:00","dateModified":"2023-06-15T16:23:15+00:00","breadcrumb":{"@id":"https://sd.deltasd.bc.ca/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https://sd.deltasd.bc.ca/"]}]},{"@type":"BreadcrumbList","@id":"https://sd.deltasd.bc.ca/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home"}]},{"@type":"WebSite","@id":"https://sd.deltasd.bc.ca/#website","url":"https://sd.deltasd.bc.ca/","name":"South Delta","description":"Secondary School | École Secondaire","potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://sd.deltasd.bc.ca/?s={search_term_string}"},"query-input":"required name=search_term_string"}],"inLanguage":"en-US"}]}</script>      
        <!-- / Yoast SEO plugin. -->


<link rel='dns-prefetch' href='//sd.public.deltasd.bc.ca' />
<link rel='dns-prefetch' href='//fonts.googleapis.com' />
<link rel="alternate" type="application/rss+xml" title="South Delta &raquo; Feed" href="https://sd.deltasd.bc.ca/feed/" />
<link rel="alternate" type="application/rss+xml" title="South Delta &raquo; Comments Feed" href="https://sd.deltasd.bc.ca/comments/feed/" />
<link rel="alternate" type="text/calendar" title="South Delta &raquo; iCal Feed" href="https://sd.deltasd.bc.ca/events-calendar/?ical=1" />
                <!-- This site uses the Google Analytics by ExactMetrics plugin v7.28.0 - Using Analytics tracking - https://www.exactmetrics.com/ -->   
                <!-- Note: ExactMetrics is not currently configured on this site. The site owner needs to authenticate with Google Analytics in the ExactMetrics settings panel. -->
                                        <!-- No tracking code set -->
                                <!-- / Google Analytics by ExactMetrics -->
                <script type="text/javascript">
/* <![CDATA[ */
window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/15.0.3\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/15.0.3\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/sd.deltasd.bc.ca\/wp-includes\/js\/wp-emoji-release.min.js"}};
/*! This file is auto-generated */
!function(i,n){var o,s,e;function c(e){try{var t={supportTests:e,timestamp:(new Date).valueOf()};sessionStorage.setItem(o,JSON.stringify(t))}catch(e){}}function p(e,t,n){e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(t,0,0);var t=new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data),r=(e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(n,0,0),new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data));return t.every(function(e,t){return e===r[t]})}function u(e,t,n){switch(t){case"flag":return n(e,"\ud83c\udff3\ufe0f\u200d\u26a7\ufe0f","\ud83c\udff3\ufe0f\u200b\u26a7\ufe0f")?!1:!n(e,"\ud83c\uddfa\ud83c\uddf3","\ud83c\uddfa\u200b\ud83c\uddf3")&&!n(e,"\ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc65\udb40\udc6e\udb40\udc67\udb40\udc7f","\ud83c\udff4\u200b\udb40\udc67\u200b\udb40\udc62\u200b\udb40\udc65\u200b\udb40\udc6e\u200b\udb40\udc67\u200b\udb40\udc7f");case"emoji":return!n(e,"\ud83d\udc26\u200d\u2b1b","\ud83d\udc26\u200b\u2b1b")}return!1}function f(e,t,n){var r="undefined"!=typeof WorkerGlobalScope&&self instanceof WorkerGlobalScope?new OffscreenCanvas(300,150):i.createElement("canvas"),a=r.getContext("2d",{willReadFrequently:!0}),o=(a.textBaseline="top",a.font="600 32px Arial",{});return e.forEach(function(e){o[e]=t(a,e,n)}),o}function t(e){var t=i.createElement("script");t.src=e,t.defer=!0,i.head.appendChild(t)}"undefined"!=typeof Promise&&(o="wpEmojiSettingsSupports",s=["flag","emoji"],n.supports={everything:!0,everythingExceptFlag:!0},e=new Promise(function(e){i.addEventListener("DOMContentLoaded",e,{once:!0})}),new Promise(function(t){var n=function(){try{var e=JSON.parse(sessionStorage.getItem(o));if("object"==typeof e&&"number"==typeof e.timestamp&&(new Date).valueOf()<e.timestamp+604800&&"object"==typeof e.supportTests)return e.supportTests}catch(e){}return null}();if(!n){if("undefined"!=typeof Worker&&"undefined"!=typeof OffscreenCanvas&&"undefined"!=typeof URL&&URL.createObjectURL&&"undefined"!=typeof Blob)try{var e="postMessage("+f.toString()+"("+[JSON.stringify(s),u.toString(),p.toString()].join(",")+"));",r=new Blob([e],{type:"text/javascript"}),a=new Worker(URL.createObjectURL(r),{name:"wpTestEmojiSupports"});return void(a.onmessage=function(e){c(n=e.data),a.terminate(),t(n)})}catch(e){}c(n=f(s,u,p))}t(n)}).then(function(e){for(var t in e)n.supports[t]=e[t],n.supports.everything=n.supports.everything&&n.supports[t],"flag"!==t&&(n.supports.everythingExceptFlag=n.supports.everythingExceptFlag&&n.supports[t]);n.supports.everythingExceptFlag=n.supports.everythingExceptFlag&&!n.supports.flag,n.DOMReady=!1,n.readyCallback=function(){n.DOMReady=!0}}).then(function(){return e}).then(function(){var e;n.supports.everything||(n.readyCallback(),(e=n.source||{}).concatemoji?t(e.concatemoji):e.wpemoji&&e.twemoji&&(t(e.twemoji),t(e.wpemoji)))}))}((window,document),window._wpemojiSettings);
/* ]]> */
</script>
<style id='wp-emoji-styles-inline-css' type='text/css'>

        img.wp-smiley, img.emoji {
                display: inline !important;
                border: none !important;
                box-shadow: none !important;
                height: 1em !important;
                width: 1em !important;
                margin: 0 0.07em !important;
                vertical-align: -0.1em !important;
                background: none !important;
                padding: 0 !important;
        }
</style>
<link rel='stylesheet' id='wp-block-library-css' href='https://sd.deltasd.bc.ca/wp-includes/css/dist/block-library/style.min.css' type='text/css' media='all' />
<style id='classic-theme-styles-inline-css' type='text/css'>
/*! This file is auto-generated */
.wp-block-button__link{color:#fff;background-color:#32373c;border-radius:9999px;box-shadow:none;text-decoration:none;padding:calc(.667em + 2px) calc(1.333em + 2px);font-size:1.125em}.wp-block-file__button{background:#32373c;color:#fff;text-decoration:none}
</style>
<style id='global-styles-inline-css' type='text/css'>
body{--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgba(255, 255, 255, 1), 6px 6px rgba(0, 0, 0, 1);--wp--preset--shadow--crisp: 6px 6px 0px rgba(0, 0, 0, 1);}:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}body .is-layout-flex{display: flex;}body .is-layout-flex{flex-wrap: wrap;align-items: center;}body .is-layout-flex > *{margin: 0;}body .is-layout-grid{display: grid;}body .is-layout-grid > *{margin: 0;}:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
.wp-block-navigation a:where(:not(.wp-element-button)){color: inherit;}
:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}
:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}
.wp-block-pullquote{font-size: 1.5em;line-height: 1.6;}
</style>
<link rel='stylesheet' id='googleFonts-css' href='//fonts.googleapis.com/css?family=Lato%3A400%2C700%2C400italic%2C700italic' type='text/css' media='all' />
<link rel='stylesheet' id='searchwp-live-search-css' href='https://sd.deltasd.bc.ca/wp-content/plugins/searchwp-live-ajax-search/assets/styles/style.css' type='text/css' media='all' />
<style id='searchwp-live-search-inline-css' type='text/css'>
.searchwp-live-search-result .searchwp-live-search-result--title a {
  font-size: 16px;
}
.searchwp-live-search-result .searchwp-live-search-result--price {
  font-size: 14px;
}
.searchwp-live-search-result .searchwp-live-search-result--add-to-cart .button {
  font-size: 14px;
}

</style>
<link rel='stylesheet' id='tablepress-default-css' href='https://sd.deltasd.bc.ca/wp-content/plugins/tablepress/css/build/default.css' type='text/css' media='all' />
<link rel='stylesheet' id='slick-css-css' href='https://sd.deltasd.bc.ca/wp-content/themes/school/library/css/slick.css' type='text/css' media='all' />  
<link rel='stylesheet' id='print-css-css' href='https://sd.deltasd.bc.ca/wp-content/themes/school/library/css/print.css' type='text/css' media='all' />  
<link rel='stylesheet' id='bones-stylesheet-css' href='https://sd.deltasd.bc.ca/wp-content/themes/school/library/css/styles.css' type='text/css' media='all' />
<!--[if lt IE 9]>
<link rel='stylesheet' id='bones-ie-only-css' href='https://sd.deltasd.bc.ca/wp-content/themes/school/library/css/ie.css' type='text/css' media='all' /> 
<![endif]-->
<link rel='stylesheet' id='pcs-styles-css' href='https://sd.deltasd.bc.ca/wp-content/plugins/post-content-shortcodes/styles/default-styles.css' type='text/css' media='screen' />
<script type="text/javascript" src="https://sd.public.deltasd.bc.ca/wp-content/plugins/jquery-manager/assets/js/jquery-3.5.1.min.js" id="jquery-core-js"></script>
<script type="text/javascript" src="https://sd.public.deltasd.bc.ca/wp-content/plugins/jquery-manager/assets/js/jquery-migrate-1.4.1.min.js" id="jquery-migrate-js"></script>
<script type="text/javascript" src="https://sd.deltasd.bc.ca/wp-content/themes/school/library/js/libs/modernizr.custom.min.js" id="bones-modernizr-js"></script>
<link rel='shortlink' href='https://sd.deltasd.bc.ca/' />
<link rel="alternate" type="application/json+oembed" href="https://sd.deltasd.bc.ca/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fsd.deltasd.bc.ca%2F" />   
<link rel="alternate" type="text/xml+oembed" href="https://sd.deltasd.bc.ca/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fsd.deltasd.bc.ca%2F&#038;format=xml" />
<meta name="tec-api-version" content="v1"><meta name="tec-api-origin" content="https://sd.deltasd.bc.ca"><link rel="alternate" href="https://sd.deltasd.bc.ca/wp-json/tribe/events/v1/" />
<link rel="shortcut icon" type="image/x-icon" href="https://sd.deltasd.bc.ca/wp-content/themes/school/favicon.ico" />
<style>#wpadminbar #wp-admin-bar-site-name>.ab-item:before { content: none !important;}li#wp-admin-bar-site-name a { background: url( "https://sd.deltasd.bc.ca/wp-content/themes/school/favicon.ico" ) left center/20px no-repeat !important; padding-left: 21px !important; background-size: 20px !important; } li#wp-admin-bar-site-name { margin-left: 5px !important; } li#wp-admin-bar-site-name {} #wp-admin-bar-site-name div a { background: none !important; }   
</style>
                <link href="https://fonts.googleapis.com/css?family=Droid+Serif:400,700|Open+Sans:400,700|Oswald:400,700|Roboto+Slab:400,700" rel="stylesheet">
                <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

        </head>

        <body class="home page-template-default page page-id-46 yellow Open+Sans lined-paper tribe-no-js" itemscope itemtype="http://schema.org/WebPage">

                <div class="language-overlay">
                        <div class="language-content">
                                <i class="material-icons close">&#xE5C9;</i>
                                <div id="google_translate_element"></div><script type="text/javascript">
                                function googleTranslateElementInit() {
                                        new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element');
                                }
                        </script><script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
                        </div>
                </div>

                <div id="container">


                        <header class="header" role="banner" itemscope itemtype="http://schema.org/WPHeader">

                                <div id="inner-header" class="wrap cf">


                                <div class="m-hide mobile-search-links-wrapper">
                                        <div class="links-wrapper">
                                                <span class="language"><i class="material-icons" aria-hidden="true">&#xE80B;</i> Language</span>
                                                <span class="login"><a href="https://cimsweb.deltasd.bc.ca/schoolconnect/parentsignone.aspx"><i class="material-icons" aria-hidden="true">&#xE7FD;</i> Parent Connect</a></span>
                                                <span class="contact"><a href="/our-school/contact-directions/"><i class="material-icons" aria-hidden="true">&#xE0BE;</i> Contact</a></span>
                                        </div><!-- /links-wrapper -->
                                                                                        <div class="header-search" role="complementary">
                                                        <div><form role="search" method="get" id="searchform" class="searchform" action="https://sd.deltasd.bc.ca/">
    <div>
        <label for="s" class="screen-reader-text">Search for:</label>
        <input type="search" id="s" name="s" data-swplive="true" data-swpengine="default" data-swpconfig="default" value="" />

        <button type="submit" id="searchsubmit" >Search</button>
    </div>
</form></div>                                           </div><!-- #primary-sidebar -->
                                                                        </div><!-- /search-links-wrapper -->

                                        <div class="logo-wrapper">
                                                <a href="https://sd.deltasd.bc.ca" rel="nofollow">
                                                        <img src="/wp-content/uploads/sites/31/assets/SouthDeltaSecondary.jpg" />
                                                                                                        </a>
                                        </div><!-- /logo-wrapper -->
                                        <div class="name-menu-wrapper">
                                                <div class="name-search-wrapper col-1-1">
                                                        <div class="name-tagline-wrapper">
                                                                <div class="school-name"><a href="https://sd.deltasd.bc.ca"><h1>South Delta</h1></a></div>
                                                                <div class="tagline"><h3>Secondary School | École Secondaire</h3></div>                 </div><!-- /name-tagline-wrapper -->
                                                        <div class="search-links-wrapper">
                                                                <div class="links-wrapper">
                                                                        <span class="language"><i class="material-icons" aria-hidden="true">&#xE80B;</i> Language</span>
                                                                        <span class="login"><a href="https://cimsweb.deltasd.bc.ca/schoolconnect/parentsignone.aspx"><i class="material-icons" aria-hidden="true">&#xE7FD;</i> Parent Connect</a></span>
                                                                        <span class="contact"><a href="/our-school/contact-directions/"><i class="material-icons" aria-hidden="true">&#xE0BE;</i> Contact</a></span>
                                                                </div><!-- /links-wrapper -->
                                                                                                                                        <div class="header-search" role="complementary">
                                                                                <div><form role="search" method="get" id="searchform" class="searchform" action="https://sd.deltasd.bc.ca/">
    <div>
        <label for="s" class="screen-reader-text">Search for:</label>
        <input type="search" id="s" name="s" data-swplive="true" data-swpengine="default" data-swpconfig="default" value="" />

        <button type="submit" id="searchsubmit" >Search</button>
    </div>
</form></div>                                                                   </div><!-- #primary-sidebar -->
                                                                                                                        </div><!-- /search-links-wrapper -->
                                                                                                        </div>
                                                <div class="menu-wrapper col-1-1 ">
                                                        <nav role="navigation" itemscope itemtype="http://schema.org/SiteNavigationElement" class="desktop"><div class="menu"><ul><li class="page_item page-item-14 page_item_has_children"><a href="https://sd.deltasd.bc.ca/our-school/">Our School</a><ul class='children'><li class="page_item page-item-58"><a href="https://sd.deltasd.bc.ca/our-school/about-our-school/">About Our School</a></li><li class="page_item page-item-640"><a href="https://sd.deltasd.bc.ca/our-school/calendar-20242025/">Calendars</a></li><li class="page_item page-item-4553"><a href="https://sd.deltasd.bc.ca/our-school/sdss-code-of-conduct/">SDSS Code of Conduct</a></li><li class="page_item page-item-4633"><a href="https://sd.deltasd.bc.ca/our-school/2023-24-school-opening-information/">2024-25 School Opening Information</a></li><li class="page_item page-item-64"><a href="https://sd.deltasd.bc.ca/our-school/school-schedule/">School Schedule</a></li><li class="page_item page-item-68"><a href="https://sd.deltasd.bc.ca/our-school/registration/">Registration</a></li><li class="page_item page-item-70"><a href="https://sd.deltasd.bc.ca/our-school/staff-directory/">Staff Directory</a></li><li class="page_item page-item-72"><a href="https://sd.deltasd.bc.ca/our-school/contact-directions/">Contact / Directions</a></li><li class="page_item page-item-6584"><a href="https://www.deltasd.bc.ca/programs/learning-services-inclusive-learning/threat-assessment-protocol-fair-notice/#new_tab">Threat Assessment Protocol &#8211; Fair Notice</a></li></ul></li><li class="page_item page-item-16 page_item_has_children"><a href="https://sd.deltasd.bc.ca/news-events/">News &amp; Events</a><ul class='children'><li class="page_item page-item-74"><a href="/events-calendar">Events Calendar</a></li><li class="page_item page-item-76"><a href="https://sd.deltasd.bc.ca/news-events/daily-announcements/">Daily Announcements</a></li><li class="page_item page-item-78"><a href="https://sd.deltasd.bc.ca/news-events/news/">News</a></li></ul></li><li class="page_item page-item-18 page_item_has_children"><a href="https://sd.deltasd.bc.ca/programs-courses/">Programs &amp; Courses</a><ul class='children'><li class="page_item page-item-82"><a href="https://sd.deltasd.bc.ca/programs-courses/course-guide/">Course Planning</a></li><li class="page_item page-item-84"><a href="https://sd.deltasd.bc.ca/programs-courses/career-programs/">Career Programs</a></li><li class="page_item page-item-86"><a href="https://sd.deltasd.bc.ca/programs-courses/international-student-program/">International Student Program</a></li></ul></li><li class="page_item page-item-20 page_item_has_children"><a href="https://sd.deltasd.bc.ca/activities-clubs/">Activities &amp; Clubs</a><ul class='children'><li class="page_item page-item-88"><a href="https://sd.deltasd.bc.ca/activities-clubs/athletics/">Athletics</a></li><li class="page_item page-item-309"><a href="https://sd.deltasd.bc.ca/activities-clubs/snow-devils-ski-club/">Snowdevils Ski Club</a></li><li class="page_item page-item-396"><a href="https://sd.deltasd.bc.ca/activities-clubs/sdss-clubs/">SDSS Clubs</a></li></ul></li><li class="page_item page-item-22 page_item_has_children"><a href="https://sd.deltasd.bc.ca/student-resources/">Student Resources</a><ul class='children'><li class="page_item page-item-106"><a href="https://sd.deltasd.bc.ca/student-resources/student-handbook/">Student Handbook</a></li><li class="page_item page-item-315"><a href="https://sd.deltasd.bc.ca/student-resources/career-center/">Career Center / Scholarship Information</a></li><li class="page_item page-item-336"><a href="https://sd.deltasd.bc.ca/student-resources/student-connect/">Student Connect</a></li><li class="page_item page-item-2508"><a href="https://sd.deltasd.bc.ca/student-resources/incoming-grade-7-students/">New Sun Devil Students</a></li><li class="page_item page-item-118"><a href="https://sd.deltasd.bc.ca/student-resources/exam-study-resources/">Exam &amp; Study Resources</a></li><li class="page_item page-item-120"><a href="https://sd.deltasd.bc.ca/student-resources/counseling-center/">Counselling Center</a></li></ul></li><li class="page_item page-item-24 page_item_has_children"><a href="https://sd.deltasd.bc.ca/parent-community/">Parent Community</a><ul class='children'><li class="page_item page-item-124"><a href="https://sd.deltasd.bc.ca/parent-community/pac/">PAC</a></li><li class="page_item page-item-338"><a href="https://sd.deltasd.bc.ca/parent-community/parent-connect/">Parent Support</a></li></ul></li><li class="page_item page-item-132 page_item_has_children"><a href="https://sd.deltasd.bc.ca/library-resources/">Library &amp; Resources</a><ul class='children'><li class="page_item page-item-134"><a href="https://sites.google.com/deltalearns.ca/sdlibrary/library-basics#new_tab">Library Learning Commons</a></li><li class="page_item page-item-1081"><a href="https://focusedresources.ca/en/district-access-iframe#new_tab">Digital Resources</a></li><li class="page_item page-item-138"><a href="https://sd.deltasd.bc.ca/library-resources/staff-resources/">Staff Resources</a></li></ul></li><li class="page_item page-item-1139"><a href="https://sd.deltasd.bc.ca/graduation-2023-information/">Graduation 2025 Info</a></li></ul></div></nav>
                                                </div><!-- /menu-wrapper -->
                                        </div><!-- /name-menu-wrapper -->
                                        <div class="mobile-menu-wrapper m-hide">
                                                <div class="mobile-trigger m-hide">Menu</div>
                                                <nav role="navigation" itemscope itemtype="http://schema.org/SiteNavigationElement" class="m-hide mobile-menu"><div class="menu"><ul><li class="page_item page-item-14 page_item_has_children"><a href="https://sd.deltasd.bc.ca/our-school/">Our School</a><ul class='children'><li class="page_item page-item-58"><a href="https://sd.deltasd.bc.ca/our-school/about-our-school/">About Our School</a></li><li class="page_item page-item-640"><a href="https://sd.deltasd.bc.ca/our-school/calendar-20242025/">Calendars</a></li><li class="page_item page-item-4553"><a href="https://sd.deltasd.bc.ca/our-school/sdss-code-of-conduct/">SDSS Code of Conduct</a></li><li class="page_item page-item-4633"><a href="https://sd.deltasd.bc.ca/our-school/2023-24-school-opening-information/">2024-25 School Opening Information</a></li><li class="page_item page-item-64"><a href="https://sd.deltasd.bc.ca/our-school/school-schedule/">School Schedule</a></li><li class="page_item page-item-68"><a href="https://sd.deltasd.bc.ca/our-school/registration/">Registration</a></li><li class="page_item page-item-70"><a href="https://sd.deltasd.bc.ca/our-school/staff-directory/">Staff Directory</a></li><li class="page_item page-item-72"><a href="https://sd.deltasd.bc.ca/our-school/contact-directions/">Contact / Directions</a></li><li class="page_item page-item-6584"><a href="https://www.deltasd.bc.ca/programs/learning-services-inclusive-learning/threat-assessment-protocol-fair-notice/#new_tab">Threat Assessment Protocol &#8211; Fair Notice</a></li></ul></li><li class="page_item page-item-16 page_item_has_children"><a href="https://sd.deltasd.bc.ca/news-events/">News &amp; Events</a><ul class='children'><li class="page_item page-item-74"><a href="/events-calendar">Events Calendar</a></li><li class="page_item page-item-76"><a href="https://sd.deltasd.bc.ca/news-events/daily-announcements/">Daily Announcements</a></li><li class="page_item page-item-78"><a href="https://sd.deltasd.bc.ca/news-events/news/">News</a></li></ul></li><li class="page_item page-item-18 page_item_has_children"><a href="https://sd.deltasd.bc.ca/programs-courses/">Programs &amp; Courses</a><ul class='children'><li class="page_item page-item-82"><a href="https://sd.deltasd.bc.ca/programs-courses/course-guide/">Course Planning</a></li><li class="page_item page-item-84"><a href="https://sd.deltasd.bc.ca/programs-courses/career-programs/">Career Programs</a></li><li class="page_item page-item-86"><a href="https://sd.deltasd.bc.ca/programs-courses/international-student-program/">International Student Program</a></li></ul></li><li class="page_item page-item-20 page_item_has_children"><a href="https://sd.deltasd.bc.ca/activities-clubs/">Activities &amp; Clubs</a><ul class='children'><li class="page_item page-item-88"><a href="https://sd.deltasd.bc.ca/activities-clubs/athletics/">Athletics</a></li><li class="page_item page-item-309"><a href="https://sd.deltasd.bc.ca/activities-clubs/snow-devils-ski-club/">Snowdevils Ski Club</a></li><li class="page_item page-item-396"><a href="https://sd.deltasd.bc.ca/activities-clubs/sdss-clubs/">SDSS Clubs</a></li></ul></li><li class="page_item page-item-22 page_item_has_children"><a href="https://sd.deltasd.bc.ca/student-resources/">Student Resources</a><ul class='children'><li class="page_item page-item-106"><a href="https://sd.deltasd.bc.ca/student-resources/student-handbook/">Student Handbook</a></li><li class="page_item page-item-315"><a href="https://sd.deltasd.bc.ca/student-resources/career-center/">Career Center / Scholarship Information</a></li><li class="page_item page-item-336"><a href="https://sd.deltasd.bc.ca/student-resources/student-connect/">Student Connect</a></li><li class="page_item page-item-2508"><a href="https://sd.deltasd.bc.ca/student-resources/incoming-grade-7-students/">New Sun Devil Students</a></li><li class="page_item page-item-118"><a href="https://sd.deltasd.bc.ca/student-resources/exam-study-resources/">Exam &amp; Study Resources</a></li><li class="page_item page-item-120"><a href="https://sd.deltasd.bc.ca/student-resources/counseling-center/">Counselling Center</a></li></ul></li><li class="page_item page-item-24 page_item_has_children"><a href="https://sd.deltasd.bc.ca/parent-community/">Parent Community</a><ul class='children'><li class="page_item page-item-124"><a href="https://sd.deltasd.bc.ca/parent-community/pac/">PAC</a></li><li class="page_item page-item-338"><a href="https://sd.deltasd.bc.ca/parent-community/parent-connect/">Parent Support</a></li></ul></li><li class="page_item page-item-132 page_item_has_children"><a href="https://sd.deltasd.bc.ca/library-resources/">Library &amp; Resources</a><ul class='children'><li class="page_item page-item-134"><a href="https://sites.google.com/deltalearns.ca/sdlibrary/library-basics#new_tab">Library Learning Commons</a></li><li class="page_item page-item-1081"><a href="https://focusedresources.ca/en/district-access-iframe#new_tab">Digital Resources</a></li><li class="page_item page-item-138"><a href="https://sd.deltasd.bc.ca/library-resources/staff-resources/">Staff Resources</a></li></ul></li><li class="page_item page-item-1139"><a href="https://sd.deltasd.bc.ca/graduation-2023-information/">Graduation 2025 Info</a></li></ul></div></nav>
                                        </div><!-- /mobile-menu-wrapper -->

                                </div>

                                <div class="megamenu-container">
                                        <div class="div-container">
                                                <nav role="navigation" itemscope itemtype="http://schema.org/SiteNavigationElement">
                                                        <div class="menu"><ul><li class="page_item page-item-14 page_item_has_children"><a href="https://sd.deltasd.bc.ca/our-school/">Our School</a><ul class='children'><li class="page_item page-item-58"><a href="https://sd.deltasd.bc.ca/our-school/about-our-school/">About Our School</a></li><li class="page_item page-item-640"><a href="https://sd.deltasd.bc.ca/our-school/calendar-20242025/">Calendars</a></li><li class="page_item page-item-4553"><a href="https://sd.deltasd.bc.ca/our-school/sdss-code-of-conduct/">SDSS Code of Conduct</a></li><li class="page_item page-item-4633"><a href="https://sd.deltasd.bc.ca/our-school/2023-24-school-opening-information/">2024-25 School Opening Information</a></li><li class="page_item page-item-64"><a href="https://sd.deltasd.bc.ca/our-school/school-schedule/">School Schedule</a></li><li class="page_item page-item-68"><a href="https://sd.deltasd.bc.ca/our-school/registration/">Registration</a></li><li class="page_item page-item-70"><a href="https://sd.deltasd.bc.ca/our-school/staff-directory/">Staff Directory</a></li><li class="page_item page-item-72"><a href="https://sd.deltasd.bc.ca/our-school/contact-directions/">Contact / Directions</a></li><li class="page_item page-item-6584"><a href="https://www.deltasd.bc.ca/programs/learning-services-inclusive-learning/threat-assessment-protocol-fair-notice/#new_tab">Threat Assessment Protocol &#8211; Fair Notice</a></li></ul></li><li class="page_item page-item-16 page_item_has_children"><a href="https://sd.deltasd.bc.ca/news-events/">News &amp; Events</a><ul class='children'><li class="page_item page-item-74"><a href="/events-calendar">Events Calendar</a></li><li class="page_item page-item-76"><a href="https://sd.deltasd.bc.ca/news-events/daily-announcements/">Daily Announcements</a></li><li class="page_item page-item-78"><a href="https://sd.deltasd.bc.ca/news-events/news/">News</a></li></ul></li><li class="page_item page-item-18 page_item_has_children"><a href="https://sd.deltasd.bc.ca/programs-courses/">Programs &amp; Courses</a><ul class='children'><li class="page_item page-item-82"><a href="https://sd.deltasd.bc.ca/programs-courses/course-guide/">Course Planning</a></li><li class="page_item page-item-84"><a href="https://sd.deltasd.bc.ca/programs-courses/career-programs/">Career Programs</a></li><li class="page_item page-item-86"><a href="https://sd.deltasd.bc.ca/programs-courses/international-student-program/">International Student Program</a></li></ul></li><li class="page_item page-item-20 page_item_has_children"><a href="https://sd.deltasd.bc.ca/activities-clubs/">Activities &amp; Clubs</a><ul class='children'><li class="page_item page-item-88"><a href="https://sd.deltasd.bc.ca/activities-clubs/athletics/">Athletics</a></li><li class="page_item page-item-309"><a href="https://sd.deltasd.bc.ca/activities-clubs/snow-devils-ski-club/">Snowdevils Ski Club</a></li><li class="page_item page-item-396"><a href="https://sd.deltasd.bc.ca/activities-clubs/sdss-clubs/">SDSS Clubs</a></li></ul></li><li class="page_item page-item-22 page_item_has_children"><a href="https://sd.deltasd.bc.ca/student-resources/">Student Resources</a><ul class='children'><li class="page_item page-item-106"><a href="https://sd.deltasd.bc.ca/student-resources/student-handbook/">Student Handbook</a></li><li class="page_item page-item-315"><a href="https://sd.deltasd.bc.ca/student-resources/career-center/">Career Center / Scholarship Information</a></li><li class="page_item page-item-336"><a href="https://sd.deltasd.bc.ca/student-resources/student-connect/">Student Connect</a></li><li class="page_item page-item-2508"><a href="https://sd.deltasd.bc.ca/student-resources/incoming-grade-7-students/">New Sun Devil Students</a></li><li class="page_item page-item-118"><a href="https://sd.deltasd.bc.ca/student-resources/exam-study-resources/">Exam &amp; Study Resources</a></li><li class="page_item page-item-120"><a href="https://sd.deltasd.bc.ca/student-resources/counseling-center/">Counselling Center</a></li></ul></li><li class="page_item page-item-24 page_item_has_children"><a href="https://sd.deltasd.bc.ca/parent-community/">Parent Community</a><ul class='children'><li class="page_item page-item-124"><a href="https://sd.deltasd.bc.ca/parent-community/pac/">PAC</a></li><li class="page_item page-item-338"><a href="https://sd.deltasd.bc.ca/parent-community/parent-connect/">Parent Support</a></li></ul></li><li class="page_item page-item-132 page_item_has_children"><a href="https://sd.deltasd.bc.ca/library-resources/">Library &amp; Resources</a><ul class='children'><li class="page_item page-item-134"><a href="https://sites.google.com/deltalearns.ca/sdlibrary/library-basics#new_tab">Library Learning Commons</a></li><li class="page_item page-item-1081"><a href="https://focusedresources.ca/en/district-access-iframe#new_tab">Digital Resources</a></li><li class="page_item page-item-138"><a href="https://sd.deltasd.bc.ca/library-resources/staff-resources/">Staff Resources</a></li></ul></li><li class="page_item page-item-1139"><a href="https://sd.deltasd.bc.ca/graduation-2023-information/">Graduation 2025 Info</a></li></ul></div>                                               </nav>
                                        </div><!-- /div-container -->
                                </div><!-- /megamenu-container -->

                        </header>

<div id="content">

        <div id="inner-content" class="wrap cf">


                        <div class="home-banner-container col-3-4 home-row right">
                                <div class="overlay"></div>
                                <ul class="home-banner-wrapper col-1-1">

                                                                                <li class="slide">
                                                <img src="https://sd.public.deltasd.bc.ca/wp-content/uploads/sites/31/2018/08/Front-1280x570.jpg">       
                                                                                                        <div class="tagline-btn-wrapper">
                                                                                                                                        <span class="tagline-wrapper"><h2>Home of the Sun Devils</h2></span>
                                                                                                                                                        </div><!-- /.tagline-btn-wrapper -->
                                                                                        </li>

                                                                        <li class="slide">
                                                <img src="https://sd.public.deltasd.bc.ca/wp-content/uploads/sites/31/2018/08/20170831_101252-1280x570.jpg">
                                                                                        </li>

                                                                        <li class="slide">
                                                <img src="https://sd.public.deltasd.bc.ca/wp-content/uploads/sites/31/2018/08/IMG_4985-1-1-1280x570.jpg">
                                                                                        </li>

                                                                        <li class="slide">
                                                <img src="https://sd.public.deltasd.bc.ca/wp-content/uploads/sites/31/2018/08/bD94BbC2-3B9ACA00-2-IMG_0858-1280x570.jpg">
                                                                                        </li>

                                                                        <li class="slide">
                                                <img src="https://sd.public.deltasd.bc.ca/wp-content/uploads/sites/31/2023/06/Vision1920x570px-1-1280x570.jpg">
                                                                                                        <div class="tagline-btn-wrapper">
                                                                                                                                        <span class="tagline-wrapper"><h2>Vision 2030 Delta School District</h2></span>
                                                                                                                                                        <a href="https://www.deltasd.bc.ca/district/our-vision/ " class="btn"> Learn more</a>
                                                                                                                        </div><!-- /.tagline-btn-wrapper -->
                                                                                        </li>


                        </ul>
                </div><!-- /home-banner-container -->


                                        <div class="sidebar main-sidebar col-1-4 cf" role="complementary">


                                                                <div class="quicklinks-wrapper col-1-1">
                        <div class="quicklink-trigger">Quicklinks</div>
                        <ul class="quicklinks-menu">
                                                                        <li><a href="https://sd.deltasd.bc.ca/our-school/about-our-school/">About Our School</a></li>
                                                                        <li><a href="https://sd.deltasd.bc.ca/parent-community/">Parent Community</a></li>
                                                                        <li><a href="https://sd.deltasd.bc.ca/parent-community/parent-connect/">Parent Support</a></li>
                                                                        <li><a href="/events-calendar">Events Calendar</a></li>
                                                        </ul>
                </div><!-- /quicklinks-wrapper -->

                <div class="announcements-wrapper col-1-1">

                                                <a href="https://sd.deltasd.bc.ca/news-events/daily-announcements/course-planning-2022/" class="remove-icon">
                                <span class="announcement-item col-1-1">
                                        <span class="announcement-item-content">
                                                                                                <span class="title-subtitle-wrapper">
                                                        <h3>Course Planning 2023 2024</h3>
                                                                                                        </span><!-- /title-subtitle-wrapper -->
                                        </span><!-- /announcement-item-content -->
                                </span><!-- /announcement-item -->
                        </a>
                        </div>
                <div class="district_news_events-wrapper widget col-1-1">
                        <h4 class="widgettitle">District News & Events</h4>
                        <div class="widget-wrapper col-1-1">
                                <div class="tabs-wrapper col-1-1">
                                        <div class="tab news active">News</div>
                                        <div class="tab events">Events</div>
                                </div>
                                <div class="lists-wrapper col-1-1">
                                                                                        <div class="news-list list-wrapper active col-1-1">
                                                                                                                        <div class="news-item">
                                                                                                                                                <h3><a href="https://www.deltasd.bc.ca/news-events/news/south-park-students-excel-at-decorating-pumpkins/" class="news-title remove-icon">South Park Students Excel at Decorating Pumpkins</a></h3>
                                                                </div>
                                                                                                                        <div class="news-item">
                                                                                                                                                <h3><a href="https://www.deltasd.bc.ca/news-events/news/new-aquatics-certification-piloted-with-delta-students/" class="news-title remove-icon">New Aquatics Certification Piloted with Delta Students</a></h3>
                                                                </div>
                                                                                                                        <div class="news-item">
                                                                                                                                                <h3><a href="https://www.deltasd.bc.ca/news-events/news/celebrating-world-teachers-day-2024/" class="news-title remove-icon">Celebrating World Teachers’ Day 2024</a></h3>
                                                                </div>
                                                                                                        </div>
                                                                                        <div class="event-list list-wrapper col-1-1">
                                                                                                                        <div class="event-item">
                                                                                <div class="cal-box date-box">
                <span class="month">Nov</span>
                <span class="day">2</span>
        </div>
                                                                                <h3><a href="https://www.deltasd.bc.ca/event/jim-byrnes-at-the-genesis-theatre/" class="event-time remove-icon">Saturday 7:30pm to 10:00pm</a></h3>
                                                                        <a href="https://www.deltasd.bc.ca/event/jim-byrnes-at-the-genesis-theatre/" class="event-title remove-icon">Jim Byrnes at the Genesis Theatre</a>
                                                                </div>
                                                                                                                        <div class="event-item">
                                                                                <div class="cal-box date-box">
                <span class="month">Jan</span>
                <span class="day">18</span>
        </div>
                                                                                <h3><a href="https://www.deltasd.bc.ca/event/brent-butt-returns-to-ladner/" class="event-time remove-icon">Saturday 7:30pm to 10:00pm</a></h3>
                                                                        <a href="https://www.deltasd.bc.ca/event/brent-butt-returns-to-ladner/" class="event-title remove-icon">Brent Butt Returns to Ladner</a>
                                                                </div>
                                                                                                        </div>
                                                                        </div>
                        </div>
                </div><!-- /district_news_events-wrapper -->

                                                <!-- Related Gallery -->


                                </div>


                <main id="main" class="col-3-4 cf right" role="main" itemscope itemprop="mainContentOfPage" itemtype="http://schema.org/Blog">


                        <div class="border-wrapper">

                                                                        <div class="home-news-wrapper col-1-1">
                                                                                                        <div class="home-news-item col-1-1 home-row">    

                                                                                                                                        <div class="news-item-content">
                                                                                <div class="title-date-wrapper">
                                                                                        <h2 class="h-one title"><a href="https://sd.deltasd.bc.ca/news-events/news/halloween-message-2024/" class="news-title">Halloween Message 2024 and Winskill Construction Update</a></h2>
                                                                                                                                                        </div><!-- /title-date-wrapper -->
                                                                                <div class="excerpt">
                                                                                        <p><a href="https://sd.deltasd.bc.ca/wp-content/uploads/sites/31/2024/10/Halloween-Message-2024.pdf">Halloween Message 2024</a>&#8230;  <a class="excerpt-read-more" href="https://sd.deltasd.bc.ca/news-events/news/halloween-message-2024/" title="Read Halloween Message 2024 and Winskill Construction Update">Read more &raquo;</a></p>
                                                                                </div><!-- /excerpt -->
                                                                                <a href="https://sd.deltasd.bc.ca/news-events/news/halloween-message-2024/" class="button">Read More</a>
                                                                        </div><!-- /news-item-content -->
                                                                                                                        </div><!-- /home-news-item -->   
                                                                                                                                                        <div class="home-news-item col-1-1 home-row">

                                                                                                                                        <a href="https://www.deltasd.bc.ca/news-events/news/walk-for-truth-and-reconciliation/" class="remove-icon"><span class="img-wrapper" style="background:url(https://sd.public.deltasd.bc.ca/wp-content/uploads/sites/2/2024/09/TR-banner-1024x577.png);"></span></a>
                                                                        <div class="news-item-content has-img">
                                                                                <div class="title-date-wrapper">
                                                                                        <h2 class="h-one title"><a href="https://www.deltasd.bc.ca/news-events/news/walk-for-truth-and-reconciliation/" class="news-title">Walk for Truth and Reconciliation</a></h2>
                                                                                                                                                        </div><!-- /title-date-wrapper -->
                                                                                <div class="excerpt">
                                                                                        <p>Walk for Truth and Reconciliation<br />
This morning, students and staff across Delta are participating in a Walk for Truth and Reconciliation.<br />
Students from Delta Secondary School and six elementary schools in Ladner (Hawthorne,&#8230;  <a class="excerpt-read-more" href="https://www.deltasd.bc.ca/news-events/news/walk-for-truth-and-reconciliation/" title="Read Walk for Truth and Reconciliation">Read more &raquo;</a></p>
                                                                                </div><!-- /excerpt -->
                                                                                <a href="https://www.deltasd.bc.ca/news-events/news/walk-for-truth-and-reconciliation/" class="button">Read More</a>
                                                                        </div><!-- /news-item-content -->
                                                                                                                        </div><!-- /home-news-item -->   
                                                                                                                                                        <div class="home-news-item col-1-1 home-row">

                                                                                                                                        <a href="https://www.deltasd.bc.ca/news-events/news/2024-welcome-back-to-school-message/" class="remove-icon"><span class="img-wrapper" style="background:url(https://sd.public.deltasd.bc.ca/wp-content/uploads/sites/2/2024/08/Back-to-school-website.jpg);"></span></a>
                                                                        <div class="news-item-content has-img">
                                                                                <div class="title-date-wrapper">
                                                                                        <h2 class="h-one title"><a href="https://www.deltasd.bc.ca/news-events/news/2024-welcome-back-to-school-message/" class="news-title">2024 Welcome Back to School Message</a></h2>
                                                                                                                                                        </div><!-- /title-date-wrapper -->
                                                                                <div class="excerpt">
                                                                                        <p>Dear Delta Students, Families and Staff,<br />
Welcome to the 2024/2025 school year! Hopefully you’ve had a wonderful summer and are returning to school relaxed, recharged and ready for the challenge and excitement of a new academic year&#8230;.  <a class="excerpt-read-more" href="https://www.deltasd.bc.ca/news-events/news/2024-welcome-back-to-school-message/" title="Read 2024 Welcome Back to School Message">Read more &raquo;</a></p>
                                                                                </div><!-- /excerpt -->
                                                                                <a href="https://www.deltasd.bc.ca/news-events/news/2024-welcome-back-to-school-message/" class="button">Read More</a>
                                                                        </div><!-- /news-item-content -->
                                                                                                                        </div><!-- /home-news-item -->   
                                                                                                                <div class="more-news-btn-wrapper"><a href="/news-events/news/" class="button more-news-btn">More News</a></div>
                                                </div>

                        </div><!-- /border-wrapper -->

                </main>

        </div><!-- /inner-content -->

</div>





                        <footer class="footer col-1-1" role="contentinfo" itemscope itemtype="http://schema.org/WPFooter">

                                <div id="inner-footer" class="wrap cf">

                                        <div class="school-footer col-1-1">

                                                <div class="footer-left col-3-5">
                                                        <img <img src="/wp-content/uploads/sites/31/assets/SouthDeltaSecondary.jpg" class="school-icon" />
                                                        <div class="footer-rows">
                                                                <div class="top-row col-1-1">
                                                                        <span class="copyright">&copy; Copyright South Delta</span>
                                                                </div><!-- /top-row -->
                                                                <div class="bottom-row col-1-1">
                                                                        <nav role="navigation">
                                                                                                                                        </nav>
                                                                                                                                                        <div class="social-icons">
                                                                                <a href="https://twitter.com/SDSSSundevils" class="social-icon twitter"><img class="icon-img" src="/wp-content/themes/school/library/images/icons/socialmedia_Twitter.png"></a>                                                  <a href="https://www.facebook.com/sdss.sundevils/" class="social-icon facebook"><img class="icon-img" src="/wp-content/themes/school/library/images/icons/socialmedia_Facebook.png"></a>                                                                          <a href="https://instagram.com/southdeltaathletics" class="social-icon instagram"><img class="icon-img" src="/wp-content/themes/school/library/images/icons/socialmedia_Instagram.png"></a>              </div>
                                                                                                                </div><!-- /bottom-row -->
                                        </div><!-- /footer-rows -->
                                </div><!-- /footer-left -->
                                <div class="footer-right col-2-5">
                                                                                                                        <div class="top-row col-1-1">    
                                                                        <span class="phone-label">Phone:</span> <span class="phone-number">604-943-7407</span>
                                                                </div>
                                                                                                                                                        <div class="bottom-row col-1-1">
                                                                                                <span>750 - 53 Street</span>                             
                        <span>Delta</span>                                              <span>BC</span>                                         <span>V4M 3B7</span>                                     </div>
                                        <div class="mobile-copyright m-hide m-hide-600"><span class="copyright">&copy; Copyright South Delta</span></div>
                                </div><!-- /footer-right -->
                            </div><!-- /school-footer -->
                    </div><!-- /inner-footer -->
                    <div class="district-footer col-1-1">
                        <div id="inner-district-footer" class="wrap">
                                <div class="district-logo"><img src="/wp-content/themes/district/library/images/logo-white.png"></div>
                                <div class="district-links">
                                        <a href="https://www.deltasd.bc.ca/">Homepage</a>
                                </div><!-- /district-links -->
                                <div class="district-copyright">&copy; Copyright Delta School District</div>
                        </div>
                    </div><!-- /district-footer -->

                  </footer>

                </div>

                                                <script>
                ( function ( body ) {
                        'use strict';
                        body.className = body.className.replace( /\btribe-no-js\b/, 'tribe-js' );
                } )( document.body );
                </script>
                        <style>
            .searchwp-live-search-results {
                opacity: 0;
                transition: opacity .25s ease-in-out;
                -moz-transition: opacity .25s ease-in-out;
                -webkit-transition: opacity .25s ease-in-out;
                height: 0;
                overflow: hidden;
                z-index: 9999995; /* Exceed SearchWP Modal Search Form overlay. */
                position: absolute;
                display: none;
            }

            .searchwp-live-search-results-showing {
                display: block;
                opacity: 1;
                height: auto;
                overflow: auto;
            }

            .searchwp-live-search-no-results {
                padding: 3em 2em 0;
                text-align: center;
            }

            .searchwp-live-search-no-min-chars:after {
                content: "Continue typing";
                display: block;
                text-align: center;
                padding: 2em 2em 0;
            }
        </style>
                <script>
            var _SEARCHWP_LIVE_AJAX_SEARCH_BLOCKS = true;
            var _SEARCHWP_LIVE_AJAX_SEARCH_ENGINE = 'default';
            var _SEARCHWP_LIVE_AJAX_SEARCH_CONFIG = 'default';
        </script>
        <script> /* <![CDATA[ */var tribe_l10n_datatables = {"aria":{"sort_ascending":": activate to sort column ascending","sort_descending":": activate to sort column descending"},"length_menu":"Show _MENU_ entries","empty_table":"No data available in table","info":"Showing _START_ to _END_ of _TOTAL_ entries","info_empty":"Showing 0 to 0 of 0 entries","info_filtered":"(filtered from _MAX_ total entries)","zero_records":"No matching records found","search":"Search:","all_selected_text":"All items on this page were selected. ","select_all_link":"Select all pages","clear_selection":"Clear Selection.","pagination":{"all":"All","next":"Next","previous":"Previous"},"select":{"rows":{"0":"","_":": Selected %d rows","1":": Selected 1 row"}},"datepicker":{"dayNames":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"dayNamesShort":["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],"dayNamesMin":["S","M","T","W","T","F","S"],"monthNames":["January","February","March","April","May","June","July","August","September","October","November","December"],"monthNamesShort":["January","February","March","April","May","June","July","August","September","October","November","December"],"monthNamesMin":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"nextText":"Next","prevText":"Prev","currentText":"Today","closeText":"Done","today":"Today","clear":"Clear"}};/* ]]> */ </script><script type="text/javascript" src="https://sd.deltasd.bc.ca/wp-content/plugins/page-links-to/dist/new-tab.js" id="page-links-to-js"></script>
<script type="text/javascript" id="swp-live-search-client-js-extra">
/* <![CDATA[ */
var searchwp_live_search_params = [];
searchwp_live_search_params = {"ajaxurl":"https:\/\/sd.deltasd.bc.ca\/wp-admin\/admin-ajax.php","origin_id":46,"config":{"default":{"engine":"default","input":{"delay":300,"min_chars":3},"results":{"position":"bottom","width":"auto","offset":{"x":0,"y":5}},"spinner":{"lines":12,"length":8,"width":3,"radius":8,"scale":1,"corners":1,"color":"#424242","fadeColor":"transparent","speed":1,"rotate":0,"animation":"searchwp-spinner-line-fade-quick","direction":1,"zIndex":2000000000,"className":"spinner","top":"50%","left":"50%","shadow":"0 0 1px transparent","position":"absolute"}}},"msg_no_config_found":"No valid SearchWP Live Search configuration found!","aria_instructions":"When autocomplete results are available use up and down arrows to review and enter to go to the desired page. Touch device users, explore by touch or with swipe gestures.","searchwp_live_search_client_nonce":"3f53114199"};;
/* ]]> */
</script>
<script type="text/javascript" src="https://sd.deltasd.bc.ca/wp-content/plugins/searchwp-live-ajax-search/assets/javascript/dist/script.min.js" id="swp-live-search-client-js"></script>
<script type="text/javascript" src="https://sd.deltasd.bc.ca/wp-content/themes/school/library/js/min/jquery.hoverIntent.js" id="hover-intent-js"></script>
<script type="text/javascript" src="https://sd.deltasd.bc.ca/wp-content/themes/school/library/js/scripts.js" id="bones-js-js"></script>
<script type="text/javascript" src="https://sd.deltasd.bc.ca/wp-content/themes/school/library/js/min/slick.min.js" id="slick-js-js"></script>
        <script type="text/javascript">
            /* <![CDATA[ */
           document.querySelectorAll("ul.nav-menu").forEach(
               ulist => {
                    if (ulist.querySelectorAll("li").length == 0) {
                        ulist.style.display = "none";

                                            }
                }
           );
            /* ]]> */
        </script>

        </body>

        </html> <!-- end of site. what a ride! -->

<!-- Cache served by Simple Cache - Last modified: Mon, 28 Oct 2024 21:12:46 GMT -->"""