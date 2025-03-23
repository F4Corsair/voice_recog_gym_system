import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:go_router/go_router.dart';

class RegisterUserPage extends StatefulWidget {
  const RegisterUserPage({super.key});

  @override
  State<RegisterUserPage> createState() => _RegisterUserPageState();
}

class _RegisterUserPageState extends State<RegisterUserPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.transparent, // 전역 LinearGradient 유지
      appBar: AppBar(
        title: Text(
          "회원등록 페이지",
          style: GoogleFonts.notoSans(
              fontSize: 24, color: Colors.white, fontWeight: FontWeight.w500),
        ),
        backgroundColor: Colors.transparent,
      ),
      // TODO: 회원가입 페이지에 맞게 변경(현재는 그냥 로그인페이지 복붙임)
      body: Center(
        child: SizedBox(
          width: double.infinity,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              TextButton(
                onPressed: () {
                  context.go("/");
                },
                child: Text(
                  '로그인페이지로 돌아가기',
                  style: GoogleFonts.notoSans(color: Colors.blue),
                ),
              ),
              TextButton(
                onPressed: () {},
                child: Text(
                  '전화번호로 로그인',
                  style: GoogleFonts.notoSans(color: Colors.grey),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
