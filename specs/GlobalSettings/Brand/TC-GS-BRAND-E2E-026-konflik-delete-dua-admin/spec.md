---
id: TC-GS-BRAND-E2E-026-konflik-delete-dua-admin
title: "Konflik Delete dan Bulk Delete Brand oleh Dua Admin"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-BRAND-103
  - TC-GS-BRAND-123
  - TC-GS-BRAND-291
coverage:
  web: automated
---

# Konflik Delete dan Bulk Delete Brand oleh Dua Admin

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (admin utama): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (admin kedua): Total Control Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`. Fixture akun belum ada; tim FE menyiapkan akun ini di Client A.
- Dua sesi browser (kelas multi-konteks): Sesi A dan Sesi B berjalan di konteks browser terpisah dengan sesi login sendiri. Keduanya login di hook `before` spec ini (seedSession, kredensial dari env var) dan berada di Global Settings > Master Reference > Brand. Hook `after` menutup konteks Sesi B dan mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` dan `GS_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data dinamis (seeding lewat API di hook `before`, semuanya bebas relasi; tidak menumpang spec lain): `Gale Co {runId}-026` (D-19), `Ulm Co {runId}-026` dan `Vine Co {runId}-026` (D-24), `Wade Co {runId}-026` dan `Xylo Co {runId}-026` (D-41). Seluruh brand dihapus oleh spec ini; tidak ada rename.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API kelima brand di atas bila masih ada. Hook `beforeEach`: tutup dialog yang terbuka di kedua sesi lalu kembali ke Global Settings > Master Reference > Brand.
- Kemampuan teknis: dua konteks browser paralel dalam satu spec; membaca status respons Delete (404); langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`; akses Sesi A (Total Control) ke Detail User Sari Dewi dan Nadia Pratama > Tab System Log, Changelog Brand, dan Activity Log.
- State global yang diubah: tidak ada (seluruh data milik spec dan dibersihkan).

## Test Steps

### TC-GS-BRAND-103: Delete Brand yang sudah dihapus admin lain

1. [Sesi A] Cari baris `Gale Co {runId}-026`, lalu klik `⋯` > Delete → dialog Delete Brand tampil
2. [Sesi B] Muat ulang halaman Brand, cari baris `Gale Co {runId}-026`, lalu klik `⋯` > Delete
3. [Sesi B] Klik [Delete]
4. [Sesi B] Tunggu hingga Delete selesai (toast sukses tampil)
5. [Sesi A] Klik [Delete]
6. [Sesi A] Verifikasi respons Delete berstatus `404`
7. [Sesi A] Verifikasi toast netral: "This brand is no longer available."
8. [Sesi A] Verifikasi list di-refresh dan `Gale Co {runId}-026` tidak ada

### TC-GS-BRAND-123: Bulk Delete saat salah satu brand sudah dihapus admin lain

9. [Sesi A] Search `{runId}-026`
10. [Sesi A] Centang baris `Ulm Co {runId}-026` dan `Vine Co {runId}-026`
11. [Sesi A] Klik `Bulk Action` > `Delete` → dialog Bulk Delete homogen (Dialog 4) tampil
12. [Sesi B] Muat ulang halaman Brand, cari baris `Ulm Co {runId}-026`, lalu klik `⋯` > Delete
13. [Sesi B] Klik [Delete]
14. [Sesi B] Tunggu hingga Delete selesai (toast sukses tampil)
15. [Sesi A] Klik [Delete]
16. [Sesi A] Verifikasi `Vine Co {runId}-026` terhapus
17. [Sesi A] Verifikasi `Ulm Co {runId}-026` dilewati tanpa pesan terpisah
18. [Sesi A] Verifikasi toast: "Success, brand has been deleted. Some items were skipped."
19. [Sesi A] Verifikasi list di-refresh dan `Ulm Co {runId}-026` serta `Vine Co {runId}-026` tidak ada

### TC-GS-BRAND-291: Bulk Delete saat seluruh brand terpilih sudah dihapus admin lain

20. [Sesi A] Search `{runId}-026`
21. [Sesi A] Centang baris `Wade Co {runId}-026` dan `Xylo Co {runId}-026`
22. [Sesi A] Klik `Bulk Action` > `Delete` → dialog Bulk Delete homogen (Dialog 4) tampil
23. [Sesi B] Muat ulang halaman Brand, lalu Search `{runId}-026`
24. [Sesi B] Centang baris `Wade Co {runId}-026` dan `Xylo Co {runId}-026`, lalu klik `Bulk Action` > `Delete`
25. [Sesi B] Klik [Delete]
26. [Sesi B] Tunggu hingga Delete selesai (toast sukses tampil)
27. [Sesi A] Klik [Delete]
28. [Sesi A] Verifikasi toast netral: "This brand is no longer available."
29. [Sesi A] Verifikasi tabel di-refresh dan `Wade Co {runId}-026` serta `Xylo Co {runId}-026` tidak ada
30. [Sesi A] Verifikasi toast sukses dan toast skipped tidak tampil
31. [Sesi A] Verifikasi Bulk Action Bar hilang dan seleksi 0

### Hitungan entri log tiga surface: TC-GS-BRAND-103 c, TC-GS-BRAND-123 d, TC-GS-BRAND-291 c

32. [Sesi A] Buka Changelog Brand, Search `{runId}-026`
33. [Sesi A] Verifikasi Changelog: tepat 1 entri `Delete` untuk `Gale Co {runId}-026` (dari admin kedua; TC-103 c)
34. [Sesi A] Verifikasi Changelog: tepat 1 entri `Delete` untuk `Ulm Co {runId}-026` (dari admin kedua; TC-123 d)
35. [Sesi A] Verifikasi Changelog: tepat 1 entri `Delete` untuk `Vine Co {runId}-026` (TC-123 d)
36. [Sesi A] Verifikasi Changelog: tepat 1 entri `Delete` untuk `Wade Co {runId}-026` (dari admin kedua; TC-291 c)
37. [Sesi A] Verifikasi Changelog: tepat 1 entri `Delete` untuk `Xylo Co {runId}-026` (dari admin kedua; TC-291 c)
38. [Sesi A] Buka Global Settings > User > Detail Sari Dewi > Tab System Log, Search `{runId}-026`
39. [Sesi A] Verifikasi System Log Sari Dewi: tepat 1 entri `Delete` untuk `Vine Co {runId}-026` dari Bulk Delete Sesi A (TC-123 d)
40. [Sesi A] Buka Global Settings > User > Detail Nadia Pratama > Tab System Log, Search `{runId}-026`
41. [Sesi A] Verifikasi System Log Nadia Pratama: tepat 1 entri `Delete` untuk `Ulm Co {runId}-026` (TC-123 d)
42. [Sesi A] Verifikasi System Log Nadia Pratama: tepat 1 entri `Delete` untuk `Wade Co {runId}-026` (TC-291 c)
43. [Sesi A] Verifikasi System Log Nadia Pratama: tepat 1 entri `Delete` untuk `Xylo Co {runId}-026` (TC-291 c)
44. [Sesi A] Buka Global Settings > Activity Log, Search `{runId}-026`
45. [Sesi A] Verifikasi Activity Log: tepat 1 entri `Delete` untuk `Gale Co {runId}-026` (TC-103 c)
46. [Sesi A] Verifikasi Activity Log: tepat 1 entri `Delete` untuk `Ulm Co {runId}-026` (TC-123 d)
47. [Sesi A] Verifikasi Activity Log: tepat 1 entri `Delete` untuk `Vine Co {runId}-026` (TC-123 d)
48. [Sesi A] Verifikasi Activity Log: tepat 1 entri `Delete` untuk `Wade Co {runId}-026` (TC-291 c)
49. [Sesi A] Verifikasi Activity Log: tepat 1 entri `Delete` untuk `Xylo Co {runId}-026` (TC-291 c)

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`. Kelas harness: multi-konteks (dua sesi admin), bagian 3 prinsip 13c.
- Seluruh TC di spec ini berujung penghapusan brand milik spec sendiri; urutan mengikuti nomor TC sumber karena data tiap TC independen. Pengecekan log dikumpulkan di bagian akhir (langkah 32 sampai 49) supaya tiap surface dibuka sekali, bukan per TC; tiap Verifikasi menyebut TC dan butir sumbernya.
- Asersi pencatatan TC-103 butir c (Changelog dan Activity Log), TC-123 butir d, dan TC-291 butir c (Changelog, System Log, dan Activity Log) ditulis sebagai asersi jumlah ("tepat 1 entri Delete per brand"), bukan asersi absence kelas g; hitungan tepat 1 sudah menyatakan tidak ada entri Delete kedua, sehingga tidak ada klausa negasi terpisah. TC-103 c tidak menyebut System Log, sehingga `Gale Co` tidak diperiksa di System Log. Asersi absence dua sesi dan request langsung dicakup spec `TC-GS-BRAND-E2E-075-log-absence-dua-sesi-dan-request-langsung`.
- System Log tercatat per aktor: entri Delete `Ulm Co`, `Wade Co`, dan `Xylo Co` milik Nadia Pratama (langkah 41 sampai 43; `Gale Co` tidak diperiksa di System Log karena TC-103 c hanya menyebut Changelog dan Activity Log), entri Delete `Vine Co` milik Sari Dewi (langkah 39).
- Brand yang dihapus Sesi B pada TC-123 dan TC-291 dihapus lewat UI (Sesi B menampilkan list sendiri), sehingga tiap TC memuat satu pembuka dialog di Sesi A sebelum Sesi B menghapus (TC sumber: "Admin kedua menghapus ...").
- Langkah penghubung: langkah 2, 12, dan 23 (muat ulang halaman Brand di Sesi B supaya tabel terbaru; langkah 23 sekaligus Search brand milik spec); langkah 4, 14, dan 26 (menunggu Delete Sesi B selesai sebelum Sesi A melanjutkan); langkah 9 dan 20 (Search `{runId}-026` di Sesi A supaya brand dinamis spec tampil sebelum dicentang); langkah 32, 38, 40, dan 44 (navigasi ke surface log dan Search brand milik spec).
- Spec memuat 49 langkah (melewati batas smell sekitar 35) karena hitungan log tiga surface dan dua sesi ditulis eksplisit; seluruhnya satu kelas harness, sehingga tidak dipecah.
- Spec ini tidak memuat aksi Sesi A yang mengubah brand milik spec lain; seeding `Wade Co` dan `Xylo Co` dibuat di `before` karena Dependensi TC sumber kosong.
