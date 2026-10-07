---
id: TC-AUTH-MFA-E2E-009-pemicu-mfa-idle-dan-independensi-platform
title: "Pemicu MFA Idle ≥30 Hari dan Evaluasi Independen Antara Web dan Mobile"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-26
  - TC-AUTH-MFA-27
  - TC-AUTH-MFA-28
  - TC-AUTH-MFA-29
coverage:
  web: automated
---
# Pemicu MFA Idle ≥30 Hari dan Evaluasi Independen Antara Web dan Mobile

## Prerequisites

- Browser uji A (device dikenali untuk user uji).
- User `Yusuf Maulana` (`yusufmaulana@qwertysystem.net`) profil IDLE (login terakhir di web 31 hari yang lalu dari lokasi Jakarta, saat ini login dari browser uji A di Jakarta).
- User `Tri Wahyuni` (`triwahyuni@qwertysystem.net`) profil IDLE_NEW (login terakhir 35 hari yang lalu di browser uji A, saat ini login dari browser uji B baru di Surabaya).
- User `Fajar Nugraha` (`fajarnugraha@qwertysystem.net`) profil DUAL (aktif setiap hari di web, namun idle >40 hari di mobile).
- Mail-catcher lingkungan uji aktif.

## Test Steps

### User idle ≥30 hari pada device dikenali dan lokasi sama memicu MFA tanpa alert

1. Buka browser uji A pada halaman login dengan kredensial `yusufmaulana@qwertysystem.net`
2. Klik [Log in]
3. Verifikasi sistem mendeteksi selisih hari sejak login terakhir adalah 31 hari (≥30 hari)
4. Verifikasi halaman `Auth > MFA > Choose Verification Method` tampil
5. Periksa kotak masuk mail-catcher untuk `yusufmaulana@qwertysystem.net`
6. Verifikasi TIDAK ADA email alert yang dikirimkan karena device dikenali dan lokasi sama (hanya idle)

### User idle ≥30 hari dari device baru / lokasi jauh memicu MFA dan email alert

7. Buka browser uji B (device baru) dengan IP Surabaya untuk user `triwahyuni@qwertysystem.net`
8. Masukkan password valid dan klik [Log in]
9. Verifikasi halaman Choose Verification Method tampil
10. Periksa kotak masuk mail-catcher untuk `triwahyuni@qwertysystem.net`
11. Verifikasi email alert unusual login terkirim (sesuai NC-03, kombinasi idle dan device baru tetap mengirim alert)

### Evaluasi idle per platform: Keaktifan di web tidak mereset idle di mobile

12. Amati riwayat user `fajarnugraha@qwertysystem.net` yang rutin login di Web namun tidak pernah membuka Mobile selama 40 hari
13. Buka aplikasi mobile TAG Samurai Android dan login dengan akun tersebut
14. Verifikasi aplikasi mobile memicu MFA karena status idle mobile dievaluasi independen dari keaktifan web

## Notes

- Sesuai `AUTHMFA-LOGIC-01a`, batas idle adalah 30 hari kalender.
- Sesuai keputusan NC-03, kriteria evaluasi anomali berjalan paralel; idle tidak menghapus email alert jika ada deteksi device baru atau lokasi jauh.
