# Suitcase Cookiecutter

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for creating
a suitcase subpackage.

A suitcase subpackage translates between the bluesky document model and a file
format. This includes:

* exporting from documents to files (potentially lossy)
* ingesting files into documents (lossless)
* "reflecting" files into an in-memory representation as documents, on demand
  (lossless)
* reading externally-written data to deference pointers in Events --- a.k.a. 
  databroker's "handlers"

Each suitcase subpackage should do these things for a particular file
format/layout. Some parameterization is possible, but if two given file layouts
are substantially different, they should be handled by different subpackages.
For example, there will not be a generic "HDF5" or "ASCII file" suitcase
subpackage, but rather specialized subpackages for NeXuS, CSV, SPEC files, etc.

The subpackages should implement a standard interface, which is sketched out in
code comments in this template.

## Use the template to create package

Install cookiecutter.

```
pip install cookiecutter
```

Use cookiecutter to generate a package, following the prompts to fill in the
name and authorship of your new suitcase subpackage.

```
cookiecutter https://github.com/NSLS-II/suitcase-cookiecutter
```

## Guidelines

* Suitcase supports Python 3.6+ only.
* Suitcase subpackages should include tests but they should *not* include binary
  files for testing. The tests should generate (and then clean up) any files
  that they need for testing.
