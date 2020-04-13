module.exports = {
    // outputDir: '',
    assetsDir: 'static',
    indexPath: '../../templates/index.html',
    // filenameHashing: false,
    // runtimeCompiler: true,
    // chainWebpack: config => {
    //   config.plugins.delete('hmr');
    //   config.plugins.delete('html');
    //   config.plugins.delete('preload');
    //   config.plugins.delete('prefetch');
    // },
    chainWebpack: config => {
        config.module.rules.delete('eslint');
    }
};
