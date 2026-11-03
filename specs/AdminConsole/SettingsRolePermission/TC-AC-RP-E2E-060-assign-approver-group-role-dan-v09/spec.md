---
id: TC-AC-RP-E2E-060-assign-approver-group-role-dan-v09
title: "Additional Approver Group Role: Assign pada Group Aktif, Banyak Group, dan V-09 Sesi Lain"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-206
  - TC-AC-RP-207
  - TC-AC-RP-422
coverage:
  web: automated
---

# Additional Approver Group Role: Assign pada Group Aktif, Banyak Group, dan V-09 Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `AC_RP_TC_PASSWORD` harus terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Admin B (TC-AC-RP-422): sesi API sesuai Hook suite "Sesi API aktor"; akun Admin B disediakan tim FE. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Pelaku kedua lewat sesi API tidak membuka konteks UI kedua.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group `Region Jawa`, `Sumatera`), #12 (`Alex Tan`, `Dewi Anggreni`), #17 (approver `Manage allocation` `Region Jawa` = `Dewi Anggraini`, `Dewi Anggreni`; `Manage hardware stock` kosong), #24 (Admin B).
- Data Dinamis: spec ini tidak membuat Data Dinamis; target Assign adalah user Pre-setup `Alex Tan` dan `Dewi Anggreni` (nama tampil dipakai asersi TC). Nilai bersuffix `+{runId}-060` tidak dipakai karena tidak ada data yang dibuat spec.
- Perubahan Pre-setup: approver `Manage allocation` `Sumatera` dan `Manage hardware stock` bertambah. Pemulihan ke approver awal memakai kemampuan reset baseline automation yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` serta sebagai langkah penghubung. Efek: Changelog Role Detail menerima entri Add dan Remove; Last Updated approver berubah.
- Kemampuan teknis: membaca jumlah entri Changelog Role Detail sebelum aksi (baseline, bagian 8b butir 10), dan mengamati status respons submit Assign pada TC-AC-RP-422 (disediakan tim FE).
- Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: mengikuti pernyataan di Hook suite `suite.md`.

## Test Steps

### TC-AC-RP-206: Assign Approver Group Role pada group aktif

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
3. Klik node `Sumatera`
4. Klik "+ Assign" pada sub-section Approvers
5. Verifikasi header popup "Assign Approver — Manage allocation (Sumatera)"
6. Centang `Alex Tan` lalu klik `[Assign]`
7. Verifikasi toast "Success, approver has been assigned."
8. Verifikasi tabel "Approvers — Sumatera" memuat `Alex Tan`
9. Klik node `Region Jawa`
10. Verifikasi Approvers `Region Jawa` tidak berubah (`Dewi Anggraini` dan `Dewi Anggreni`)

### TC-AC-RP-207: User yang sama dapat menjadi approver di banyak group

11. Klik node `Sumatera`
12. Klik "+ Assign" pada sub-section Approvers
13. Centang `Dewi Anggreni` lalu klik `[Assign]`
14. Verifikasi Assign sukses: tabel "Approvers — Sumatera" memuat `Dewi Anggreni`
15. Klik node `Region Jawa`
16. Verifikasi `Dewi Anggreni` tercatat di `Region Jawa` dan di `Sumatera` sebagai baris terpisah per group

### TC-AC-RP-422: Assign Approver ke user yang sudah menjadi approver lewat sesi lain ditolak V-09

17. Pulihkan baseline automation: approver `Manage allocation` `Sumatera` kosong
18. Buka halaman `Settings > Role & Permission`
19. Klik tab `System`
20. Pada section Global Role, klik `⋯` pada baris `Manage hardware stock` lalu klik `Detail`
21. Buka Changelog Role Detail lewat icon Changelog, catat jumlah entri sebagai baseline, lalu tutup modal
22. Sesi A: klik "+ Assign" pada section Approvers, centang `Alex Tan`
23. Sesi B (sesi API Admin B): Assign Approver `Alex Tan` pada `Manage hardware stock` hingga approver tersimpan
24. Sesi A: klik `[Assign]`
25. Verifikasi inline alert "Alex Tan is no longer eligible. Please select another." (`V-09`)
26. Verifikasi respons submit Sesi A berstatus `422` (submit ditolak seluruhnya)
27. Verifikasi centangan `Alex Tan` auto-clear
28. Klik `✕` pada popup
29. Verifikasi tabel Approvers memuat `Alex Tan` satu kali
30. Buka Changelog Role Detail lewat icon Changelog
31. Verifikasi Changelog mencatat tepat satu entri baru dengan Action `Add` dibanding baseline pada langkah 21

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Tanda "→" pada kolom Langkah Uji TC tidak diasersi.
- Langkah penghubung (S-03): langkah 17 (pemulihan baseline), 18 sampai 20 (navigasi ke Role Detail `Manage hardware stock`), 21 (baseline Changelog, S-12), 28 (tutup popup tanpa dialog Unsaved Changes karena popup picker bukan form), 30 (buka Changelog).
- Pelaku kedua pada langkah 23 memakai sesi API (bukan konteks UI kedua), sehingga tidak memerlukan butir `P-2`.
- Temuan untuk QA:
  - TC-AC-RP-422 menyebut "dua sesi paralel" (Manual Only kriteria d) dan Sesi B "Assign Approver"; spec memakai sesi API untuk Sesi B karena Sesi B hanya memicu perubahan state. Bila QA menghendaki sesi UI kedua, spec dipindah ke kelas c.
  - TC-AC-RP-422 Expected "Changelog hanya mencatat satu entri `Add`" tidak memberi langkah membuka Changelog; spec menambah langkah penghubung 21, 30 (klik icon Changelog) tanpa memberi path lain. Status `422` pada Expected tidak punya cara pengamatan yang ditulis di TC; spec mengasumsikan pengamatan respons jaringan browser.
  - TC-AC-RP-207 Expected hanya menyebut "Assign sukses" tanpa teks toast; spec tidak mengasersi toast.
  - TC-AC-RP-207 Langkah 4 menulis "Assign Approver `Dewi Anggreni`" tanpa rincian klik; spec memakai rincian yang sama dengan TC-AC-RP-206.
  - Email Admin B (Pre-setup #24) tidak tertulis; ditulis "disediakan tim FE".
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-13).
