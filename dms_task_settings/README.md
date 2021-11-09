# AWS DMS JSON table mappings example.
Table mapping specifies rules that identify the schemas, tables, and views that your task migrates from the source endpoint and how they are migrated to the target endpoint.

Selection rules determine what schema, tables, and views you want to include (or exclude) for your migration task. You can specify multiple selection rules. At least one of them must contain an "include" action. AMS DMS processes the "exclude" actions after the "include" actions. You can use source filters to limit the number and type of records transferred from your source to your target.

Transformation rules can specify certain changes to schemas, tables, views, and columns of some or all of the objects included using the selection rules. Transformation rules can include expressions to specify fine-grained control of these changes.

Table-settings rules specify how your task loads the data for individual tables. For example, these rules can specify if and how specific tables are loaded using multithreading and what modes are used for migrating LOB data.
Additional table mapping rules are also available for specific endpoints.

## Links
- https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html#CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation
- https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html#CHAP_Tasks.CustomizingTasks.TaskSettings.Example

