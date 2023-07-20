LogsParser is an opensource python library created by Wallix ( http://www.wallix.org ).
It is used as the core mechanism for logs tagging and normalization by Wallix's LogBox
( http://www.wallix.com/index.php/products/wallix-logbox ).

Logs come in a variety of formats. In order to parse many different types of
logs, a developer used to need to write an engine based on a large list of complex
regular expressions. It can become rapidly unreadable and unmaintainable.

By using LogsParser, a developer can free herself from the burden of writing a
log parsing engine, since the module comes in with "batteries included".
Furthermore, this engine relies upon XML definition files that can be loaded at
runtime. The definition files were designed to be easily readable and need very
little skill in programming or regular expressions, without sacrificing
powerfulness or expressiveness.

Purpose
:::::::

The LogsParser module uses normalization definition files in order to tag
log entries. The definition files are written in XML.

The definition files allow anyone with a basic understanding of regular
expressions and knowledge of a specific log format to create and maintain
a customized pool of parsers.

Basically a definition file will consist of a list of log patterns, each
composed of many keywords. A keyword is a placeholder for a notable and/or
variable part in the described log line, and therefore associated to a tag
name. It is paired to a tag type, e.g. a regular expression matching the
expected value to assign to this tag. If the raw value extracted this way needs
further processing, callback functions can be applied to this value.

This format also allows to add useful meta-data about parsed logs, such as
extensive documentation about expected log patterns and log samples.
