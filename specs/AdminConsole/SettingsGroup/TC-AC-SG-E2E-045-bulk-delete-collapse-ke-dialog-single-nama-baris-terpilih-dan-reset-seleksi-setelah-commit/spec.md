---
id: TC-AC-SG-E2E-045-bulk-delete-collapse-ke-dialog-single-nama-baris-terpilih-dan-reset-seleksi-setelah-commit
title: "Bulk Delete: Collapse ke Dialog Single, Nama Baris Terpilih Saja, dan Reset Seleksi Setelah Commit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-160
  - TC-AC-SG-161
  - TC-AC-SG-168
  - TC-AC-SG-399
coverage:
  web: automated
---

# Bulk Delete: Collapse ke Dialog Single, Nama Baris Terpilih Saja, dan Reset Seleksi Setelah Commit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor Hapus Utama (Pre-setup #21) `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_HAPUS_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup #21 (entitas `Distributor Hapus Utama`), nama literal karena TC mengasersi nama baris pada dialog:
  - `Hapus Bulk 3` (tanpa entitas), dipilih pada TC-160.
  - `Hapus Campur M1` dan `Hapus Campur M2` (masing-masing satu Client Active; nama Client tidak tertulis di Pre-setup).
  - `Hapus Warn A` dan `Hapus Warn B` (tanpa entitas; `Hapus Warn B` punya subgroup `Hapus Warn B1` dan `Hapus Warn B2`).
  - `Hapus Campur 1` (tanpa entitas), dihapus pada TC-168.
- Spec ini menghapus node Pre-setup `Hapus Campur 1` pada TC-168 (TC mengasersi baris Pre-setup, S-06 pengecualian 2026-10-30); TC lain hanya membuka dialog lalu membatalkan atau menutupnya. Pemulihan lewat Fixture BE di hook `before` dan `after`; TC-168 berada paling akhir. Efek: Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) entitas bertambah oleh penghapusan dan pemulihan dan tidak diasersi.
- Kemampuan teknis: Fixture BE (pemulihan baseline entitas uji), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-160: Seleksi satu baris collapse ke dialog Delete single

1. Ketik Search `Hapus Bulk 3`, tekan Enter
2. Centang kolom Checkbox pada baris `Hapus Bulk 3`
3. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
4. Verifikasi dialog memakai title "Delete Group" (singular)
5. Verifikasi dialog memuat satu bullet `Hapus Bulk 3`
6. Verifikasi kalimat dialog berakhir "...delete it?" (bentuk tunggal, bukan jamak)
7. Klik `[Cancel]`
8. Klik ikon `×` pada Bulk Actions Bar

### TC-AC-SG-161: Seleksi satu baris yang punya member collapse ke dialog blok single

9. Ganti isi kotak search dengan `Hapus Campur M1`, tekan Enter
10. Centang kolom Checkbox pada baris `Hapus Campur M1`
11. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
12. Verifikasi dialog blok single D-03 tampil: title "Cannot Delete Group" dengan bullet `Hapus Campur M1` dan "This group or its subgroups still have members. Remove all members before deleting." (bukan varian jamak D-09)
13. Klik `[OK]`
14. Klik ikon `×` pada Bulk Actions Bar

### TC-AC-SG-399: Bulk Delete node yang punya subgroup: dialog memuat nama baris terpilih saja tanpa turunan

15. Ganti isi kotak search dengan `Hapus Warn`, tekan Enter
16. Centang kolom Checkbox pada baris `Hapus Warn A` dan `Hapus Warn B` (`Hapus Warn B1` dan `Hapus Warn B2` tidak dicentang)
17. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
18. Verifikasi dialog bulk homogen D-06 tampil: title "Delete Groups", body bullet `Hapus Warn A` dan `Hapus Warn B` serta "Are you sure you want to delete them? This action cannot be undone." dengan `[Cancel]` dan `[Delete]`
19. Verifikasi body dialog tidak memuat bullet `Hapus Warn B1` dan `Hapus Warn B2`
20. Klik `[Cancel]`
21. Ganti isi kotak search dengan `Hapus Campur M1`, tekan Enter
22. Centang kolom Checkbox pada baris `Hapus Campur M1`
23. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
24. Verifikasi dialog D-07 tampil dan kelompok bullet "The following will be deleted:" hanya memuat `Hapus Warn A` dan `Hapus Warn B`
25. Verifikasi `Hapus Campur M1` berada pada kelompok skipped ("The following have members and will be skipped:")
26. Verifikasi turunan `Hapus Warn B1` dan `Hapus Warn B2` tidak dibulletkan pada kedua kelompok
27. Klik `[Cancel]`
28. Klik ikon `×` pada Bulk Actions Bar

### TC-AC-SG-168: Bulk action ter-commit mereset seleksi termasuk item yang di-skip

29. Ganti isi kotak search dengan `Hapus Campur`, tekan Enter
30. Centang kolom Checkbox pada baris `Hapus Campur 1` dan `Hapus Campur M2`
31. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
32. Klik `[Continue]`
33. Verifikasi Bulk Actions Bar hilang dan seleksi 0
34. Verifikasi baris `Hapus Campur M2` tetap tampil
35. Verifikasi baris `Hapus Campur M2` tidak tercentang

## Notes

- Langkah penghubung (S-03): langkah 1, 9, 15, 21, dan 29 (Search untuk menemukan baris target, R-16); langkah 7, 13, 20, dan 27 (menutup dialog); langkah 8, 14, dan 28 (membersihkan seleksi, S-09); langkah 16 mengikuti TC (hanya dua baris induk yang dicentang).
- Spec ini berisi 35 langkah (tepat pada batas smell sekitar 35); semua blok satu kelas (Bulk Delete fungsional) pada entitas yang sama dan berdiri sendiri, kegagalan satu blok tidak membuat blok lain kehilangan makna, dan TC-168 yang menghapus data berada di akhir.
- Temuan untuk QA:
  - TC-AC-SG-399 butir b ("Bila `Hapus Campur M1` ikut dicentang") bersyarat; spec menjalankannya sebagai skenario kedua tanpa langkah bersyarat (langkah 21 sampai 27).
  - TC-AC-SG-160 tidak menyebut kalimat dampak lengkap pada dialog single; spec hanya mengasersi bentuk singular "...delete it?".
  - TC-AC-SG-168 tidak menyebut toast hasil; spec tidak mengasersinya.
  - Nama Client pada `Hapus Campur M1` dan `Hapus Campur M2` tidak tertulis di Pre-setup #21.
