---
id: TC-GS-NLU-E2E-029-create-klik-backdrop-clear-field-dan-klik-ganda-submit
title: "Create: klik backdrop, Clear Field, dan klik ganda Submit"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-61
  - TC-GS-NLU-62
  - TC-GS-NLU-92
coverage:
  web: automated
---

# Create: klik backdrop, Clear Field, dan klik ganda Submit

## Prerequisites

- Mode: FE+BE (backend nyata; jumlah request Create dan record hasil Create dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 12, hanya dibaca): Division `Logistics`, Login User `Ahmad Fauzi` (pool Represented By).
- Data Dinamis milik spec: Non-Login User `Hari Santoso {runId}-029` (First Name `Hari`, Last Name `Santoso {runId}-029`), Email `harisantoso+{runId}-029@qwertysystem.net`, Division `Logistics`, Represented By `Ahmad Fauzi` (satu-satunya record yang tersimpan). Nilai TC-GS-NLU-62 (`Wahyu`, `Hidayat`, Email `wahyuhidayat+{runId}-029@qwertysystem.net`) tidak disubmit. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-029` lewat API (mekanisme disediakan tim FE/BE).
- Kemampuan teknis: mencatat jumlah request yang dikirim ke endpoint Create Non-Login User sepanjang klik ganda `[Submit]` (pencatat request di browser; endpoint tidak disebut TC, PRD, atau LLD).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### TC-GS-NLU-61: Klik backdrop tidak menutup popup

1. Klik `[+ Non-Login User]`
2. Klik area gelap di luar popup
3. Verifikasi popup tetap terbuka
4. Isi First Name `Anton`
5. Klik area gelap di luar popup
6. Verifikasi popup tetap terbuka
7. Verifikasi dialog Unsaved Changes tidak muncul
8. Verifikasi isian First Name tetap `Anton`

### TC-GS-NLU-62: Clear Field mengosongkan seluruh isian tanpa menutup popup

9. Ganti isi First Name dengan `Wahyu`
10. Isi Last Name `Hidayat` dan Email `wahyuhidayat+{runId}-029@qwertysystem.net`, lalu pilih Division `Logistics`
11. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
12. Centang `Set as Temporary User`
13. Centang `Stay on this form after submitting`
14. Klik `[Clear Field]`
15. Verifikasi First Name, Last Name, dan Email kosong
16. Verifikasi Division kembali placeholder `Select division`
17. Verifikasi Represented By kembali `[+ Select User]`
18. Verifikasi checkbox `Set as Temporary User` tidak tercentang dan field Temporary Until hilang
19. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
20. Verifikasi popup tetap terbuka tanpa dialog konfirmasi

### TC-GS-NLU-92: Klik ganda cepat Submit hanya diproses sekali

21. Hapus centang `Stay on this form after submitting`
22. Isi First Name `Hari`, Last Name `Santoso {runId}-029`, dan Email `harisantoso+{runId}-029@qwertysystem.net`, lalu pilih Division `Logistics`
23. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
24. Klik ganda cepat `[Submit]`
25. Verifikasi tombol `[Submit]` langsung masuk Saving state setelah klik pertama
26. Verifikasi hanya satu request Create yang dikirim dan diproses
27. Verifikasi satu toast sukses `Success, non-login user has been created.` tampil
28. Ketik Search `Hari Santoso {runId}-029`, tekan Enter
29. Verifikasi tepat satu baris `Hari Santoso {runId}-029` tampil di tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-GS-NLU-61 dan TC-GS-NLU-62 tidak submit dan memakai satu pembukaan popup; TC-GS-NLU-92 melanjutkan popup yang sama (aksi submit sukses di akhir; S-10).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 9 (mengganti isian `Anton` sisa TC-GS-NLU-61; S-09), langkah 21 (checkbox Stay default tidak tercentang pada TC-GS-NLU-92; sisa TC-GS-NLU-62), langkah 28 (Search untuk menemukan baris target lewat Name bersuffix; R-16; kolom Email tidak termasuk kolom Search List).
- Langkah 25 mengasersi Saving state segera setelah klik pertama (8b.5); langkah 26 memakai pencatat request pada Prerequisites.
- Temuan untuk QA:
  - TC-GS-NLU-92 Expected a ("hanya satu request diproses") tidak menyebut endpoint atau cara mengamati; spec menuliskannya sebagai kemampuan teknis disediakan tim FE.
  - TC-GS-NLU-62 Expected a tidak menyebut keadaan avatar dan Position setelah Clear Field; spec tidak mengasersinya.
