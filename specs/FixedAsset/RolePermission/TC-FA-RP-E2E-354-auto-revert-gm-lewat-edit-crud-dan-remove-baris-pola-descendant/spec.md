---
id: TC-FA-RP-E2E-354-auto-revert-gm-lewat-edit-crud-dan-remove-baris-pola-descendant
title: "Edit CRUD baris pola GM pada node descendant memicu auto-revert D-05: GM lepas, seluruh baris pola dipertahankan"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1189
coverage:
  web: automated
---

# Edit CRUD baris pola GM pada node descendant memicu auto-revert D-05: GM lepas, seluruh baris pola dipertahankan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #13 (Kevin Susanto, Group Manager hanya di `Data Center`; baris pola GM di `Data Center` dan `Rack A1`: Group Role katalog selain `Manage user & role` dengan CRUD penuh; baris non-pola: Group Role `Manage user & role` di `Data Center`, Group Role `Manage files` Read dan Delete di `Helpdesk`, Global Role `Manage accounting` hanya Read), #18 (pohon Group; `Rack A1` adalah descendant `Data Center`), #24 (`Company Changelog`; dipakai sebagai latar log, tidak diasersi).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): membaca jumlah entri Changelog Detail Role `Manage group` dan jumlah entri ber-Action `Remove (via Group Manager)` di dalamnya sebagai baseline (langkah 1 dan 2) dan membaca nilai tersimpan baris Detail Role (langkah 11).
- State yang diubah dan pemulihannya: penugasan Group Manager Kevin Susanto di `Data Center` dilepas oleh langkah 13 (seluruh baris pola GM dipertahankan sebagai penugasan biasa; baris `Rack A1` yang diedit berubah menjadi Delete tidak tercentang). Hook `before` memastikan state Pre-setup #13 dan hook `after` memulihkannya (Group Manager `Data Center` beserta baris pola) lewat fixture backend yang disediakan tim FE/BE, tidak berasumsi langkah spec berhasil penuh (TC: "dipulihkan ke state Pre-setup #13 oleh automation baseline"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1189: Edit CRUD baris pola GM pada node descendant memicu auto-revert D-05

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Changelog Detail Role `Manage group`
2. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri ber-Action `Remove (via Group Manager)` pada Changelog Detail Role `Manage group`
3. Klik Tab `System`
4. Buka Detail Role `Manage group`
5. Klik node `Rack A1` pada Sidebar Group Tree
6. Hapus centang Delete pada baris Kevin Susanto
7. Verifikasi dialog severity danger: Title `Remove Group Manager`, Body `• Kevin S` lalu `This edit will remove Group Manager status for this group.` lalu `Their individual role permissions will remain as edited.` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` dan `[Remove]` (copy usulan, PRD 12 #7)
8. Klik `[Cancel]`
9. Verifikasi checkbox Delete baris Kevin Susanto kembali tercentang
10. Verifikasi tidak ada toast
11. Verifikasi tidak ada perubahan tersimpan pada Delete baris Kevin Susanto lewat kemampuan baca
12. Hapus centang Delete pada baris Kevin Susanto
13. Klik `[Remove]` pada dialog
14. Verifikasi toast sukses `Success, permissions have been updated. Kevin Susanto is no longer Group Manager for Data Center.`
15. Verifikasi baris Kevin Susanto tetap tampil pada node `Rack A1` dengan Delete tidak tercentang (baris yang diedit dipertahankan)
16. Klik node `Data Center` pada Sidebar Group Tree
17. Verifikasi baris Kevin Susanto tetap tampil pada node `Data Center` (baris pola dipertahankan)
18. Klik ikon Changelog Detail Role `Manage group`
19. Verifikasi jumlah entri Changelog bertambah dari baseline langkah 1
20. Verifikasi entri `Edit` Field `Delete` untuk `Rack A1` (aksi pemicu) tampil pada entri teratas sebanyak selisih
21. Verifikasi Modified By entri itu `Siti R`
22. Verifikasi jumlah entri ber-Action `Remove (via Group Manager)` sama dengan baseline langkah 2
23. Tutup modal Changelog
24. Klik Tab `Group Manager`
25. Verifikasi sedikitnya satu baris Group Manager lain tampil di Tab `Group Manager`
26. Verifikasi Kevin Susanto tidak ada di Tab `Group Manager`
27. Klik Tab `System`
28. Buka Detail Role `Manage files`
29. Klik node `Helpdesk` pada Sidebar Group Tree
30. Verifikasi baris non-pola Kevin Susanto di `Helpdesk` tidak berubah: Read dan Delete tetap tercentang
31. Klik Tab `System`
32. Buka Detail Role Global Role `Manage accounting`
33. Verifikasi baris Kevin Susanto di Global Role `Manage accounting` tidak berubah: hanya Read tercentang

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 33 langkah.
- Langkah penghubung (S-03): langkah 1 dan 2 (baseline Changelog, S-12), langkah 3 sampai 5, 16, 24, 27 sampai 29, dan 31 sampai 32 (navigasi Tab, Detail Role, node), langkah 23 (menutup modal Changelog). Tanpa Search pada tabel Detail Role: tiap node memuat paling banyak enam baris, dalam satu halaman (R-16). Langkah 25 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 26 (bagian 8b butir 2); langkah 9 menjadi anchor atas langkah 10; langkah 19 dan 20 menjadi anchor positif atas asersi langkah 22.
- Urutan langkah mengikuti keadaan: baris Kevin Susanto di `Rack A1` dan `Data Center` serta modal Changelog dibaca selagi Detail Role `Manage group` masih terbuka, lalu Tab `Group Manager` dan baris non-pola.
- Pembacaan Changelog langkah 19 sampai 22 memakai selisih jumlah entri terhadap baseline (S-12); entri baru dibaca pada baris teratas urutan default Date terbaru sebanyak selisih, tanpa mengasersi urutan di antaranya (S-14). Tidak ada asersi total entri. Langkah 22 bukan asersi kelas g (S-05, P-1): state auto-revert dibangun spec ini sendiri pada langkah 12 dan 13.
- Pembagian TC lintas spec: TC-FA-RP-1192 (Remove baris Approver pola GM, varian Role Transaksi) ada di spec 365.
- Fix pass 4 (keputusan: auto-revert GM mempertahankan baris): baris Kevin Susanto yang diedit dan baris pola `Data Center` tetap ada, tidak ada entri `Remove (via Group Manager)`, copy D-05 penutup `Their individual role permissions will remain as edited.`
- Temuan untuk QA:
  - TC-FA-RP-1189 Expected a menandai copy dialog D-05 sebagai `copy usulan, PRD 12 #7`; spec menulis teks TC apa adanya dan perlu diselaraskan bila PRD 12 #7 menetapkan lain.
  - Nama Action `Remove (via Group Manager)` di Changelog belum ditetapkan PRD; spec memakai nama dari TC sebagai pembanding baseline. Jumlah entri baru yang dihasilkan satu auto-revert tidak disebut TC; spec hanya mengasersi kenaikan terhadap baseline, entri aksi pemicu, dan tidak bertambahnya entri `Remove (via Group Manager)`.
  - Seed Kevin Susanto tidak konsisten antar sumber: Pre-setup #13 dan #43 hanya `Data Center`, Pre-setup #38 dan beberapa TC lain `Data Center` dan `Helpdesk`. Spec mengikuti #13 (Group Manager hanya di `Data Center`; `Helpdesk` hanya baris non-pola `Manage files`).
  - Post Condition "Kevin Susanto dipulihkan ke state Pre-setup #13" tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
  - Expected a menyebut "tidak ada perubahan tersimpan" tanpa indikator UI; spec memakai kemampuan baca (langkah 11).
  - Pre-setup #24 (`Company Changelog`) disebut Precondition tetapi TC tidak menyebut perannya; spec memakainya sebagai latar log tanpa asersi.
  - Interpretasi "baris yang diedit tetap ada dengan nilai hasil edit" dan "baris pola lain tetap ada" mengikuti keputusan PM terbaru (TC diperbarui).
