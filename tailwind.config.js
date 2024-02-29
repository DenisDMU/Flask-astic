/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./templates/*"],
  theme: {
    extend: {
      // Ajout de font persos que j'ai sur mon mac :D
      fontFamily:{
        arthemys:['Arthemys-Light-DEMO','serif'],
        abril : ['AbrilFatface-Regular','serif'],
        saol : ['SaolDisplay-Light','serif']
      }
    },
  },
  plugins: [],
}

