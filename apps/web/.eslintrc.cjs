module.exports = {
  root: true,
  parser: '@typescript-eslint/parser',
  parserOptions: {
    project: ['./tsconfig.json'],
    sourceType: 'module'
  },
  plugins: ['@typescript-eslint', 'unused-imports', 'import'],
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
    'plugin:import/typescript'
  ],
  rules: {
    '@typescript-eslint/no-explicit-any': 'error',
    '@typescript-eslint/no-floating-promises': 'error',
    'import/order': 'error',
    'unused-imports/no-unused-imports': 'error'
  }
};
