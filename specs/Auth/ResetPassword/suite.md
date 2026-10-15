---
name: Auth Reset Password
id: suite-auth-reset-password
description: Spec e2e turunan tc-reset-password.md untuk Auth > Reset Password
executionOrder: 5.0
parallel: false
---

# Suite: Auth Reset Password

Suite ini mencakup halaman Request Reset (web dan Android), validasi Email dan reCAPTCHA, evaluasi status akun, cooldown 60 detik serta rate limit per email dan per IP, halaman Email Sent! dan Resend, validasi tautan token (masa berlaku 24 jam, 404 Expired dan Already Used), Setup New Password (Password Policy, validasi, penolakan server), Submit sukses beserta efek turunannya (pemulihan lock, sesi berakhir, refresh token biometric), pencatatan Activity Log Session dan User Log, serta ketahanan terhadap kegagalan server, defense-in-depth, dan konkurensi.

`parallel: false` karena spec rate limit per IP, geser jam server, fixture counter, dan perubahan status atau email user di Global Settings memakai state global (counter per email dan per IP, jam server, lock akun). Setiap spec tetap menyiapkan datanya sendiri lewat hook dan tidak bergantung pada spec lain.

Hook `beforeEach` suite me-reset counter rate limit per IP penguji (batas 20 Request per jam, `RSTPWD-LOGIC-04d`) sebelum tiap spec, karena spec dalam suite ini mengirim lebih dari 20 Request dari IP yang sama. Spec yang menguji counter itu sendiri (014, 015, 043) mengaturnya setelah reset dan menuliskannya di `## Prerequisites`. Mekanisme reset (fixture BE atau skrip uji) tidak didefinisikan di TC, PRD, maupun LLD dan disediakan tim FE/BE.
