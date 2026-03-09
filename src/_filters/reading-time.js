/**
 * Reading time filter
 */
const readingTime = require("reading-time");

module.exports = (content) => {
  const readTime = readingTime(content);
  return Math.ceil(readTime.minutes);
};
