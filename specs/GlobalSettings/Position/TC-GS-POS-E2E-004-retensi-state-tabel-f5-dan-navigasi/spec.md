---
id: TC-GS-POS-E2E-004-retensi-state-tabel-f5-dan-navigasi
title: "Retensi Search, Sort, Filter, dan Halaman Tabel Position saat F5, Reset saat Klik Sidebar, dan Retensi saat Pindah Sub-tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-13
  - TC-GS-POS-14
  - TC-GS-POS-15
coverage:
  web: automated
---

# Retensi Search, Sort, Filter, dan Halaman Tabel Position saat F5, Reset saat Klik Sidebar, dan Retensi saat Pindah Sub-tab

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > User > Position; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi sidebar (klik sidebar dan sub-tab pada TC-GS-POS-14 dan 15 adalah bagian dari uji retensi).
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 10 `IT Manager`, 11 `Finance Analyst`, 12 `Warehouse Supervisor`, 13 `Customer Success Manager`, 14 `Procurement Officer`, 15 `Field Technician`, 16 `Sales Coordinator` (7 record).
- Data Dinamis (di-seed lewat API di hook `before`; nama bersuffix per run; fixture baru `Fixture.position.retentionSeed004`): 8 Position `iOS Developer {runId}-004`, `Legal Counsel {runId}-004`, `Marketing Executive {runId}-004`, `Quality Assurance Analyst {runId}-004`, `Data Engineer {runId}-004`, `Office Administrator {runId}-004`, `Logistics Coordinator {runId}-004`, dan `Payroll Specialist {runId}-004`. Dengan 7 record Pre-setup, jumlah seluruh record Position N = 15 (memenuhi 11 ≤ N ≤ 20 pada precondition TC). N diturunkan dari seeding (7 Pre-setup + 8 Data Dinamis) dan dihitung oleh hook `before`, bukan dibaca dari tabel yang hanya menampilkan satu halaman (bagian 8b butir 10).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-004` yang masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true, lihat `suite.md`.
- Kemampuan teknis: muat ulang halaman (F5) tanpa dialog `beforeunload` (tidak ada form terbuka); pembacaan nilai Search, indikator sort, nilai rentang Filter, ukuran halaman, dan halaman aktif.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### TC-GS-POS-15: Pindah sub-tab User List lalu kembali ke Position, status Search/Filter/Sort/halaman

1. Ketik Search `Manager`, tekan Enter
2. Verifikasi baris `IT Manager` tampil di tabel
3. Verifikasi tabel tersaring sehingga setiap baris memuat `Manager` pada Name
4. Catat baris hasil Search sebagai pembanding
5. Klik sub-tab User List
6. Klik sub-tab Position
7. Verifikasi keyword Search `Manager` tetap terisi
8. Verifikasi tabel tetap tersaring dengan baris yang sama dengan yang dicatat
9. Verifikasi Sort sama seperti sebelum pindah tab (default Name A-Z)
10. Verifikasi tidak ada indikator panah sort aktif
11. Buka Filter Panel
12. Verifikasi Filter Panel tanpa nilai ter-apply
13. Tutup Filter Panel
14. Verifikasi halaman aktif 1
15. Verifikasi ukuran halaman 10
16. Klik `(←)` pada kotak Search (menutup input dan mereset tabel)

### TC-GS-POS-14: Klik ulang menu sidebar User mereset kondisi List Position

17. Ketik Search `Manager`, tekan Enter
18. Klik header Name
19. Klik header Name sekali lagi (Z-A)
20. Ubah ukuran halaman ke 25
21. Klik menu sidebar Global Settings > User
22. Klik sub-tab Position
23. Verifikasi Search kosong
24. Verifikasi sort kembali default Name A-Z
25. Verifikasi halaman aktif 1
26. Verifikasi ukuran halaman kembali ke default 10
27. Buka Filter Panel
28. Verifikasi Filter Panel tanpa nilai ter-apply
29. Tutup Filter Panel

### TC-GS-POS-13: Refresh F5 mempertahankan Search, Sort, Filter, halaman, dan ukuran halaman

30. Ketik Search `a`, tekan Enter
31. Klik header Last Updated (Oldest First)
32. Catat Last Updated baris pertama sebagai batas awal rentang Filter
33. Buka Filter
34. Pilih rentang Last Updated dari batas awal hingga hari ini (mencakup semua record)
35. Klik `[Apply]`
36. Tutup Filter Panel dengan klik ikon Filter
37. Ubah ukuran halaman ke 25
38. Catat halaman aktif
39. Tekan F5
40. Verifikasi keyword Search `a` tetap terisi
41. Verifikasi tabel menampilkan sedikitnya satu baris
42. Verifikasi tabel tetap tersaring
43. Verifikasi sort Last Updated Oldest First tetap aktif
44. Buka Filter Panel
45. Verifikasi Filter Last Updated tetap ter-apply dengan rentang yang sama
46. Tutup Filter Panel
47. Verifikasi ukuran halaman tetap 25
48. Verifikasi halaman aktif tetap sama dengan yang dicatat
49. Ubah ukuran halaman ke 10
50. Klik menu sidebar Global Settings > User
51. Klik sub-tab Position

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 15, 14, 13. TC-GS-POS-15 dan 14 memakai Search `Manager` yang sama dan state tabel awal bersih; TC-GS-POS-13 mengubah Sort, Filter, dan ukuran halaman sehingga ditaruh terakhir. Urutan ini menyimpang dari urutan TC sumber (13, 14, 15). Pembukaan Global Settings > User > Position dilakukan hook `beforeEach` dan dipakai bersama ketiga TC. Spec 004 dipisah dari spec 003 (pagination, dataset sama) karena gabungannya 77 langkah (27 dan 51) dan F5 pada TC-GS-POS-13 memuat ulang halaman sehingga kegagalan keras di blok itu menghilangkan makna blok pagination.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 (mencatat baris hasil Search sebagai pembanding "baris yang sama" pada langkah 8), langkah 16 (klik `(←)` pada kotak Search untuk menutup input dan mereset tabel sebelum TC-GS-POS-14), langkah 32 dan 38 (mencatat pembanding Filter dan halaman), langkah 36 (menutup Filter Panel yang tetap terbuka sesudah `[Apply]`, sehingga langkah 44 membukanya dari keadaan tertutup), langkah 49 (memulihkan ukuran halaman ke 10 secara eksplisit sesudah TC-GS-POS-13 mengubahnya ke 25), serta dua langkah terakhir (klik menu sidebar lalu sub-tab Position agar state tabel kembali default).
- Buka dan tutup Filter Panel pada langkah 11, 27, dan 44 (beserta penutupnya) diperlukan untuk mengamati nilai Filter ter-apply (Expected TC menyebut Filter Panel/Filter tetap ter-apply atau kosong); pembukaan panel tidak mengubah state.
- Expected b TC-GS-POS-15 menyebut Sort, Filter, halaman aktif, dan ukuran halaman "sama seperti sebelum pindah tab"; langkah TC hanya mengisi Search sehingga nilai pembandingnya adalah nilai default (Sort Name A-Z, tanpa Filter, halaman 1, ukuran 10).
- Langkah 2 (baris pembanding `IT Manager`) dan langkah 3 (setiap baris memuat `Manager`) adalah asersi tambahan sebagai anchor positif agar "tabel tetap tersaring" pada langkah 8 bermakna; keduanya tidak ada di Expected TC-GS-POS-15 (S-03).
- Langkah 41 adalah asersi tambahan di luar Expected TC-GS-POS-13: pembanding generik "sedikitnya satu baris" sebagai anchor positif agar "tabel tetap tersaring" pada langkah 42 bermakna.
- Spec melewati sekitar 35 langkah (51 langkah). Seluruhnya satu kelas (retensi state tabel Position), satu akun, dataset yang sama, tanpa aksi yang mengubah data; tiap blok TC memulai dari state tabel bersih dan tetap bermakna bila blok lain gagal.
- Temuan untuk QA:
  - TC sumber tidak menyatakan bahwa entitas Total Control tidak memuat Position selain Pre-setup 10 sampai 16; spec mengasumsikan N = 15 hanya dari 7 Pre-setup dan 8 Data Dinamis.
  - Keadaan Filter Panel sesudah F5 tidak didefinisikan di TC; spec menutup panel sebelum F5 (langkah 36) dan membukanya lagi sesudah F5 (langkah 44).
  - TC-GS-POS-13 tidak menyebut halaman aktif sebelum F5; spec mencatatnya sebelum F5 (dengan Search `a` dan ukuran 25, hasil muat satu halaman sehingga halaman 1).
  - TC-GS-POS-14 langkah 3 mengklik menu sidebar "Global Settings > User" lalu sub-tab Position; TC tidak menyebut sub-tab yang aktif sesudah klik sidebar, sehingga spec mengklik sub-tab Position secara eksplisit.
