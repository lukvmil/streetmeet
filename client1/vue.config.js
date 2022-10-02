const { defineConfig } = require("@vue/cli-service");
const path = require("path");

let config = {
  outputDir: path.resolve(__dirname, "../static"),
  transpileDependencies: true,
  lintOnSave: false,
  devServer: {
    proxy: {
      "/api": {
        target: "https://streetmeet.lukvmil.com",
        changeOrigin: true,
      },
    },
  },
};

if (process.env.NODE_ENV == "production") {
  config.publicPath = "/streetmeet/static";
}

module.exports = defineConfig(config);
