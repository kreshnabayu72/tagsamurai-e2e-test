---
id: TC-AUTH-MFA-E2E-013-decay-pasangan-negara-dan-single-step-refresh
title: "Decay 180 Hari Pasangan Negara Trusted dan Pembaruan Waktu via Login Single-Step"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-41
  - TC-AUTH-MFA-42
  - TC-AUTH-MFA-43
  - TC-AUTH-MFA-44
coverage:
  web: automated
---
# Decay 180 Hari Pasangan Negara Trusted dan Pembaruan Waktu via Login Single-Step

## Prerequisites

- Browser uji A (device dikenali).
- User `Reza Alamsyah` (`rezaalamsyah@qwertysystem.net`) profil XCT (pasangan ID-SG terakhir terlihat 181 hari lalu).
- User `Lia Wulandari` (`liawulandari@qwertysystem.net`) profil XCT (pasangan ID-SG terakhir terlihat 179 hari lalu).
- User `Hari Purnomo` (`haripurnomo@qwertysystem.net`) profil XCT (pasangan ID-SG trusted, window 90 hari sudah terlewati).
- User `Vina Melati` (`vinamelati@qwertysystem.net`) profil XCT (pasangan ID-SG trusted).
- Lingkungan uji dengan kemampuan manipulasi waktu server dan mail-catcher aktif.

## Test Steps

### Gugurnya trust pasangan negara setelah tidak aktif >180 hari (Decay)

1. Buka browser uji A pada halaman login dengan akun `rezaalamsyah@qwertysystem.net`
2. Simulasikan login dari IP Singapura (SG) setelah pasangan negara tidak terlihat selama 181 hari
3. Klik [Log in]
4. Verifikasi status trusted pasangan negara ID-SG dinyatakan gugur oleh evaluasi decay
5. Verifikasi sistem memicu MFA (halaman Choose Verification Method tampil) dan mengirimkan email alert
6. Verifikasi hitungan pasangan negara dimulai ulang dari 1

### Pasangan negara yang terlihat pada hari ke-179 tetap berstatus Trusted

7. Buka browser uji A pada halaman login dengan akun `liawulandari@qwertysystem.net`
8. Simulasikan login dari IP Singapura setelah pasangan negara terakhir terlihat 179 hari lalu (<180 hari)
9. Klik [Log in]
10. Verifikasi status trusted pasangan negara ID-SG masih berlaku sah
11. Verifikasi login langsung berakhir single-step ke Portal — Product Hub tanpa memicu MFA dan tanpa email alert

### Lewatnya tumbling window 90 hari tidak mencabut status pasangan yang sudah trusted

12. Login dengan user `haripurnomo@qwertysystem.net` yang pasangan negaranya telah trusted sejak 120 hari lalu (window 90 hari terlewati, namun belum mencapai decay 180 hari)
13. Verifikasi status Trusted tetap bertahan dan login berjalan single-step ke Portal — Product Hub

### Login single-step memperbarui waktu terakhir terlihat pasangan negara

14. Login dengan user `vinamelati@qwertysystem.net` yang memiliki pasangan trusted ID-SG pada hari ke-150 sejak login pertama
15. Verifikasi login berjalan single-step
16. Verifikasi timestamp `last_seen_at` untuk pasangan negara ID-SG diperbarui ke waktu saat ini
17. Simulasikan lompatan waktu 60 hari ke depan (total 210 hari dari awal, tetapi hanya 60 hari dari pembaruan login single-step terakhir)
18. Lakukan login kembali dan verifikasi login tetap single-step karena trust tidak gugur berkat pembaruan berkala

## Notes

- Sesuai `AUTHMFA-LOGIC-02d` dan keputusan NC-02, evaluasi decay (180 hari) bersifat lazy pada saat login berikutnya.
- Login single-step yang berhasil membuat sesi memperbarui waktu terlihat pasangan negara sehingga pola mobilitas yang aktif tidak gugur.
