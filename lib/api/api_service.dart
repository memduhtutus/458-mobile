import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/login_request.dart';
import '../models/survey_form_data.dart';

class ApiService {
  static const String baseUrl = 'http://127.0.0.1:5000';

  // Login method
  Future<Map<String, dynamic>> login(LoginRequest loginRequest) async {
    try {
      final response = await http.post(
        Uri.parse(baseUrl),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: {
          'username': loginRequest.email,
          'password': loginRequest.password,
        },
      );

      if (response.statusCode == 200) {
        return jsonDecode(response.body);
      } else {
        throw Exception('Failed to login: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Error during login: $e');
    }
  }

  // Submit survey method
  Future<void> submitSurvey(SurveyFormData surveyData, String token) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/survey'),
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer $token',
        },
        body: jsonEncode(surveyData.toJson()),
      );

      if (response.statusCode != 201) {
        throw Exception('Failed to submit survey: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Error submitting survey: $e');
    }
  }
}
