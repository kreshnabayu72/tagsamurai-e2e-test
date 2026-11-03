---
id: TC-AC-RP-E2E-061-remove-approver-single
title: "Remove Additional Approver: Confirm Global Role, Cancel, Dialog Group Role, dan Aktor Me-Remove Baris Miliknya"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-208
  - TC-AC-RP-209
  - TC-AC-RP-210
  - TC-AC-RP-439
coverage:
  web: automated
---

# Remove Additional Approver: Confirm Global Role, Cancel, Dialog Group Role, dan Aktor Me-Remove Baris Miliknya

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `AC_RP_TC_PASSWORD` harus terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group `Region Jawa`), #17 (approver `Manage TAG stock` = `Sarah Kimura`; `Manage allocation` `Region Jawa` = `Dewi Anggraini`, `Dewi Anggreni`; `Manage hardware stock` kosong).
- Data Dinamis (Tabel Data Uji Dinamis TC #9): `Siti Nurhaliza` sebagai approver `Manage hardware stock`, di-assign oleh Default User `Bambang Hartono`; disiapkan sebelum TC-AC-RP-439 (dipakai sebagai precondition TC, tidak diasersi) lewat kemampuan seeding yang disediakan tim FE/BE. Nilai bersuffix `+{runId}-061` tidak dipakai karena data memakai user Pre-setup.
- Perubahan Pre-setup: approver `Manage TAG stock` (Sarah Kimura dihapus pada TC-AC-RP-208) dan `Manage hardware stock` (Siti Nurhaliza dihapus pada TC-AC-RP-439). Pemulihan memakai kemampuan reset baseline automation yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` serta sebagai langkah penghubung. Efek: Changelog Role Detail menerima entri Remove; Last Updated approver berubah.
- Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: mengikuti pernyataan di Hook suite `suite.md`.

## Test Steps

### TC-AC-RP-208: Screening dan Confirm Remove Approver Global Role

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
3. Klik `⋯` baris `Sarah Kimura` lalu `Remove`
4. Verifikasi dialog Title "Remove Approver", body • Sarah K, "They will no longer be able to review Duplicate Identifier Approval requests.", "Are you sure you want to remove it?", tombol `[Cancel]` dan `[Remove]`
5. Klik `[Remove]`
6. Verifikasi toast "Success, approver has been removed."
7. Verifikasi tabel Approvers menampilkan empty state "No approvers yet"

### TC-AC-RP-210: Cancel dialog Remove Approver

8. Pulihkan baseline automation: approver `Manage TAG stock` kembali `Sarah Kimura`, lalu muat ulang halaman
9. Klik `⋯` baris `Sarah Kimura` lalu `Remove`
10. Klik `[Cancel]`
11. Verifikasi dialog tertutup
12. Verifikasi tabel Approvers tetap memuat `Sarah Kimura` tanpa perubahan

### TC-AC-RP-209: Screening dialog Remove Approver Group Role

13. Buka halaman `Settings > Role & Permission`
14. Klik tab `System`
15. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
16. Klik node `Region Jawa`
17. Klik `⋯` baris `Dewi Anggreni` lalu `Remove`
18. Verifikasi dialog Title "Remove Approver" dengan kalimat "They will no longer be able to approve these requests."
19. Klik `[Cancel]`

### TC-AC-RP-439: Aktor yang sudah menjadi approver me-Remove baris approver miliknya

20. Siapkan precondition: `Siti Nurhaliza` sudah menjadi approver `Manage hardware stock`, di-assign oleh Default User `Bambang Hartono`
21. Buka halaman `Settings > Role & Permission`
22. Klik tab `System`
23. Pada section Global Role, klik `⋯` pada baris `Manage hardware stock` lalu klik `Detail`
24. Klik `⋯` baris `Siti Nurhaliza`
25. Verifikasi aksi `Remove` pada baris milik aktor enabled
26. Klik `Remove`
27. Verifikasi dialog Title "Remove Approver" dengan bullet • Siti N
28. Klik `[Remove]`
29. Verifikasi toast "Success, approver has been removed."
30. Verifikasi tabel Approvers tidak memuat `Siti Nurhaliza`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Tanda "→" pada kolom Langkah Uji TC tidak diasersi.
- Urutan TC di spec: 208, 210, 209, 439. Alasan: TC-AC-RP-210 memakai target dan dialog yang sama dengan TC-AC-RP-208 sehingga diletakkan berurutan sesudah baseline dipulihkan (S-10).
- Langkah penghubung (S-03): langkah 8 (pemulihan baseline dan muat ulang), 13 sampai 16 (navigasi ke Role Detail `Manage allocation`), 19 (tutup dialog), 20 sampai 23 (precondition dan navigasi). Langkah 30 memakai toast langkah 29 sebagai anchor absence (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-RP-439 berada di Coverage Ledger (`tc-settings-role-permission.md` L171), bukan di tabel Section 3h; lokasi baris TC perlu dipindah ke Section 3h atau dikonfirmasi QA.
  - TC-AC-RP-439 Precondition d menyebut `Siti Nurhaliza` di-assign sebagai approver oleh Default User `Bambang Hartono`, tetapi mekanisme seeding tidak disebut di TC, PRD, atau LLD (S-13); ditulis sebagai kemampuan yang disediakan tim FE/BE.
  - TC-AC-RP-209 tidak punya langkah penutup dialog; langkah 19 (`[Cancel]`) adalah langkah penghubung.
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-13).
