var Lock = function () {

    return {
        //main function to initiate the module
        init: function () {

             $.backstretch([
		        "static/static_admin/img/bg/1.jpg",
		        "static/static_admin/img/bg/2.jpg",
		        "static/static_admin/img/bg/3.jpg",
		        "static/static_admin/img/bg/4.jpg"
		        ], {
		          fade: 1000,
		          duration: 8000
		      });
        }

    };

}();