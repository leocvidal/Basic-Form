oc delete bc basic-form
oc delete deployment basic-form
oc delete service basic-form
#oc new-app python:3.8~https://github.com/leocvidal/Basic-Form
oc new-app https://github.com/leocvidal/Basic-Form
oc expose service/basic-form