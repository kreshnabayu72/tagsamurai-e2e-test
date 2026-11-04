---
id: TC-FA-RP-E2E-331-home-group-constraint-diabaikan-untuk-total-control-dan-read-only
title: "Home Group constraint diabaikan untuk Total Control dan Read Only"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1175
coverage:
  web: automated
---

# Home Group constraint diabaikan untuk Total Control dan Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Siti Rahmawati (Pre-setup #2), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #15 (Ahmad Fauzi, pool pengguna Standard), #17 (Gunawan Halim, Home Group `Data Center`), #18 (pohon Group), #39 (Detail Role `Manage files`; node `Helpdesk` memuat lima baris pola dan Budi Santoso, node `IT Infrastructure` hanya lima baris pola), #41 (kandidat popup Assign Total Control, termasuk Gunawan Halim).
- Precondition d TC (dipakai sebagai precondition TC, tidak diasersi; seeding di hook `before` lewat sesi API Total Control, kemampuan disediakan tim FE/BE tanpa endpoint karangan): Ahmad Fauzi di-seed berstatus Total Control dengan baris pola Group Role pada setiap group, tanpa Home Group; Gunawan Halim berstatus Standard dengan Home Group `Data Center`.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): Ahmad Fauzi dikembalikan ke state Pre-setup #15 (Standard, tanpa Home Group, tanpa baris pola), Gunawan Halim dikembalikan ke state Pre-setup #17 (Standard, Home Group `Data Center`, tanpa baris pola Total Control), mengikuti catatan "Pemulihan fixture destruktif" di TC dan Pre-setup #32; pemulihan dijamin fixture backend yang disediakan tim FE/BE.
- Data Dinamis: tidak ada data yang dibuat spec.
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1175: Home Group constraint diabaikan untuk Total Control dan Read Only

1. Buka Settings > User > Detail Ahmad Fauzi
2. Klik field Home Group, pilih `Data Center`, lalu klik `[Select]`
3. Verifikasi Home Group Ahmad Fauzi tersimpan `Data Center`
4. Verifikasi dialog `D-10` tidak tampil
5. Buka Detail Role Group Role `Manage files` dari Tab `System` pada Settings > Role & Permission
6. Klik node `Helpdesk` pada Sidebar Group Tree
7. Verifikasi baris pola Ahmad Fauzi di `Helpdesk` tetap ada
8. Buka Tab `Total Control` pada Settings > Role & Permission
9. Klik `[+ Assign]`
10. Ketik Search `Gunawan Halim` pada popup Assign, tekan Enter
11. Centang Gunawan Halim
12. Klik `[Assign]`
13. Verifikasi toast sukses `Success, Total Control has been assigned.`
14. Verifikasi tidak ada error constraint yang tampil
15. Buka Detail Role Group Role `Manage files` dari Tab `System` pada Settings > Role & Permission
16. Klik node `Helpdesk` pada Sidebar Group Tree
17. Verifikasi baris pola Gunawan Halim tampil di `Helpdesk`
18. Klik node `IT Infrastructure` pada Sidebar Group Tree
19. Verifikasi baris pola Gunawan Halim tampil di `IT Infrastructure`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 19 langkah.
- Langkah penghubung (S-03): langkah 5, 8, 9, 15 (navigasi dan membuka popup), langkah 10 dan 11 (Search kandidat Gunawan Halim pada Table User Picker yang memuat lebih dari sepuluh kandidat, Pre-setup #41; R-16 dan R-22), langkah 6, 16, dan 18 (memilih node). Langkah 14 mengasersi absence error constraint dengan anchor positif toast sukses langkah 13; langkah 4 mengasersi absence dialog `D-10` sesudah anchor langkah 3 (Home Group tersimpan).
- Detail User dibuka dengan satu langkah "Buka Settings > User > Detail Ahmad Fauzi" mengikuti TC (tanpa Search eksplisit), seperti spec 119. Tabel Detail Role tidak memakai Search: tiap node memuat paling banyak tujuh baris (lima baris pola, satu baris non-pola Pre-setup #39, dan satu baris Ahmad Fauzi atau Gunawan Halim), dalam satu halaman.
- Tab Total Control memuat sembilan baris sebelum dan sepuluh baris sesudah Assign (Pre-setup #36); Search tidak dipakai pada tab itu.
- Temuan untuk QA:
  - Judul TC menyebut baris pola ditulis "di semua group", sedangkan Expected d hanya menyebut `Helpdesk` dan `IT Infrastructure`; spec mengasersi kedua node itu sesuai Expected. `Data Center` (Home Group Gunawan Halim) tidak diasersi.
  - Precondition d menyatakan Ahmad Fauzi berstatus Total Control, sedangkan Pre-setup #15 menyebutnya pool Standard dan Pre-setup #36 menyebutnya di Tab Total Control; spec mengikuti precondition d dan seeding ulang disediakan tim FE/BE.
  - Expected a menulis "baris pola Group Role di luar constraint tidak didaftar dan tidak dicabut" sebagai keterangan dialog `D-10`; asersi "tidak dicabut" ada di langkah 7, dan "tidak didaftar" tercakup oleh absence dialog langkah 4.
  - Teks dialog `D-10` tidak disebut di TC ini (hanya id); asersi absence tidak memerlukan teksnya. Expected d tanpa teks error constraint; langkah 14 mengasersi tidak ada error constraint secara umum.
  - Post Condition ("dipulihkan ke state seed oleh automation baseline") tidak punya langkah observasi dan tidak diasersi; dipenuhi hook `after`.
  - Pernyataan Pre-setup bersama di `suite.md` belum menyebut Pre-setup #39; pemulihannya dijamin tim FE/BE.
