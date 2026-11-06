---
id: TC-FA-RP-E2E-388-gate-menilai-node-penugasan-baris-literal-descendant-tetap-eligible-di-luar-constraint-tidak
title: "Gate menilai node penugasan: baris literal, descendant tetap eligible, node di luar constraint tidak"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1227
coverage:
  web: automated
---

# Gate menilai node penugasan: baris literal, descendant tetap eligible, node di luar constraint tidak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #17 (Joko Santoso, Home Group `IT Infrastructure`; Active, Activated), #18 (pohon Group: `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`; `Head Office` > `Logistics Warehouse` > `Dock 1`), dan #19 (penugasan Role Transaksi `IT Infrastructure` sub-tab `Disposal`; `Helpdesk` tanpa baris penugasan manual dan memuat baris pola Asset Admin).
- Kemampuan teknis (disediakan tim FE/BE lewat fixture BE, tanpa endpoint karangan): seeding precondition TC di hook `before` berupa Joko Santoso tanpa penugasan Role Transaksi pada node mana pun (dipakai sebagai precondition TC, tidak diasersi), pencabutan baris Joko Santoso Asset Admin pada `IT Infrastructure` sub-tab `Disposal`, dan pemulihan Pre-setup #17 dan #19.
- State yang diubah dan pemulihannya: langkah 6 menambah baris Joko Santoso Asset Admin pada `IT Infrastructure` sub-tab `Disposal` (Pre-setup #19 bersama). Baris itu dicabut pada langkah 21 dan di hook `after` sebagai cadangan (tidak berasumsi langkah spec berhasil penuh) lewat fixture BE, sehingga Pre-setup #19 kembali ke kondisi Tabel Data Uji Pre-setup TC (jumlah header Asset Admin `IT Infrastructure` sub-tab `Disposal` kembali ke nilai sebelum spec). Entri Changelog yang tercatat tetap ada (audit trail permanen). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture. Spec ini tidak login sebagai Joko Santoso.

## Test Steps

### TC-FA-RP-1227: Gate Home Group menilai node penugasan: baris literal, descendant tetap eligible, node di luar constraint tidak

1. Klik Tab `Transaction Role`, klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Asset Admin
3. Ketik Search `Joko Santoso`, tekan Enter
4. Verifikasi Joko Santoso ada di daftar picker
5. Centang Joko Santoso
6. Klik `[Assign]`
7. Verifikasi muncul toast sukses: `Success, Asset Admin has been assigned.`
8. Verifikasi baris Joko Santoso tampil di section Asset Admin `IT Infrastructure`
9. Klik node `Helpdesk` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
10. Verifikasi section Asset Admin `Helpdesk` menampilkan sedikitnya satu baris
11. Verifikasi tidak ada baris Joko Santoso di section Asset Admin `Helpdesk` (baris literal hanya pada node penugasan; gate tidak mengevaluasi tiap descendant yang tercakup)
12. Klik `[+ Assign]` pada section Asset Admin
13. Ketik Search `Joko Santoso`, tekan Enter
14. Verifikasi Joko Santoso ada di daftar picker (descendant di dalam constraint; pemegang role yang sama di ancestor tidak disaring)
15. Tutup popup Assign lewat `[×]`
16. Klik node `Logistics Warehouse` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
17. Klik `[+ Assign]` pada section Asset Admin
18. Ketik Search `Joko Santoso`, tekan Enter
19. Verifikasi empty state `No results found` tampil sehingga Joko Santoso tidak ada di daftar picker (node di luar constraint)
20. Tutup popup Assign lewat `[×]`
21. Pulihkan lewat fixture BE: cabut baris Joko Santoso Asset Admin pada `IT Infrastructure` sub-tab `Disposal`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 21 langkah.
- Langkah penghubung (S-03): langkah 1, 9, dan 16 (navigasi Tab, node, sub-tab; sub-tab `Disposal` diklik ulang di tiap node agar sub-tab aktif deterministik), langkah 2, 12, dan 17 (membuka popup Assign), langkah 15 dan 20 (menutup popup, S-09), dan langkah 21 (pemulihan, S-09; hook `after` hanya cadangan). Langkah 3, 13, dan 18 adalah Search nama kandidat di Table User Picker yang dapat memuat lebih dari satu halaman (R-16, R-22); popup ditutup oleh `[Assign]` pada langkah 6 sehingga Search tidak perlu dibersihkan.
- Asersi absence langkah 11 didahului langkah 10 sebagai anchor positif (sedikitnya satu baris pembanding pada section yang sama; Pre-setup #19 menyatakan `Helpdesk` memuat baris pola Asset Admin) dan toast sukses langkah 7 menjadi anchor bahwa penugasan di `IT Infrastructure` sudah diproses server sebelum `Helpdesk` diamati (bagian 8b butir 2). Asersi absence langkah 19 memakai empty state `No results found` hasil Search sebagai anchor positif; langkah 4 dan 14 membuktikan Joko Santoso muncul di picker pada node yang memenuhi constraint.
- Langkah 10 adalah asersi tambahan di luar Expected TC yang dicatat sebagai anchor (S-03); TC tidak mendefinisikan baris pembanding.
- Pemeriksaan "tidak ada entri log" tidak diasersi (S-05; TC tidak memuatnya). Hak efektif pada modul konsumen tidak diasersi.
- Temuan untuk QA:
  - NC-20 / Open Item #9 (menunggu PM): arah gate Home Group sebagai constraint, termasuk baris literal per node penugasan dan descendant tetap eligible walau ancestor memegang role yang sama, belum dikonfirmasi PM; bila PM menetapkan lain, Expected 1227.a sampai 1227.e usang.
  - TC-FA-RP-1227 tidak memuat asersi preview scope popup dan PRD tidak memuat locator preview scope; spec tidak mengasersinya. Teks empty state `No results found` mengikuti pola picker pada spec lain di suite ini; TC hanya menyebut "tidak ada di daftar picker".
  - Spec menulis ke data Pre-setup bersama (`IT Infrastructure` sub-tab `Disposal`, Pre-setup #19) karena constraint Joko Santoso adalah `IT Infrastructure` dan TC menetapkan node itu sebagai node penugasan (S-06); target yang dibuat spec dicabut lewat fixture BE (langkah 21 dan hook `after`) dan efek pada Changelog dicatat di Prerequisites. Bila auditor menilai target harus data milik spec, TC perlu memberi node bersuffix dengan constraint yang sama.
  - Email Joko Santoso tidak tertulis di Pre-setup #17 dan tidak dipakai login oleh spec ini.
  - Precondition TC-FA-RP-1227 ("tanpa penugasan Role Transaksi") tidak menyebut cara membentuknya; spec menetapkannya lewat fixture BE yang disediakan tim FE/BE (kemampuan seeding dan pemulihan Pre-setup #17 belum punya nama di Pre-setup).
  - TC-FA-RP-1227.c "tidak ada baris Joko Santoso" tidak menyebut pembanding; spec menambah anchor langkah 10 dan mencatatnya di atas. Pencarian baris Joko Santoso di tabel Role Transaksi tidak memakai Search (TC tidak menyebutnya); tabel `Helpdesk` Asset Admin memuat baris pola dalam jumlah kecil (Pre-setup #19) sehingga baris dapat diamati tanpa paginasi.
  - Post Condition TC-FA-RP-1227 kosong ("-").
