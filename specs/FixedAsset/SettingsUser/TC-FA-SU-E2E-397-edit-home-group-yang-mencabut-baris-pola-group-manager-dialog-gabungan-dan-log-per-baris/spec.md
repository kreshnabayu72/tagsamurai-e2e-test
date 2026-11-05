---
id: TC-FA-SU-E2E-397-edit-home-group-yang-mencabut-baris-pola-group-manager-dialog-gabungan-dan-log-per-baris
title: "Edit Home Group yang Mencabut Baris Pola Group Manager: Dialog Gabungan, Pencabutan Baris Pola, dan Log per Baris"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1095
coverage:
  web: automated
---

# Edit Home Group yang Mencabut Baris Pola Group Manager: Dialog Gabungan, Pencabutan Baris Pola, dan Log per Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite; hook `after` memulihkan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23), dan Group Manager `FaUserGM` (#48). Pengguna target: Putri Anggraeni (Pre-setup #48 dan #43): Group Manager Finance & Accounting (turunan Accounts Payable), Home Group Finance & Accounting, dengan baris pola Group Manager pada kedua node (6 Group Role katalog selain Manage user & role dengan CRUD penuh; Transaction Role Asset Admin dan Approver pada kesembilan Jenis Transaksi), ditambah Group Role Manage user & role pada Finance & Accounting (Read dan Update), Transaction Role Disposal × Staff pada IT Infrastructure, dan Damaged × Monitoring & Report pada Branch Surabaya. Nama pengguna dan grup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Jumlah baris pola yang dicabut (turunan dari Pre-setup #48): Group Role 12 (6 Group Role katalog × 2 node) dan Transaction Role 36 (Asset Admin dan Approver × 9 Jenis Transaksi × 2 node).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group`, `Auto-Revert`, dan entri yang memuat `(via Group Manager)` pada Tab Changelog Putri Anggraeni, Tab System Log aktor, dan Activity Log, serta entri `Remove (via Group Manager)` pada modal Changelog User > Group Role dan > Transaction Role, dibaca sebelum aksi (baseline, S-12) dan sesudah aksi. Audit trail bersifat permanen sehingga asersi memakai selisih terhadap baseline, bukan angka absolut. Log yang menunggu eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group, status Group Manager, dan baris pola Putri Anggraeni ke kondisi Pre-setup #48. Pemulihan dijalankan sebagai langkah penghubung terakhir dan di hook `after` (cadangan).
- State yang diubah dan pemulihannya: Home Group Putri Anggraeni berubah ke IT Infrastructure, status Group Manager terlepas, dan baris pola terhapus (Last Updated dan Modified By berubah); entri log permanen bertambah. Dipulihkan ke Pre-setup #48 lewat seed API. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat jumlah entri `Edit Home Group`, `Auto-Revert`, dan yang memuat `(via Group Manager)` pada Tab Changelog Putri Anggraeni, Tab System Log aktor, dan Activity Log, serta jumlah entri `Remove (via Group Manager)` pada modal Changelog User > Group Role dan > Transaction Role Putri Anggraeni sebagai baseline
2. Ketik Search `Putri Anggraeni`, tekan Enter
3. Klik ⋯ pada baris Putri Anggraeni lalu klik `Edit Home Group`
4. Klik node IT Infrastructure lalu klik `[Select]`
5. Verifikasi dialog D-10 mendaftar pencabutan di luar constraint `Manage user & role — Finance & Accounting`
6. Verifikasi dialog D-10 mendaftar pencabutan di luar constraint `Monitoring & Report — Damaged — Branch Surabaya`
7. Verifikasi dialog D-10 mendaftar pencabutan di luar constraint `Group Manager — Finance & Accounting`
8. Verifikasi baris pola Group Manager (Group Role dan Transaction Role) tidak didaftar satu per satu di dialog D-10
9. Klik `[Revoke]` pada dialog D-10
10. Verifikasi toast "Success, home group has been updated." tampil
11. Verifikasi tidak ada toast tambahan selain toast pada langkah 10
12. Verifikasi Home Group Putri Anggraeni pada baris menjadi IT Infrastructure
13. Klik Name `Putri Anggraeni`, klik Tab Role lalu Sub-tab Group Role
14. Verifikasi banner `This user is a Group Manager for:` tidak tampil (status Group Manager terlepas)
15. Verifikasi tidak ada baris pola Group Manager Finance & Accounting maupun Accounts Payable pada Sub-tab Group Role
16. Verifikasi Group Role non-pola Manage user & role pada Finance & Accounting (di luar IT Infrastructure) tidak ada (tercabut silent)
17. Klik Changelog icon pada Sub-tab Group Role
18. Verifikasi jumlah entri `Remove (via Group Manager)` pada modal bertambah 12 dibanding baseline
19. Verifikasi baris teratas sebanyak selisih (himpunan, urutan di antaranya tidak diasersi) masing-masing Action `Remove (via Group Manager)`, Old Value `Assigned`, New Value `—`, Field `[Role Name] — [Group Name]`, dan Modified By `Lina M`
20. Tutup modal Changelog
21. Klik Sub-tab Transaction Role
22. Verifikasi tidak ada baris pola Asset Admin maupun Approver pada Finance & Accounting dan Accounts Payable di Sub-tab Transaction Role
23. Verifikasi baris Transaction Role Disposal × Staff pada IT Infrastructure tetap ada
24. Verifikasi baris Transaction Role non-pola Damaged × Monitoring & Report pada Branch Surabaya (di luar IT Infrastructure) tidak ada (tercabut silent)
25. Klik Changelog icon pada Sub-tab Transaction Role
26. Verifikasi jumlah entri `Remove (via Group Manager)` pada modal bertambah 36 dibanding baseline
27. Verifikasi baris teratas sebanyak selisih (himpunan, urutan di antaranya tidak diasersi) masing-masing Action `Remove (via Group Manager)`, Old Value `Assigned`, New Value `—`, Field `[Transaction Type] — [Group Name] — [Role]`, dan Modified By `Lina M`
28. Tutup modal Changelog
29. Klik Tab Changelog
30. Verifikasi jumlah entri `Edit Home Group` pada Tab Changelog Putri Anggraeni bertambah 1 dibanding baseline
31. Verifikasi jumlah entri `Auto-Revert` dengan Field `Group Manager — Finance & Accounting` pada Tab Changelog Putri Anggraeni bertambah 1 dibanding baseline
32. Verifikasi jumlah entri yang memuat `(via Group Manager)` pada Tab Changelog Putri Anggraeni sama dengan baseline
33. Baca jumlah entri `Edit Home Group`, `Auto-Revert`, dan yang memuat `(via Group Manager)` pada Tab System Log aktor dan Activity Log
34. Verifikasi jumlah entri `Edit Home Group` dan `Auto-Revert` bertambah masing-masing 1 dibanding baseline pada Tab System Log aktor dan Activity Log
35. Verifikasi jumlah entri yang memuat `(via Group Manager)` sama dengan baseline pada Tab System Log aktor dan Activity Log
36. Pulihkan Home Group, status Group Manager, dan baris pola Putri Anggraeni ke Pre-setup #48 lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Langkah 4 TC-FA-SU-1095 ("Baca dialog D-10 lalu konfirmasi seperti pada TC-FA-SU-294") disalin utuh menjadi langkah 5 sampai 9 (S-04): baca dialog, lalu klik `[Revoke]` sesuai TC-FA-SU-294 dan TC-FA-SU-295. Asersi judul dialog dan teks tombol milik TC-FA-SU-294 tidak diulang karena bukan Expected TC-FA-SU-1095 (S-02).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (baseline), 2 (Search untuk menemukan baris target, R-16 dan R-23; kotak Search masih berisi nilainya sehingga Klik Name pada langkah 13 tidak diawali Search ulang), 20 dan 28 (tutup modal), 21, 29, 33, dan 36 (pemulihan).
- Anchor asersi absence (bagian 8b butir 2): langkah 5 sampai 7 untuk langkah 8; Table Tools Sub-tab dan tabel yang sudah termuat sebagai anchor permukaan untuk langkah 14, 15, 16, 22, dan 24 (dibuktikan juga oleh langkah 23); entri `Edit Home Group` pada langkah 30 untuk langkah 32; langkah 34 untuk langkah 35. Entri `(via Group Manager)` pada langkah 32 dan 35 dibandingkan dengan baseline langkah 1, sehingga audit trail yang sudah memuat entri serupa tidak membuat asersi salah.
- Langkah 19 dan 27 membaca baris teratas sebanyak selisih jumlah sebagai himpunan karena entri baru jatuh dalam menit yang sama (S-14); urutan di antaranya tidak diasersi.
- Langkah 11: TC menulis "tanpa toast tambahan" (T-13a); spec mengasersi bahwa toast pada langkah 10 satu-satunya yang tampil.
- Pencabutan silent Group Role dan Role Transaksi non-pola di luar constraint (TC-FA-SU-1095 Expected a dan e, gate Home Group): dialog mendaftar keduanya (langkah 5 dan 6), keduanya tidak ada sesudah konfirmasi (langkah 16 dan 24), dan Disposal × Staff pada IT Infrastructure (di dalam constraint) tetap (langkah 23). "Tanpa entri log" pada pencabutan itu diasersi lewat selisih tepat 12 (langkah 18) dan 36 (langkah 26) pada modal Changelog: hanya baris pola Group Manager yang bertambah.
- Jumlah langkah 36 (di atas 35 langkah) dengan alasan: satu TC (1095) memakai satu dialog D-10; Expected mencakup daftar dialog, pencabutan silent Group Role non-pola dan Role Transaksi non-pola, pencabutan per baris pola GM, dan log per baris, masing-masing satu Verifikasi pada seed yang sama.
- Temuan untuk QA:
  - Jumlah baris pola yang dicabut (12 Group Role dan 36 Transaction Role) diturunkan dari deskripsi Pre-setup #48, bukan dari Expected TC yang hanya menulis "per baris pola"; perlu dikonfirmasi pemilik TC.
  - Post Condition a TC-FA-SU-1095 ("satu notifikasi in-app view-only per grup terlepas terkirim ke Putri") tidak punya langkah observasi di TC sehingga tidak diasersi; Putri Anggraeni juga tidak punya email dan nama env password di Pre-setup TC.
  - Expected c menyebut "Modified By aktor" untuk entri modal; spec memakai `Lina M` (format `[First Name] [Last Initial]`, R-14).
  - Expected a menyebut dialog mendaftar `Manage user & role — Finance & Accounting`; nasib Group Role itu sesudah konfirmasi tidak punya Expected (hanya `Group Manager — Finance & Accounting` pada Field Auto-Revert) dan tidak diasersi.
  - Pre-setup TC memberi satu penugasan GM Putri pada Finance & Accounting (turunan Accounts Payable), sedangkan Expected b menyebut baris pola "Finance & Accounting serta Accounts Payable"; spec mengikuti Expected.
