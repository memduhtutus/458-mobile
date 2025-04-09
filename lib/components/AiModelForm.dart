import 'package:flutter/material.dart';

class AiModelForm extends StatefulWidget {
  final String modelName;
  final Function(String) onChange;
  final VoidCallback onDelete;
  final Function(String)? onModelNameChange;

  const AiModelForm({
    Key? key,
    required this.modelName,
    required this.onChange,
    required this.onDelete,
    this.onModelNameChange,
  }) : super(key: key);

  @override
  State<AiModelForm> createState() => _AiModelFormState();
}

class _AiModelFormState extends State<AiModelForm> {
  final TextEditingController _modelNameController = TextEditingController();

  @override
  void dispose() {
    _modelNameController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final bool isOther = widget.modelName == 'Other';

    return Card(
      margin: const EdgeInsets.symmetric(vertical: 8.0, horizontal: 16.0),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                if (!isOther)
                  Text(
                    widget.modelName,
                    style: const TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  )
                else
                  const SizedBox.shrink(),
                IconButton(
                  icon: const Icon(Icons.close),
                  onPressed: widget.onDelete,
                  color: Colors.red,
                ),
              ],
            ),
            if (isOther) ...[
              const SizedBox(height: 16),
              TextField(
                controller: _modelNameController,
                decoration: const InputDecoration(
                  labelText: 'Model Name',
                  hintText: 'Enter the name of the AI model...',
                  border: OutlineInputBorder(),
                ),
                onChanged: widget.onModelNameChange,
              ),
            ],
            const SizedBox(height: 16),
            TextField(
              decoration: const InputDecoration(
                labelText: 'Defects or Cons',
                hintText: 'Enter the defects or cons of this model...',
                border: OutlineInputBorder(),
              ),
              maxLines: 3,
              onChanged: widget.onChange,
            ),
          ],
        ),
      ),
    );
  }
}
