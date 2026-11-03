---
id: TC-AC-RP-E2E-055-bulk-remove-role-detail-bar-dialog-dan-cancel
title: "Bulk Remove Role Detail: Bulk Action Bar, Dialog Jamak dan Single, serta Cancel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-192
  - TC-AC-RP-193
  - TC-AC-RP-194
  - TC-AC-RP-200
coverage:
  web: automated
---

# Bulk Remove Role Detail: Bulk Action Bar, Dialog Jamak dan Single, serta Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup: #11, #3 dan #13 (Read Only `Dewi Anggraini`, Total Control `Rina Wijaya`), #12 (`Jane Smith`, `John Dohan`), #15 (`Manage device master data` memuat baris `John Dohan`, `Jane Smith`, `Rina Wijaya`, `Dewi Anggraini`).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Spec ini tidak menyimpan perubahan data (semua dialog Remove ditutup dengan `[Cancel]`). Pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`

### TC-AC-RP-200: Tampilan Bulk Action Bar Role Detail

3. Centang baris `John Dohan`
4. Verifikasi Bulk Action Bar tampil dengan counter "1 User selected", tombol dropdown `Bulk Action`, dan icon clear selection
5. Centang baris `Jane Smith`
6. Verifikasi counter berubah menjadi "2 Users selected"
7. Klik `Bulk Action`
8. Verifikasi dropdown `Bulk Action` terbuka dan memuat aksi `Remove` (danger)

### TC-AC-RP-194: Cancel dialog Bulk Remove mempertahankan seleksi

9. Klik `Remove` pada dropdown `Bulk Action`
10. Klik `[Cancel]`
11. Verifikasi dialog tertutup
12. Verifikasi seleksi tetap 2 baris
13. Verifikasi Bulk Action Bar tetap tampil

### TC-AC-RP-193: Bulk Remove tepat satu baris memakai dialog single

14. Hapus centang baris `Jane Smith` sehingga hanya `John Dohan` terpilih
15. Klik `Bulk Action` > `Remove` pada Bulk Action Bar
16. Verifikasi dialog yang tampil adalah dialog "Remove Role" (single, D-03), bukan "Remove Roles"
17. Klik `[Cancel]`

### TC-AC-RP-192: Bulk Remove dengan dua baris bertanda memakai kalimat jamak

18. Klik icon clear selection
19. Centang baris `Rina Wijaya` dan `Dewi Anggraini`
20. Klik `Bulk Action` > `Remove` pada Bulk Action Bar
21. Verifikasi body dialog memuat • Rina W — "Total Control" dan • Dewi A — "Read Only"
22. Verifikasi body dialog memuat "The users marked above will lose their access level as a result."
23. Klik `[Cancel]`
24. Klik icon clear selection

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-AC-RP-190 dan TC-AC-RP-191 (Bulk Remove berhasil) ada di spec 056.
- Urutan menyimpang dari nomor TC: TC-AC-RP-200 lebih dulu karena membangun seleksi dua baris yang dipakai TC-AC-RP-194; TC-AC-RP-193 dan TC-AC-RP-192 kemudian. Tidak ada TC yang menyimpan perubahan (semua dialog di-Cancel).
- TC-AC-RP-194 memakai seleksi dan dropdown `Bulk Action` yang sudah terbentuk pada TC-AC-RP-200 (langkah 9 melanjutkan dropdown yang terbuka).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 17 dan 23 (`[Cancel]` menutup dialog yang hanya diamati), dua langkah icon clear selection (reset seleksi, S-09), dan penghapusan centang `Jane Smith` yang membentuk seleksi satu baris.
- Temuan untuk QA:
  - TC-AC-RP-192 Data tidak menyebut apakah `Rina Wijaya` dan `Dewi Anggraini` ada di `Manage device master data`; TC-AC-RP-191 memakai `Rina Wijaya` pada role yang sama, dan `Dewi Anggraini` diasumsikan memegang role ini sebagai Read Only.
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
