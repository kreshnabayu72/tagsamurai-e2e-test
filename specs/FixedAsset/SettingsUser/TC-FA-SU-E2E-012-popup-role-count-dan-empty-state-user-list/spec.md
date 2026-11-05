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
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` dengan 25 pengguna (#20), penugasan (#23: Budi Santoso `4 roles`, Lina Marlina Total Control; Oscar Pranata Group Manager IT Infrastructure dan Accounts Payable, #9, dengan baris pola Group Manager yang termaterialisasi) dan Transaction Role (#39). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis (di-seed lewat API di hook `before`, dihapus di hook `after`):
  - Pengguna R `Pengguna Role Count {runId}-012`, email `rolecount+{runId}-012@qwertysystem.net`: Global Role aktif 1 (Import Data); Group Role Manage group di 3 grup (Finance & Accounting, Branch Surabaya, Logistics Warehouse); Transaction Role Approver Missing di 2 grup (Branch Surabaya, General Affairs). Label Role dan header popup R menjadi 6 (3 + 2 + Global Role aktif 1) menurut TC-FA-SU-36.
- Kemampuan teknis: seed API penugasan Global Role, Group Role, dan Transaction Role untuk pengguna dinamis (disediakan tim BE/FE); klik pada backdrop popup.
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
15. Verifikasi hitungan Transaction Role literal per penugasan tersimpan (dua penugasan: Branch Surabaya dan General Affairs) dan node descendant yang hanya tercakup tidak dihitung, sehingga angka header tetap 6
16. Tutup popup lewat ✕

### TC-FA-SU-37: Popup Role Count: dismiss lewat ✕ dan Esc, klik backdrop tidak menutup, dan pengecualian tier

17. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
18. Klik label `4 roles` pada Budi Santoso
19. Klik backdrop popup
20. Verifikasi popup tidak tertutup oleh klik backdrop
21. Tekan Esc
22. Verifikasi popup tertutup oleh Esc
23. Klik label `4 roles` pada Budi Santoso
24. Klik tombol ✕ pada popup
25. Verifikasi popup tertutup oleh ✕
26. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter
27. Klik badge `Total Control` pada Lina Marlina
28. Verifikasi tidak ada popup role list yang terbuka dan badge tier tetap tampil di kolom Role
29. Ganti isi kotak search dengan `Oscar Pranata`, tekan Enter
30. Verifikasi kolom Role Oscar Pranata menampilkan label jumlah numerik berupa link (bukan `0 roles`) tanpa badge
31. Klik label jumlah pada Oscar Pranata
32. Verifikasi Popup Role Count terbuka memuat baris pola Group Manager (seksi Group Role dan Transaction Role) tanpa badge, dan status Group Manager tidak tampil sebagai bullet

### TC-FA-SU-38: Empty state User List: hasil pencarian atau filter kosong

33. Ganti isi kotak search dengan `zzzz`, tekan Enter
34. Verifikasi empty state menampilkan ilustrasi 100x100, Title "No results found", dan Description "Try adjusting your search or filter."
35. Klik `(←)` pada kotak Search
36. Verifikasi Ahmad Dahlan (Default User) tampil di tabel sehingga empty state genuinely empty tidak berlaku

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9, 16 (menutup popup, S-09), langkah 10, 17, 26, 29, dan 33 (Search untuk menemukan baris target, R-16), langkah 35 (mengosongkan Search sebelum asersi baris Default User, S-09). Langkah 4, 20, dan 32 adalah asersi absence atau tidak tertutup; anchor positifnya adalah popup yang terbuka pada langkah 1 dan 18 serta popup Oscar Pranata yang terbuka pada langkah 31.
- Jumlah langkah 36, satu di atas smell 35 langkah; semua blok satu kelas harness (screening baca tanpa menyimpan data) dan berdiri sendiri, kegagalan satu blok tidak membuat blok lain kehilangan makna; kelebihan berasal dari satu Verifikasi per klausa Expected (S-01).
- Pembagian TC lintas spec: kolom Name, Role, dan Home Group User List (TC-FA-SU-9 sampai 11) ada di spec 004.
- Temuan untuk QA:
  - TC-FA-SU-35 Expected b dan d memuat seksi Group Role dan Transaction Role pada Budi Santoso, tetapi Pre-setup #23 dan #39 tidak merinci Group Role atau Transaction Role Budi Santoso; spec mengasersi format dan urutan dari data yang tampil dan membutuhkan Budi Santoso memiliki sedikitnya satu bullet Group Role dan satu bullet Transaction Role, yang perlu dijamin seed.
  - TC-FA-SU-37 Expected c (terbaru): pengguna Group Manager menampilkan label jumlah numerik berupa link karena baris pola Group Manager adalah assignment aktif biasa. Spec memakai Oscar Pranata (Pre-setup #9). Angka pasti (`48 roles`) turunan dan Open Item 3 PM belum diputuskan, sehingga hanya diasersi longgar (numerik, bukan `0 roles`) dan isi popup diasersi per seksi, bukan per angka. Pengguna dinamis G (Group Manager tanpa peran lain) tidak dipakai lagi karena penugasan Group Manager selalu memiliki baris pola.
  - TC-FA-SU-36 Langkah Uji 1 ("Siapkan assignment sesuai Data Uji") tidak menyebut nama Global Role aktif; spec memakai `Import Data` yang ada di Pre-setup #20, #23.
  - TC-FA-SU-36 Expected b diperbarui: hitungan Transaction Role literal per penugasan tersimpan dan descendant yang hanya tercakup tidak dihitung. Data pengguna R tidak menyertakan penugasan di node yang punya descendant (Branch Surabaya dan General Affairs), sehingga langkah 15 hanya mengasersi hitungan literal 2 penugasan dan total 6; kasus descendant tercakup yang tidak dihitung ada di TC-FA-SU-1113 (E2E-421).
  - TC-FA-SU-36 Expected a menyebut "3 + 2 + Global Role aktif" tanpa total; spec mengasersi total 6 (turunan dari Data Uji).
  - TC-FA-SU-38 Langkah Uji 2 ("Hapus keyword") tidak menyebut cara; spec memakai `(←)` pada kotak Search sesuai bagian 8b butir 9.
