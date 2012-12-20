//Main js file
$(document).ready( function() {

    function showSaveButton() {
        $('#save_button').show();
    }

    function showMainForm() {
        $('#main_form').show();
        showSaveButton();
    }

    function init () {
        //main container
        var $container = $('#main_container');
        $container.delay('300').fadeIn('slow');

        //Use my FB profile button
        landing_fb_connect
        var $fbConnect = $('#landing_fb_connect');
        $fbConnect.on('click', function() {
            $('#inputSchool').val('Telecoms');
            $('#inputMajor').val('IA, Security, Hacking');
            $('#inputPeriod').val('10 june to 30 sept');
            $("#datepicker_from").datepicker("setDate", "05/01/2012");
            $("#datepicker_to").datepicker("setDate", "09/30/2012");
            $('#inputKeywords').val('IA, Security, Hacking');
            showMainForm();
        });

        //Enter your info manually link
        var $enterInfoManually = $('#enter_info_manually');
        $enterInfoManually.on('click', function() {
            showMainForm();
        });

        //date picker
        $(function() {
            $( "#datepicker_from" ).datepicker();
            $( "#datepicker_to" ).datepicker();
        });
    }

    init();

});
