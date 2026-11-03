---
id: TC-AC-RP-E2E-063-resilience-tulis-approver
title: "Resilience Tulis Approver: Bulk Remove, Assign, dan Remove Gagal 5xx"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-214
  - TC-AC-RP-215
coverage:
  web: automated
---

# Resilience Tulis Approver: Bulk Remove, Assign, dan Remove Gagal 5xx

## Prerequisites

- Mode: FE+BE (intercept respons 5xx di atas backend nyata).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `AC_RP_TC_PASSWORD` harus terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group `Region Jawa`), #12 (`Alex Tan`), #17 (approver `Manage allocation` `Region Jawa` = `Dewi Anggraini`, `Dewi Anggreni`; `Manage TAG stock` = `Sarah Kimura`).
- Data Dinamis: spec ini tidak membuat Data Dinamis. Nilai bersuffix `+{runId}-063` tidak dipakai karena tidak ada data yang dibuat spec.
- Kemampuan teknis (Pre-setup #23): intercept respons jaringan untuk memaksa respons 5xx pada submit Bulk Remove approver, Assign approver, dan Remove approver; intercept dilepas segera setelah pemicu selesai. Semua request tulis ditolak sehingga data Pre-setup tidak berubah; hook `after` tetap menjalankan pemulihan baseline automation dan melepas intercept bila spec gagal di tengah.
- Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: mengikuti pernyataan di Hook suite `suite.md`.

## Test Steps

### TC-AC-RP-214: Bulk Remove Approver gagal 5xx

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
3. Klik node `Region Jawa`
4. Pasang intercept respons 5xx pada submit Remove approver
5. Centang kedua approver (`Dewi Anggraini` dan `Dewi Anggreni`) lalu klik `Bulk Action` > `Remove` pada Bulk Action Bar
6. Klik `[Remove]`
7. Verifikasi toast "Error, failed to remove approver."
8. Verifikasi seleksi dipertahankan
9. Verifikasi Bulk Action Bar dipertahankan
10. Lepas intercept respons
11. Muat ulang halaman
12. Buka halaman `Settings > Role & Permission`

### TC-AC-RP-215: Assign dan Remove Approver single gagal 5xx

13. Klik tab `System`
14. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
15. Pasang intercept respons 5xx pada submit Assign approver
16. Klik "+ Assign" pada section Approvers
17. Centang `Alex Tan` lalu klik `[Assign]`
18. Verifikasi toast "Error, failed to assign approver."
19. Verifikasi popup Assign tetap terbuka
20. Lepas intercept Assign lalu pasang intercept respons 5xx pada submit Remove approver
21. Klik `✕` pada popup
22. Klik `⋯` baris `Sarah Kimura` lalu `Remove`
23. Klik `[Remove]`
24. Verifikasi toast "Error, failed to remove approver."
25. Verifikasi dialog tetap terbuka tanpa perubahan
26. Verifikasi baris `Sarah Kimura` tetap di tabel Approvers
27. Lepas intercept respons

## Notes

- Mode: FE+BE (intercept). Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec resilience ini mengasersi baris yang tetap ada di tabel Approvers hasil baca dari server nyata, sehingga tidak `Mode: mock` (bagian 6).
- Subjudul `###` memetakan langkah ke id TC granular. Tanda "→" pada kolom Langkah Uji TC tidak diasersi.
- Langkah penghubung (S-03, S-09): langkah 10 dan 27 (lepas intercept), 11 dan 12 (muat ulang dan buka ulang halaman agar dialog dan seleksi sisa tidak terbawa), 13 dan 14 (navigasi ke Role Detail), 20 (ganti intercept), 21 (tutup popup tanpa dialog Unsaved Changes karena popup picker bukan form).
- Temuan untuk QA:
  - TC-AC-RP-214 menulis "kedua approver" tanpa nama; spec memakai `Dewi Anggraini` dan `Dewi Anggreni` dari Pre-setup #17.
  - TC-AC-RP-214 Expected tidak menyebut status dialog `[Remove]` setelah gagal; tidak diasersi (TC-AC-RP-215 menyebut dialog tetap terbuka untuk Remove single).
  - TC-AC-RP-215 Langkah Uji 4 menulis "Assign Approver `Alex Tan`" tanpa rincian klik; spec memakai rincian yang sama dengan TC-AC-RP-204 (klik "+ Assign", centang, `[Assign]`).
