const { defineConfig } = require("@vue/cli-service");
const path = require("path");

module.exports = defineConfig({
  publicPath: "./static",
  outputDir: path.resolve(__dirname, "../static"),
  transpileDependencies: true,
  lintOnSave: false,
  devServer: {
    proxy: {
      "/api": {
        target: "http://streetmeet.lukvmil.com",
        changeOrigin: true,
      },
    },
  },
});
