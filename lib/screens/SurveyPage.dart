import 'package:flutter/material.dart';
import '../components/AiModelForm.dart';
import '../models/survey_form_data.dart';

class SurveyPage extends StatefulWidget {
  const SurveyPage({super.key});

  @override
  State<SurveyPage> createState() => _SurveyPageState();
}

class _SurveyPageState extends State<SurveyPage> {
  final _formKey = GlobalKey<FormState>();
  final _nameController = TextEditingController();
  final _surnameController = TextEditingController();
  final _dailyLifeBenefitsController = TextEditingController();
  String _selectedEducation = 'High School';
  double _sliderValue = 0.0;

  // List to store selected AI models
  final List<String> _selectedAIModels = [];

  final Map<String, String> _aiModelResponses = {};
  final Map<String, String> _customModelNames = {};

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

  String? _selectedDropdownValue; // new state variable for dropdown

  @override
  void dispose() {
    _nameController.dispose();
    _surnameController.dispose();
    _dailyLifeBenefitsController.dispose();
    super.dispose();
  }

  void _submitForm() {
    if (_formKey.currentState!.validate()) {
      final List<AIModelResponse> aiModelResponses =
          _selectedAIModels.map((model) {
        return AIModelResponse(
          modelName: model == 'Other'
              ? _customModelNames[model] ?? 'Unknown Model'
              : model,
          cons: _aiModelResponses[model] ?? '',
        );
      }).toList();

      final surveyData = SurveyFormData(
        name: _nameController.text,
        surname: _surnameController.text,
        educationLevel: _selectedEducation,
        gender: _sliderValue == 0
            ? 'You are nonbinary'
            : _sliderValue > 0
                ? 'You are ${(_sliderValue).round()}% man'
                : 'You are ${(_sliderValue.abs()).round()}% woman',
        genderValue: _sliderValue,
        selectedAIModels: aiModelResponses,
        dailyLifeBenefits: _dailyLifeBenefitsController.text,
      );

      // Print the formatted survey data
      print('\n${surveyData.toString()}');

      // TODO: Send the data to your backend or process it further
    }
  }

  void _updateCustomModelName(String model, String name) {
    setState(() {
      _customModelNames[model] = name;
    });
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
                        setState(() {
                          _aiModelResponses[model] = value;
                        });
                      },
                      onModelNameChange: model == 'Other'
                          ? (value) => _updateCustomModelName(model, value)
                          : null,
                      onDelete: () {
                        setState(() {
                          _selectedAIModels.remove(model);
                          _aiModelResponses.remove(model);
                          _customModelNames.remove(model);
                        });
                      },
                    ),
                  )),
              // Add new dropdown for AI model selection (always displaying "Select AI Model" as its hint)
              DropdownButtonFormField<String>(
                value: null, // always remain null to display the hint
                decoration: const InputDecoration(
                  labelText: 'Select AI Model',
                  border: OutlineInputBorder(),
                ),
                hint: const Text('Select AI Model'),
                items: _aiModels.map((String model) {
                  return DropdownMenuItem<String>(
                    value: model,
                    child: Text(model),
                  );
                }).toList(),
                onChanged: (value) {
                  if (value != null && value.isNotEmpty) {
                    setState(() {
                      // Do not update the dropdown value; just add the selected model
                      if (!_selectedAIModels.contains(value)) {
                        _selectedAIModels.add(value);
                        if (value == 'Other') {
                          _customModelNames[value] = '';
                        }
                      }
                    });
                  }
                },
              ),
              const SizedBox(height: 24),
              TextFormField(
                controller: _dailyLifeBenefitsController,
                maxLines: 4,
                decoration: const InputDecoration(
                  labelText:
                      'What are the daily life benefits of using AI models?',
                  border: OutlineInputBorder(),
                  hintText:
                      'Please describe how AI models benefit your daily life...',
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please share your thoughts on AI benefits';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 24),
              ElevatedButton(
                onPressed: _selectedAIModels.isEmpty ? null : _submitForm,
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
