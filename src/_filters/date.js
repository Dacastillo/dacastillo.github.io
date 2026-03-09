/**
 * Date filters for 11ty
 */
const { DateTime } = require("luxon");

module.exports = {
  date: (dateObj) => {
    if (!dateObj) return "";
    return DateTime.fromJSDate(dateObj).toLocaleString(DateTime.DATE_MED);
  },

  dateIso: (dateObj) => {
    if (!dateObj) return "";
    return DateTime.fromJSDate(dateObj).toISODate();
  },

  readableDate: (dateObj) => {
    if (!dateObj) return "";
    return DateTime.fromJSDate(dateObj).setZone("America/Santiago").toFormat("MMMM dd, yyyy");
  },

  htmlDateString: (dateObj) => {
    if (!dateObj) return "";
    return DateTime.fromJSDate(dateObj).toFormat("yyyy-LL-dd");
  }
};
