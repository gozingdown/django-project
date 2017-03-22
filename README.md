# django-project
==========================================================
Some notes on Session:
https://docs.djangoproject.com/en/1.10/topics/http/sessions/#using-sessions-out-of-views

You can access session via 
1. SessionStore 
2. Session model 
3. request.session in a view

But you cannot modify session data via Session model. Unless you overwrite the session.session_data field, which is actually encoded.
If via Session model, you can only access session data via get_decoded().


You can access (udpdate) session out side a view via SessionStore.
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
