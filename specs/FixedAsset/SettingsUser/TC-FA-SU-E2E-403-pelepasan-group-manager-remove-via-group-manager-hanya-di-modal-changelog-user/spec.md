---
id: TC-FA-SU-E2E-403-pelepasan-group-manager-remove-via-group-manager-hanya-di-modal-changelog-user
title: "Pelepasan Group Manager: Tanpa Entri Remove (via Group Manager) per Baris Pola di Surface Mana Pun dan Tanpa Notifikasi Tambahan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1098
coverage:
  web: automated
---

# Pelepasan Group Manager: Tanpa Entri Remove (via Group Manager) per Baris Pola di Surface Mana Pun dan Tanpa Notifikasi Tambahan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun kedua (ganti akun eksplisit di langkah 38): Putri Anggraeni (Pre-setup #20 dan #48). Email dan kredensial disediakan tim FE; Pre-setup TC dan `suite.md` tidak memuat email maupun nama env password akun ini (lihat Temuan untuk QA).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), penugasan (Pre-setup #23), dan varian Group Manager (Pre-setup #48).
- Pengguna target: Putri Anggraeni, Group Manager Finance & Accounting (turunan: Accounts Payable) dengan baris pola Group Manager pada kedua node (Pre-setup #48).
- Data uji (precondition TC, langkah 3 sampai 7 menyalin utuh aksi pelepasan TC-FA-SU-1082, tanpa asersi Expected-nya): baris Manage files × Accounts Payable, centang Delete dihapus, dialog `Remove Group Manager` dikonfirmasi lewat `[Remove]`. Aktor pemicu: Ahmad Dahlan.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan Putri Anggraeni ke Pre-setup #48; pembacaan jumlah entri `Remove (via Group Manager)` pada modal Changelog Group Role dan Transaction Role (selisih nol diasersi), jumlah entri `Auto-Revert` pada Tab Changelog target, Modal Combined Changelog, Tab System Log aktor, dan Activity Log FAMS, serta jumlah notifikasi in-app Putri Anggraeni sebelum aksi sebagai baseline (bagian 8b butir 10). Entri log dan notifikasi muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: status Group Manager Putri Anggraeni dan baris Manage files × Accounts Payable (seluruh baris pola lain dipertahankan sebagai baris biasa); dipulihkan ke Pre-setup #48 lewat seed API pada langkah penghubung dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### Pelepasan Group Manager Putri Anggraeni (precondition TC-FA-SU-1098)

1. Catat baseline: jumlah entri `Remove (via Group Manager)` pada modal Changelog Group Role dan Transaction Role, jumlah entri `Auto-Revert` pada Tab Changelog Putri Anggraeni, Modal Combined Changelog, Tab System Log aktor, dan Activity Log FAMS, serta jumlah notifikasi in-app Putri Anggraeni
2. Ketik Search `Putri Anggraeni`, tekan Enter, lalu klik Name `Putri Anggraeni`
3. Klik Tab Role lalu Sub-tab Group Role
4. Klik `[Assign Group]` pada baris Manage files
5. Hapus centang Delete pada Accounts Payable
6. Klik `[Save]`
7. Klik `[Remove]` pada dialog `Remove Group Manager`
8. Tunggu aksi selesai (toast sukses tampil dan banner Group Manager hilang)

### TC-FA-SU-1098: Auto-Revert Group Manager tidak menulis `Remove (via Group Manager)` per baris di surface mana pun, termasuk dua Modal Changelog User, dan tanpa notifikasi tambahan

9. Klik Changelog icon pada Sub-tab Group Role
10. Verifikasi modal Group Role memuat entri aksi pemicu untuk baris Manage files × Accounts Payable
11. Verifikasi modal Group Role tidak memuat entri `Remove (via Group Manager)` untuk baris pola mana pun (jumlah sama dengan baseline)
12. Verifikasi baris pola Group Role yang dipertahankan tidak mendapat entri apa pun (entri baru pada modal Group Role dibanding baseline hanya entri aksi pemicu)
13. Ketik Search `via Group Manager` pada modal Group Role
14. Verifikasi Search `via Group Manager` pada modal Group Role tidak menampilkan baris
15. Tutup modal Group Role
16. Klik Sub-tab Transaction Role lalu klik Changelog icon
17. Verifikasi modal Transaction Role tampil
18. Verifikasi modal Transaction Role tidak memuat entri `Remove (via Group Manager)` untuk baris pola mana pun (jumlah sama dengan baseline)
19. Ketik Search `via Group Manager` pada modal Transaction Role
20. Verifikasi Search `via Group Manager` pada modal Transaction Role tidak menampilkan baris
21. Tutup modal Transaction Role
22. Klik Sub-tab Global Role lalu klik Changelog icon
23. Verifikasi modal Changelog Global Role tampil
24. Verifikasi modal Global Role tidak memuat entri `(via Group Manager)`
25. Tutup modal Global Role
26. Buka Tab Changelog, ketik Search `Putri Anggraeni`, tekan Enter, lalu muat ulang sampai entri tampil
27. Verifikasi tepat satu entri `Auto-Revert` Object `Group Manager` untuk Finance & Accounting bertambah dibanding baseline di Tab Changelog
28. Verifikasi Tab Changelog tidak memuat entri `(via Group Manager)` dan entri baru lain hanya entri aksi pemicu
29. Buka Modal Combined Changelog, lalu muat ulang sampai entri tampil
30. Verifikasi tepat satu entri `Auto-Revert` Object `Group Manager` untuk Finance & Accounting bertambah dibanding baseline di Modal Combined Changelog
31. Verifikasi Modal Combined Changelog tidak memuat entri `(via Group Manager)` dan entri baru lain hanya entri aksi pemicu
32. Buka Tab System Log aktor, lalu muat ulang sampai entri tampil
33. Verifikasi tepat satu entri `Auto-Revert` Object `Group Manager` untuk Finance & Accounting bertambah dibanding baseline di Tab System Log aktor
34. Verifikasi Tab System Log aktor tidak memuat entri `(via Group Manager)` dan entri baru lain hanya entri aksi pemicu
35. Buka Activity Log FAMS, lalu muat ulang sampai entri tampil
36. Verifikasi tepat satu entri `Auto-Revert` Object `Group Manager` untuk Finance & Accounting bertambah dibanding baseline di Activity Log
37. Verifikasi Activity Log tidak memuat entri `(via Group Manager)` dan entri baru lain hanya entri aksi pemicu
38. Logout lalu login sebagai Putri Anggraeni
39. Buka panel notifikasi lalu muat ulang sampai notifikasi tampil
40. Verifikasi Putri Anggraeni menerima satu notifikasi in-app view-only untuk grup yang terlepas (Finance & Accounting), bertambah satu dibanding baseline
41. Tunggu 5 detik tanpa memuat ulang halaman
42. Verifikasi tidak ada notifikasi tambahan untuk pencabutan baris pola (jumlah notifikasi tetap bertambah satu dibanding baseline)
43. Pulihkan Putri Anggraeni ke Pre-setup #48 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 8, 15, 21, 25, 41 dan 43. Langkah 3 sampai 7 menyalin utuh aksi pelepasan TC-FA-SU-1082 sebagai precondition tanpa asersi (S-04); pelepasan itu dijalankan di spec ini sendiri sehingga spec tidak bergantung pada hasil spec lain. Search `Putri Anggraeni` pada langkah 2 dan 26 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline log dan notifikasi mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #48 (S-06, S-09).
- TC-FA-SU-1082 (dialog dan hasil pelepasan, baris pola dipertahankan) ada di spec 392.
- Langkah pola baca-log: langkah 9 sampai 37 (buka surface, muat ulang sampai entri tampil, lalu `Verifikasi` kolom log). Blok ini tidak dihitung terhadap ambang sekitar 35 langkah. Spec ini 43 langkah: satu TC dengan satu pelepasan berat dan sepuluh surface yang dibaca, tiap Expected wajib satu `Verifikasi` (S-01); memecahnya menyalin ulang aksi pelepasan (S-04) dan memisahkan baseline bersama.
- TC-FA-SU-1098 diasersi sebagai absence: Auto-Revert tidak menulis `Remove (via Group Manager)` per baris pola di surface mana pun. Tiap absence ditulis sebagai `Verifikasi` berbaseline di spec ini dengan butir `P-1` (S-05): asersinya melekat pada state berat yang dibangun langkah 3 sampai 7 di spec yang sama. Anchor positifnya adalah entri aksi pemicu pada modal Group Role (langkah 10, untuk langkah 11 sampai 14), modal Transaction Role tampil (langkah 17, untuk langkah 18 sampai 20), modal Global Role tampil (langkah 23, untuk langkah 24), serta entri `Auto-Revert` yang tampil pada surface yang sama (langkah 27, 30, 33 dan 36 untuk langkah 28, 31, 34 dan 37: Tab Changelog, Modal Combined Changelog, Tab System Log aktor, dan Activity Log). Spec absence tidak memuat aksi nyata untuk TC ini.
- Absence notifikasi tambahan pada langkah 42 didahului anchor positif langkah 40 dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 41), pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Entri `Remove (via Group Manager)` per baris hanya ada pada jalur penghapusan (Edit Home Group, TC-FA-SU-1095); jalur itu tidak diasersi di spec ini.
- Temuan untuk QA:
  - Putri Anggraeni dipakai sebagai aktor notifikasi (langkah 38) tetapi tidak ada baris aktor Pre-setup untuknya dan `suite.md` tidak mendaftarkan nama env password untuknya; spec tidak membuat nama env baru dan menuliskan kebutuhan itu di Prerequisites. Mohon didaftarkan.
  - TC-FA-SU-1098 versi sebelumnya mengasersi entri `Remove (via Group Manager)` per baris pola; keputusan terbaru membalik asersinya (Auto-Revert hanya melepas penugasan GM dan mempertahankan baris pola). Judul spec ini diperbarui; slug `id` dan folder tidak diubah (tanpa penomoran ulang) sehingga masih memuat kata lama.
  - TC-FA-SU-1098 Expected a menyebut entri aksi pemicu sebagai `Edit` untuk baris Manage files × Accounts Payable tanpa jumlah; spec mengasersi keberadaan entri untuk baris itu tanpa mengasersi Action maupun jumlah.
  - TC-FA-SU-1098 Expected a ("baris pola yang dipertahankan tidak mendapat entri apa pun") tidak punya cara observasi langsung; spec membandingkan entri baru modal Group Role dengan baseline dan mengasersi hanya entri aksi pemicu yang bertambah (langkah 12).
  - TC-FA-SU-1098 Expected c ("Search `via Group Manager` tidak menampilkan baris") tidak menyebut tampilan hasil kosong; spec mengasersi tidak ada baris pada kedua modal tanpa mengasersi teks empty state.
  - TC-FA-SU-1098 Expected c menyebut "entri aksi pemicu" tanpa Action pada surface selain modal Group Role; belum jelas apakah baris pemicu `Edit` dicatat. Spec mengasersi entri baru lain hanya entri aksi pemicu tanpa jumlah.
  - TC-FA-SU-1098 Expected d menyebut copy `notification.md` §5.1f tanpa teks persis; spec tidak mengasersi teks notifikasi.
  - TC-FA-SU-1098 menyebut "tepat satu entri per grup" pada precondition yang hanya melepas satu grup Group Manager (Finance & Accounting); spec mengasersi satu entri `Auto-Revert`.
  - Precondition TC-FA-SU-1098 butir d ("TC-FA-SU-1082 sudah dijalankan") digantikan salinan aksi pelepasan pada langkah 3 sampai 7 (S-04).
