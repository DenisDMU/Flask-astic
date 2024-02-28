/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./templates/*"],
  theme: {
    extend: {
      fontFamily:{
        arthemys:['Arthemys-Light-DEMO','serif'],
        abril : ['AbrilFatface-Regular','serif'],
        saol : ['SaolDisplay-Light','serif']
      }
    },
  },
  plugins: [],
}

