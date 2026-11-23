---
id: TC-FA-SU-E2E-351-state-tab-dan-sub-tab-detail-user-serta-default-dan-ordering
title: "State Tab dan Sub-tab Detail User serta Default dan Ordering"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1025
  - TC-FA-SU-1026
coverage:
  web: automated
---

# State Tab dan Sub-tab Detail User serta Default dan Ordering

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Responsibilities (#24, #25), Non-Login User (#26), Changelog (#27), System Log (#28), Transaction Admin Log (#29), User Log (#30), Transaction Role (#39). Target: Doni Prasetyo (Inactive, 0 roles) dan Budi Santoso (Detail dengan semua tab berisi data).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec hanya membaca: tidak ada data yang diubah. Tiap tabel Budi Santoso yang diasersi urutannya memuat sedikitnya dua nilai distinct pada kolom urutan menurut Pre-setup #24 sampai #30 (S-11, S-14).
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah; state Search, Filter, Sort, dan page size sisi klien dikosongkan pada langkah penghubung terakhir, sehingga tidak ada pemulihan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1026: Default dan ordering: Role Count 0 roles, strip nilai kosong, dan tanpa filter default

1. Ketik Search `Doni Prasetyo`, tekan Enter
2. Verifikasi kolom Role baris Doni Prasetyo menampilkan `0 roles` sebagai teks biasa
3. Verifikasi kolom Employee ID baris Doni Prasetyo menampilkan `—` untuk nilai kosong
4. Klik `Filter` pada Table Tools
5. Verifikasi Filter Panel kosong (tidak ada filter terisi)
6. Verifikasi tidak ada indikator filter aktif pada Table Tools
7. Tutup Filter Panel, ganti isi kotak search dengan `Budi`, tekan Enter, lalu klik nama Budi Santoso
8. Buka Tab Changelog
9. Verifikasi urutan default Tab Changelog adalah kolom tanggal menurun (terbaru di atas)
10. Buka Tab System Log
11. Verifikasi urutan default Tab System Log adalah kolom tanggal menurun (terbaru di atas)
12. Buka Tab Transaction Admin Log sub-tab Borrow
13. Verifikasi urutan default Tab Transaction Admin Log sub-tab Borrow adalah kolom tanggal menurun (terbaru di atas)
14. Buka Tab User Log sub-tab Borrow
15. Verifikasi urutan default Tab User Log sub-tab Borrow adalah kolom tanggal menurun (terbaru di atas)
16. Buka Tab User Log sub-tab Assignment
17. Verifikasi urutan default Tab User Log sub-tab Assignment adalah kolom tanggal menurun (terbaru di atas)
18. Buka Tab User Log sub-tab Session
19. Verifikasi urutan default Tab User Log sub-tab Session adalah kolom tanggal menurun (terbaru di atas)
20. Buka Tab Role > Sub-tab Transaction Role
21. Verifikasi urutan default Sub-tab Transaction Role adalah Transaction A-Z
22. Buka Tab Responsibilities > Sub-tab Borrowed Assets
23. Verifikasi urutan default Sub-tab Borrowed Assets adalah Due Return Date ascending
24. Buka Tab Responsibilities > Sub-tab Assigned Assets
25. Verifikasi urutan default Sub-tab Assigned Assets adalah Name A-Z
26. Buka Tab Responsibilities > Sub-tab Pending Approvals
27. Verifikasi urutan default Sub-tab Pending Approvals adalah Submission Date ascending
28. Buka Tab Responsibilities > Sub-tab Pending Tasks
29. Verifikasi urutan default Sub-tab Pending Tasks adalah Request Date ascending
30. Buka Tab Non-Login User
31. Verifikasi urutan default Tab Non-Login User adalah Name A-Z

### TC-FA-SU-1025: Navigasi antar tab dan sub-tab mempertahankan state Search, Filter, Sort, dan page size per tab

32. Buka Tab Changelog, ketik Search `Home`, tekan Enter, terapkan Filter pada kolom Action, klik satu header kolom sortable, dan ubah page size ke 25
33. Buka Tab Role lalu kembali ke Tab Changelog
34. Verifikasi Search `Home` pada Tab Changelog masih ada
35. Verifikasi Filter kolom Action pada Tab Changelog masih ada
36. Verifikasi Sort kolom yang diklik pada Tab Changelog masih ada
37. Verifikasi page size 25 pada Tab Changelog masih ada
38. Buka Tab Responsibilities > Sub-tab Borrowed Assets dan klik satu header kolom sortable
39. Pindah ke Sub-tab Assigned Assets
40. Verifikasi Sub-tab Assigned Assets tidak terpengaruh sort Sub-tab Borrowed Assets (urutan tetap Name A-Z)
41. Kembali ke Sub-tab Borrowed Assets
42. Verifikasi Sort Sub-tab Borrowed Assets masih ada
43. Klik `(←)` pada kotak Search Tab Changelog, hapus Filter kolom Action, kembalikan Sort dan page size Tab Changelog ke default, lalu kembalikan Sort Sub-tab Borrowed Assets ke default

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah (TC-FA-SU-1026 lebih dulu, lalu TC-FA-SU-1025) supaya default sort dibaca sebelum Search, Filter, Sort, dan page size diubah (S-14).
- Search untuk menemukan baris target (R-16) dicatat sebagai langkah penghubung.
- TC-FA-SU-1026 Expected c menyebut "Changelog dan log lain" tanggal menurun; spec mengasersi Tab Changelog, Tab System Log, Tab Transaction Admin Log (sub-tab Borrow), dan sub-tab Borrow, Assignment, dan Session Tab User Log.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 7, 43.
- Spec ini 43 langkah (di atas smell 35 langkah, dihitung dengan ekspansi). Alasan: seluruh blok hanya membaca Detail Budi Santoso dan tidak mengubah state apa pun; ekspansi berasal dari TC-FA-SU-1026 yang menuntut pemeriksaan default sort pada dua belas surface (enam surface log dan enam tabel Tab Role, Tab Responsibilities, dan Tab Non-Login User), satu pembukaan dan satu `Verifikasi` per surface.
- Temuan untuk QA:
  - TC-FA-SU-1025 tidak menyebut kolom Filter, kolom Sort, dan nilai Filter pada Tab Changelog; spec memakai kolom Action untuk Filter dan satu header kolom sortable untuk Sort.
  - Expected b TC-FA-SU-1026 menulis "Nilai kosong ditampilkan `—`" tanpa menyebut surface; spec memakai kolom Employee ID baris Doni Prasetyo (nilai `—` pada Pre-setup #43).
  - TC-FA-SU-1026 menyebut "tiap tab" dan "log lain" tanpa daftar tab; spec mengasersi seluruh surface yang disebut Expected c.
