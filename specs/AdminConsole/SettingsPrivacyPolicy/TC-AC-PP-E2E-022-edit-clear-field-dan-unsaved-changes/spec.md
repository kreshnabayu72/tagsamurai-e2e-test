---
id: TC-AC-PP-E2E-022-edit-clear-field-dan-unsaved-changes
title: "Edit: Clear Field dan Dialog Unsaved Changes pada Modal State Edit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-61
  - TC-AC-PP-62
  - TC-AC-PP-63
  - TC-AC-PP-65
  - TC-AC-PP-66
  - TC-AC-PP-72
coverage:
  web: automated
---

# Edit: Clear Field dan Dialog Unsaved Changes pada Modal State Edit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Hook `before` login akun ini dan membuka Settings > Privacy Policy; hook `after` mengembalikan sesi ke akun default suite yang sama (Total Control). Nama env `AC_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active diterbitkan `John Doe` 10 Aug 2026 20:30 UTC dengan H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`; Version 2 `John Doe` 02 Jul 2026; Version 1 `Jane Smith` 15 Jan 2026, akun sudah dihapus). Hook `before` men-seed Riwayat A lewat Fixture BE (riwayat versi append-only dan tidak dapat dihapus lewat UI); hook `after` mengembalikan dataset ke Riwayat A. Spec ini tidak mem-publish versi (semua penutupan lewat `[Leave]` atau tanpa perubahan).
- Dokumen Privacy Policy bersifat tunggal platform-wide; suite berjalan serial (`parallel: false`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Kemampuan teknis: tombol keyboard Esc dan Backspace; asersi atribut tampilan dialog (severity warning, gaya tombol Text/Contrast).

## Test Steps

### TC-AC-PP-61: Clear Field pada state Edit versi Active mengosongkan editor total (bukan revert)

1. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
2. Tunggu konten editor termuat
3. Klik `[Clear Field]`
4. Verifikasi editor kosong dengan placeholder "Enter privacy policy content"
5. Verifikasi tidak ada dialog konfirmasi apa pun
6. Verifikasi Modal tetap di state Edit
7. Verifikasi Title Modal tetap "Edit Privacy Policy"
8. Verifikasi info bar tetap `Version 3 · Published At 10 Aug 26 · Published By John D`
9. Verifikasi kursor fokus di area editor

### TC-AC-PP-72: Clear Field lalu menutup modal pada versi yang sudah berisi konten dianggap perubahan

10. Klik `✕` di header
11. Verifikasi Dialog "Unsaved Changes" tampil karena editor kosong berbeda dari snapshot
12. Klik `[Leave]`
13. Verifikasi Modal tertutup
14. Verifikasi tabel Version History tampil
15. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
16. Tunggu konten editor termuat
17. Verifikasi editor terisi konten Version 3 asli (H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`) sehingga Version 3 di server tetap berisi konten aslinya
18. Klik `✕` di header (tanpa perubahan konten, modal tertutup tanpa dialog)

### TC-AC-PP-62: Dialog Unsaved Changes dari titik masuk langsung

19. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
20. Tunggu konten editor termuat
21. Klik di akhir konten lalu ketik " Draft change."
22. Klik `✕` di header
23. Verifikasi Dialog "Unsaved Changes" (severity warning) tampil
24. Verifikasi body dialog "You have unsaved changes. Are you sure you want to leave?"
25. Verifikasi tombol `[Cancel]` bergaya Text, Contrast
26. Verifikasi tombol `[Leave]` berseverity warning
27. Klik `[Cancel]`
28. Verifikasi dialog tertutup
29. Verifikasi Modal tetap di state Edit
30. Verifikasi konten editor masih memuat " Draft change."
31. Klik `✕` di header
32. Verifikasi Dialog "Unsaved Changes" tampil
33. Klik `[Leave]`
34. Verifikasi dialog tertutup sepenuhnya
35. Verifikasi Modal tertutup sepenuhnya
36. Verifikasi tabel Version History tampil
37. Verifikasi tidak ada toast yang tampil
38. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
39. Tunggu konten editor termuat
40. Verifikasi editor terisi konten Version 3 asli tanpa " Draft change."
41. Klik `✕` di header (tanpa perubahan konten, modal tertutup tanpa dialog)

### TC-AC-PP-63: Leave dari state Edit yang dibuka lewat [Edit] di footer View mengembalikan modal ke state View

42. Klik teks tautan `Version 3`
43. Verifikasi Modal View terbuka
44. Klik `[Edit]` di footer
45. Tunggu konten editor termuat
46. Ketik " Edited in view path." di akhir konten
47. Klik `✕` di header
48. Verifikasi Dialog "Unsaved Changes" tampil
49. Klik `[Leave]`
50. Verifikasi Modal tidak tertutup
51. Verifikasi Modal kembali ke state View `Version 3`
52. Verifikasi konten View adalah konten asli tanpa teks tambahan
53. Verifikasi footer menampilkan kembali tombol `[Edit]`
54. Verifikasi tidak ada toast yang tampil
55. Klik `✕` di header untuk menutup Modal View

### TC-AC-PP-65: Konten diubah lalu dikembalikan identik dengan snapshot dianggap clean

56. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
57. Tunggu konten editor termuat
58. Ketik "X" di akhir konten
59. Tekan Backspace satu kali sehingga konten identik dengan konten awal
60. Klik `✕` di header
61. Verifikasi Modal tertutup langsung
62. Verifikasi tidak ada Dialog Unsaved Changes
63. Verifikasi tabel Version History tampil

### TC-AC-PP-66: Esc pada state Edit yang sudah diubah memunculkan Dialog Unsaved Changes, Esc pada dialog setara Cancel

64. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
65. Tunggu konten editor termuat
66. Ketik " Changed." di akhir konten
67. Tekan Esc
68. Verifikasi Dialog "Unsaved Changes" tampil
69. Tekan Esc sekali lagi
70. Verifikasi dialog tertutup (setara `[Cancel]`)
71. Verifikasi Modal tetap di state Edit
72. Verifikasi " Changed." dipertahankan di editor
73. Verifikasi tidak ada dialog kedua yang bertumpuk
74. Klik `✕` di header
75. Verifikasi Dialog "Unsaved Changes" tampil
76. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC berubah dari urutan nomor: TC-AC-PP-72 ditaruh langsung sesudah TC-AC-PP-61 dan berbagi sesi modal Edit dengannya, karena langkah 1-2 TC-AC-PP-72 ("Edit, tunggu konten termuat, `[Clear Field]`") sama dengan TC-AC-PP-61 dan menghemat satu kali buka form (prinsip 6 konvensi: jumlah buka form tidak melebihi jumlah kejadian menutup). Langkah 3 TC-AC-PP-72 (`[✕]`) dilanjutkan dari editor yang sudah dikosongkan. Expected b TC-AC-PP-72 (Version 3 di server tetap berisi konten aslinya) diverifikasi di blok TC-AC-PP-72 sendiri dengan membuka ulang Edit (langkah 15-17). TC-AC-PP-63, 65, 66 mengikuti urutan nomor.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 15-16 (membuka ulang Edit untuk mengamati konten server), langkah 18 dan 41 (menutup editor tanpa perubahan; tidak ada dialog), langkah 55 (menutup Modal View). Penutupan modal dirty selalu `✕`, Verifikasi Dialog "Unsaved Changes" tampil, lalu `[Leave]` (S-08): Verifikasi dialog ditambahkan sebelum `[Leave]` pada blok TC-AC-PP-62 (langkah 32), TC-AC-PP-63 (langkah 48), dan TC-AC-PP-66 (langkah 75) sebagai asersi tambahan yang dicatat di sini (S-03).
- Asersi tambahan yang dicatat: langkah 17 memverifikasi editor terisi konten asli untuk memenuhi Expected b TC-AC-PP-72 ("Version 3 di server tetap berisi konten aslinya") yang tidak punya langkah observasi sendiri di TC-nya; langkah 40 adalah Expected d TC-AC-PP-62. Langkah 52 memverifikasi konten View asli sebagai bentuk "dibuang" dari Expected a TC-AC-PP-63 ("konten asli tanpa teks tambahan"). Klausa majemuk Expected dipecah satu `Verifikasi` per klausa (S-01).
- Jumlah langkah (76) melewati sekitar 35 langkah karena satu `Verifikasi` per klausa Expected (S-01) dan enam TC satu topik (Clear Field dan Unsaved Changes) dalam satu kelas harness; tiap blok `###` membuka sesi Edit sendiri dan tetap bermakna walau blok sebelumnya gagal, sehingga spec tidak dipecah.
- Post Condition TC ("Tidak ada versi baru dan tidak ada record audit", "Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Temuan untuk QA:
  - TC-AC-PP-72 Expected b menyatakan `[Leave]` menutup modal dan Version 3 di server tetap berisi konten asli, tetapi langkah TC berhenti di klik `[✕]`; langkah `[Leave]` dan observasi konten server tidak ada. Spec menambah klik `[Leave]` (langkah 12) dan membuka ulang Edit untuk observasi (langkah 15-17).
  - TC-AC-PP-63 Expected a menyebut "konten asli tanpa teks tambahan" untuk state View; cara mengamati konten State View (render HTML) tidak dirinci.
