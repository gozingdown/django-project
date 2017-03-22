# django-project
==========================================================
Some notes on Session:
https://docs.djangoproject.com/en/1.10/topics/http/sessions/#using-sessions-out-of-views

You can access session via 
1. SessionStore 
2. Session model 
3. request.session in a view

[1] You can modiy a session like this: request.session['xx']='yy'

Note for this case, where Session is NOT modified, because this alters request.session['foo'] instead of request.session.

request.session['foo']['bar'] = 'baz'



[2] But you cannot modify session data via Session model. Unless you overwrite the session.session_data field, which is actually encoded.

If via Session model, you can only access session data via get_decoded().

[3] You can access (udpdate) session out side a view via SessionStore.
Access SessionStore as dict.


==========================================================
Some notes on Form and Field Validation
https://docs.djangoproject.com/en/1.10/ref/forms/validation/#form-and-field-validation

Field.to_python()
Field.validate()
Field.run_validators()
Field.clean()
Form.clean_<fieldname>()
FOrm.clean()

'These methods are run in the order given above, one field at a time. That is, for each field in the form (in the order they are declared in the form definition), the Field.clean() method (or its override) is run, then clean_<fieldname>(). Finally, once those two methods are run for every field, the Form.clean() method, or its override, is executed whether or not the previous methods have raised errors.'

'As mentioned, any of these methods can raise a ValidationError. For any field, if the Field.clean() method raises a ValidationError, any field-specific cleaning method is not called. However, the cleaning methods for all remaining fields are still executed.'


===========================================================
Some notes on Model Validation
There are three steps involved in validating a model:

1. Validate the model fields - Model.clean_fields()
2. Validate the model as a whole - Model.clean()
3. Validate the field uniqueness - Model.validate_unique()

All three steps are performed when you call a model’s full_clean() method.


===========================================================
Some notes on ModelForm Validation

There are two main steps involved in validating a ModelForm:

1. Validating the form
2. Validating the model instance

Just like normal form validation, model form validation is triggered implicitly when calling is_valid() or accessing the errors attribute and explicitly when calling full_clean(), although you will typically not use the latter method in practice.

Model validation (Model.full_clean()) is triggered from within the form validation step, right after the form’s clean() method is called.

