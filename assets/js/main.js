//Main js file
$(document).ready( function() {

    function showSaveButton() {
        $('#save_button').parent().show();
    }

    function showMainForm() {
        $('#main_form').show();
        showSaveButton();
    }

    function newDates() {
        $clones = $('#internship').children().clone();
        $clones.find('input').val("");
        $('#internship').parent().append($clones);
        $('.datepicker').datepicker();
        $('.internship_plus').unbind('click');
        $('.internship_plus').on('click', newDates);
    }

    function init () {
        //main container
        var $container = $('#main_container');
        $container.delay('300').fadeIn('slow');

        //Use my FB profile button
        var $fbConnect = $('#landing_fb_connect');
        $fbConnect.on('click', function() {

            FB.login(function(response) {
                if (response.authResponse) {
                    FB.api('/me', function(response) {
                        console.log(response);
                        $('input[name=first_name]').val(response.first_name);
                        $('#welcome').html(response.first_name);
                        $('input[name=sur_name]').val(response.last_name);
                        $('input[name=facebook_id]').val(response.id);
                        if (response.hasOwnProperty('education')){
                            var last_education = response.education[response.education.length -1];
                            var school = response.education[response.education.length -1].school;
                            $('input[name=school_facebook_id]').val(school.id);
                            $('#school_picture').attr('src', 'http://graph.facebook.com/' + school.id + '/picture?type=normal');
                            $('#inputSchool').val(school.name);

                            if (last_education.hasOwnProperty('classes')) {
                                var keywords = [];
                                $.each(last_education.classes, function(index, cls){
                                    keywords.push(cls.name);
                                });
                                $('input[name=majors]').val(keywords.join(', '));
                            }
                        }
                    });
                } else {
                    console.log('User cancelled login or did not fully authorize.');
                }
            });
            showMainForm();
        });

        //date picker
        $(function() {
            $(".datepicker").datepicker();
        });

        $('.internship_plus').on('click', newDates);

        //Enter your info manually link
        var $enterInfoManually = $('#enter_info_manually');
        $enterInfoManually.on('click', function() {
            showMainForm();
        });

    }

    init();

});
