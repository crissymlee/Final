function dropdown(num) {
  document.querySelector(`.mydropdown${num}`).classList.toggle('show')
}

function filterFunction(num) {
  const filter = document.querySelector(`#myInput${num}`).value.toUpperCase()
  const a = document.querySelectorAll(`#select${num} option`)
  const aList = Array.from(a)

  for (i = 0; i < aList.length; i++) {
    if (aList[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = ''
    } else {
      a[i].style.display = 'none'
    }
  }
}

const btn1 = document.querySelector('#dropbtn1')
const btn2 = document.querySelector('#dropbtn2')

const input1 = document.querySelector('#myInput1')
const input2 = document.querySelector('#myInput2')

btn1.addEventListener('click', function () {
  dropdown(1)
})
btn2.addEventListener('click', function () {
  dropdown(2)
})

input1.addEventListener('keyup', function () {
  filterFunction(1)
})
input2.addEventListener('keyup', function () {
  filterFunction(2)
})

document.querySelector('#select1').addEventListener('change', function (e) {
  document.querySelector('#span1').innerHTML = e.target.value
  document.querySelector(`.mydropdown1`).classList.toggle('show')
})

document.querySelector('#select2').addEventListener('change', function (e) {
  document.querySelector('#span2').innerHTML = e.target.value
  document.querySelector(`.mydropdown2`).classList.toggle('show')
})
