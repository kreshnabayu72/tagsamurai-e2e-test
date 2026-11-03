---
id: TC-FA-SU-E2E-012-popup-role-count-dan-empty-state-user-list
title: "Popup Role Count dan Empty State User List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-35
  - TC-FA-SU-36
  - TC-FA-SU-37
  - TC-FA-SU-38
coverage:
  web: automated
---

# Popup Role Count dan Empty State User List

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` dengan 25 pengguna (#20), penugasan (#23: Budi Santoso `4 roles`, Lina Marlina Total Control) dan Transaction Role (#39). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis (di-seed lewat API di hook `before`, dihapus di hook `after`):
  - Pengguna R `Pengguna Role Count {runId}-012`, email `rolecount+{runId}-012@qwertysystem.net`: Global Role aktif 1 (Import Data); Group Role Manage group di 3 grup (Finance & Accounting, Branch Surabaya, Logistics Warehouse); Transaction Role Approver Missing di 2 grup (Branch Surabaya, General Affairs). Label Role dan header popup R menjadi 6 (3 + 2 + Global Role aktif 1) menurut TC-FA-SU-36.
  - Pengguna G `Pengguna Group Manager Saja {runId}-012`, email `gmsaja+{runId}-012@qwertysystem.net`: Group Manager pada IT Infrastructure tanpa Global Role, Group Role, atau Transaction Role.
- Kemampuan teknis: seed API penugasan Global Role, Group Role, Transaction Role, dan Group Manager untuk pengguna dinamis (disediakan tim BE/FE); klik pada backdrop popup.
- State global: tidak ada yang diubah pada Pre-setup bersama. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-35: Popup Role Count: seksi, format bullet, urutan, dan angka header

1. Klik label `4 roles` pada Budi Santoso
2. Verifikasi header popup "Active Roles (4)" dengan ikon close ✕
3. Verifikasi seksi Global Role, Group Role, dan Transaction Role dipisah divider
4. Verifikasi seksi yang kosong tidak tampil
5. Verifikasi Group Role satu bullet per role dengan format "[Role Name] — 1 group" atau "[Role Name] — [N] groups" tanpa nama grup dan tanpa tooltip
6. Verifikasi Transaction Role satu bullet per kombinasi (Role × Jenis Transaksi) dengan format "[Role] — [Transaction] — [N] groups"
7. Verifikasi urutan bullet A-Z by Role Name (Transaction Role: Role lalu Transaction)
8. Verifikasi angka header dihitung per assignment sehingga dapat lebih besar dari jumlah bullet setelah konsolidasi
9. Tutup popup lewat ✕

### TC-FA-SU-36: Popup Role Count: label dan header memakai hitungan assignment yang sama

10. Ketik Search email pengguna R, tekan Enter
11. Verifikasi label kolom Role pengguna R `6 roles` (3 + 2 + Global Role aktif 1)
12. Klik label `6 roles` pada pengguna R
13. Verifikasi header popup "Active Roles (6)" sama dengan angka pada label kolom Role
14. Verifikasi jumlah bullet popup lebih kecil dari angka header karena satu Group Role di tiga grup menjadi satu bullet
15. Tutup popup lewat ✕

### TC-FA-SU-37: Popup Role Count: dismiss lewat ✕ dan Esc, klik backdrop tidak menutup, dan pengecualian tier

16. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
17. Klik label `4 roles` pada Budi Santoso
18. Klik backdrop popup
19. Verifikasi popup tidak tertutup oleh klik backdrop
20. Tekan Esc
21. Verifikasi popup tertutup oleh Esc
22. Klik label `4 roles` pada Budi Santoso
23. Klik tombol ✕ pada popup
24. Verifikasi popup tertutup oleh ✕
25. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter
26. Klik badge `Total Control` pada Lina Marlina
27. Verifikasi tidak ada popup role list yang terbuka dan badge tier tetap tampil di kolom Role
28. Ganti isi kotak search dengan email pengguna G, tekan Enter
29. Verifikasi kolom Role pengguna G `0 roles`
30. Klik `0 roles` pada pengguna G
31. Verifikasi status Group Manager tidak tampil di popup (tidak ada popup yang terbuka)

### TC-FA-SU-38: Empty state User List: hasil pencarian atau filter kosong

32. Ganti isi kotak search dengan `zzzz`, tekan Enter
33. Verifikasi empty state menampilkan ilustrasi 100x100, Title "No results found", dan Description "Try adjusting your search or filter."
34. Klik `(←)` pada kotak Search
35. Verifikasi Ahmad Dahlan (Default User) tampil di tabel sehingga empty state genuinely empty tidak berlaku

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9, 15 (menutup popup, S-09), langkah 10, 16, 25, 28, dan 32 (Search untuk menemukan baris target, R-16), langkah 34 (mengosongkan Search sebelum asersi baris Default User, S-09). Langkah 4, 19, dan 31 adalah asersi absence atau tidak tertutup; anchor positifnya adalah popup yang terbuka pada langkah 1 dan 17 serta kolom Role pengguna G pada langkah 29.
- Pembagian TC lintas spec: kolom Name, Role, dan Home Group User List (TC-FA-SU-9 sampai 11) ada di spec 004.
- Temuan untuk QA:
  - TC-FA-SU-35 Expected b dan d memuat seksi Group Role dan Transaction Role pada Budi Santoso, tetapi Pre-setup #23 dan #39 tidak merinci Group Role atau Transaction Role Budi Santoso; spec mengasersi format dan urutan dari data yang tampil dan membutuhkan Budi Santoso memiliki sedikitnya satu bullet Group Role dan satu bullet Transaction Role, yang perlu dijamin seed.
  - TC-FA-SU-37 Expected c ("Group Manager tanpa Global Role, Group Role, atau Transaction Role") tidak memiliki pengguna Pre-setup yang memenuhi syarat (Oscar Pranata memiliki 2 roles); spec memakai pengguna dinamis G.
  - TC-FA-SU-36 Langkah Uji 1 ("Siapkan assignment sesuai Data Uji") tidak menyebut nama Global Role aktif; spec memakai `Import Data` yang ada di Pre-setup #20, #23.
  - TC-FA-SU-36 Expected a menyebut "3 + 2 + Global Role aktif" tanpa total; spec mengasersi total 6 (turunan dari Data Uji).
  - TC-FA-SU-38 Langkah Uji 2 ("Hapus keyword") tidak menyebut cara; spec memakai `(←)` pada kotak Search sesuai bagian 8b butir 9.
