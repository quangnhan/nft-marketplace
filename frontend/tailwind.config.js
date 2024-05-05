/** @type {import('tailwindcss').Config} */
// eslint-disable-next-line import/no-anonymous-default-export
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
      extend: {
          fontFamily: {
              inter: ["Inter", "sans-serif"],
          },
          colors: {
              primary: "#121212",
              secondary: "#c00",
              tertiary: '#38383f'
          },
      },
  },
  plugins: [],
};
