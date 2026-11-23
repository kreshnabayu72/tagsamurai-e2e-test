---
id: TC-AUTH-SES-E2E-006-screening-biometric-mobile
title: "Screening Layar Biometric di Aplikasi Mobile"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-14
  - TC-AUTH-SES-15
  - TC-AUTH-SES-16
coverage:
  mobile: automated
---

# Screening Layar Biometric di Aplikasi Mobile

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) pada perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric dan minimal 1 sidik jari terdaftar di OS), terpasang di perangkat atau emulator uji. Tiga TC memakai perangkat yang sama secara berurutan.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: user Activated, Active ON), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-14: `Putri Rahayu` (`putrirahayu+{runId}-006@qwertysystem.net`), profil BIO (Tabel Data Uji Pre-setup #9) yang belum pernah enroll biometric
  - TC-AUTH-SES-15: `Eko Anggraini` (`ekoanggraini+{runId}-006@qwertysystem.net`), profil BIO; sudah enroll biometric di perangkat Android uji B dan tanpa sesi platform aktif (email cache lokal = email user ini) lewat langkah 10-17
  - TC-AUTH-SES-16: `Wulan Wibowo` (`wulanwibowo+{runId}-006@qwertysystem.net`), profil BIOPOL (Tabel Data Uji Pre-setup #22): sudah enroll biometric dan tanpa sesi platform aktif lewat langkah 26-33; Privacy Policy versi lebih baru dipublish sesudah enroll (langkah 34), sehingga user belum menyetujui versi terbaru
- Privacy Policy: ketiga user di-seed menyetujui versi yang berlaku saat `before`, dan tidak ada versi baru yang dipublish di `before`, sehingga profil BIO TC-AUTH-SES-14 dan 15 tidak memicu Agreement (Tabel Data Uji Pre-setup #9). Versi baru dipublish hanya di langkah 34 (sebelum layar TC-AUTH-SES-16) oleh akun aktor `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` (Principal staff Admin Console, Tabel Data Uji Pre-setup #4), kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`, dan versi awal dipulihkan oleh akun yang sama di `after`.
- Kondisi state aplikasi di perangkat (enroll biometric per user dan email cache lokal) disiapkan oleh langkah penghubung di `## Test Steps` sebelum TC-AUTH-SES-15 dan 16 mengikuti Tabel Data Uji Pre-setup #29 (login, [Enable], lulus verifikasi sidik jari, lalu sesi platform hasil login enroll diakhiri lewat API yang disediakan tim BE tanpa menghapus token biometric lokal), karena satu perangkat hanya menyimpan satu email cache lokal.
- Hook `after`: akhiri semua sesi uji, hapus data aplikasi mobile di perangkat Android uji B (cache email lokal dan binding biometric), pulihkan versi Privacy Policy ke kondisi awal (oleh akun aktor Principal), hapus ketiga user. Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`); state global yang diubah: versi Privacy Policy yang dipublish sebelum TC-AUTH-SES-16, binding biometric di perangkat uji, dan perangkat fisik bersama (Android uji B), dipulihkan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: driver otomasi Android (aplikasi native) dengan kemampuan menutup paksa aplikasi dan menghapus data aplikasi; simulasi biometrik OS (sidik jari terdaftar, OS biometric prompt dapat dilulusi dan dibaca keberadaannya); pembacaan layar blocking full-screen, tautan, dan checkbox pada aplikasi; API yang disediakan tim BE untuk mengakhiri sesi platform user hasil login enroll tanpa menghapus token biometric lokal (Tabel Data Uji Pre-setup #29); klien HTTP untuk mempublish dan memulihkan versi Privacy Policy oleh akun aktor Principal.
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada aplikasi mobile di perangkat Android uji B.

## Test Steps

### TC-AUTH-SES-14: Screening Prompt Enable Biometric setelah login pertama sukses di mobile

1. Buka aplikasi mobile di perangkat Android uji B → halaman Login tampil
2. Login dengan `putrirahayu+{runId}-006@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD` → Prompt muncul
3. Susuri prompt dari atas ke bawah
4. Verifikasi **Header**: Title "Enable biometric sign-in?"
5. Verifikasi **Header**: Prompt modal mobile
6. Verifikasi **Header**: Prompt dapat ditutup
7. Verifikasi **Body**: Body "Sign in faster next time without typing your password"
8. Verifikasi **Footer**: [Enable] (variant solid, severity primary)
9. Verifikasi **Footer**: [Not now] (variant text, severity contrast)

### TC-AUTH-SES-15: Screening Screen Sign in with biometrics saat app dibuka tanpa sesi

10. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu buka aplikasi mobile → halaman Login tampil
11. Ketik `ekoanggraini+{runId}-006@qwertysystem.net` pada field Email
12. Ketik `Spectra.env.SES_PASSWORD` pada field Password
13. Ketuk [Login] → Prompt Enable Biometric muncul
14. Ketuk [Enable] → OS biometric prompt muncul
15. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub (email cache lokal = email itu)
16. Akhiri sesi platform `ekoanggraini+{runId}-006@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal (Tabel Data Uji Pre-setup #29)
17. Hapus app dari recent apps
18. Buka aplikasi mobile di perangkat Android uji B → layar tampil
19. Susuri layar dari atas ke bawah sebelum menyentuh sensor
20. Verifikasi **Header**: Logo aplikasi di bagian atas
21. Verifikasi **Body**: Title "Sign in with biometrics"
22. Verifikasi **Body**: Body "Sign in as ekoanggraini+{runId}-006@qwertysystem.net"
23. Verifikasi **Body**: OS biometric prompt tampil otomatis (hanya biometric; tanpa opsi passcode perangkat)
24. Verifikasi **Footer**: Layar blocking full-screen menggantikan form Login
25. Verifikasi [Try Again] dan tautan "Sign in with password instead" belum tampil sebelum ada kegagalan

### TC-AUTH-SES-16: Screening Screen Confirm to Continue pada Biometric Re-login saat Agreement terpicu

26. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu buka aplikasi mobile → halaman Login tampil
27. Ketik `wulanwibowo+{runId}-006@qwertysystem.net` pada field Email
28. Ketik `Spectra.env.SES_PASSWORD` pada field Password
29. Ketuk [Login] → Prompt Enable Biometric muncul
30. Ketuk [Enable] → OS biometric prompt muncul
31. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub (email cache lokal = email itu)
32. Akhiri sesi platform `wulanwibowo+{runId}-006@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal (Tabel Data Uji Pre-setup #29)
33. Hapus app dari recent apps
34. Publish versi Privacy Policy yang lebih baru lewat API oleh akun aktor Principal `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #4), sehingga `wulanwibowo+{runId}-006@qwertysystem.net` belum menyetujui versi terbaru
35. Buka aplikasi mobile di perangkat Android uji B dan lulus OS biometric prompt → layar tampil
36. Susuri layar dari atas ke bawah
37. Verifikasi **Header**: Layar blocking full-screen
38. Verifikasi **Header**: Title "Confirm to Continue"
39. Verifikasi **Header**: Body "By accessing TAG Samurai, you agree to comply with our Privacy Policy. Please read the full document before continuing. Your continued use of the platform means you accept the terms described in the Privacy Policy."
40. Verifikasi **Header**: Tautan "Read the full Privacy Policy" tampil pada Body
41. Verifikasi **Body**: checkbox "I have read and agree to the Privacy Policy *" (default tidak dicentang)
42. Verifikasi **Body**: Label checkbox "I have read and agree to the Privacy Policy *" bukan tautan
43. Verifikasi **Footer**: button [Continue ➔]
44. Verifikasi Tidak ada tombol Cancel atau Back

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (hardware biometrik) dan mobile.
- Urutan mengikuti TC sumber: TC-AUTH-SES-14, 15, lalu 16; tidak ada penyimpangan (S-05, S-10). Tiap TC memakai user sendiri.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah 10-17 dan 26-33 (tutup paksa aplikasi, hapus data aplikasi, enroll biometric dan email cache lokal user TC berikutnya menurut Tabel Data Uji Pre-setup #29, akhiri sesi platform lewat API tim BE, hapus app dari recent apps); langkah 34 (publish versi Privacy Policy yang lebih baru sesudah enroll Wulan, agar tidak memicu Agreement pada user TC-AUTH-SES-14 dan 15); menyusuri prompt dan layar tanpa menyentuh sensor atau tombol. Blok enroll berpola (langkah 10-17 dan 26-33) tidak dihitung ke batas sekitar 35 langkah.
- Asersi pencatatan (Enable Biometric, Biometric Re-login, Agreement di Activity Log > Session dan User Log) tidak diasersikan di spec ini; pencatatan diuji di spec pencatatan dan absence modul ini (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-15 dan 16 menyebut "sudah enroll biometric" dan "app ditutup paksa sebelumnya" tanpa langkah penyiapan, sementara satu perangkat Android uji B dipakai tiga user berurutan dan hanya menyimpan satu email cache lokal; cara menyiapkan mengikuti Tabel Data Uji Pre-setup #29 (langkah 10-17 dan 26-33). TC-AUTH-SES-16 tidak menyebut kapan versi Privacy Policy yang lebih baru dipublish; spec mempublishnya sesudah enroll (langkah 34) agar login enroll tidak memicu Agreement. API pengakhiran sesi platform dan klien publish Privacy Policy disediakan tim FE/BE; TC, PRD, dan LLD tidak menyebut endpoint-nya, spec tidak mengarang endpoint (S-13). (2) TC-AUTH-SES-14 langkah 2 menyebut "password yang benar" tanpa nilai; spec memakai `Spectra.env.SES_PASSWORD`. (3) TC-AUTH-SES-16 Expected a menaruh Body "By accessing TAG Samurai..." di bawah **Header** i/ii dan checkbox di bawah **Body**; spec mengikuti pengelompokan itu apa adanya. (4) TC-AUTH-SES-14 tidak menyebut reCAPTCHA atau langkah masuk pada Login mobile; spec mengikuti TC.
