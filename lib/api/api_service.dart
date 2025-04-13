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
  Future<Map<String, dynamic>> submitSurvey(SurveyFormData surveyData) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/survey'),
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode(surveyData.toJson()),
      );

      final responseData = jsonDecode(response.body);

      if (response.statusCode == 201) {
        return responseData;
      } else if (response.statusCode == 400) {
        throw Exception(responseData['error'] ?? 'Missing required fields');
      } else {
        throw Exception(responseData['message'] ??
            'Failed to submit survey: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Error submitting survey: $e');
    }
  }

  // Google authentication method
  Future<Map<String, dynamic>> authenticateWithGoogle() async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/auth/google'),
        headers: {
          'Content-Type': 'application/json',
        },
      );

      if (response.statusCode == 200) {
        return jsonDecode(response.body);
      } else {
        throw Exception(
            'Failed to authenticate with Google: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Error during Google authentication: $e');
    }
  }
}
