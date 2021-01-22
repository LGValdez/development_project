
# Development Projects

Odoo Module to Handle Development Projects

Initial specifications

1. Uses **Projects** module as base.

2. Adds the following permission groups.
    * **Admin.** It can see all tickets and all custom fields. It can edit all fields.
    * **Admin assistant.** It can see all tickets and all custom fields, but it cannot edit any of the new, custom fields.
    * **Developer.** It can only see tickets assigned or if it's included in the the new custom field *Developer*. It cannot edit custom fields. It cannot see fields *Estimated total hours*, *Estimated expense* and *Estimated income*.

3. Adds the following custom fields.
    * **Developer:** This will be a developer who is not primarily responsible for a ticket but who will develop work for it.  This field may have several developers.
    * **Priority:** Select field with a 1-10 scale.
    * **Bonus:** Amount to be recived if requirement is delivered before bonus deadline.
    * **Bonus deadline:** Deadline to complete work and receive a bonus.
    * **Estimated total hours:** Development hours expected to complete the task.
    * **Estimated expense:** Amount expected for development to cost.
    * **Estimated income:** Amount expected for the client to pay.
