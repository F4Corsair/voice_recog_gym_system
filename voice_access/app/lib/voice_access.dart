import 'package:app/pages/register_user_page.dart';
import 'package:app/pages/voice_login_page.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class VoiceAccess extends StatelessWidget {
  VoiceAccess({super.key});
  // 라우터(페이지) 설정
  final GoRouter _router = GoRouter(routes: [
    GoRoute(path: "/", builder: (context, state) => VoiceLoginPage()),
    GoRoute(
        path: "/register-user", builder: (context, state) => RegisterUserPage())
  ]);
  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      routerConfig: _router,
      theme: ThemeData(
        scaffoldBackgroundColor: Colors.transparent, // Scaffold 기본 배경 투명화
      ),
      builder: (context, child) {
        return Container(
          width: double.infinity,
          decoration: const BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: [Colors.blue, Colors.purple], // 원하는 색상 지정
            ),
          ),
          child: child,
        );
      },
    );
  }
}
