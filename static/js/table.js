// var btns = document.getElementsByClassName('tables');

// console.log(btns)

// for (i = 0; i < btns.length; i++){
//     var classes = btns[i].classList
//     console.log(classes)

//     btns[i].addEventListener('click', function() {
//         var result = classes.toggle('table-success')

//         if (result) {
//             classes.add('visually-hidden')
//         } else {
//             classes.remove('visually-hidden')
//         }
//     })

// }
$(document).ready(function() {
	$('[data-toggle="toggle"]').change(function(){
		$(this).parents().next('.hide').toggle();
	});
});