What does API even mean?
========================

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

* Run any of the .py files by replacing <script_name> as required

.. code:: bash

   python <script_name>

* e.g.

.. code:: bash

   python eighty_beers.py

Trump to speech
---------------

* In order to run trump_to_speech.py you'll need to create an account on VoiceRSS
  and get an API key - you can do that here_. Once you have a key, run this command:

.. _here: http://www.voicerss.org/personel

.. code:: bash

   echo VOICE_RSS_API_KEY=<your_api_key_here> > .env

Reference
---------

APIs used in this talk:

* `Brewdog Punk API <https://punkapi.com/documentation/v2>`_

* `Tronald Dump <https://www.tronalddump.io/>`_

* `Voice RSS <http://www.voicerss.org/tts/default.aspx>`_
