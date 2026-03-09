const { DateTime } = require("luxon");
const readingTime = require("reading-time");
const markdownIt = require("markdown-it");
const markdownItKatex = require("markdown-it-katex");
const pluginSyntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");
const pluginRss = require("@11ty/eleventy-plugin-rss");

module.exports = function(eleventyConfig) {
  // Plugins
  eleventyConfig.addPlugin(pluginSyntaxHighlight, {
    alwaysWrapLineHighlights: false,
    trim: true
  });
  eleventyConfig.addPlugin(pluginRss);

  // Passthrough file copies
  eleventyConfig.addPassthroughCopy("src/assets/css");
  eleventyConfig.addPassthroughCopy("src/assets/js");
  eleventyConfig.addPassthroughCopy("src/assets/images");
  eleventyConfig.addPassthroughCopy("src/assets/fonts");

  // Collections
  eleventyConfig.addCollection("posts", function(collectionApi) {
    return collectionApi.getFilteredByGlob("src/content/blog/posts/*.md")
      .filter(item => !item.data.draft)
      .sort((a, b) => b.date - a.date);
  });

  eleventyConfig.addCollection("featuredPosts", function(collectionApi) {
    return collectionApi.getFilteredByGlob("src/content/blog/posts/*.md")
      .filter(item => item.data.featured && !item.data.draft)
      .sort((a, b) => b.date - a.date)
      .slice(0, 3);
  });

  eleventyConfig.addCollection("pages", function(collectionApi) {
    return collectionApi.getFilteredByGlob("src/content/pages/*.md");
  });

  // Filters
  eleventyConfig.addFilter("date", (dateObj) => {
    return DateTime.fromJSDate(dateObj).toLocaleString(DateTime.DATE_MED);
  });

  eleventyConfig.addFilter("dateIso", (dateObj) => {
    return DateTime.fromJSDate(dateObj).toISODate();
  });

  eleventyConfig.addFilter("readableDate", (dateObj) => {
    return DateTime.fromJSDate(dateObj).setZone("America/Santiago").toFormat("MMMM dd, yyyy");
  });

  eleventyConfig.addFilter("readingTime", (content) => {
    return Math.ceil(readingTime(content).minutes);
  });

  eleventyConfig.addFilter("markdownify", (str) => {
    const md = new markdownIt();
    return md.render(str);
  });

  eleventyConfig.addFilter("excerpt", (str) => {
    if (!str) return "";
    return str.substring(0, 160);
  });

  eleventyConfig.addFilter("absoluteUrl", (url) => {
    const siteUrl = eleventyConfig.globalData.site.url;
    return siteUrl + url;
  });

  // Template Formats
  eleventyConfig.setTemplateFormats(["md", "njk", "html"]);

  // Markdown Library
  const mdLibrary = markdownIt({
    html: true,
    breaks: true,
    linkify: true,
    typographer: true
  });

  mdLibrary.use(markdownItKatex);

  eleventyConfig.setLibrary("md", mdLibrary);

  // Watch Targets
  eleventyConfig.addWatchTarget("src/assets/css/");
  eleventyConfig.addWatchTarget("src/assets/js/");

  // Server Options
  eleventyConfig.setServerOptions({
    port: 8080,
    watch: true,
    liveReload: true
  });

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data"
    },
    templateFormats: ["md", "njk", "html"],
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk",
    passthroughFileCopy: true
  };
};
