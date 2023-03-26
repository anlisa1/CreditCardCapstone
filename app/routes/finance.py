
# Created, Read, Updated or Deleted (CRUD)

from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import User, total_Data, Module
from app.classes.forms import MarkasCompleteForm, verifyCourseForm, ModulesForm
from flask_login import login_required
import datetime as dt





@app.route('/module/list')
@app.route('/modules')
# This means the user must be logged in to see this page
def moduleList():
    all_modules = Module.objects()
    
    verified = total_Data.verified_courses
    courses_complete = current_user.courses.marked

    # if current_user.is_authenticated:
      # this fnction checks for if user is logged in without forcing them to login in!!
      
    return render_template('modules.html',modules=all_modules, verified_data = verified,  amount_complete = courses_complete)
    # italics, type on template

@app.route('/module/list')
@app.route('/verify')
def verifyList():
  all_modules = Module.objects()    
  verified = total_Data.verified_courses

  return render_template('verify_modules.html',modules=all_modules, verified_data = verified)
# if you have a form, you need a method, security issue
@app.route('/module/<moduleID>', methods=['GET', 'POST'])
# This route will only run if the user is logged in
@login_required
def module(moduleID):
    form = MarkasCompleteForm()
    admin_form = verifyCourseForm()
    
    thisModule = Module.objects.get(id=moduleID)
    if form.validate_on_submit():
        current_user.courses_completed.append(thisModule)
        
    if admin_form.validate_on_submit():
        total_Data.verified_courses.append(thisModule)
    
    verified = total_Data.verified_courses
    return render_template('module.html',module=thisModule,form=form, adminForm=admin_form, verifiedCourses = verified)
    #  whta the stuff after tghe hytml file, sending variables to form.

@app.route('/module/new', methods=['GET', 'POST'])

@login_required
def moduleNew():
  form = ModulesForm()
  if form.validate_on_submit():
    newModule = Module(
      author= current_user.id,
      title = form.title.data,
      content1 = form.content1.data,
      video1 =form.video1.data,
      content2 = form.content2.data,
      video2 =form.video2.data,
      content3= form.content3.data,
      video3 =form.video3.data,
      content4 = form.content4.data,
      # ask wright how to start with phtot
      # ask wright how to leave empty if there is photo
    )
    if form.cover_image.data:
        if newModule.cover_image:
          newModule.cover_image.delete()
        newModule.cover_image.put(form.cover_image.data, content_type = 'cover_image/jpeg')
          
        newModule.save()

    if form.image1.data:
      if form.image1:
        form.image1.delete()
      form.image1.put(form.image1.data, content_type = 'image1/jpeg')
      form.save()

    if form.image2.data:
      if newModule.image2:
        newModule.image2.delete()
      newModule.image2.put(form.image2.data, content_type = 'image2/jpeg')
        # This saves all the updates
      newModule.save()
    
    if form.image3.data:
      if newModule.image3:
        newModule.image3.delete()
      newModule.image4.put(form.image4.data, content_type = 'image3/jpeg')
        # This saves all the updates
      newModule.save()
    newModule.save()
    return redirect(url_for('module',moduleID=newModule.id))
  return render_template('moduleform.html',form=form)

@app.route('/module/delete/<moduleID>')
# Only run this route if the user is logged in.
@login_required
def moduleDelete(moduleID):
    deleteModule = Module.objects.get(id=moduleID)

    if current_user == deleteModule.author:
        if deleteModule in current_user.courses_marked:
            current_user.courses_marked.remove(deleteModule)
            total_Data.verified_courses.remove(deleteModule)
# dont forget method to delete all users with that course as marked done perhaps
        deleteModule.delete()
        flash('The Module was deleted.')
    else:
        flash("You can't delete a Module you don't own.")
    modules = Module.objects()  

    return render_template('modules.html',modules=modules)
          


@app.route('/module/edit/<moduleID>', methods=['GET', 'POST'])
@login_required
def moduleEdit(moduleID):
    editModule = Module.objects.get(id=moduleID)
    # if request edit, user is author then  go, if not go back,
    if current_user != editModule.author:
        flash("You can't edit a module you don't own.")
        return redirect(url_for('module',moduleID=moduleID))

    form = ModulesForm()
    # If the user has submitted the form then update the course
    if form.validate_on_submit():
      # update() is mongoengine method for updating an existing document with new data.
      editModule.update(
          title = form.title.data,
          content1 = form.content1.data,
          video1 =form.video1.data,
          content2 = form.content2.data,
          video2 =form.video2.data,
          content3= form.content3.data,
          video3 =form.video3.data,
          content4 = form.content4.data,
          modify_date = dt.datetime.utcnow,
      )
      if form.cover_image.data:
        if editModule.cover_image:
          editModule.cover_image.delete()
        editModule.cover_image.put(form.cover_image.data, content_type = 'image/jpeg')
          
        editModule.save()

      if form.image1.data:
        if editModule.image1:
          editModule.image1.delete()
        editModule.image1.put(form.image1.data, content_type = 'image/jpeg')
        editModule.save()

      if form.image2.data:
        if editModule.image2:
          editModule.image2.delete()
        editModule.image2.put(form.image2.data, content_type = 'image/jpeg')
          # This saves all the updates
        editModule.save()
      
      if form.image3.data:
        if editModule.image3:
          editModule.image3.delete()
        editModule.image4.put(form.image4.data, content_type = 'image/jpeg')
          # This saves all the updates
        editModule.save()
      # After updating the document, send the user to the updated blog using a redirect.
      return redirect(url_for('module',moduleID=moduleID))

    # if the form has NOT been submitted then take the data from the editBlog object
    # and place it in the form object so it will be displayed to the user on the template.
    form.title.data = editModule.title
    form.content1.data = editModule.content1
    form.video1.data = editModule.video1
    form.content2.data = editModule.content2
    form.video2.data = editModule.video2
    form.content3.data = editModule.content3
    form.video3.data = editModule.video3
    form.content4.data = editModule.content4
    # fom database, prepopulate the form


    # Send the user to the blog form that is now filled out with the current information
    # from the form.
    return render_template('moduleform.html',form=form)

