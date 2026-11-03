---
id: TC-AC-SG-E2E-038-delete-group-dialog-warning-d04-cancel-backdrop-tooltip-path-elipsis-sidebar
title: "Delete Group: Dialog Warning D-04, Cancel, Backdrop, Tooltip Full Path, dan Elipsis Sidebar"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-131
  - TC-AC-SG-132
  - TC-AC-SG-135
  - TC-AC-SG-149
  - TC-AC-SG-150
coverage:
  web: automated
---

# Delete Group: Dialog Warning D-04, Cancel, Backdrop, Tooltip Full Path, dan Elipsis Sidebar

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor Hapus Utama (Pre-setup #21) `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_HAPUS_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup #21 (entitas `Distributor Hapus Utama`, dibaca saja), nama literal karena dialog mengasersi nama node dan jumlah user:

| Node | Isi seed | Total User (distinct, termasuk Total Control dan Read Only) |
|---|---|---|
| `Hapus Warn A` | tanpa entitas; Group Role `Manage partner` pada `Joko Susilo` | 3 |
| `Hapus Warn B` | tanpa entitas; Group Role pada `Nina Amelia`; anak `Hapus Warn B1` (Group Manager `Lia Marlina`) dan `Hapus Warn B2` | 4 (node dan seluruh subtree) |

- Spec ini tidak menghapus atau mengubah node: setiap dialog Delete hanya dibuka lalu dibatalkan (`[Cancel]`, klik backdrop, atau dibiarkan sampai `[Cancel]`). Pre-setup #21 dipakai langsung karena TC mengasersi nama node dan jumlah user Pre-setup (S-06, aksi dibatalkan, hanya dibaca); Last Updated, Modified By, dan audit trail tidak berubah.
- Hook `before` dan `after` memulihkan entitas `Distributor Hapus Utama` ke baseline Pre-setup #21 lewat Fixture BE.
- Kemampuan teknis: Fixture BE (pemulihan baseline entitas uji), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-131: Dialog warning Delete (D-04) pada node tanpa entitas menampilkan nama, subgroup, dan jumlah user distinct

1. Ketik Search `Hapus Warn B`, tekan Enter
2. Klik ikon `⋯` pada baris `Hapus Warn B`, lalu pilih "Delete"
3. Verifikasi dialog tampil dengan title "Delete Group" (tanpa tanda tanya)
4. Verifikasi body diawali bullet nama group yang terdampak: `Hapus Warn B`, `Hapus Warn B1`, `Hapus Warn B2`
5. Hover bullet `Hapus Warn B`
6. Verifikasi tooltip full path tampil untuk bullet `Hapus Warn B`
7. Hover bullet `Hapus Warn B1`
8. Verifikasi tooltip full path tampil untuk bullet `Hapus Warn B1`
9. Hover bullet `Hapus Warn B2`
10. Verifikasi tooltip full path tampil untuk bullet `Hapus Warn B2`
11. Verifikasi kalimat dampak "This group has 4 users assigned — deleting it will remove their group assignments. This action cannot be undone. Are you sure you want to delete it?"
12. Verifikasi tombol `[Cancel]` dan `[Delete]` tampil
13. Klik `[Cancel]`

### TC-AC-SG-132: Dialog warning D-04 selalu tampil walau tidak ada Group Role maupun Group Manager

14. Ganti isi kotak search dengan `Hapus Warn A`, tekan Enter
15. Klik ikon `⋯` pada baris `Hapus Warn A`, lalu pilih "Delete"
16. Verifikasi dialog "Delete Group" tampil dengan bullet `Hapus Warn A` (Delete tidak berjalan tanpa dialog peringatan)
17. Verifikasi kalimat dampak "This group has 3 users assigned — deleting it will remove their group assignments. This action cannot be undone. Are you sure you want to delete it?"
18. Klik `[Cancel]`

### TC-AC-SG-135: Delete lewat elipsis sidebar memakai guard dan dialog yang sama

19. Klik ikon `⋯` pada node `Hapus Warn A` di sidebar, lalu pilih "Delete"
20. Verifikasi dialog "Delete Group" yang sama dengan Delete dari row action tampil dengan bullet `Hapus Warn A`
21. Klik `[Cancel]`

### TC-AC-SG-149: Bullet nama pada dialog Delete menampilkan tooltip full path

22. Ganti isi kotak search dengan `Hapus Warn B`, tekan Enter
23. Klik ikon `⋯` pada baris `Hapus Warn B`, lalu pilih "Delete"
24. Hover bullet `Hapus Warn B1` pada dialog
25. Verifikasi tooltip menampilkan full path "Hapus Warn B > Hapus Warn B1"
26. Klik `[Cancel]`

### TC-AC-SG-150: Klik backdrop tidak menutup dialog Delete

27. Ganti isi kotak search dengan `Hapus Warn A`, tekan Enter
28. Klik ikon `⋯` pada baris `Hapus Warn A`, lalu pilih "Delete"
29. Klik area gelap di luar dialog
30. Verifikasi dialog tetap terbuka
31. Klik `[Cancel]`
32. Verifikasi dialog tertutup (tombol `[Cancel]` menutup dialog)
33. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1, 14, 22, dan 27 (Search untuk menemukan baris target, R-16); langkah 13, 18, 21, dan 26 (`[Cancel]` menutup dialog sebelum blok berikutnya, S-09); langkah 31 (`[Cancel]` penutup dialog, hasilnya diasersi di langkah 32); langkah 33 (reset Search).
- Tooltip diasersi segera setelah hover sebelum hover berikutnya (bagian 8b butir 5).
- TC-AC-SG-134 (`[Cancel]` tanpa toast dan tanpa entri log) berada di spec absence kelas g 091 dengan aksi nyata dan baseline sendiri (S-05); TC-133 (konfirmasi Delete) ada di spec 041.
- Temuan untuk QA:
  - TC-AC-SG-131 butir b menyebut "masing-masing dengan tooltip hover full path" tanpa teks path untuk bullet level 1 (`Hapus Warn B`); spec hanya mengasersi bahwa tooltip full path tampil untuk tiap bullet, dan teks persis diasersi hanya untuk `Hapus Warn B1` (TC-149).
  - Jumlah user pada dialog (4 untuk `Hapus Warn B` dan subtree, 3 untuk `Hapus Warn A`) bergantung pada Total Control dan Read Only entitas ikut terhitung; Pre-setup #21 tidak menulis akun Read Only entitas `Distributor Hapus Utama` secara eksplisit.
  - Email akun `Joko Susilo`, `Nina Amelia`, dan `Lia Marlina` tidak tertulis di Pre-setup (hanya nama tampil); S-12 mensyaratkan identifikasi user lewat email.
