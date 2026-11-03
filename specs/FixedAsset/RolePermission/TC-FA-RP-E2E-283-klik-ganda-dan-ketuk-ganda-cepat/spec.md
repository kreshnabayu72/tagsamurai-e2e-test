---
id: TC-FA-RP-E2E-283-klik-ganda-dan-ketuk-ganda-cepat
title: "Klik ganda dan ketuk ganda cepat"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1000
  - TC-FA-RP-1001
  - TC-FA-RP-1002
  - TC-FA-RP-1003
coverage:
  web: automated
---

# Klik ganda dan ketuk ganda cepat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Env var yang dipakai: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #15 (Ahmad Fauzi, Budi Santoso), #39 (Detail Role Global Role `Manage accounting` terisi, termasuk baris Ahmad Fauzi; TC-FA-RP-1003), #18, dan #19 (Require Approval Off di semua node). Budi Santoso memegang Global Role `Manage Open API` (TC-FA-RP-1001); Ahmad Fauzi tanpa tingkat akses (TC-FA-RP-1000) dan memegang baris `Manage accounting` dengan Create tidak aktif (TC-FA-RP-1003). Disiapkan lewat seeding di hook `before`. Ahmad Fauzi menjadi Total Control pada TC-FA-RP-1000, sehingga sebelum TC-FA-RP-1003 ia dipulihkan lewat seeding API (langkah 24) ke tanpa tingkat akses dengan baris `Manage accounting` Create nonaktif; tanpa itu klik Create dapat memicu dialog auto-revert.
- Kemampuan teknis: Kemampuan baca jumlah entri (disediakan tim FE/BE, tanpa endpoint karangan, bagian 8b butir 10): jumlah entri Changelog surface terkait dibaca sebelum aksi (baseline) dan sesudahnya; asersi memakai perbandingan terhadap baseline, bukan angka absolut (S-12).
- Waktu: klik ganda dilakukan sebagai dua klik berurutan cepat oleh driver browser (jeda di bawah satu detik).
- State global: spec mengubah penugasan pool #15 dan nilai Require Approval `Disposal` pada `IT Infrastructure`; keduanya dipulihkan di hook `after`.
- Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-1000: Klik ganda `[Assign]` hanya memproses satu permintaan

1. Tunggu toast lama hilang otomatis
2. Catat baseline jumlah entri Changelog Tab Total Control lewat kemampuan baca jumlah entri
3. Klik `[+ Assign]` di Tab Total Control
4. Centang Ahmad Fauzi
5. Klik `[Assign]` dua kali cepat
6. Verifikasi hanya satu toast sukses `Success, Total Control has been assigned.`
7. Ketik Search `Ahmad Fauzi`, tekan Enter
8. Verifikasi hanya satu baris Ahmad Fauzi tampil di Tab Total Control
9. Verifikasi jumlah entri Changelog Tab Total Control bertambah tepat satu dibanding baseline (satu entri log Ahmad Fauzi)
10. Klik `(←)` pada kotak Search

### TC-FA-RP-1001: Klik ganda `[Remove]` pada dialog hanya memproses satu permintaan

11. Tunggu toast lama hilang otomatis
12. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
13. Catat baseline jumlah entri Changelog Detail Role `Manage Open API` lewat kemampuan baca jumlah entri
14. Klik `[⋯]` baris Budi Santoso lalu `Remove`
15. Klik `[Remove]` dua kali cepat
16. Verifikasi hanya satu toast sukses `Success, user has been removed.`
17. Verifikasi jumlah entri Changelog Detail Role `Manage Open API` bertambah tepat satu dibanding baseline (satu entri log Remove)

### TC-FA-RP-1002: Klik ganda toggle Require Approval hanya memproses satu perubahan

18. Tunggu toast lama hilang otomatis
19. Klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Disposal`
20. Catat baseline jumlah entri Changelog Transaction Role lewat kemampuan baca jumlah entri
21. Klik toggle `Require Approval for Disposal` dua kali cepat
22. Verifikasi toggle Disabled selama proses
23. Verifikasi jumlah entri Changelog Transaction Role bertambah tepat satu dibanding baseline (satu entri log Edit Require Approval)

### TC-FA-RP-1003: Ketuk ganda cepat checkbox CRUD hanya memproses satu perubahan

24. Pulihkan Ahmad Fauzi ke tanpa tingkat akses dengan baris `Manage accounting` Create nonaktif lewat seeding API, hingga tersimpan
25. Klik Tab `System`, klik Role Name `Manage accounting` pada section Global Role
26. Catat baseline jumlah entri Changelog Detail Role `Manage accounting` lewat kemampuan baca jumlah entri
27. Klik checkbox Create baris Ahmad Fauzi dua kali cepat
28. Verifikasi cell Create baris Ahmad Fauzi Disabled selama proses sehingga klik kedua tidak membuat permintaan ganda
29. Verifikasi jumlah entri Changelog Detail Role `Manage accounting` bertambah tepat satu dibanding baseline (satu entri log Edit Create)

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-1000, 1001, 1002, 1003).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): mencatat baseline jumlah entri Changelog (S-12); Search untuk menemukan baris Ahmad Fauzi (langkah 7) dan menutup Search dengan `(←)` (langkah 10); "Tunggu toast lama hilang otomatis" sebelum asersi toast berikutnya (R-12); membuka tab, Detail Role, node, dan sub-tab.
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 24 (pemulihan Ahmad Fauzi sebelum TC-FA-RP-1003, karena TC-FA-RP-1000 menjadikannya Total Control); tidak ada `Verifikasi`.
- Expected "satu entri log" pada TC-FA-RP-1000 sampai TC-FA-RP-1003 adalah asersi jumlah (selisih satu terhadap baseline), bukan asersi absence; surface log yang diamati adalah Changelog surface yang disentuh aksi.
- Pembagian TC lintas spec: TC-FA-RP-1000 sampai TC-FA-RP-1003 tidak memuat klausa "tidak ada entri log"; tidak ada rujukan ke spec absence.
- Temuan untuk QA:
  - Expected TC-FA-RP-1000 sampai TC-FA-RP-1003 menyebut "satu entri log" tanpa menyebut surface; spec memakai Changelog surface yang disentuh aksi dan tidak mengasersi System Log dan Activity Log.
  - TC-FA-RP-1002 menyebut "Toggle disabled selama proses sehingga hanya satu permintaan diproses" dan TC-FA-RP-1003 "Cell disabled selama proses"; hanya state Disabled yang teramati di UI, jumlah permintaan dibuktikan lewat jumlah entri log.
  - Hasil dua klik pada toggle (TC-FA-RP-1002) tidak menyebut keadaan akhir toggle; spec tidak mengasersinya dan memulihkan nilainya di hook `after`.
