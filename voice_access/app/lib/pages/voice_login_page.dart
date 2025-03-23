import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:go_router/go_router.dart';

class VoiceLoginPage extends StatefulWidget {
  const VoiceLoginPage({super.key});

  @override
  State<VoiceLoginPage> createState() => _VoiceLoginPageState();
}

class _VoiceLoginPageState extends State<VoiceLoginPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.transparent, // 전역 LinearGradient 유지
      appBar: AppBar(
        title: Text(
          "음성로그인 페이지",
          style: GoogleFonts.notoSans(
              fontSize: 24, color: Colors.white, fontWeight: FontWeight.w500),
        ),
        backgroundColor: Colors.transparent,
      ),
      body: Center(
        child: SizedBox(
          width: double.infinity,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              ElevatedButton(
                onPressed: () {},
                child: const Icon(
                  Icons.mic,
                  size: 150,
                ),
              ),
              const SizedBox(height: 30),
              Text(
                "음성출입을 위해 녹음 버튼을 눌러주세요",
                style: GoogleFonts.notoSans(
                    fontSize: 18,
                    color: Colors.white,
                    fontWeight: FontWeight.w500),
              ),
              const SizedBox(height: 20),
              TextButton(
                onPressed: () {
                  context.go("/register-user");
                },
                child: Text(
                  '회원등록',
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
