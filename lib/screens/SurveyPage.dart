import 'package:flutter/material.dart';
import '../components/AiModelForm.dart';

class SurveyPage extends StatefulWidget {
  const SurveyPage({super.key});

  @override
  State<SurveyPage> createState() => _SurveyPageState();
}

class _SurveyPageState extends State<SurveyPage> {
  final _formKey = GlobalKey<FormState>();
  final _nameController = TextEditingController();
  final _surnameController = TextEditingController();
  String _selectedEducation = 'High School';
  double _sliderValue = 0.0;

  // List to store selected AI models
  final List<String> _selectedAIModels = [];

  final List<String> _educationLevels = [
    'High School',
    'Bachelor\'s Degree',
    'Master\'s Degree',
    'PhD',
    'Other'
  ];

  final List<String> _aiModels = [
    'ChatGPT',
    'Claude',
    'Gemini',
    'Copilot',
    'Other'
  ];

  @override
  void dispose() {
    _nameController.dispose();
    _surnameController.dispose();
    super.dispose();
  }

  void _submitForm() {
    if (_formKey.currentState!.validate()) {
      print('Name: ${_nameController.text}');
      print('Surname: ${_surnameController.text}');
      print('Education: $_selectedEducation');
      print('Selected AI Models:');
      for (var model in _selectedAIModels) {
        print('- $model');
      }
    }
  }

  void _addNewAIModel(String? value) {
    if (value != null && value.isNotEmpty) {
      setState(() {
        _selectedAIModels.add(value);
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('User Survey'),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              TextFormField(
                controller: _nameController,
                decoration: const InputDecoration(
                  labelText: 'Name',
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter your name';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              TextFormField(
                controller: _surnameController,
                decoration: const InputDecoration(
                  labelText: 'Surname',
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter your surname';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              DropdownButtonFormField<String>(
                value: _selectedEducation,
                decoration: const InputDecoration(
                  labelText: 'Education Level',
                  border: OutlineInputBorder(),
                ),
                items: _educationLevels.map((String level) {
                  return DropdownMenuItem<String>(
                    value: level,
                    child: Text(level),
                  );
                }).toList(),
                onChanged: (String? newValue) {
                  setState(() {
                    _selectedEducation = newValue!;
                  });
                },
              ),
              const SizedBox(height: 24),
              const Text(
                'Define your gender',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Row(
                children: [
                  const Text(
                    'Woman',
                    style: TextStyle(fontSize: 14),
                  ),
                  Expanded(
                    child: Slider(
                      value: _sliderValue,
                      min: -100,
                      max: 100,
                      divisions: 200,
                      label: _sliderValue.round().toString(),
                      onChanged: (double value) {
                        setState(() {
                          _sliderValue = value;
                        });
                      },
                    ),
                  ),
                  const Text(
                    'Man',
                    style: TextStyle(fontSize: 14),
                  ),
                ],
              ),
              Text(
                _sliderValue == 0
                    ? 'You are nonbinary'
                    : _sliderValue > 0
                        ? 'You are ${(_sliderValue).round()}% man'
                        : 'You are ${(_sliderValue.abs()).round()}% woman',
                textAlign: TextAlign.center,
                style: const TextStyle(fontSize: 16),
              ),
              const SizedBox(height: 24),
              const Text(
                'Which AI models do you use?',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 8),
              // Show selected AI models
              ..._selectedAIModels.map((model) => Padding(
                    padding: const EdgeInsets.only(bottom: 8.0),
                    child: AiModelForm(
                      modelName: model,
                      onChange: (value) {
                        // Handle the defects/cons text change
                        setState(() {
                          // You might want to store these values in a map or list
                          // For now, we'll just print it
                          print('Defects for $model: $value');
                        });
                      },
                      onDelete: () {
                        setState(() {
                          _selectedAIModels.remove(model);
                        });
                      },
                    ),
                  )),
              // Add new dropdown for AI model selection
              DropdownButtonFormField<String>(
                decoration: const InputDecoration(
                  labelText: 'Select AI Model',
                  border: OutlineInputBorder(),
                ),
                items: _aiModels.map((String model) {
                  return DropdownMenuItem<String>(
                    value: model,
                    child: Text(model),
                  );
                }).toList(),
                onChanged: _addNewAIModel,
              ),
              const SizedBox(height: 24),
              ElevatedButton(
                onPressed: _submitForm,
                style: ElevatedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 16),
                ),
                child: const Text(
                  'Submit Survey',
                  style: TextStyle(fontSize: 16),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
