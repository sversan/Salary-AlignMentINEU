How to use the code:
1.Install the necessary libraris
pip install flask, Flask, pandas, zip
2.It might come an error mesasage for the zip library even though is a default library in python.
we will need to add it to our function and fix the issue as per bellow:

 # Ensure zip is defined correctly in the template rendering context
    return render_template('index.html', countries=countries, salaries=salaries, colors=colors,**zip=zip**)
3.Run code :python.exe app.py
