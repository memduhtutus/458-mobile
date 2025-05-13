import 'package:flutter/material.dart';

class Condition {
  final int questionIndex;
  final String operator;
  final dynamic value;

  Condition({
    required this.questionIndex,
    required this.operator,
    required this.value,
  });
}

class Question {
  final String type;
  final String text;
  final List<String>? options;
  final Map<String, bool>? selectedOptions;
  final String? selectedRadio;
  final int? rating;
  final String? selectedDropdown;
  final Condition? condition;

  Question({
    required this.type,
    required this.text,
    this.options,
    this.selectedOptions,
    this.selectedRadio,
    this.rating,
    this.selectedDropdown,
    this.condition,
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
  bool _isConditional = false;
  int? _selectedConditionQuestion;
  String _selectedOperator = 'equals';
  String _selectedConditionValue = '';

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
            condition: _isConditional && _selectedConditionQuestion != null
                ? Condition(
                    questionIndex: _selectedConditionQuestion!,
                    operator: _selectedOperator,
                    value: _selectedConditionValue,
                  )
                : null,
          ),
        );
        _questionController.clear();
        _currentOptions.clear();
        _isConditional = false;
        _selectedConditionQuestion = null;
        _selectedConditionValue = '';
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

  Widget _buildConditionalUI() {
    if (!_isConditional || _questions.isEmpty) return const SizedBox.shrink();

    return Card(
      margin: const EdgeInsets.only(top: 16),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              'Conditional Logic',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 16),
            DropdownButton<int>(
              value: _selectedConditionQuestion,
              hint: const Text('Select previous question'),
              items: _questions.asMap().entries.map((entry) {
                return DropdownMenuItem<int>(
                  value: entry.key,
                  child: Text('${entry.key + 1}. ${entry.value.text}'),
                );
              }).toList(),
              onChanged: (value) {
                setState(() {
                  _selectedConditionQuestion = value;
                });
              },
            ),
            const SizedBox(height: 16),
            DropdownButton<String>(
              value: _selectedOperator,
              items: const [
                DropdownMenuItem(value: 'equals', child: Text('Equals')),
                DropdownMenuItem(
                    value: 'not_equals', child: Text('Not Equals')),
                DropdownMenuItem(value: 'contains', child: Text('Contains')),
                DropdownMenuItem(
                    value: 'greater_than', child: Text('Greater Than')),
                DropdownMenuItem(value: 'less_than', child: Text('Less Than')),
              ],
              onChanged: (value) {
                setState(() {
                  _selectedOperator = value!;
                });
              },
            ),
            const SizedBox(height: 16),
            if (_selectedConditionQuestion != null)
              TextField(
                decoration: const InputDecoration(
                  labelText: 'Condition Value',
                  border: OutlineInputBorder(),
                ),
                onChanged: (value) {
                  setState(() {
                    _selectedConditionValue = value;
                  });
                },
              ),
          ],
        ),
      ),
    );
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
                      key: Key('survey_preview_title'),
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

                            // Check if question should be shown based on conditions
                            if (question.condition != null) {
                              final condition = question.condition!;
                              final previousQuestion =
                                  _questions[condition.questionIndex];
                              bool shouldShow = false;

                              switch (previousQuestion.type) {
                                case 'checkbox':
                                  final selectedOptions =
                                      checkboxStates[condition.questionIndex] ??
                                          {};
                                  shouldShow =
                                      selectedOptions[condition.value] ?? false;
                                  break;
                                case 'radio':
                                  shouldShow =
                                      (radioStates[condition.questionIndex] ??
                                              '') ==
                                          condition.value;
                                  break;
                                case 'rating':
                                  final rating =
                                      ratingStates[condition.questionIndex] ??
                                          0;
                                  final compareValue =
                                      int.tryParse(condition.value) ?? 0;
                                  switch (condition.operator) {
                                    case 'equals':
                                      shouldShow = rating == compareValue;
                                      break;
                                    case 'not_equals':
                                      shouldShow = rating != compareValue;
                                      break;
                                    case 'greater_than':
                                      shouldShow = rating > compareValue;
                                      break;
                                    case 'less_than':
                                      shouldShow = rating < compareValue;
                                      break;
                                    default:
                                      shouldShow = false;
                                  }
                                  break;
                                case 'dropdown':
                                  shouldShow = (dropdownStates[
                                              condition.questionIndex] ??
                                          '') ==
                                      condition.value;
                                  break;
                                case 'text':
                                  final text =
                                      dropdownStates[condition.questionIndex] ??
                                          '';
                                  switch (condition.operator) {
                                    case 'equals':
                                      shouldShow = text == condition.value;
                                      break;
                                    case 'not_equals':
                                      shouldShow = text != condition.value;
                                      break;
                                    case 'contains':
                                      shouldShow =
                                          text.contains(condition.value);
                                      break;
                                    default:
                                      shouldShow = false;
                                  }
                                  break;
                              }

                              if (!shouldShow) return const SizedBox.shrink();
                            }

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
                                    if (question.condition != null)
                                      Padding(
                                        padding: const EdgeInsets.only(top: 4),
                                        child: Text(
                                          'Shown when question ${question.condition!.questionIndex + 1} ${question.condition!.operator} ${question.condition!.value}',
                                          style: const TextStyle(
                                            fontSize: 12,
                                            color: Colors.grey,
                                          ),
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
                          key: const Key('close_dialog_button'),
                          onPressed: () => Navigator.of(context).pop(),
                          child: const Text('Close'),
                        ),
                        const SizedBox(width: 8),
                        ElevatedButton(
                          key: const Key('save_survey_dialog_button'),
                          onPressed: () {
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
            key: const Key('save_survey_button'),
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
                      key: const Key('question_type_dropdown'),
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
                      key: const Key('question_text_field'),
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
                              key: const Key('option_text_field'),
                              controller: _optionController,
                              decoration: const InputDecoration(
                                labelText: 'Option',
                                border: OutlineInputBorder(),
                              ),
                            ),
                          ),
                          IconButton(
                            key: const Key('add_option_button'),
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
                    CheckboxListTile(
                      title: const Text('Make this question conditional'),
                      value: _isConditional,
                      onChanged: (value) {
                        setState(() {
                          _isConditional = value ?? false;
                        });
                      },
                    ),
                    _buildConditionalUI(),
                    const SizedBox(height: 16),
                    ElevatedButton(
                      key: const Key('add_question_button'),
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
                              .contains(question.type) ||
                          question.condition != null,
                      subtitle: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text('Type: ${question.type}'),
                          if (question.condition != null)
                            Text(
                              'Condition: Question ${question.condition!.questionIndex + 1} ${question.condition!.operator} ${question.condition!.value}',
                              style: const TextStyle(color: Colors.grey),
                            ),
                          if (['checkbox', 'radio', 'dropdown']
                              .contains(question.type))
                            Wrap(
                              spacing: 8,
                              children: question.options!.map((option) {
                                return Chip(label: Text(option));
                              }).toList(),
                            ),
                        ],
                      ),
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
