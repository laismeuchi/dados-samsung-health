# Email Data Processing

In this project, the idea was to use a data source that in some cases is the only way to ingest data that is not in any system or storage source: sending data by email.

In some projects I worked on, reading emails and their attachments was used as a solution to import this type, such as business rule parameters to be applied in processing that did not exist in any system. And generally, this was data that could be changed by the user at any time for reprocessing.

## Architecture

To simulate the scenario described previously, I created this project in which I export the data from my physical activities in the [Samsung Health] cell phone application (https://www.samsung.com/br/apps/samsung-health/) and send for my email.

The email is monitored by [Logic Apps](https://learn.microsoft.com/pt-br/azure/logic-apps/logic-apps-overview) which detects the email and sends the attachment to _storage_ in Azure.

This _storage_ has been registered on [Databricks](https://www.databricks.com/br) as an _external location_ and a _job_ is triggered when a new file is added to it.

The _job_ loads the _csv_ for the layers _bronze_, _silver_ and _gold_.
This way, the process was completely automated based on receipt of the email.

![image](https://github.com/user-attachments/assets/f860889c-f8d7-4a43-9d45-f056c298345f)


## Demonstration

I made this video to present the project live:

<div>
    <a href="https://www.loom.com/share/4f6bd833f2124609b722481f4c5bb378">
      <p>Samsung Health data analysis - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/4f6bd833f2124609b722481f4c5bb378">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/4f6bd833f2124609b722481f4c5bb378-f0c7c565dc0c883c-full-play.gif">
    </a>
  </div>

## Dashboard

With the _bronze_ data I made this simple panel in Databricks to present the results.

![image](https://github.com/user-attachments/assets/c470f403-5f30-41f4-bacf-9235b8447143)


## Source code

Here in this project is the code used in Databricks' _job_.
