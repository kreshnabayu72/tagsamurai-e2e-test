---
id: TC-FA-SU-E2E-102-popup-select-home-group-role-count-dan-popup-tree-group-search-dan-restriksi-node
title: "Popup Select Home Group, Role Count, dan Popup Tree Group: Search dan Restriksi Node"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-905
  - TC-FA-SU-906
  - TC-FA-SU-907
coverage:
  web: automated
---

# Popup Select Home Group, Role Count, dan Popup Tree Group: Search dan Restriksi Node

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Aktor kedua dan ketiga berganti akun lewat langkah eksplisit.
- Aktor Manage global user & role (Update) Qori Akbar (Pre-setup #4), kredensial `Spectra.env.FA_MURG_UPD_PASSWORD`; email akun ini tidak tertulis di Pre-setup TC (disediakan tim FE).
- Aktor Manage user & role Group (Update) Sinta Dewi (Pre-setup #6; Group Role Manage user & role pada Finance & Accounting), kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`; email akun ini tidak tertulis di Pre-setup TC (disediakan tim FE). Hook `after` memulihkan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23), Transaction Role (#39). Pengguna: Wawan Setiawan (label `7 roles`, 7 assignment Group Role), Mira Anggraini (Transaction Role pada Finance & Accounting), dan Gita Permata (target popup Edit Home Group). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-906: Popup Role Count (Total Control)

1. Ketik Search `Wawan Setiawan`, tekan Enter
2. Klik label jumlah `7 roles` pada baris Wawan Setiawan
3. Verifikasi header `Active Roles (7)` dengan close `[✕]` tampil
4. Verifikasi seksi `Group Role` tampil dan seksi kosong `Global Role` serta `Transaction Role` tidak tampil
5. Verifikasi bullet Group Role berformat `[Role Name] — 1 group` atau `[Role Name] — [N] groups` (`Manage files — 2 groups`, `Manage group — 3 groups`, `Manage purchase — 2 groups`)
6. Verifikasi urutan bullet A-Z per Role Name (Manage files, Manage group, Manage purchase)
7. Hover salah satu bullet
8. Verifikasi tidak ada tooltip hover
9. Klik backdrop
10. Verifikasi popup tidak tertutup
11. Tekan Esc
12. Verifikasi popup tertutup
13. Klik label jumlah `7 roles` pada baris Wawan Setiawan
14. Klik `[✕]`
15. Verifikasi popup tertutup

### TC-FA-SU-905: Search popup Select Home Group dan restriksi node (Manage global user & role)

16. Ganti akun: Logout lalu login sebagai Manage global user & role (Update) Qori Akbar
17. Buka Fixed Asset > Settings > User dari sidebar
18. Ketik Search `Gita Permata`, tekan Enter
19. Klik ⋯ pada baris Gita Permata lalu klik `Edit Home Group`
20. Verifikasi pohon menampilkan seluruh pohon entitas (Finance & Accounting, IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse, Region Jawa)
21. Verifikasi tidak ada node Disabled `already assigned`
22. Ketik Search `Surabaya`, tekan Enter
23. Verifikasi node Branch Surabaya tampil
24. Verifikasi node Finance & Accounting tidak tampil
25. Ganti isi kotak Search dengan `zzz`, tekan Enter
26. Verifikasi empty state `No results found` dan `Try adjusting your search or filter.` tampil
27. Klik `[Cancel]`

### TC-FA-SU-907: Popup tree Group pada modal Assign Transaction Role (Manage user & role Group)

28. Ganti akun: Logout lalu login sebagai Manage user & role Group (Update) Sinta Dewi
29. Buka Fixed Asset > Settings > User dari sidebar
30. Ketik Search `Mira Anggraini`, tekan Enter
31. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role
32. Buka modal Assign Transaction Role lalu buka popup tree Group
33. Verifikasi popup tree Group hanya menampilkan Finance & Accounting dan Accounts Payable
34. Ketik Search `Account`, tekan Enter
35. Verifikasi node Accounts Payable tampil
36. Ganti isi kotak Search dengan `zzz`, tekan Enter
37. Verifikasi empty state `No results found` tampil

## Notes

- Jumlah langkah 37, di atas smell 35 langkah; semua blok satu kelas harness (popup pilih Home Group dan tree grup, tanpa mengubah data) dan berdiri sendiri; kelebihan berasal dari Search per baris target (R-16) dan satu Verifikasi per klausa Expected (S-01).
- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Role Matrix ringan (bagian 3a): tiga aktor dengan langkah berbeda sehingga ditulis per blok aktor; ganti akun menuntut langkah eksplisit (akun pertama login di hook `before`).
- Urutan TC sumber diubah: TC-FA-SU-906 (Total Control, akun hook) diletakkan lebih dulu, lalu TC-FA-SU-905 dan TC-FA-SU-907, supaya ganti akun hanya dua kali.
- Langkah penghubung (tanpa awalan `Verifikasi`): menutup popup (Esc, `[✕]`, `[Cancel]`), ganti akun, membuka sidebar Fixed Asset > Settings > User sesudah tiap ganti akun (langkah 17 dan 29, S-14), Search untuk menemukan baris target (langkah 1, 18, dan 30; R-16 dan butir 8b.13), dan membuka ulang popup Role Count.
- Temuan untuk QA (S-15): (1) TC-FA-SU-906 Expected a menyebut seksi `Global Role`, `Group Role`, `Transaction Role` dipisah divider; Wawan Setiawan hanya memiliki Group Role sehingga divider dan format Transaction Role (`[Role] — [Transaction] — 1 group`) tidak teramati. (2) TC-FA-SU-907 tidak menyebut pengguna target; spec memakai Mira Anggraini (Transaction Role pada Finance & Accounting, Pre-setup #39). (3) TC-FA-SU-905 tidak menyebut pengguna target Edit Home Group; spec memakai Gita Permata. Expected b ("Total Control, Default User, dan Manage global user & role melihat seluruh pohon") hanya diamati untuk aktor Manage global user & role. (4) Keyword tanpa hasil ditulis `zzz`. (5) Email akun Manage global user & role (Update) dan Manage user & role Group (Update) tidak tertulis di Pre-setup TC.
