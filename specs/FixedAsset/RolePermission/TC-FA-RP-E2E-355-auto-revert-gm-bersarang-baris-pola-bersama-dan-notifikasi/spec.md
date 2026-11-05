---
id: TC-FA-RP-E2E-355-auto-revert-gm-bersarang-baris-pola-bersama-dan-notifikasi
title: "Auto-revert pada baris pola bersama penugasan GM bersarang: seluruh penugasan GM lepas, satu entri Auto-Revert dan satu notifikasi per penugasan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1188
coverage:
  web: automated
---

# Auto-revert pada baris pola bersama penugasan GM bersarang: seluruh penugasan GM lepas, satu entri Auto-Revert dan satu notifikasi per penugasan

## Prerequisites

- Mode: FE+BE.
- Akun:

| Urutan | Akun | Pre-setup | Email | Env password |
|---|---|---|---|---|
| 1 (hook `before`) | Total Control, Siti Rahmawati | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 (langkah 33, ganti akun eksplisit) | Dimas Pranata (Group Manager yang dilepas; memiliki akun login) | #15 | Email dan password akun ini tidak tertulis di Pre-setup TC dan belum punya nama env di `suite.md`; akun disediakan tim FE | disediakan tim FE |

- Login akun urutan 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #15 (Dimas Pranata, pengguna Standard; precondition TC: Group Manager di `IT Infrastructure` dan di `Data Center`, dengan baris pola Group Role `Manage files` bersama di `Data Center`; disiapkan lewat seed API di hook `before`), #18 (pohon Group), #24 (`Company Changelog`; dipakai sebagai latar log, tidak diasersi).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): membaca jumlah entri Changelog Tab Group Manager (baseline langkah 1), jumlah notifikasi in-app Dimas Pranata (baseline langkah 2), serta jumlah entri Changelog Detail Role `Manage files` dan jumlah entri ber-Action `Remove (via Group Manager)` di dalamnya (baseline langkah 3 dan 4). Jendela absence notifikasi "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD).
- State yang diubah dan pemulihannya: kedua penugasan Group Manager Dimas Pranata dilepas oleh langkah 10 (seluruh baris pola GM dipertahankan sebagai penugasan biasa; baris `Data Center` yang diedit berubah menjadi Delete tidak tercentang). Hook `after` memulihkan Dimas Pranata ke state Pre-setup #15 lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #15 oleh automation baseline"), tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1188: Auto-revert pada baris pola bersama penugasan GM bersarang

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Changelog Tab `Group Manager`
2. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah notifikasi in-app Dimas Pranata
3. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Changelog Detail Role `Manage files`
4. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri ber-Action `Remove (via Group Manager)` pada Changelog Detail Role `Manage files`
5. Klik Tab `System`
6. Buka Detail Role `Manage files`
7. Klik node `Data Center` pada Sidebar Group Tree
8. Hapus centang Delete pada baris Dimas Pranata
9. Verifikasi dialog D-05 varian pemicu edit: Body `• Dimas P` lalu `This edit will remove Group Manager status for this group.` lalu `Their individual role permissions will remain as edited.` dan `Are you sure you want to remove it?` (copy usulan, PRD 12 #7)
10. Klik `[Remove]` pada dialog
11. Verifikasi toast sukses berawalan `Success, permissions have been updated.`
12. Klik Tab `Group Manager`
13. Verifikasi sedikitnya satu baris Group Manager lain tampil di Tab `Group Manager`
14. Verifikasi tidak ada baris Dimas Pranata di `IT Infrastructure` maupun `Data Center` pada Tab `Group Manager`
15. Klik ikon Changelog di toolbar Tab `Group Manager`
16. Verifikasi jumlah entri Changelog bertambah tepat dua dari baseline langkah 1 (satu entri per penugasan GM yang lepas)
17. Verifikasi dua entri teratas ber-Action `Auto-Revert`: `Dimas Pranata — IT Infrastructure` dan `Dimas Pranata — Data Center`
18. Verifikasi Modified By kedua entri `Siti R`
19. Tutup modal Changelog
20. Klik Tab `System`
21. Buka Detail Role `Manage files`
22. Klik `All Groups` pada Sidebar Group Tree
23. Ketik Search `Dimas Pranata`, tekan Enter
24. Verifikasi baris Dimas Pranata tampil pada node `IT Infrastructure`, `Data Center`, dan descendant-nya (seluruh baris pola GM dipertahankan)
25. Verifikasi baris Dimas Pranata pada node `Data Center` tampil dengan Delete tidak tercentang (nilai hasil edit)
26. Klik ikon Changelog Detail Role `Manage files`
27. Verifikasi jumlah entri Changelog bertambah dari baseline langkah 3
28. Verifikasi entri `Edit` Field `Delete` untuk aksi pemicu tampil pada entri teratas sebanyak selisih
29. Verifikasi jumlah entri ber-Action `Remove (via Group Manager)` sama dengan baseline langkah 4
30. Tutup modal Changelog
31. Klik `(←)` pada kotak Search
32. Logout (ganti akun)
33. Login sebagai Dimas Pranata
34. Klik Bell icon
35. Verifikasi notifikasi `You are no longer Group Manager for IT Infrastructure` tampil
36. Verifikasi notifikasi `You are no longer Group Manager for Data Center` tampil
37. Tunggu 5 detik tanpa memuat ulang halaman
38. Verifikasi jumlah notifikasi Dimas Pranata bertambah tepat dua dari baseline langkah 2 (satu notifikasi per penugasan GM yang lepas)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 38 langkah.
- Alasan di atas sekitar 35 langkah (38 langkah): satu TC dengan satu aksi pemicu yang tidak dapat diulang (penugasan GM bersarang dilepas sekali) dan empat surface Expected (Tab `Group Manager`, Changelog Tab `Group Manager`, Detail Role beserta Changelog-nya, notifikasi Dimas Pranata) yang harus diamati dari aksi yang sama; memecahnya berarti mengulang aksi pemicu pada state yang sudah berubah. Empat langkah baseline menyumbang sebagian besar tambahan.
- Langkah penghubung (S-03): langkah 1 sampai 4 (baseline Changelog, notifikasi, dan Changelog Detail Role, S-12 dan bagian 8b butir 10), langkah 5 sampai 7, 12, 15, 20 sampai 22, dan 26 (navigasi), langkah 19 dan 30 (menutup modal Changelog), langkah 31 (mengosongkan Search sebelum ganti akun, S-09), langkah 37 (jendela notifikasi 5 detik, bagian 6). Langkah 23 memakai Search `Dimas Pranata` untuk menelusuri `All Groups` yang memuat lebih dari satu halaman (R-16 dan R-23). Langkah 13 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 14; langkah 35 dan 36 adalah anchor positif atas asersi selisih langkah 38; langkah 27 dan 28 adalah anchor positif atas asersi langkah 29.
- Ganti akun eksplisit (S-07): langkah 32 dan 33. Notifikasi login target disusun inline sebagai langkah akhir spec ini; Bell icon diklik langsung sesudah login karena navbar tampil di halaman landing.
- Pembacaan Changelog langkah 16 sampai 18 dan 27 sampai 29 memakai selisih jumlah entri terhadap baseline (S-12) dan entri teratas dibaca sebagai himpunan tanpa mengasersi urutan di antaranya (S-14). Langkah 29 bukan asersi kelas g (S-05, P-1): state auto-revert dibangun spec ini sendiri pada langkah 8 sampai 10.
- Fix pass 4 (keputusan: auto-revert GM mempertahankan baris): hasil Search `All Groups` kini mengasersi baris Dimas Pranata tetap ada (bukan empty state), tanpa entri `Remove (via Group Manager)`; copy D-05 penutup `Their individual role permissions will remain as edited.`
- Temuan untuk QA:
  - TC-FA-RP-1188 menandai copy dialog D-05 sebagai `copy usulan, PRD 12 #7`; Title dialog tidak disebut TC sehingga tidak diasersi.
  - Klausa group pada toast GM bersarang tidak ditetapkan PRD (Gap Spec); spec hanya mengasersi prefix `Success, permissions have been updated.`.
  - Teks notifikasi kedua ditulis TC sebagai `... for Data Center`; spec membacanya sebagai `You are no longer Group Manager for Data Center`. TC juga tidak menyebut apakah teks itu Title atau Body notifikasi; spec tidak membedakannya.
  - Email dan password login Dimas Pranata tidak tertulis di Pre-setup TC dan belum punya nama env di `suite.md`; spec tidak mengarang nama env (akun disediakan tim FE).
  - Expected b menyebut "dua entri `Auto-Revert`" tanpa menyebut kolom tempat teks `Dimas Pranata — <group>` tampil; spec membacanya sebagai isi entri.
  - Expected c menyebut "seluruh baris pola GM (di `IT Infrastructure`, `Data Center`, dan descendant-nya)" tanpa merinci Detail Role selain `Manage files`; spec menelusuri hasil Search `All Groups` pada Detail Role `Manage files` saja.
  - Post Condition "Dimas Pranata dipulihkan ke state Pre-setup #15" tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
