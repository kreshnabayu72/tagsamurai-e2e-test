---
id: TC-FA-FATR-E2E-016-overrides-kolom
title: "Column Visibility tabel Overrides tersimpan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EB-SRC-5@tabel-overrides, EB-KOL-2@tabel-overrides, EB-KOL-3]
smoke: []
dependsOn: []
trace:
  EB-SRC-5@tabel-overrides: [9, 13]
  EB-KOL-2@tabel-overrides: [22, 25]
  EB-KOL-3: [28, 30, 33, 35, 39]
anchor: [5, 21]
coverage:
  web: automated
---

# Column Visibility tabel Overrides tersimpan

## Prerequisites
- Aktor: Total Control `Rina Wulandari`.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-016-1: Category leaf `Machinery {runId}`, ada di entitas aktor.
  - DU-016-2: Group tingkat atas `Proyek Karawang {runId}`.
  - DU-016-3: override Group `Proyek Karawang {runId}` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Max duration (30 days)`, dibuat oleh `Rina Wulandari`; kata kunci Search yang dipakai atasnya: `Karawang {runId}`.
  - DU-016-4: entri Changelog Category `Machinery {runId}`, Field `Borrow (Max duration)`, Old Value `Inherit`, New Value `30 days`, Action `Edit`, Modified By `Rina W`.
- Kondisi:
  - Kolom `Target`, `Created By`, dan `Category` tabel Overrides serta kolom `Category` tabel Changelog bernilai bawaan untuk `Rina Wulandari`: kolom `Category` tabel Overrides tidak ditampilkan, kolom lain ditampilkan.

## Test Steps

### Search tidak mencocokkan kolom yang disembunyikan dan mencocokkannya lagi saat ditampilkan
1. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
2. Klik node `Machinery {runId}` di Sidebar Category Tree
3. Klik tab `Borrow`
4. Ketik Search `Karawang {runId}` pada tabel Overrides, tekan Enter
5. Verifikasi baris dengan Target `Proyek Karawang {runId}` dan Overridden `Max duration (30 days)` tampil di tabel Overrides sebelum kolom Target disembunyikan
6. Klik header kolom Actions pada tabel Overrides
7. Hapus centang kolom `Target`
8. Ganti isi kotak Search dengan `Karawang {runId}` lagi, tekan Enter
9. Verifikasi `No results found` tampil di tabel Overrides karena kolom Target disembunyikan
10. Klik header kolom Actions pada tabel Overrides
11. Centang kolom `Target`
12. Ganti isi kotak Search dengan `Karawang {runId}` lagi, tekan Enter
13. Verifikasi baris dengan Target `Proyek Karawang {runId}` tampil lagi karena kolom Target ditampilkan

### Konfigurasi kolom bertahan sesudah muat ulang halaman
14. Klik header kolom Actions pada tabel Overrides
15. Hapus centang kolom `Created By`
16. Muat ulang halaman
17. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
18. Klik node `Machinery {runId}` di Sidebar Category Tree
19. Klik tab `Borrow`
20. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
21. Verifikasi baris dengan Target `Proyek Karawang {runId}` tampil di tabel Overrides sesudah muat ulang halaman
22. Verifikasi kolom `Created By` tidak tampil pada tabel Overrides
23. Klik header kolom Actions pada tabel Overrides
24. Centang kolom `Created By`
25. Verifikasi kolom `Created By` tampil pada tabel Overrides

### Konfigurasi kolom tabel Overrides tidak mengubah kolom tabel Changelog
26. Klik header kolom Actions pada tabel Overrides
27. Centang kolom `Category`
28. Verifikasi kolom `Category` tampil pada tabel Overrides
29. Klik ikon Changelog di header
30. Verifikasi kolom `Category` tampil pada tabel Changelog sebagai kolom bawaan
31. Klik header kolom Actions pada tabel Changelog
32. Hapus centang kolom `Category`
33. Verifikasi kolom `Category` tidak tampil pada tabel Changelog
34. Klik `✕` pada dialog Changelog
35. Verifikasi kolom `Category` tetap tampil pada tabel Overrides
36. Klik ikon Changelog di header
37. Klik header kolom Actions pada tabel Changelog
38. Centang kolom `Category`
39. Verifikasi kolom `Category` tampil pada tabel Changelog
40. Klik `✕` pada dialog Changelog
41. Klik header kolom Actions pada tabel Overrides
42. Hapus centang kolom `Category`
