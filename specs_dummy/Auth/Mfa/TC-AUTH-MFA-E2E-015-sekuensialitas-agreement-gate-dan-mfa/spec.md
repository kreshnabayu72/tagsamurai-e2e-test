---
id: TC-AUTH-MFA-E2E-015-sekuensialitas-agreement-gate-dan-mfa
title: "Sekuensialitas Agreement Gate Sebelum Evaluasi MFA dan Deteksi Platform Kedua"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-47
  - TC-AUTH-MFA-48
  - TC-AUTH-MFA-49
coverage:
  web: automated
---
# Sekuensialitas Agreement Gate Sebelum Evaluasi MFA dan Deteksi Platform Kedua

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- Perangkat mobile TAG Samurai Android.
- User `Indah Permata` (`indahpermata@qwertysystem.net`) profil AGR (belum menyetujui Terms & Conditions / Privacy Policy terbaru).
- User `Kiki Fatmala` (`kikifatmala@qwertysystem.net`) profil PLAT2 (sudah pernah login sukses di Web, belum pernah di Mobile).
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Agreement Gate harus disetujui sebelum evaluasi MFA berlangsung

1. Buka halaman login di browser dengan kredensial `indahpermata@qwertysystem.net`
2. Klik [Log in]
3. Verifikasi halaman berpindah ke `Agreement Gate` (bukan ke halaman MFA)
4. Setujui dokumen perjanjian pada Agreement Gate lalu klik [Continue]
5. Verifikasi sistem melanjutkan ke evaluasi MFA dan menampilkan halaman `Auth > MFA > Choose Verification Method`

### Penolakan Agreement Gate membatalkan alur tanpa mengevaluasi MFA

6. Lakukan login ulang dengan akun lain yang memiliki pending agreement
7. Pada halaman Agreement Gate, tolak perjanjian / klik [Cancel]
8. Verifikasi browser kembali ke halaman `/login` dan evaluasi MFA tidak pernah dijalankan

### Login pertama kali di platform kedua diperlakukan sebagai Device Baru

9. Gunakan akun `kikifatmala@qwertysystem.net` yang sudah aktif di platform Web
10. Buka aplikasi mobile TAG Samurai Android dan login dengan akun tersebut
11. Verifikasi sesuai keputusan NC-04, sistem memperlakukan login ini sebagai login dari Device Baru (bukan first login):
    - Halaman MFA wajib tampil
    - Email alert unusual login terkirim ke kotak masuk pengguna

## Notes

- Sesuai `auth-foundation.md` §3.1, Agreement Gate memiliki urutan prioritas di atas evaluasi MFA.
- Sesuai keputusan NC-04, `first_login_at` berlaku per user global; login perdana di platform kedua dihitung sebagai device baru sehingga menghasilkan email alert.
