---
id: TC-AC-CS-E2E-096-list-setup-column-screening-hide-curated-urutan-pin
title: "List Setup Column: Screening, Hide, Curated, Urutan, Pin"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-365
  - TC-AC-CS-366
  - TC-AC-CS-367
  - TC-AC-CS-368
  - TC-AC-CS-369
  - TC-AC-CS-370
coverage:
  web: automated
---

# List Setup Column: Screening, Hide, Curated, Urutan, Pin

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup: dataset #82 pada tab Current (baca-saja); Cache Setup Column browser dikosongkan sebelum tiap blok TC (precondition TC) lewat kemampuan menghapus preferensi kolom di browser yang disediakan tim FE, dan dipulihkan di hook `after` (bagian 4). Suite mendaftarkan spec ini sebagai spec yang menyimpan konfigurasi kolom.
- Kemampuan teknis (disediakan tim FE): penghapusan preferensi kolom di browser; pengaturan viewport sempit sehingga tabel dapat digulir horizontal (TC-AC-CS-370).
- State global yang diubah: konfigurasi kolom List Subscriptions yang disimpan di browser; dipulihkan lewat penghapusan preferensi kolom di hook `after` dan antar blok.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-365: Screening overlay Column Visibility

1. Klik header kolom Actions `⋯`
2. Verifikasi item "Setup Column..." ada di bagian bawah panel
3. Verifikasi daftar kolom berurutan: Subscription ID, Client, Product, Plan, Status, Start Date, End Date, Plan Owner (Hideable, checked, enabled) dan Grace End (Curated, unchecked, enabled)
4. Verifikasi setiap baris kolom punya drag handle
5. Tutup overlay Column Visibility

### TC-AC-CS-366: Screening modal Setup Column dan Live Preview

6. Klik header kolom Actions `⋯`, lalu klik `[Setup Column]`
7. Verifikasi Header modal: Title "Setup Column", deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.", dan tombol silang `[✕]`
8. Verifikasi Body memuat daftar kolom dengan checkbox, drag handle, dan icon Pin, dan Grace End unchecked
9. Verifikasi Live Preview menampilkan urutan header dan data sel sama dengan tabel
10. Verifikasi Footer memuat `[Reset to Default]` dan `[Save]` rata kanan tanpa `[Cancel]`
11. Tutup modal Setup Column dengan `✕`

### TC-AC-CS-367: Hide dan unhide kelas kolom Hideable lewat modal lalu Save

12. Klik header kolom Actions `⋯`, klik `[Setup Column]`, lalu hilangkan centang `Product` dan `Plan Owner`
13. Verifikasi Live Preview langsung menyembunyikan Product dan Plan Owner
14. Klik `[Save]`
15. Verifikasi tabel menyembunyikan kolom Product dan Plan Owner
16. Muat ulang halaman (F5)
17. Verifikasi kolom Product dan Plan Owner tetap tersembunyi (tersimpan di cache browser)
18. Hapus preferensi kolom di browser lewat kemampuan tim FE, lalu muat ulang halaman

### TC-AC-CS-368: Menampilkan kolom Curated Grace End lalu Save

19. Klik header kolom Actions `⋯`, klik `[Setup Column]`, lalu centang `Grace End`
20. Klik `[Save]`
21. Verifikasi kolom Grace End tampil pada tabel setelah Save
22. Verifikasi baris Expired dan Grace menampilkan tanggal Grace End dan baris lain menampilkan "—"
23. Hapus preferensi kolom di browser lewat kemampuan tim FE, lalu muat ulang halaman

### TC-AC-CS-369: Geser urutan kolom Hideable lalu Save

24. Klik header kolom Actions `⋯`, klik `[Setup Column]`, lalu seret `Plan Owner` ke posisi paling atas
25. Verifikasi Live Preview menempatkan Plan Owner sebagai kolom pertama
26. Verifikasi kedelapan kolom Hideable dan kolom Curated dapat dipindah tanpa posisi terkunci
27. Klik `[Save]`
28. Verifikasi tabel menempatkan Plan Owner sebagai kolom pertama
29. Muat ulang halaman (F5)
30. Verifikasi urutan bertahan setelah F5
31. Hapus preferensi kolom di browser lewat kemampuan tim FE, lalu muat ulang halaman

### TC-AC-CS-370: Pin dan unpin kolom lalu Save

32. Atur viewport sempit sehingga tabel dapat digulir horizontal, klik header kolom Actions `⋯`, klik `[Setup Column]`, lalu klik icon Pin pada kolom `Client`
33. Klik `[Save]`, lalu gulir tabel ke kanan
34. Verifikasi kolom Client tetap di posisinya saat tabel digulir horizontal setelah Pin
35. Muat ulang halaman (F5)
36. Gulir tabel ke kanan
37. Verifikasi state Pin bertahan setelah F5
38. Klik header kolom Actions `⋯`, klik `[Setup Column]`, klik icon Pin pada kolom `Client` untuk unpin, lalu klik `[Save]`
39. Tunggu aksi selesai (modal Setup Column tertutup)
40. Gulir tabel ke kanan
41. Verifikasi setelah Unpin kolom Client ikut bergeser saat digulir
42. Pulihkan viewport dan hapus preferensi kolom di browser lewat kemampuan tim FE

## Notes

- Langkah penghubung: penutupan overlay dan modal, penghapusan preferensi kolom di browser antar blok (precondition TC "Cache Setup Column dikosongkan"), dan gulir tabel ke kanan (langkah 36) setelah F5 agar state Pin terlihat sebelum Verifikasi.
- TC-AC-CS-370 butir c ("State Pin bertahan setelah F5") diamati setelah Pin dan sebelum Unpin karena state sementara harus diamati sebelum langkah yang mengubahnya (bagian 8b butir 5); urutan langkah di TC adalah Pin, Save, gulir, Unpin, Save.
- Alasan spec lebih dari sekitar 35 langkah: seluruh blok satu topik (Setup Column List), satu layar, dan satu jenis harness (cache browser); tiap blok berdiri sendiri dengan penghapusan preferensi kolom di antaranya sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, bagian 8b butir 8): langkah `Tunggu aksi selesai` (langkah 39) menunggu modal Setup Column tertutup sesudah `[Save]` sebelum langkah berikutnya mengubah permukaan.
- Temuan untuk QA: (1) TC-AC-CS-369 butir c ("Kedelapan kolom Hideable dan kolom Curated dapat dipindah tanpa posisi terkunci") hanya punya langkah menggeser satu kolom; spec mengasersi kemampuan dipindah pada baris modal. (2) TC-AC-CS-365 dan TC-AC-CS-366 memakai label `[Setup Column]` dan "Setup Column..." untuk item yang sama; spec memakai teks TC masing-masing. (3) TC-AC-CS-367 butir a menyebut Live Preview langsung menyembunyikan kolom sebelum Save; spec mengamatinya sebelum klik `[Save]`.
