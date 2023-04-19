
# Created, Read, Updated or Deleted (CRUD)

from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import User, Module
from app.classes.forms import ModulesForm
from flask_login import login_required
import datetime as dt


@app.route('/loginplease')
def loginplease():
  return render_template('../templates/notloggedin.html')

@app.route('/Modules')
# This means the user must be logged in to see this page
def moduleList():
  verified_modules = Module.objects(verified=True)
  
  modules =  Module.objects()
  return render_template('modules.html',verified_modules=verified_modules, modules=modules )
  # italics, type on template

@app.route('/verify')
def verifyList():
  if current_user.email=='s_anlisa.liu@ousd.org' or  current_user.email=='s_amy.tran@ousd.org':
    all_unverified_modules = Module.objects(verified=False)  
    modules =  Module.objects()  
    return render_template('verify_modules.html', unverified_modules = all_unverified_modules, modules=modules)
  else:
    return redirect(url_for('index'))
# if you have a form, you need a method, security issue

@app.route('/verifyModule/<moduleID>')
def verifyModule(moduleID):
  thisModule = Module.objects.get(id=moduleID)
  thisModule.update(
    verified = True
  )
  return redirect(url_for('module', moduleID=thisModule.id))

@app.route('/completeModule/<moduleID>')
def completeModule(moduleID):
  # thisModule = Module.objects.get(id=moduleID)
  currUser = User.objects.get(id=current_user.id)
  thisModule = Module.objects.get(id=moduleID)

  if current_user.is_authenticated:
    currUser.CompletedModules.append(thisModule)
    currUser.save()
    return redirect(url_for('module', moduleID=thisModule.id))
  else:
    return redirect(url_for('loginplease'))


@app.route('/module/<moduleID>', methods=['GET', 'POST'])
# This route will only run if the user is logged in
# you cannot do two validate on submits at a time, only first one will run.
def module(moduleID):
    thisModule = Module.objects.get(id=moduleID)

    return render_template('module.html',module=thisModule)
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
      image1size = form.image1size.data,
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
        newModule.cover_image.put(form.cover_image.data, content_type='image/jpeg')
        newModule.save()

    if form.image1.data:
      newModule.image1.put(form.image1.data, content_type='image/jpeg')
      newModule.save()

    if form.image2.data:
      newModule.image2.put(form.image2.data, content_type = 'image/jpeg')
        # This saves all the updates
      newModule.save()
    
    if form.image3.data:
      newModule.image3.put(form.image3.data, content_type = 'image/jpeg')
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
  all_users=User.objects()
  if current_user.email == "s_anlisa.liu@ousd.org" or  current_user.email == "s_amy.tran@ousd.org":
    for user in all_users:
      if deleteModule == user.CompletedModules:
        user.CompletedModules.remove(deleteModule)
        user.save()
    deleteModule.delete()
    flash('The Module was deleted.')
    all_unverified_modules = Module.objects(verified=False)    
    return render_template('verify_modules.html', unverified_modules = all_unverified_modules)
  else:
      flash("Only Admins can delete, why are you here?")
      return redirect(url_for('index'))

   
          


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
          image1size = form.image1size.data,
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
    form.image1size.data = editModule.image1size
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

