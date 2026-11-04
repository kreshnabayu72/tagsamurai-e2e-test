---
id: TC-FA-RP-E2E-336-multi-konteks-notifikasi-auto-revert-varian-role-transaksi
title: "Multi-konteks: notifikasi auto-revert varian Role Transaksi untuk Total Control dan Read Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1164
coverage:
  web: automated
---

# Multi-konteks: notifikasi auto-revert varian Role Transaksi untuk Total Control dan Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #3 (Rina Wulandari, Total Control kedua dengan baris pola Transaction Role Asset Admin dan Approver; target blok pertama) `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, #12 (Maya Anggraeni, Read Only dengan baris pola Monitoring & Report; target blok kedua), #18 (pohon group: `IT Infrastructure`), #19 (seed Role Transaksi sub-tab `Disposal`).
- Sesi UI kedua: konteks browser terpisah yang login sebagai akun target dan menjadi objek asersi notifikasi (pengecualian `P-2` tidak berlaku karena sesi kedua adalah objek asersi, bukan pemicu); satu sesi per blok, ditutup di akhir blok (S-09). Rina Wulandari memakai `Spectra.env.FA_TC2_PASSWORD`. Email dan password Maya Anggraeni tidak tertulis di Pre-setup TC dan belum punya nama env di `suite.md`; disediakan tim FE (lihat Temuan untuk QA).
- Format `[Date]` pada Body notifikasi mengikuti General Settings (Pre-setup #34, Date Format); nilai `[Date]` adalah tanggal aksi pemicu. `[Admin Name]` adalah Siti Rahmawati (aktor).
- Notifikasi: Title dan Body mengikuti TC (katalog notifikasi `fixed-asset/notification/PRD/notification.md` dirujuk TC; `fixed-asset/settings-role-permission/PRD/settings-role-permission.md §8.8`). Overlay Notifikasi dibuka dari Bell icon navbar.
- Kemampuan teknis: membaca jumlah notifikasi in-app per penerima (baseline langkah 1 dan 13) lewat kemampuan baca yang disediakan tim FE/BE, tanpa endpoint karangan. Jendela asersi notifikasi: "Tunggu 5 detik tanpa memuat ulang halaman" (pilihan spec, bukan nilai TC atau PRD; langkah 10 dan 20).
- State yang diubah dan pemulihannya: Remove baris pola (D-04) melepas tier Total Control Rina Wulandari (langkah 5) dan tier Read Only Maya Anggraeni (langkah 15) beserta baris pola. Hook `after` memulihkan keduanya ke Pre-setup #3 dan #12 lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #3 dan #12"), tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`, `FA_TC2_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1164: Notifikasi auto-revert varian Role Transaksi: Total Control (Rina Wulandari)

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah notifikasi Rina Wulandari dengan Title `Your Total Control access was removed`
2. Klik Tab `Transaction Role`
3. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
4. Klik `[⋯]` baris Rina Wulandari di section Approver lalu `Remove`
5. Klik `[Remove]` pada dialog konfirmasi `D-04`
6. Tunggu aksi selesai: dialog tertutup
7. Buka sesi UI kedua, login sebagai Rina Wulandari, lalu klik Bell icon
8. Verifikasi notifikasi baru Title `Your Total Control access was removed` dengan Body `Siti Rahmawati removed your Total Control access on [Date].` tampil, `[Date]` terformat sesuai General Settings
9. Verifikasi notifikasi itu view-only: hanya tombol `[Mark as Read]` tanpa tombol navigasi atau CTA lain
10. Tunggu 5 detik tanpa memuat ulang halaman
11. Verifikasi jumlah notifikasi Title `Your Total Control access was removed` bertambah tepat satu terhadap baseline langkah 1 (satu notifikasi per user, tidak ada notifikasi per baris pola)
12. Tutup sesi UI kedua

### TC-FA-RP-1164: Notifikasi auto-revert varian Role Transaksi: Read Only (Maya Anggraeni)

13. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah notifikasi Maya Anggraeni dengan Title `Your Read Only access was removed`
14. Klik `[⋯]` baris Maya Anggraeni di section Monitoring & Report pada sub-tab `Disposal` node `IT Infrastructure` lalu `Remove`
15. Klik `[Remove]` pada dialog konfirmasi `D-04`
16. Tunggu aksi selesai: dialog tertutup
17. Buka sesi UI kedua, login sebagai Maya Anggraeni, lalu klik Bell icon
18. Verifikasi notifikasi baru Title `Your Read Only access was removed` dengan Body `Siti Rahmawati removed your Read Only access on [Date].` tampil, `[Date]` terformat sesuai General Settings
19. Verifikasi notifikasi itu view-only: hanya tombol `[Mark as Read]` tanpa tombol navigasi atau CTA lain
20. Tunggu 5 detik tanpa memuat ulang halaman
21. Verifikasi jumlah notifikasi Title `Your Read Only access was removed` bertambah tepat satu terhadap baseline langkah 13 (satu notifikasi per user, tidak ada notifikasi per baris pola)
22. Tutup sesi UI kedua

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular (satu TC, dua blok penerima). Spec ini memuat 22 langkah.
- Kelas c (multi-konteks): sesi UI kedua akun target menjadi objek asersi notifikasi in-app; aktor pemicu tetap Total Control pada sesi utama. Pengecualian `P-2` tidak dipakai.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 13 (baseline jumlah notifikasi per penerima, S-12 dan bagian 8b butir 10), langkah 2 dan 3 (membuka Tab dan sub-tab; sesi utama tetap di `IT Infrastructure` sub-tab `Disposal` untuk blok kedua), langkah 6 dan 16 (tunggu aksi selesai sebelum berpindah sesi, bagian 8b butir 8), langkah 10 dan 20 (jendela 5 detik; bagian 6 dan 8b butir 11), langkah 12 dan 22 (penutupan sesi UI kedua, S-09). Akun aktor pertama sudah login di hook `before` (S-07).
- Login sesi UI kedua pada langkah 7 dan 17 adalah ganti akun eksplisit (S-07); Bell icon langsung diklik sesudah login karena halaman landing sesi kedua menampilkan navbar.
- Anchor absence: asersi "tidak ada notifikasi per baris pola" ditulis sebagai selisih jumlah tepat satu (langkah 11 dan 21) sesudah langkah 8 dan 18 (notifikasi tampil, anchor positif) dan jendela 5 detik.
- Search tidak dipakai untuk menemukan baris Rina Wulandari dan Maya Anggraeni: section Approver dan Monitoring & Report `IT Infrastructure` sub-tab `Disposal` memuat baris Pre-setup #19 dan baris pola, tidak melebihi satu halaman.
- Pembagian TC lintas spec: TC-FA-RP-1163 (log Transaction Role per baris pola) ada di spec 335. Spec 322, 324, dan 342 merujuk TC-FA-RP-1164 sebagai tempat pembuktian notifikasi. Nomor cadangan 349 dan 350 tidak dipakai.
- Temuan untuk QA:
  - TC-FA-RP-1164 langkah 1 menyebut "satu baris pola milik Rina Wulandari" dan langkah 3 "baris Monitoring & Report Maya Anggraeni" tanpa menyebut node dan sub-tab; spec memakai `IT Infrastructure` sub-tab `Disposal` (baris Approver untuk Rina, Monitoring & Report untuk Maya).
  - Akun login Rina Wulandari memakai `FA_TC2_PASSWORD` (Pre-setup #3); email dan password login Maya Anggraeni tidak tertulis di Pre-setup TC dan belum punya nama env di `suite.md`. Spec tidak mengarang nama env; disediakan tim FE.
  - Body notifikasi pada TC memakai placeholder `[Admin Name]`; spec memakai nama aktor `Siti Rahmawati` (selaras spec 262) dan `[Date]` terformat sesuai General Settings tanpa nilai tanggal tertulis.
  - Expected a dan b menyebut notifikasi "view-only"; spec menerjemahkannya sebagai hanya tombol `[Mark as Read]` tanpa CTA, mengikuti pola spec 262. TC tidak menyebut tombol itu secara eksplisit.
  - Expected c "Tidak ada notifikasi per baris pola" tidak menyebut cara membaca jumlah notifikasi; spec memakai baseline per penerima dan kemampuan baca yang disediakan tim FE/BE.
  - Post Condition "Rina Wulandari dan Maya Anggraeni dipulihkan ke state Pre-setup #3 dan #12" tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
  - Langkah TC 3 ("Ulangi dengan Remove baris Monitoring & Report Maya Anggraeni") tidak menyebut apakah konfirmasi `D-04` juga muncul untuk Read Only; spec mengonfirmasi dialog dengan `[Remove]` tanpa mengasersi teksnya.
