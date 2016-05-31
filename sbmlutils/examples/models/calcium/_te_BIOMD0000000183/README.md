
        # Tellurium 1.3.3 experiment
        This COMBINE archive stores an tellurium experiment.
        http://tellurium.analogmachine.org/

        ## Run Experiment
        To reproduce the experiment and to create the figures and data run
        ```
        import tellurium as te
        omexPath = 'BIOMD0000000183.sedx'
        te.executeSEDML(omexPath)
        ```
        in tellurium, with `omexPath` the path to this archive file.
        