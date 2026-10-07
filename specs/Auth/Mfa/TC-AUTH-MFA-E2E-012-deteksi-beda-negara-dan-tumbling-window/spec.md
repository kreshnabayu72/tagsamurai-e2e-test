---
id: TC-AUTH-MFA-E2E-012-deteksi-beda-negara-dan-tumbling-window
title: "Deteksi Beda Negara, Pembentukan Trusted Country Pair, dan Tumbling Window 90 Hari"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-35
  - TC-AUTH-MFA-36
  - TC-AUTH-MFA-37
  - TC-AUTH-MFA-38
  - TC-AUTH-MFA-39
  - TC-AUTH-MFA-40
coverage:
  web: automated
---
# Deteksi Beda Negara, Pembentukan Trusted Country Pair, dan Tumbling Window 90 Hari

## Prerequisites

- Browser uji A (device dikenali) dan browser uji B (device baru).
- User `Irfan Maulana` (`irfanmaulana@qwertysystem.net`) profil XC (login terakhir Batam ID, login sekarang Singapura SG <100 km, pasangan ID-SG belum trusted).
- User `Sekar Ayu` (`sekarayu@qwertysystem.net`) profil XCT (pasangan ID-SG sudah trusted).
- User `Yoga Pranata` (`yogapranata@qwertysystem.net`) profil XCT (pasangan ID-SG trusted, login dari device baru).
- User `Mega Safitri` (`megasafitri@qwertysystem.net`) profil XCTF (pasangan ID-SG trusted, login dari Jakarta ke Singapura >100 km).
- User `Taufik Hidayat` (`taufikhidayat@qwertysystem.net`) profil XC (pasangan ID-SG dengan 2 login sukses sebelumnya).
- User `Anisa Fitriani` (`anisafitriani@qwertysystem.net`) profil XC (window pasangan negara >90 hari).
- Lingkungan uji dengan IP Batam (ID) dan Singapura (SG) serta mail-catcher aktif.

## Test Steps

### Deteksi beda negara walau jarak <100 km (Batam ke Singapura)

1. Buka browser uji A pada halaman login dengan kredensial `irfanmaulana@qwertysystem.net`
2. Konfigurasikan request dari IP Singapura (SG) (login terakhir dari Batam ID, jarak ~25 km <100 km)
3. Klik button [Log in]
4. Verifikasi sistem mendeteksi perbedaan kode negara ISO (ID ≠ SG) pada pasangan yang belum trusted
5. Verifikasi halaman Choose Verification Method tampil dan email alert unusual login terkirim

### Pasangan negara trusted membebaskan pengecekan negara

6. Login menggunakan user `sekarayu@qwertysystem.net` (pasangan ID-SG sudah trusted) dari IP Singapura
7. Verifikasi login langsung berhasil menuju Portal — Product Hub (single-step) tanpa memicu MFA dan tanpa email alert

### Pasangan negara trusted tidak membebaskan device baru dan jarak >100 km

8. Buka browser uji B (device baru) dan login dengan user `yogapranata@qwertysystem.net` dari IP Singapura
9. Verifikasi MFA tetap terpicu dan email alert terkirim karena device baru dievaluasi independen dari status pasangan negara
10. Buka browser uji A dan login dengan user `megasafitri@qwertysystem.net` dari IP Singapura (login terakhir dari Jakarta, jarak >100 km)
11. Verifikasi MFA tetap terpicu dan email alert terkirim karena jarak >100 km tetap dievaluasi independen

### Pembentukan pasangan trusted pada MFA ke-3 dan kelulusan perpindahan ke-4

12. Gunakan user `taufikhidayat@qwertysystem.net` yang telah memiliki 2 login MFA sukses pada pasangan ID-SG dalam 90 hari
13. Lakukan login ke-3 dari Singapura, selesaikan verifikasi faktor-2 MFA hingga mendarat di Portal — Product Hub
14. Verifikasi hitungan pasangan ID-SG kini mencapai 3 sehingga pasangan negara berstatus Trusted
15. Lakukan logout, lalu login ke-4 dari Batam (ID) menggunakan browser yang sama
16. Verifikasi login ke-4 langsung berakhir single-step ke Portal — Product Hub tanpa memicu MFA

### Reset tumbling window 90 hari pada pasangan yang belum trusted

17. Gunakan akun `anisafitriani@qwertysystem.net` yang memiliki 1 kemunculan pasangan negara berumur 91 hari lalu
18. Lakukan login baru melintasi pasangan negara tersebut
19. Verifikasi window 90 hari telah terlewati sehingga hitungan di-reset ke 1 (window baru dimulai) dan login tetap memicu MFA

## Notes

- Sesuai `AUTHMFA-LOGIC-02d` dan F-AUTHMFA-08, pasangan negara menjadi trusted setelah mencapai hitungan ≥3 dalam satu tumbling window 90 hari.
- Pasangan negara trusted hanya mengabaikan perbedaan negara; faktor anomali device baru dan jarak >100 km tetap dievaluasi terpisah.
