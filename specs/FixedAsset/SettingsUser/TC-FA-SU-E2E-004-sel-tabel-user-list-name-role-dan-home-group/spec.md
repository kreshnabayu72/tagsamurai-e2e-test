---
id: TC-FA-SU-E2E-004-sel-tabel-user-list-name-role-dan-home-group
title: "Sel Tabel User List: Name, Role, dan Home Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-9
  - TC-FA-SU-10
  - TC-FA-SU-11
coverage:
  web: automated
---

# Sel Tabel User List: Name, Role, dan Home Group

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Data Pre-setup: Client `FaUserMain` dengan 25 pengguna (#20) dan penugasan (#23, hanya dibaca); pohon grup (#21); varian `FaUserHG` (#46): Home Group Vina Maharani menjadi `Jakarta Selatan Distribution Center` (parent `Region Jawa`, 35 karakter). Varian #46 dibentuk lewat seed API di hook `before` spec ini dan dipulihkan lewat seed API di hook `after` (Last Updated Vina Maharani berubah selama spec; dipulihkan oleh seed). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis: satu pengguna tanpa Home Group, nama `Zzz Tanpa Home Group {runId}-004`, email `tanpa.homegroup+{runId}-004@qwertysystem.net`, di-seed lewat API di hook `before` dan dihapus di hook `after`; nama diawali `Zzz` supaya berada di akhir urutan Name A-Z (halaman 3 sebagai baris terakhir). Pre-setup #43 tidak memuat pengguna tanpa Home Group sehingga pengguna ini dibutuhkan TC-FA-SU-11 Expected a (lihat Temuan untuk QA).
- Kemampuan teknis: seed API variasi Home Group dan pembuatan pengguna dinamis (disediakan tim BE/FE); pembacaan tooltip hover.
- State global: Home Group Vina Maharani (varian #46) dan pengguna dinamis; dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-9: Sel Name: avatar, nama lengkap, dan badge Pending

1. Verifikasi sel Name berbentuk `[Avatar] Full Name` dalam satu sel
2. Verifikasi Hana Kusuma dan Kartika Sari menampilkan badge `Pending Activation` (warning) di samping nama
3. Verifikasi Indra Wijaya menampilkan badge `Pending Email Confirmation` (warning)
4. Klik nama `Hana Kusuma`
5. Verifikasi halaman Detail User Hana Kusuma terbuka
6. Klik segmen Breadcrumb `User`
7. Klik halaman 2 pada pagination
8. Verifikasi Lukman Hakim menampilkan badge `Pending Email Confirmation` (warning)
9. Verifikasi badge `Pending Activation` dan `Pending Email Confirmation` saling eksklusif (tidak ada baris dengan kedua badge)
10. Verifikasi pengguna lain pada halaman 2 (Lina Marlina) tanpa badge

### TC-FA-SU-10: Sel Role: label jumlah, badge tier, dan Popup Role Count tidak berlaku untuk 0 roles

11. Verifikasi Lina Marlina menampilkan badge `Total Control` pada kolom Role
12. Verifikasi Oscar Pranata tidak menampilkan badge atau label Group Manager pada kolom Role dan menampilkan label jumlah numerik berupa link (bukan `0 roles`; baris pola Group Manager dihitung sebagai assignment aktif biasa)
13. Klik halaman 1 pada pagination
14. Verifikasi kolom Role: Budi Santoso `4 roles`, Eka Wulandari `3 roles`, Gita Permata `3 roles`, Indra Wijaya `1 role`, Doni Prasetyo dan Hana Kusuma `0 roles`
15. Verifikasi Ahmad Dahlan badge `Total Control` dan Citra Lestari badge `Read Only`
16. Verifikasi badge tier menggantikan label jumlah pada baris Ahmad Dahlan dan Citra Lestari
17. Klik `0 roles` pada Doni Prasetyo
18. Verifikasi `0 roles` berupa teks biasa dan tidak membuka popup
19. Klik `4 roles` pada Budi Santoso
20. Verifikasi Popup Role Count terbuka
21. Tutup Popup Role Count lewat ✕

### TC-FA-SU-11: Sel Home Group: badge, strip kosong, dan hover hierarki

22. Verifikasi pengguna dengan Home Group menampilkan badge nama grup (Budi Santoso `Finance & Accounting`, Eka Wulandari `Branch Surabaya`)
23. Klik halaman 3 pada pagination
24. Verifikasi pengguna dinamis tanpa Home Group menampilkan `—`
25. Hover badge Home Group Vina Maharani
26. Verifikasi tooltip menampilkan hierarki lengkap `Region Jawa > Jakarta Selatan Distribution Center`
27. Verifikasi badge Vina Maharani dipotong menjadi `Jakarta Sela..ution Center` (12 huruf pertama, `..`, 12 huruf terakhir)
28. Verifikasi hover menampilkan nilai penuh `Jakarta Selatan Distribution Center`
29. Hover badge Home Group Wawan Setiawan (`Finance & Accounting`)
30. Verifikasi tooltip menampilkan hierarki lengkap dengan format `[Parent] > [Child]`
31. Verifikasi nama grup `Finance & Accounting` (25 karakter atau kurang) tampil penuh tanpa potongan
32. Klik halaman 1 pada pagination

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 (kembali ke User List lewat Breadcrumb), 7, 13, 23, dan 32 (pindah halaman pagination supaya baris yang diasersi tampil, S-14), langkah 21 (menutup popup, S-09). Klik nama pada langkah 4 dan Verifikasi langkah 5 memenuhi Expected a TC-FA-SU-9 ("klik nama membuka Detail"). Urutan langkah TC-FA-SU-9 dan TC-FA-SU-10 mengikuti halaman pagination yang sedang terbuka (halaman 2 lebih dulu di TC-FA-SU-10) supaya tidak ada klik halaman bolak-balik.
- Pembagian TC lintas spec: kolom Modified By dan Last Updated (TC-FA-SU-12) ada di spec 015.
- Temuan untuk QA:
  - TC-FA-SU-11 Expected a menyebut pengguna tanpa Home Group menampilkan `—`, tetapi Pre-setup #43 memberi Home Group untuk ke-25 pengguna; tidak ada pengguna Pre-setup tanpa Home Group. Spec memakai pengguna dinamis tanpa Home Group (Data Dinamis).
  - TC-FA-SU-11 Langkah Uji 3 menyebut "varian Pre-setup #46" tanpa cara membentuknya; spec membentuknya lewat seed API (kemampuan disediakan tim BE/FE).
  - TC-FA-SU-10 Expected d: status Group Manager tidak punya badge atau label, sedangkan baris pola Group Manager (Group Role dan Transaction Role) dihitung sebagai assignment aktif biasa (Oscar Pranata `48 roles`, Qori Akbar `25 roles`; TC-FA-SU-1096). Angka itu turunan dan Open Item 3 PM belum diputuskan; spec memakai Oscar Pranata (Pre-setup #9, #23) dan mengasersi longgar: label jumlah numerik berupa link, bukan `0 roles`, tanpa badge atau label Group Manager; angka pasti tidak diasersi.
  - TC-FA-SU-11 Expected b menyebut hover hierarki `[Parent] > [Child]` untuk badge `Finance & Accounting` tanpa menyebut parent-nya; spec mengasersi format.
