What does API even mean?
------------------------

This repo contains scripts run during the 'What does API even mean?' lightning talk.

Setup  (for Mac)
----------------

* Install pyenv_

..  _pyenv: https://github.com/pyenv/pyenv#installation

* Create and activate virtual environment

.. code:: bash

   pyenv virtualenv -p python3.7 3.7.0 whatapi
   pyenv activate whatapi

* Install requirements

.. code:: bash

   pip install -r requirements.txt

Run
---

* Execute below command replacing <script_name> as required

.. code:: bash

   python <script_name>

* In order to run tts.py you'll need to create an account on VoiceRSS
  and get an API key - you can do that here_. Once you have a key, run this command:

.. _here: http://www.voicerss.org/personel

.. code:: bash

   echo VOICE_RSS_API_KEY=<your_api_key_here> > .env
