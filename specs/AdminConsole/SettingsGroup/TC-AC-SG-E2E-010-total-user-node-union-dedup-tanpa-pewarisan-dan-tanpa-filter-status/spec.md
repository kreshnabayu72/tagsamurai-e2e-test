---
id: TC-AC-SG-E2E-010-total-user-node-union-dedup-tanpa-pewarisan-dan-tanpa-filter-status
title: "Total User Node: Union, Dedup, Tanpa Pewarisan Ancestor, Tanpa Filter Status, dan Tidak Pernah 0"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-37
  - TC-AC-SG-38
  - TC-AC-SG-39
  - TC-AC-SG-40
  - TC-AC-SG-45
coverage:
  web: automated
---

# Total User Node: Union, Dedup, Tanpa Pewarisan Ancestor, Tanpa Filter Status, dan Tidak Pernah 0

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group); Total User per node (#17): `Default Group` 5, `Region A` 5, `Branch 1` 4, `Floor 1` 2, node lain 2 (hanya Total Control `Budi Santoso` dan Read Only `Rina Wijaya`); penugasan user (#18): `Region A` Group Manager `Andi Pratama`, Group Role `Manage partner` dan `Manage allocation` pada `Sari Dewi` (tampil `2 roles`), Group Role `Manage active client` pada `Dewi Lestari`; `Branch 1` Group Role `Manage allocation` pada `Yoga Pratama` dan `Manage partner` pada `Sari Dewi`; `Default Group` user `Hendra Saputra` berstatus Inactive.
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `{runId}-010`, maupun cleanup.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-37: Total User node adalah union Group Role di node itu, Group Manager di node itu, dan seluruh Total Control/Read Only

1. Ketik Search `Branch 1`, tekan Enter
2. Klik angka Total User pada baris `Branch 1`
3. Verifikasi popup "Users" terbuka dengan title flat "Users"
4. Verifikasi teks identitas satu baris di bawah title "Region A > Branch 1 (4)"
5. Verifikasi baris popup: `Budi Santoso` (Total Control), `Rina Wijaya` (Read Only), `Yoga Pratama` (Manage allocation), `Sari Dewi` (Manage partner)
6. Verifikasi `Andi Pratama` (Group Manager `Region A`) tidak ada di popup karena Group Manager tanpa inheritance
7. Tutup popup "Users"

### TC-AC-SG-38: User dengan dua Group Role pada node yang sama dihitung sekali

8. Ganti isi kotak search dengan `Region A`, tekan Enter
9. Verifikasi sel Total User baris `Region A` bernilai 5
10. Klik angka Total User pada baris `Region A`
11. Cari user `Sari Dewi` pada popup
12. Verifikasi `Sari Dewi` muncul satu kali dengan Group Role "2 roles"
13. Tutup popup "Users"

### TC-AC-SG-40: Total User dihitung tanpa filter status keaktifan

14. Ganti isi kotak search dengan `Default Group`, tekan Enter
15. Verifikasi sel Total User baris `Default Group` bernilai 5
16. Klik angka Total User pada baris `Default Group`
17. Cari user `Hendra Saputra` (berstatus Inactive) pada popup
18. Verifikasi `Hendra Saputra` tetap tampil di popup walau berstatus Inactive
19. Tutup popup "Users"

### TC-AC-SG-39: Group Role dan Group Manager pada ancestor tidak dihitung pada descendant

20. Klik `(←)` pada kotak Search
21. Klik node `Region A` di Sidebar Group Tree
22. Perhatikan baris `Branch 2`
23. Verifikasi sel Total User baris `Floor 1` bernilai 2
24. Klik angka Total User pada baris `Floor 1`
25. Verifikasi popup "Users" `Floor 1` memuat `Budi Santoso` (Total Control) dan `Rina Wijaya` (Read Only)
26. Verifikasi `Andi Pratama`, `Sari Dewi`, dan `Dewi Lestari` dari `Region A` tidak muncul di popup `Floor 1`
27. Tutup popup "Users"
28. Klik node `Region A` sekali lagi untuk melepas pilihan

### TC-AC-SG-45: Total User tidak pernah menampilkan 0 karena Total Control selalu terhitung

29. Sortir kolom Total User ascending
30. Verifikasi baris pertama tabel (nilai terkecil dari seluruh 14 baris) bernilai Total User 2
31. Verifikasi tidak ada baris bernilai Total User 0
32. Kembalikan sort kolom Total User ke urutan semula

## Notes

- Urutan TC di spec: TC-AC-SG-37, 38, 40, 39, lalu 45, supaya tiga blok yang memakai Search berurutan dan blok yang memilih node di sidebar (TC-AC-SG-39) dan mengubah sort (TC-AC-SG-45) ditaruh sesudahnya (S-10).
- Langkah penghubung (S-03, R-16): langkah 1, 8, 14 (Search untuk menemukan baris target karena tabel All Groups terbagi dua halaman), langkah 7, 13, 19, 27 (menutup popup), langkah 20 (mengosongkan Search), langkah 22 (mengamati tanpa asersi sendiri), langkah 28 (melepas pilihan node), dan langkah 32 (mengembalikan sort).
- Langkah 9, 15, dan 23 membaca nilai sel Total User sebagai padanan klausa "terhitung dalam Total User: N" atau "Total User 2" pada Expected TC; langkah 6 dan 26 (absence) berjangkar pada baris popup lain yang tampil (langkah 5 dan 25).
- Langkah 30 dan 31: nilai terkecil dibaca pada baris pertama hasil sort ascending; sort pada kolom ber-nilai sama (2) memuat dua nilai distinct (2, 3, 4, 5) pada 14 baris (S-11).
- Temuan untuk QA:
  - TC-AC-SG-39 langkah 2 ("perhatikan baris `Branch 2`") tidak punya Expected padanan; spec menuliskannya sebagai aksi tanpa asersi (langkah 22).
  - TC-AC-SG-45 Expected membaca nilai terkecil "pada seluruh 14 baris" sementara tabel membagi dua halaman; spec memakai sort ascending agar nilai terkecil teramati di baris pertama.
