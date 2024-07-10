# Basic-Form
To deploy on OCP:  
 - oc new-app python:3.8~https://github.com/leocvidal/Basic-Form --allow-missing-images
 - oc expose svc/basic-form
