class AIModelResponse {
  final String modelName;
  final String cons;

  AIModelResponse({
    required this.modelName,
    required this.cons,
  });

  Map<String, dynamic> toJson() {
    return {
      'modelName': modelName,
      'cons': cons,
    };
  }

  @override
  String toString() {
    return 'AI Model: $modelName\nCons: $cons';
  }
}

class SurveyFormData {
  final String name;
  final String surname;
  final String educationLevel;
  final String gender;
  final double genderValue;
  final List<AIModelResponse> selectedAIModels;
  final String dailyLifeBenefits;

  SurveyFormData({
    required this.name,
    required this.surname,
    required this.educationLevel,
    required this.gender,
    required this.genderValue,
    required this.selectedAIModels,
    required this.dailyLifeBenefits,
  });

  Map<String, dynamic> toJson() {
    return {
      'name': name,
      'surname': surname,
      'educationLevel': educationLevel,
      'genderValue': genderValue,
      'selectedAIModels':
          selectedAIModels.map((model) => model.toJson()).toList(),
      'dailyLifeBenefits': dailyLifeBenefits,
      'gender': gender,
    };
  }

  @override
  String toString() {
    final genderText = genderValue == 0
        ? 'Nonbinary'
        : genderValue > 0
            ? '${genderValue.round()}% Man'
            : '${genderValue.abs().round()}% Woman';

    final aiModelsText =
        selectedAIModels.map((model) => model.toString()).join('\n\n');

    return '''
Survey Response:
---------------
Name: $name
Surname: $surname
Education Level: $educationLevel
Gender: $genderText

Selected AI Models:
$aiModelsText

Daily Life Benefits:
$dailyLifeBenefits
''';
  }
}
