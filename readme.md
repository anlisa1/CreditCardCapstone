This template requires credentials from:
1) Mongodb.com
2) Google OAuth - https://console.cloud.google.com/apis/dashboard



The modules folder will also be updated for reference and also for emergency usage (in case the classes don't work)

pip install flask-ckeditor

please install this onto the website(still learning on the above)

 Anlisa TD ->  fix add course button, different color (form and modules cret\ation first)
               also form and module -> get ready
               (ask wright) 3. add module function (working on ck editor so far)
               1. mark as done function //
               2. accounatbility and progress of module progression, progress bar of thermometer

Anlisa -> some notes to recall
    in the py files when rendering html templates, you can send variables to the html file and use in jinja by
    render_template('file.html', variable =  stuff, varaible = stuff)
    the variable will be used on the html file with jinja, and the stuff is from the python file

Anlisa - code to maybe reuse and take off of testibg file
    in python
        form = MarkasCompleteForm()
        if form.validate_on_submit():
            currUser = User.objects.get(id=current_user.id)
            current_user.courses_completed.append(thisBlog)

    in html
        {% if blog in current_user.courses_completed %}
            
        {% else %}
            <form method=post>
                {{form.hidden_tag()}}
                <button style=" border:none; background-color:#2a7877; border-radius:15px; padding:0.5%; text-decoration:none;">
                    {{form.mark_completion(class='text-light',style="border:none; background-color:#2a7877;")}}
                </button>
            </form>
        {% endif %} 