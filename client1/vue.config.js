const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
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
