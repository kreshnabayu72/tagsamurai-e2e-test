---
id: TC-AUTH-SES-E2E-059-pencatatan-biometric
title: "Pencatatan Biometric Re-login Sukses, Biometric via MFA, dan Continue tanpa Centang Agreement"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-209
  - TC-AUTH-SES-210
  - TC-AUTH-SES-267
coverage:
  web: automated
  mobile: automated
---

# Pencatatan Biometric Re-login Sukses, Biometric via MFA, dan Continue tanpa Centang Agreement

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user milik Client Alpha Logistik (Tabel Data Uji Pre-setup #5 dan #9: Activated, Active ON), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-209: `Siti Damayanti` (`sitidamayanti+{runId}-059@qwertysystem.net`), profil BIO (Tabel Data Uji Pre-setup #9) yang sudah enroll biometric di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric dan sidik jari terdaftar di OS); tidak ada sesi platform aktif di perangkat itu
  - TC-AUTH-SES-210: `Andi Rahayu` (`andirahayu+{runId}-059@qwertysystem.net`), profil BIOMFA (Tabel Data Uji Pre-setup #23: profil BIO yang MFA-nya terpicu bila logout terakhir lebih dari 30 hari lalu; kondisi itu belum berlaku saat seeding dan enrollment, dan baru diterapkan di langkah 13); sudah enroll biometric di perangkat Android uji B; Authenticator terdaftar dan secret-nya dimuat ke aplikasi authenticator uji (TOTP); tidak ada sesi platform aktif di perangkat itu
  - TC-AUTH-SES-267: `Tari Rahayu` (`tarirahayu+{runId}-059@qwertysystem.net`), profil BIOPOL (Tabel Data Uji Pre-setup #22: profil BIO yang terkena kondisi BIOPOL bila versi Privacy Policy lebih baru dari yang disetujui; kondisi itu belum berlaku saat seeding dan enrollment, dan baru diterapkan di langkah 30) yang sudah enroll biometric di perangkat Android uji B; tidak ada sesi platform aktif di perangkat itu
- Konteks dan akun (dibuka di hook `before`, login pertama tiap konteks ada di hook): Browser Admin dengan akun aktor Total Control (Global Settings) di atas, dipakai membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`; perangkat Android uji B dengan aplikasi mobile TAG Samurai.
- Hook `after`: akhiri semua sesi seed (mobile), cabut kredensial biometric seed, tutup konteks Browser Admin, hapus ketiga user, dan bersihkan token biometric lokal di perangkat B. Pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); state global yang diubah: perangkat fisik Android uji B dipakai bersama (data aplikasi dan token biometric lokal), dipulihkan di hook `after`.
- Kemampuan teknis: driver otomasi Android (aplikasi native) pada perangkat Android uji B; simulasi verifikasi sidik jari yang terdaftar pada OS biometric prompt (sukses); perangkat B dipakai bergantian oleh ketiga user sehingga tiap TC memulai dari aplikasi tanpa sesi platform aktif dan dengan token biometric lokal milik user TC itu; aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) untuk Andi Rahayu; API yang disediakan tim FE/BE untuk mengakhiri sesi platform hasil login enroll tanpa menghapus token biometric lokal (Tabel Data Uji Pre-setup #29); kemampuan yang disediakan tim FE/BE untuk menerapkan kondisi MFA terpicu dan kondisi BIOPOL pada user yang sudah enroll; pembacaan stempel waktu entri log untuk membedakan entri baru dari entri seeding.
- Akun yang dipakai: user uji masing-masing TC di perangkat Android uji B (bukan akun aktor); akun aktor di Browser Admin.
- Kondisi "sudah enroll biometric di perangkat Android uji B" dan "token biometric lokal" per user disiapkan lewat alur Prompt Enable Biometric (login, [Enable], lulus verifikasi sidik jari; TC-AUTH-SES-14; Tabel Data Uji Pre-setup #29) pada langkah penghubung `siapkan enrollment`, karena token biometric lokal dan email cache lokal disimpan per perangkat dan perangkat B dipakai bergantian oleh ketiga user. Sesi platform hasil login enroll diakhiri lewat API yang disediakan tim FE/BE (tanpa menghapus token biometric lokal, bukan lewat Log Out di UI). Kondisi MFA terpicu saat biometric re-login `Andi Rahayu` (logout terakhir lebih dari 30 hari lalu, Tabel Data Uji Pre-setup #23) dan kondisi BIOPOL `Tari Rahayu` (versi Privacy Policy lebih baru dari yang terakhir disetujui, Tabel Data Uji Pre-setup #22) diterapkan sesudah enrollment masing-masing, pada langkah penghubung 13 dan 30, lewat kemampuan yang disediakan tim FE/BE.

## Test Steps

### TC-AUTH-SES-209: Pencatatan Biometric Re-login sukses

1. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu siapkan enrollment `sitidamayanti+{runId}-059@qwertysystem.net` sebagai user yang sudah enroll biometric di perangkat (token biometric lokal dan email cache lokal = email itu; Tabel Data Uji Pre-setup #29) tanpa sesi platform aktif
2. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
3. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub
4. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Siti Damayanti` yang dibuat sesudah langkah 2 dimulai
5. Verifikasi Entri baru tampil di `Global Settings > Activity Log > Session`: Activity `Login`, Status `Success`, Note `Login with biometric`
6. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > Activity Log > Session`
7. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
8. Buka `Global Settings > User > Detail > User Log` milik `Siti Damayanti` dan cari entri yang dibuat sesudah langkah 2 dimulai
9. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Login`, Status `Success`, Note `Login with biometric`
10. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
11. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-210: Pencatatan Biometric Re-login via MFA dicatat setelah MFA tuntas

12. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu siapkan enrollment `andirahayu+{runId}-059@qwertysystem.net` sebagai user yang sudah enroll biometric di perangkat (token biometric lokal dan email cache lokal = email itu; Tabel Data Uji Pre-setup #29) tanpa sesi platform aktif
13. Terapkan kondisi MFA terpicu pada `Andi Rahayu` (logout terakhir lebih dari 30 hari lalu; Tabel Data Uji Pre-setup #23) lewat kemampuan yang disediakan tim FE/BE
14. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
15. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app diarahkan ke halaman MFA
16. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Andi Rahayu` yang dibuat sesudah langkah 14 dimulai (sebelum kode TOTP dikirim)
17. Verifikasi Belum ada entri `Login with biometric` baru untuk `Andi Rahayu` di `Global Settings > Activity Log > Session` sebelum MFA tuntas
18. Buka `Global Settings > User > Detail > User Log` milik `Andi Rahayu` dan cari entri yang dibuat sesudah langkah 14 dimulai (sebelum kode TOTP dikirim)
19. Verifikasi Belum ada entri `Login with biometric` baru di `Global Settings > User > Detail > User Log` sebelum MFA tuntas
20. Pindah ke perangkat Android uji B, ketik kode TOTP yang benar dari aplikasi authenticator uji pada halaman MFA → app masuk Portal — Product Hub
21. Pindah ke Browser Admin, muat ulang `Global Settings > Activity Log > Session`, dan cari entri untuk `Andi Rahayu` yang dibuat sesudah langkah 14 dimulai
22. Verifikasi Entri baru tampil di `Global Settings > Activity Log > Session`: Activity `Login`, Status `Success`, Note `Login with biometric`
23. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > Activity Log > Session`
24. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
25. Buka `Global Settings > User > Detail > User Log` milik `Andi Rahayu` dan cari entri yang dibuat sesudah langkah 14 dimulai
26. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Login`, Status `Success`, Note `Login with biometric`
27. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
28. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-267: Pencatatan Continue tanpa centang Agreement pada Biometric Re-login

29. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu siapkan enrollment `tarirahayu+{runId}-059@qwertysystem.net` sebagai user yang sudah enroll biometric di perangkat (token biometric lokal dan email cache lokal = email itu; Tabel Data Uji Pre-setup #29) tanpa sesi platform aktif
30. Terapkan kondisi BIOPOL pada `Tari Rahayu` (versi Privacy Policy lebih baru dari yang terakhir disetujui; Tabel Data Uji Pre-setup #22) lewat kemampuan yang disediakan tim FE/BE
31. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
32. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → Screen Confirm to Continue tampil
33. Ketuk [Continue ➔] tanpa mencentang checkbox
34. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Tari Rahayu` yang dibuat sesudah langkah 31 dimulai
35. Verifikasi Entri baru tampil di `Global Settings > Activity Log > Session`: Activity `Login`, Status `Failed`, Note `Consent not given`
36. Buka `Global Settings > User > Detail > User Log` milik `Tari Rahayu` dan cari entri yang dibuat sesudah langkah 31 dimulai
37. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Login`, Status `Failed`, Note `Consent not given`
38. Pindah ke perangkat Android uji B, centang checkbox persetujuan pada Screen Confirm to Continue, lalu ketuk [Continue ➔]
39. Verifikasi Token pra-autentikasi tetap valid: Continue dengan centang berhasil dan app masuk Portal — Product Hub

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: pencatatan (Status/Note spesifik) dibaca lewat akun aktor di Browser Admin, dengan perangkat Android dan simulasi biometrik (harness eksternal). Asersi absence ada di spec `TC-AUTH-SES-E2E-060-absence-pencatatan-sesi` dan `TC-AUTH-SES-E2E-070-absence-biometric`; TC-AUTH-SES-212 (Biometric Enroll dan Disable tidak dicatat, sepenuhnya absence) ada di spec 070. Asersi "belum ada entri sebelum MFA tuntas" pada TC-AUTH-SES-210 (langkah 17 dan 19) adalah asersi urutan waktu dari TC pencatatan itu sendiri, bukan absence kelas g. TC-AUTH-SES-267 adalah TC campuran: asersi presence (entri `Consent not given`, Status `Failed`) dan Post Condition token pra-autentikasi.
- Urutan mengikuti TC sumber (209, 210, 267). Tiap TC memakai user sendiri, jadi urutan tidak membuat TC saling bergantung.
- Langkah dependensi disalin (S-04): TC-AUTH-SES-209 dari TC-AUTH-SES-152 (langkah 2–3, precondition enroll di-seed); TC-AUTH-SES-210 dari TC-AUTH-SES-161 (langkah 14–15 dan 20, dengan pengecekan log disisipkan sebelum kode TOTP sesuai Langkah Uji TC); TC-AUTH-SES-267 dari TC-AUTH-SES-164 (langkah 31–33). Asersi hasil dependensi (Portal, screen biometric, Screen Confirm to Continue) diuji di spec pemilik TC dependensi.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): memuat aplikasi ke keadaan awal TC (langkah 1, 12, 29), menerapkan kondisi MFA terpicu dan kondisi BIOPOL sesudah enrollment (langkah 13 dan 30), mencentang checkbox lalu Continue (langkah 38) dan perpindahan antar perangkat B dan Browser Admin. Entri "baru" dibedakan dari entri seeding lewat stempel waktu: hanya entri yang dibuat sesudah langkah pembuka TC itu yang dihitung.
- Temuan untuk QA:
  - TC-AUTH-SES-267 Expected butir b ("Continue berikutnya dengan centang berhasil") tidak disebut di Langkah Uji; spec menambah langkah 38 sesudah asersi log (S-14) supaya asersi log tidak tercampur entri `Login with biometric` yang ditulis oleh Continue yang berhasil.
  - Kolom "User" pada Expected butir b TC-AUTH-SES-209 dan 210 tidak ada di surface User Log (PRD §8 surface #3); spec mengasersi kolom User hanya di `Global Settings > Activity Log > Session`.
  - TC-AUTH-SES-210 Expected tidak menyebut layar yang tampil setelah biometric sukses; spec menulis "halaman MFA" mengikuti TC-AUTH-SES-161 Expected butir a.
  - Pembaca log tidak menyebut klien akun aktor; spec mengasumsikan akun aktor dapat membaca log user Client Alpha Logistik.
- Temuan untuk QA (lanjutan): TC-AUTH-SES-209 dan 210 menyebut "token biometric lokal" dan "sudah enroll biometric" tanpa langkah penyiapan; spec memakai cara penyiapan dari Tabel Data Uji Pre-setup #29 sebagai langkah penghubung (S-15). Untuk TC-AUTH-SES-210 enrollment (langkah 12) dan kondisi MFA terpicu pada re-login (langkah 13) berjalan berurutan; cara menerapkan kondisi MFA setelah enrollment tidak ditulis di TC dan disediakan tim FE/BE.
- Temuan untuk QA (TC-AUTH-SES-267): TC memakai token biometric lokal per user pada satu perangkat; spec memakai cara penyiapan Tabel Data Uji Pre-setup #29. Kemampuan menerapkan versi Privacy Policy lebih baru sesudah enrollment `Tari Rahayu` (Pre-setup #22; langkah 30) disediakan tim FE/BE; cara penerapannya tidak ditulis di TC.
