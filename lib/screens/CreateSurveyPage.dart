import 'package:flutter/material.dart';

class Question {
  final String type;
  final String text;
  final List<String>? options;
  final Map<String, bool>? selectedOptions;
  final String? selectedRadio;
  final int? rating;
  final String? selectedDropdown;

  Question({
    required this.type,
    required this.text,
    this.options,
    this.selectedOptions,
    this.selectedRadio,
    this.rating,
    this.selectedDropdown,
  });
}

class CreateSurveyPage extends StatefulWidget {
  const CreateSurveyPage({super.key});

  @override
  State<CreateSurveyPage> createState() => _CreateSurveyPageState();
}

class _CreateSurveyPageState extends State<CreateSurveyPage> {
  final List<Question> _questions = [];
  final _formKey = GlobalKey<FormState>();
  final _questionController = TextEditingController();
  final _optionController = TextEditingController();
  String _selectedQuestionType = 'text';
  List<String> _currentOptions = [];

  @override
  void dispose() {
    _questionController.dispose();
    _optionController.dispose();
    super.dispose();
  }

  void _addQuestion() {
    if (_questionController.text.isNotEmpty) {
      setState(() {
        _questions.add(
          Question(
            type: _selectedQuestionType,
            text: _questionController.text,
            options: ['text', 'checkbox', 'radio', 'dropdown']
                    .contains(_selectedQuestionType)
                ? List.from(_currentOptions)
                : null,
            selectedOptions: _selectedQuestionType == 'checkbox' ? {} : null,
            selectedRadio: _selectedQuestionType == 'radio' ? null : null,
            rating: _selectedQuestionType == 'rating' ? 0 : null,
            selectedDropdown: _selectedQuestionType == 'dropdown' ? null : null,
          ),
        );
        _questionController.clear();
        _currentOptions.clear();
      });
    }
  }

  void _addOption() {
    if (_optionController.text.isNotEmpty) {
      setState(() {
        _currentOptions.add(_optionController.text);
        _optionController.clear();
      });
    }
  }

  void _saveSurvey() {
    if (_questions.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
            content: Text('Please add at least one question to the survey')),
      );
      return;
    }

    // Create maps to store states
    Map<int, Map<String, bool>> checkboxStates = {};
    Map<int, String> radioStates = {};
    Map<int, int> ratingStates = {};
    Map<int, String> dropdownStates = {};

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return StatefulBuilder(
          builder: (BuildContext context, StateSetter setState) {
            return Dialog(
              child: Container(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    const Text(
                      'Survey Preview',
                      style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.bold,
                      ),
                      textAlign: TextAlign.center,
                    ),
                    const SizedBox(height: 16),
                    Flexible(
                      child: SingleChildScrollView(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.stretch,
                          children: _questions.asMap().entries.map((entry) {
                            final index = entry.key;
                            final question = entry.value;
                            return Card(
                              margin: const EdgeInsets.only(bottom: 16),
                              child: Padding(
                                padding: const EdgeInsets.all(16.0),
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(
                                      '${index + 1}. ${question.text}',
                                      style: const TextStyle(
                                        fontSize: 16,
                                        fontWeight: FontWeight.bold,
                                      ),
                                    ),
                                    const SizedBox(height: 8),
                                    if (question.type == 'text')
                                      TextField(
                                        decoration: const InputDecoration(
                                          border: OutlineInputBorder(),
                                          hintText: 'Enter your answer',
                                        ),
                                      )
                                    else if (question.type == 'checkbox' &&
                                        question.options != null)
                                      Column(
                                        children:
                                            question.options!.map((option) {
                                          if (!checkboxStates
                                              .containsKey(index)) {
                                            checkboxStates[index] = {};
                                          }
                                          if (!checkboxStates[index]!
                                              .containsKey(option)) {
                                            checkboxStates[index]![option] =
                                                false;
                                          }

                                          return CheckboxListTile(
                                            title: Text(option),
                                            value:
                                                checkboxStates[index]![option],
                                            onChanged: (bool? value) {
                                              setState(() {
                                                checkboxStates[index]![option] =
                                                    value ?? false;
                                              });
                                            },
                                          );
                                        }).toList(),
                                      )
                                    else if (question.type == 'radio' &&
                                        question.options != null)
                                      Column(
                                        children:
                                            question.options!.map((option) {
                                          if (!radioStates.containsKey(index)) {
                                            radioStates[index] = '';
                                          }

                                          return RadioListTile<String>(
                                            title: Text(option),
                                            value: option,
                                            groupValue: radioStates[index],
                                            onChanged: (String? value) {
                                              setState(() {
                                                radioStates[index] =
                                                    value ?? '';
                                              });
                                            },
                                          );
                                        }).toList(),
                                      )
                                    else if (question.type == 'rating')
                                      Row(
                                        mainAxisAlignment:
                                            MainAxisAlignment.center,
                                        children: List.generate(5, (starIndex) {
                                          if (!ratingStates
                                              .containsKey(index)) {
                                            ratingStates[index] = 0;
                                          }

                                          return IconButton(
                                            icon: Icon(
                                              starIndex <
                                                      (ratingStates[index] ?? 0)
                                                  ? Icons.star
                                                  : Icons.star_border,
                                              color: Colors.amber,
                                            ),
                                            onPressed: () {
                                              setState(() {
                                                ratingStates[index] =
                                                    starIndex + 1;
                                              });
                                            },
                                          );
                                        }),
                                      )
                                    else if (question.type == 'dropdown' &&
                                        question.options != null)
                                      DropdownButtonFormField<String>(
                                        decoration: const InputDecoration(
                                          border: OutlineInputBorder(),
                                          contentPadding: EdgeInsets.symmetric(
                                              horizontal: 16, vertical: 8),
                                        ),
                                        hint: const Text('Select an option'),
                                        value: dropdownStates[index],
                                        items: question.options!.map((option) {
                                          return DropdownMenuItem<String>(
                                            value: option,
                                            child: Text(option),
                                          );
                                        }).toList(),
                                        onChanged: (String? value) {
                                          setState(() {
                                            dropdownStates[index] = value ?? '';
                                          });
                                        },
                                      ),
                                  ],
                                ),
                              ),
                            );
                          }).toList(),
                        ),
                      ),
                    ),
                    const SizedBox(height: 16),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.end,
                      children: [
                        TextButton(
                          onPressed: () => Navigator.of(context).pop(),
                          child: const Text('Close'),
                        ),
                        const SizedBox(width: 8),
                        ElevatedButton(
                          onPressed: () {
                            // TODO: Implement actual survey saving logic
                            Navigator.of(context).pop();
                            ScaffoldMessenger.of(context).showSnackBar(
                              const SnackBar(
                                  content: Text('Survey saved successfully!')),
                            );
                          },
                          child: const Text('Save Survey'),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            );
          },
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Create Survey'),
        actions: [
          IconButton(
            icon: const Icon(Icons.save),
            onPressed: _saveSurvey,
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Card(
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    DropdownButton<String>(
                      value: _selectedQuestionType,
                      items: const [
                        DropdownMenuItem(
                            value: 'text', child: Text('Text Question')),
                        DropdownMenuItem(
                            value: 'checkbox',
                            child: Text('Checkbox Question')),
                        DropdownMenuItem(
                            value: 'radio', child: Text('Radio Question')),
                        DropdownMenuItem(
                            value: 'rating', child: Text('Rating Question')),
                        DropdownMenuItem(
                            value: 'dropdown',
                            child: Text('Dropdown Question')),
                      ],
                      onChanged: (value) {
                        setState(() {
                          _selectedQuestionType = value!;
                          _currentOptions.clear();
                        });
                      },
                    ),
                    const SizedBox(height: 16),
                    TextField(
                      controller: _questionController,
                      decoration: const InputDecoration(
                        labelText: 'Question Text',
                        border: OutlineInputBorder(),
                      ),
                    ),
                    if (['checkbox', 'radio', 'dropdown']
                        .contains(_selectedQuestionType)) ...[
                      const SizedBox(height: 16),
                      Row(
                        children: [
                          Expanded(
                            child: TextField(
                              controller: _optionController,
                              decoration: const InputDecoration(
                                labelText: 'Option',
                                border: OutlineInputBorder(),
                              ),
                            ),
                          ),
                          IconButton(
                            icon: const Icon(Icons.add),
                            onPressed: _addOption,
                          ),
                        ],
                      ),
                      if (_currentOptions.isNotEmpty) ...[
                        const SizedBox(height: 8),
                        Wrap(
                          spacing: 8,
                          children: _currentOptions.map((option) {
                            return Chip(
                              label: Text(option),
                              onDeleted: () {
                                setState(() {
                                  _currentOptions.remove(option);
                                });
                              },
                            );
                          }).toList(),
                        ),
                      ],
                    ],
                    const SizedBox(height: 16),
                    ElevatedButton(
                      onPressed: _addQuestion,
                      child: const Text('Add Question'),
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 16),
            Expanded(
              child: ListView.builder(
                itemCount: _questions.length,
                itemBuilder: (context, index) {
                  final question = _questions[index];
                  return Card(
                    child: ListTile(
                      title: Text(question.text),
                      trailing: IconButton(
                        icon: const Icon(Icons.delete),
                        onPressed: () {
                          setState(() {
                            _questions.removeAt(index);
                          });
                        },
                      ),
                      isThreeLine: ['checkbox', 'radio', 'dropdown']
                          .contains(question.type),
                      subtitle: ['checkbox', 'radio', 'dropdown']
                              .contains(question.type)
                          ? Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text('Type: ${question.type}'),
                                Wrap(
                                  spacing: 8,
                                  children: question.options!.map((option) {
                                    return Chip(label: Text(option));
                                  }).toList(),
                                ),
                              ],
                            )
                          : Text('Type: ${question.type}'),
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
