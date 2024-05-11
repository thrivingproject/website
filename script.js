console.log(
    "A HaiKu is a three line poem.\n\n" +
    "It's supposed to be about nature, so mine isn't very good, but beauty is in the eyes of the beholder.\n\n" +
    "Email me your own HaiKu!"
);

// change em to email address when clicked
document.querySelector('em').addEventListener('click', () => {
    document.querySelector('em').textContent = 'christianisaman@outlook.com';
  });