module.exports = {
    extends: [
        // add more generic rulesets here, such as:
        // 'eslint:recommended',
        // 'plugin:vue/recommended'
        'plugin:vue/base'
    ],
    rules: {
        'no-console': 'off',
    },
    // parserOptions: {
    //     "parser": "babel-eslint"
    // }
};

// TODO ESLINT的配置先不搞 不然build的时候一堆error