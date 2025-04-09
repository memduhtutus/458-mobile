import 'package:flutter/material.dart';

class AiModelForm extends StatelessWidget {
  final String modelName;
  final Function(String) onChange;
  final VoidCallback onDelete;

  const AiModelForm({
    Key? key,
    required this.modelName,
    required this.onChange,
    required this.onDelete,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
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
                Text(
                  modelName,
                  style: const TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                IconButton(
                  icon: const Icon(Icons.close),
                  onPressed: onDelete,
                  color: Colors.red,
                ),
              ],
            ),
            const SizedBox(height: 16),
            TextField(
              decoration: const InputDecoration(
                labelText: 'Defects or Cons',
                hintText: 'Enter the defects or cons of this model...',
                border: OutlineInputBorder(),
              ),
              maxLines: 3,
              onChanged: onChange,
            ),
          ],
        ),
      ),
    );
  }
}
