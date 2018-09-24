author_screen
=============

This is a tiny library for screening author forms.

To install the library run

.. code-block:: bash

   pip install git+https://github.com/ihmeuw/author_screen.git

.. contents::
   :depth: 1
   :local:
   :backlinks: none

Screening author forms
----------------------

This library installs a command line tool called ``screen_forms`` that you
can run to screen your author forms. You can run it with

.. code-block:: bash

   screen_forms <options> form_directory

where ``form_directory`` is the directory containing the author forms you
wish to screen.

The AuthorForm class
--------------------

This class is a programmatic representation of an author form. You can use
this directly to develop new screening criteria or to debug.

.. code-block:: python

   from author_screen import AuthorForm

   a = AuthorForm('/path/to/author/form.pdf')
   print(a)

.. code-block:: python

   AuthorForm(title=Global, regional, and national age-sex-specific mortality for 282 causes of death, 1980
   2017: a systematic analysis for the Global Burden of Disease Study 2017
              author=Gregory A. Roth
              article_type=Article
              reference_number=THELANCET-D-18-02005
              editor=Elizabeth Zuccala
              contributions=Contributions for each individual author are described in the methods appendix.
              conflicts=Funding provided by the Bill & Melinda Gates Foundation Grant OPP1152504. The funder of the study had no role in study design; collection, analysis, and interpretation of data; or writing of the report. The correspondina and had responsibility for final submission of the manuscript.
              signatory_1=Signatory(name='Dr. Molly R. Nixon', degree='PhD', signature=True, date='18.08.08')
              signatory_2=Signatory(name='', degree='', signature=False, date='')
              signatory_3=Signatory(name='', degree='', signature=False, date='')
              signatory_4=Signatory(name='', degree='', signature=False, date='')
              signatory_5=Signatory(name='', degree='', signature=False, date='')
              signatory_6=Signatory(name='', degree='', signature=False, date='')
              signatory_7=Signatory(name='', degree='', signature=False, date='')
              signatory_8=Signatory(name='', degree='', signature=False, date='')
              signatory_9=Signatory(name='', degree='', signature=False, date='')
              signatory_10=Signatory(name='', degree='', signature=False, date='')




Development instructions
------------------------

If you need to be able to edit this code for development, you can install
it in an editable mode from source. First use ``git`` to clone the repository,
then use pip to install.

.. code-block:: bash

   git clone https://github.com/ihmeuw/author_screen.git
   cd author_screen
   pip install -e .

You should then be able to run the code including whatever changes you make.
