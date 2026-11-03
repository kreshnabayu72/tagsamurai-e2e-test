---
id: TC-AC-DC-E2E-080-log-changelog-delete-family-dan-immutability
title: "Changelog Category: Delete Family Pre-order dan Snapshot Entri Tidak Berubah"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-219
  - TC-AC-DC-227
  - TC-AC-DC-228
coverage:
  web: automated
---

# Changelog Category: Delete Family Pre-order dan Snapshot Entri Tidak Berubah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control #1 (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Budi Santoso; Modified By tampil `Budi S`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture backend (disediakan tim FE/BE; endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: pohon Pre-setup #14 (`Hardware` > `Handheld Reader`) hanya dibaca sebagai induk node milik spec dan tidak diubah. Riwayat Changelog Pre-setup #17 dibaca pada langkah 37 sampai 39 (baris `Scanner Max`). General Settings Pre-setup #19 (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta) tidak diubah.
- Data Dinamis (suffix `{runId}-080`), dibuat lewat sesi API aktor di hook `before` di bawah `Handheld Reader`:
  - Family untuk TC-AC-DC-219: `Keluarga Uji {runId}-080` dengan anak `Anak A Keluarga Uji {runId}-080` (leaf) dan `Anak B Keluarga Uji {runId}-080` yang memiliki anak `Cucu Keluarga Uji {runId}-080`. Semua nama memuat `Keluarga Uji {runId}-080`.
  - Target rename TC-AC-DC-227: `Rename Uji {runId}-080`, direname menjadi `Nama Dua {runId}-080` (langkah 17), lalu `Nama Tiga {runId}-080` (langkah 19).
  - Target TC-AC-DC-228: `Hapus Uji {runId}-080`, direname menjadi `Daun Sementara {runId}-080` (langkah 29), lalu dihapus (langkah 30 dan 31).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API sisa node dengan nama di atas bila masih ada (`Keluarga Uji {runId}-080` beserta anak, `Nama Tiga {runId}-080`). Entri Changelog tidak dapat dihapus; nama bersuffix run.
- Kemampuan teknis (disediakan tim FE/BE; tanpa endpoint karangan): membaca jumlah total entri Changelog Category sebelum aksi (N219, langkah 1) karena Changelog adalah audit trail permanen.
- State global: tidak ada yang diubah.

## Test Steps

### TC-AC-DC-219: Delete family mencatat satu entri per node dengan urutan pre-order pada timestamp sama

1. Baca dan catat jumlah entri Changelog Category sebagai N219 (kemampuan baca)
2. Expand `Hardware`, lalu expand `Handheld Reader`
3. Hover node `Keluarga Uji {runId}-080`, lalu klik aksi Delete
4. Klik `[Delete]` pada dialog konfirmasi
5. Tunggu aksi selesai
6. Klik ikon Changelog pada header Sidebar Category
7. Ketik Search `Keluarga Uji {runId}-080`, tekan Enter
8. Verifikasi jumlah entri Changelog Category bertambah tepat empat dibanding N219 (kemampuan baca)
9. Verifikasi hasil Search memuat tepat empat baris dengan Action "Delete", satu per node: `Keluarga Uji {runId}-080`, `Anak A Keluarga Uji {runId}-080`, `Anak B Keluarga Uji {runId}-080`, `Cucu Keluarga Uji {runId}-080`
10. Verifikasi keempat baris Delete tersebut: Field "Category", New Value "—", dan Modified By "Budi S"
11. Verifikasi keempat baris Delete tersebut memiliki Date identik
12. Verifikasi urutan baris Delete default Newest First dari atas ke bawah: `Cucu Keluarga Uji {runId}-080`, `Anak B Keluarga Uji {runId}-080`, `Anak A Keluarga Uji {runId}-080`, `Keluarga Uji {runId}-080` (descendant dahulu, parent terakhir)
13. Klik header Date sekali (Oldest First)
14. Verifikasi urutan baris Delete dari atas ke bawah: `Keluarga Uji {runId}-080`, `Anak A Keluarga Uji {runId}-080`, `Anak B Keluarga Uji {runId}-080`, `Cucu Keluarga Uji {runId}-080` (pre-order, parent dahulu)
15. Tutup modal Changelog lewat `[×]`

### TC-AC-DC-227: Snapshot immutability: rename kedua tidak mengubah entri rename pertama

16. Hover node `Rename Uji {runId}-080`, lalu klik aksi Edit
17. Ubah nama menjadi "Nama Dua {runId}-080", lalu klik `[Save]`
18. Hover node `Nama Dua {runId}-080`, lalu klik aksi Edit
19. Ubah nama menjadi "Nama Tiga {runId}-080", lalu klik `[Save]`
20. Tunggu aksi selesai
21. Klik ikon Changelog pada header Sidebar Category
22. Ketik Search `Nama Dua {runId}-080`, tekan Enter
23. Verifikasi hasil Search menampilkan tepat dua baris Action "Edit"
24. Verifikasi entri rename pertama: Category "Nama Dua {runId}-080", Old Value "Rename Uji {runId}-080", New Value "Nama Dua {runId}-080"
25. Verifikasi entri rename kedua: Category "Nama Tiga {runId}-080", Old Value "Nama Dua {runId}-080", New Value "Nama Tiga {runId}-080"
26. Verifikasi entri rename pertama tetap menampilkan Category "Nama Dua {runId}-080" dan tidak berubah menjadi "Nama Tiga {runId}-080"
27. Tutup modal Changelog lewat `[×]`

### TC-AC-DC-228: Entri log lama tetap utuh setelah node diubah lalu dihapus

28. Hover node `Hapus Uji {runId}-080`, lalu klik aksi Edit
29. Ubah nama menjadi "Daun Sementara {runId}-080", lalu klik `[Save]`
30. Hover node `Daun Sementara {runId}-080`, lalu klik aksi Delete
31. Klik `[Delete]` pada dialog konfirmasi
32. Tunggu aksi selesai
33. Klik ikon Changelog pada header Sidebar Category
34. Ketik Search `Daun Sementara {runId}-080`, tekan Enter
35. Verifikasi entri Edit: Old Value "Hapus Uji {runId}-080", New Value "Daun Sementara {runId}-080", Category "Daun Sementara {runId}-080"
36. Verifikasi entri Delete: Category "Daun Sementara {runId}-080" dan Old Value "Daun Sementara {runId}-080"
37. Ganti isi kotak search dengan `Scanner Max`, tekan Enter
38. Verifikasi baris Action "Edit" dengan Old Value "Scanner Pro" dan New Value "Scanner Max" tampil
39. Verifikasi tidak ada entri lama yang berubah: baris Action "Edit" dengan Old Value "Scanner Pro", New Value "Scanner Max", Modified By "Budi S", Date 10/09/26 12:25 tetap sama

## Notes

- Alasan melewati 35 langkah (spec ini 39 langkah): ketiga blok memakai satu surface (Changelog Category), data milik tiap blok sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 5, 20, dan 32 (Tunggu aksi selesai sesudah `[Delete]` dan `[Save]` yang hasilnya tidak diasersi, karena langkah berikutnya membuka modal Changelog, 8b butir 8), langkah 15 dan 27 (menutup modal dan mereset Search dan Sort), serta Search pada langkah 7, 22, 34, dan 37 untuk menemukan baris target (R-16). Search menyaring ke baris unik bersuffix sehingga hasilnya tidak bergantung pada ukuran halaman audit trail.
- Pembagian TC lintas spec: Create, Edit, dan Delete leaf ada di spec 079; System Log dan Activity Log di spec 081 dan 082; absence log di spec 083, 084, 097, dan 098 (S-05).
- Temuan untuk QA:
  - TC-AC-DC-219 Expected a, b, c menulis jumlah absolut ("16 entri total"; empat baris terakhir pada halaman 2). Changelog adalah audit trail permanen yang tumbuh tiap run, sehingga angka absolut dan posisi halaman tidak dapat diasersi (S-12, S-14); spec mengasersi selisih tepat empat terhadap N219 dan urutan relatif baris Delete di hasil Search. Hasil Search juga dapat memuat baris Create hasil seeding (bila seeding lewat API menulis Changelog); urutan Create terhadap Delete tidak diasersi.
  - TC-AC-DC-219 menyatakan "timestamp sama" tetapi kolom Date berketelitian menit; urutan descendant dahulu pada Newest First bergantung pada aturan tie-break yang tidak tertulis di TC.
  - TC-AC-DC-227 dan 228 memakai node literal Pre-setup #14 (`Rugged Scanner`, `Hapus Daun`) sebagai target tulis; spec memakai node bersuffix milik spec (keputusan data tulis). Langkah 37 sampai 39 (baris literal Pre-setup #17 `Scanner Max` sebagai wakil "entri lama") bergantung pada nama literal itu dan pada keberadaan riwayat Pre-setup #17; TC tidak menyebut baris mana yang dimaksud "entri lama".
