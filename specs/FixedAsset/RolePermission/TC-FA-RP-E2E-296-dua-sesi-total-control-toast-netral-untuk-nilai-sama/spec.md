---
id: TC-FA-RP-E2E-296-dua-sesi-total-control-toast-netral-untuk-nilai-sama
title: "Dua sesi Total Control: edit, toggle, dan toggle registrasi bernilai sama menampilkan toast netral"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-276
  - TC-FA-RP-350
  - TC-FA-RP-372
coverage:
  web: automated
---

# Dua sesi Total Control: edit, toggle, dan toggle registrasi bernilai sama menampilkan toast netral

## Prerequisites

- Mode: FE+BE.
- Akun Sesi 1 (UI): Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Akun Sesi 2 (konteks browser kedua, objek asersi): Total Control kedua Rina Wulandari (Pre-setup #3), `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC2_PASSWORD`. Konteks ini dibuka dan ditutup di dalam tiap blok TC; sesi login browser terkait dihapus sebelum blok berikutnya (S-09). Sesi UI kedua dipakai karena toast Sesi 2 diasersi (kelas c, bagian 3 prinsip 13c); `P-2` tidak berlaku.
- Env var yang dipakai: `FA_TC_PASSWORD`, `FA_TC2_PASSWORD` (nama dan arti di `suite.md`, Env password akun aktor). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip, halaman awal, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup (Company Alpha; identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #15 (Ahmad Fauzi), #18 (pohon group), #19 (Require Approval OFF di semua node; Approver Pandu Wijaya hanya pada `IT Infrastructure`), #21 (pemegang Update `Manage asset & TAG`: Ahmad Fauzi di `Head Office`, Budi Santoso di `IT Infrastructure`, Dimas Pranata di `Data Center`; toggle Require Approval for Registration OFF).
- Seeding di hook `before` lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan): Ahmad Fauzi memegang Global Role `Manage accounting` dengan hanya Read aktif (TC-FA-RP-276); toggle `Require Approval for Disposal` pada `IT Infrastructure` OFF (TC-FA-RP-350); toggle `Require Approval for Registration` pada `IT Infrastructure` OFF (TC-FA-RP-372).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog Detail Role, modal Changelog, dan log Edit Require Approval sub-tab `Disposal` sebagai baseline sebelum aksi (S-12); membuka konteks browser kedua dengan login terpisah.
- State yang diubah dan pemulihannya: Create Ahmad Fauzi pada `Manage accounting`, toggle `Require Approval for Disposal` dan `Require Approval for Registration` pada `IT Infrastructure`. Hook `after` memulihkan Pre-setup #15, #19, dan #21 ke kondisi Tabel Data Uji Pre-setup TC lewat fixture backend yang disediakan tim FE/BE (suite.md, Hook suite).

## Test Steps

### TC-FA-RP-276: Edit dengan nilai yang sama dengan nilai tersimpan memunculkan toast netral tanpa entri log

1. Klik Tab `System`, klik Role Name `Manage accounting` pada section Global Role
2. Klik ikon Changelog di toolbar Detail Role `Manage accounting`, lalu catat jumlah entri sebagai baseline
3. Tutup modal Changelog
4. Ganti akun: buka konteks browser Sesi 2, login sebagai Total Control Rina Wulandari
5. Di Sesi 2, buka Fixed Asset > Settings > Role & Permission > Tab System, klik Role Name `Manage accounting` pada section Global Role
6. Ganti ke Sesi 1, centang Create pada baris Ahmad Fauzi
7. Verifikasi Sesi 1: muncul toast sukses: `Success, permissions have been updated.`
8. Ganti ke Sesi 2 (belum disegarkan), centang Create pada baris Ahmad Fauzi
9. Verifikasi Sesi 2: muncul toast netral (Info): `No changes to save.`
10. Ganti ke Sesi 1, klik ikon Changelog di toolbar Detail Role `Manage accounting`
11. Verifikasi jumlah entri Changelog bertambah tepat satu dibanding baseline
12. Verifikasi entri baru adalah Edit Create untuk Ahmad Fauzi
13. Tutup modal Changelog, lalu tutup konteks Sesi 2 dan hapus sesi login Sesi 2

### TC-FA-RP-350: Toggle atau radio dengan nilai yang sama memunculkan toast netral tanpa log

14. Klik Tab `Transaction Role`
15. Klik node `IT Infrastructure` pada Sidebar Group Tree
16. Klik sub-tab `Disposal`
17. Catat jumlah entri log Edit Require Approval sub-tab `Disposal` pada `IT Infrastructure` sebagai baseline lewat kemampuan baca
18. Buka konteks browser kedua dan login sebagai Total Control kedua (Rina Wulandari)
19. Sesi 2: klik Tab `Transaction Role`
20. Sesi 2: klik node `IT Infrastructure` pada Sidebar Group Tree
21. Sesi 2: klik sub-tab `Disposal`
22. Sesi 1: aktifkan toggle `Require Approval for Disposal`
23. Verifikasi Sesi 1 menampilkan toast sukses `Success, permissions have been updated.`
24. Sesi 2 (belum disegarkan): aktifkan toggle `Require Approval for Disposal`
25. Verifikasi Sesi 2 menampilkan toast netral (Info) `No changes to save.`
26. Verifikasi selisih jumlah entri log Edit Require Approval terhadap baseline langkah 17 tepat satu
27. Tutup konteks browser kedua dan hapus sesi login Sesi 2

### TC-FA-RP-372: Toggle registrasi dengan nilai sama, toast netral tanpa log

28. Klik Tab `System`
29. Buka Detail Role `Manage asset & TAG`
30. Klik node `IT Infrastructure` pada Sidebar Group Tree
31. Catat jumlah entri Changelog Detail Role `Manage asset & TAG` sebagai baseline lewat kemampuan baca
32. Buka konteks browser kedua dan login sebagai Total Control kedua (Rina Wulandari)
33. Sesi 2: klik Tab `System`
34. Sesi 2: buka Detail Role `Manage asset & TAG`
35. Sesi 2: klik node `IT Infrastructure` pada Sidebar Group Tree
36. Sesi 1: aktifkan toggle `Require Approval for Registration`
37. Tunggu aksi Sesi 1 selesai (toggle aktif kembali)
38. Sesi 2 (belum disegarkan): aktifkan toggle `Require Approval for Registration`
39. Verifikasi Sesi 2 menampilkan toast netral `No changes to save.`
40. Verifikasi selisih jumlah entri Changelog Detail Role `Manage asset & TAG` terhadap baseline langkah 31 tepat satu
41. Tutup konteks browser kedua dan hapus sesi login Sesi 2

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec kelas c (multi-konteks, bagian 3 prinsip 13c): ketiga TC memakai konteks browser kedua yang menjadi objek asersi (toast Sesi 2), bukan hanya pemicu state; `P-2` tidak berlaku. Satu jenis harness (dua sesi UI Total Control); ketiganya bertanda Manual Only (d) dua sesi paralel di TC.
- Pembagian TC lintas spec: TC-FA-RP-277 dan TC-FA-RP-278 ada di spec 081; TC-FA-RP-348, 349, 355, dan 360 ada di spec 105; TC-FA-RP-361 sampai TC-FA-RP-364 dan TC-FA-RP-371 ada di spec 108.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 sampai 6, 8, dan 10 (membuka tab, Detail Role, dan berpindah sesi); langkah 14 sampai 22 dan 24 (navigasi dan berpindah sesi); langkah 28 sampai 30, 32 sampai 36, dan 38 (navigasi dan berpindah sesi); langkah 3, 13, 27, dan 41 (menutup modal atau konteks Sesi 2, S-09); langkah 2, 17, dan 31 (baseline, S-12); langkah 37 (tunggu aksi selesai karena sesi berpindah sesudah aksi tanpa asersi, bagian 8b butir 8).
- Keadaan awal toggle OFF untuk TC-FA-RP-350 dan TC-FA-RP-372 (asumsi spec, lihat Temuan untuk QA) dijamin seeding hook `before` (Pre-setup #19 dan #21), sehingga spec ini tidak memuat langkah "Matikan toggle"; langkah itu hanya diperlukan bila toggle sudah ON oleh blok sebelumnya, dan urutan spec ini tidak menyalakannya sebelum blok yang mensyaratkan OFF.
- Klausa "hanya satu entri log" TC-FA-RP-276 butir c, TC-FA-RP-350 butir c, dan TC-FA-RP-372 butir b diasersi sebagai selisih jumlah entri terhadap baseline (langkah 11 dan 12, 26, dan 40), asersi jumlah dan bukan absence (bagian 3 prinsip 13g); isi entri Edit Create Ahmad Fauzi diperiksa pada langkah 12.
- Ukuran spec: 41 langkah, di atas batas sekitar 35 langkah. Alasan: ketiga blok berkelas sama (dua sesi UI Total Control sebagai objek asersi) dan tiap blok memerlukan pembukaan konteks kedua, navigasi di dua sesi, baseline, dan penutupan konteks sendiri (13 sampai 14 langkah per blok); kegagalan satu blok tidak membuat blok lain kehilangan makna, sedangkan hook, login Sesi 1, dan seeding dipakai bersama. Memecahnya menjadi tiga spec menambah tiga login dan hook tanpa mengurangi langkah (konvensi bagian 3, batas ukuran).
- Temuan untuk QA:
  - TC-FA-RP-276, 350, dan 372 bertanda `Manual Only — (d) dua sesi paralel` di TC; spec memakai konteks browser kedua (kelas c) dan mengasersinya.
  - TC-FA-RP-276 tidak menyebut keadaan awal Create pada baris Ahmad Fauzi; spec mengasumsikan hanya Read aktif (seed hook `before`).
  - TC-FA-RP-276 dan TC-FA-RP-372 menyebut "dua sesi Total Control" tanpa akun Sesi 2; spec memakai Total Control kedua Pre-setup #3 (Rina Wulandari).
  - TC-FA-RP-350 dan TC-FA-RP-372 tidak menyebut keadaan awal toggle; spec men-seed OFF di hook `before`.
  - TC-FA-RP-350 menyebut node dan sub-tab "yang sama" tanpa menyebut node; spec memakai `IT Infrastructure` sub-tab `Disposal` (satu-satunya node ber-Approver pada Pre-setup #19).
  - TC-FA-RP-372 tidak menyebut surface log yang dimaksud "entri log Edit"; spec memakai Changelog Detail Role `Manage asset & TAG`.
  - Post Condition TC-FA-RP-276, 350, dan 372 tidak memberi langkah observasi tambahan; tidak diasersi.
