---
id: TC-GS-ACTLOG-E2E-015-absence-concurrent-limit-download-dan-aksi-sumber-gagal-tidak-tercatat
title: "Absence: Concurrent Limit, Download, dan Aksi Sumber Gagal Tidak Tercatat"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-47
  - TC-GS-ACTLOG-138
  - TC-GS-ACTLOG-212
coverage:
  web: automated
---

# Absence: Concurrent Limit, Download, dan Aksi Sumber Gagal Tidak Tercatat

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun Total Control Client A (Sari Dewi) dan halaman Global Settings > Brand (kemampuan disediakan tim FE/BE)
- Akun aktor: Total Control Client A (Sari Dewi), `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Activity Log > Session.
- Checkbox "Stay on this form after submitting" pada form Create Brand dibiarkan default (tidak dicentang), sehingga [Submit] yang sukses menutup modal.
- Environment variable: `GS_TC_PASSWORD`, `ACTLOG_PASSWORD` (password uji yang dipasang ke user dinamis modul Activity Log). Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- State global yang diubah: batas lisensi Concurrent Fixed Asset Client A diturunkan ke nilai uji (nilai awal dan nilai uji disediakan tim FE) di hook `before` supaya login Fixed Asset berikutnya mencapai batas; hook `after` memulihkan nilai awal walau spec gagal di tengah. State ini dipakai bersama spec lain pada Client A, sehingga suite berjalan serial (`parallel: false`, lihat suite.md). Selain itu hanya intercept sementara pada langkah 26 sampai 29. Spec ini tidak menggeser jam.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi):
  - User `John Doe {runId}-015` dengan akses Fixed Asset pada Client A, dibuat lewat API di hook `before`; login Fixed Asset user ini mencapai batas Concurrent sehingga event `Concurrent limit reached` tercatat untuk produk Fixed Asset milik user ini; entri Login platform user ini ada. Password `Spectra.env.ACTLOG_PASSWORD`.
  - Brand `Rollback Test {runId}-015`: diajukan lewat form Create Brand dan gagal 5xx (tidak pernah tercipta).
  - Brand `Brand Anchor {runId}-015`: dibuat spec lewat UI pada TC-GS-ACTLOG-212 sebagai anchor positif.
- Kemampuan teknis (disediakan tim FE/BE): (a) pemicu event `Concurrent limit reached` untuk produk Fixed Asset (batas Concurrent Fixed Asset dibuat tercapai lalu login Fixed Asset berikutnya dikirim oleh user uji); (b) `Spectra.intercept()` pada request Create Brand modul Brand dengan respons 5xx (endpoint sesuai LLD modul Brand, tidak ditentukan di TC ini), dipasang sesaat sebelum [Submit] pertama dan dilepas segera sesudahnya (langkah 26 sampai 29); (c) penangkapan berkas unduhan browser untuk Download CSV dan XLSX.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API user `John Doe {runId}-015` dan Brand `Brand Anchor {runId}-015` (serta `Rollback Test {runId}-015` bila ternyata tercipta); pulihkan batas Concurrent Fixed Asset Client A; lepaskan intercept bila masih terpasang.

## Test Steps

### TC-GS-ACTLOG-47: Note Concurrent limit reached tidak muncul di Tab Session

1. Buka Global Settings > Activity Log > Session
2. Ketik Search `John Doe {runId}-015`, tekan Enter
3. Verifikasi baris Login platform milik `John Doe {runId}-015` tampil
4. Ganti isi kotak search dengan `Concurrent`, tekan Enter
5. Verifikasi tidak ada baris dengan Note `Concurrent limit reached`
6. Verifikasi tampil `"No results found"`
7. Verifikasi tampil `"Try adjusting your search or filter."`
8. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
9. Verifikasi tabel Session memuat baris log (tidak lagi `"No results found"`)
10. Ketik Search `John Doe {runId}-015`, tekan Enter
11. Verifikasi baris Login `John Doe {runId}-015` tetap tampil setelah Search dikosongkan

### TC-GS-ACTLOG-138: Download tidak menghasilkan entri log baru

12. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel, lalu catat jumlah baris dan penanda waktu entri terbaru tab Session sebagai baseline
13. Klik Tab `User Action`, catat jumlah baris dan penanda waktu entri terbaru tab User Action sebagai baseline
14. Klik Tab `Session`, klik icon Download, pilih `Download as CSV`
15. Verifikasi berkas CSV tab Session terunduh
16. Klik Tab `User Action`, klik icon Download, pilih `Download as XLSX`
17. Verifikasi berkas XLSX tab User Action terunduh
18. Muat ulang tab User Action
19. Verifikasi tabel User Action termuat kembali setelah muat ulang (baris log tampil)
20. Verifikasi tidak ada entri baru pada tab User Action yang berasal dari aksi Download (jumlah baris dan penanda waktu entri terbaru sama dengan baseline)
21. Klik Tab `Session`, muat ulang tab Session
22. Verifikasi tabel Session termuat kembali setelah muat ulang (baris log tampil)
23. Verifikasi tidak ada baris baru pada tab Session yang berasal dari aksi Download (jumlah baris dan penanda waktu entri terbaru sama dengan baseline)

### TC-GS-ACTLOG-212: Aksi sumber yang gagal tidak meninggalkan entri di Tab User Action

24. Buka Global Settings > Brand
25. Klik [+ Brand]
26. Pasang intercept 5xx pada request Create Brand dengan `Spectra.intercept()`
27. Isi Brand Name `Rollback Test {runId}-015`, klik [Submit] hingga permintaan gagal
28. Tunggu aksi selesai: tombol [Submit] aktif kembali
29. Lepas intercept
30. Ganti isi Brand Name menjadi `Brand Anchor {runId}-015`, klik [Submit]
31. Tunggu aksi selesai: modal Create Brand tertutup
32. Buka Global Settings > Activity Log > User Action, ketik Search `Brand Anchor {runId}-015`, tekan Enter
33. Verifikasi entri `Create` `Brand` `Brand Anchor {runId}-015` tampil
34. Ganti isi kotak search dengan `Rollback Test {runId}-015`, tekan Enter
35. Verifikasi tidak ada entri `Create` `Brand` `Rollback Test {runId}-015`
36. Verifikasi tampil `"No results found"`

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-47, 138, 212). Spec kelas g (asersi absence); ketiganya berisi aksi nyata (Search, Download, Create Brand yang gagal) dengan baseline masing-masing.
- Anchor positif (bagian 8b butir 2): TC-GS-ACTLOG-47 memakai baris Login platform `John Doe {runId}-015` (langkah 3) dan baris yang sama setelah Search ditutup lewat `(←)` (langkah 11); TC-GS-ACTLOG-138 memakai jumlah awal yang dicatat pada kedua tab (langkah 12 dan 13) serta bukti berkas terunduh (langkah 15 dan 17, ditambahkan sebagai anchor bahwa aksi Download benar-benar terjadi); TC-GS-ACTLOG-212 memakai entri Create Brand `Brand Anchor {runId}-015` dari modul yang sama (langkah 33).
- Pengecualian P-5: TC-GS-ACTLOG-212 memuat pemicu kelas b (respons 5xx lewat `Spectra.intercept()`) yang hanya membentuk kondisi yang diasersi tidak tercatat, bukan objek uji (P-5 butir a). Intercept dilepas segera setelah [Submit] gagal (langkah 29, S-09).
- Langkah penghubung (tanpa awalan `Verifikasi`): mengetik atau mengganti Search nama subjek bersuffix (langkah 2, 4, 10, 32, 34), menutup Search lewat `(←)` (langkah 8 dan 12), membuka halaman Brand dan Activity Log, serta mengganti Brand Name pada form Create yang sama untuk membuat Brand anchor (langkah 30), sehingga tidak ada penutupan form dirty. Langkah 28 dan 31 ("Tunggu aksi selesai") menunggu [Submit] selesai sebelum melepas intercept dan sebelum berpindah ke Activity Log (bagian 8b butir 8).
- Langkah 9 dan 10 mengganti pembacaan langsung baris Login John setelah Search dikosongkan (Expected b TC-GS-ACTLOG-47): tabel penuh tidak menjamin baris John berada di halaman pertama, sehingga baris diamati lewat Search nama subjek (langkah 10 dan 11) setelah langkah 9 membuktikan tabel sudah kembali tanpa saringan (S-03).
- Langkah 19 dan 22 (tabel termuat kembali setelah muat ulang) adalah anchor positif tambahan sebelum asersi tidak ada entri atau baris baru (S-03, bagian 8b butir 2).
- Spec ini 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu kelas harness (g, asersi absence) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah 6 dan 7 dipisah karena Expected a memuat dua teks.
- TC-GS-ACTLOG-48 (`Logged out by admin`) berada di spec `TC-GS-ACTLOG-E2E-014-isi-kolom-tab-session-reset-password-change-password-session-force-logout`; spec ini tidak memuatnya.
- Temuan untuk QA:
  - TC-GS-ACTLOG-47 tidak menyebut batas Concurrent Fixed Asset atau cara memicu event; ditulis sebagai kemampuan teknis dan state global yang disediakan tim FE/BE.
  - TC-GS-ACTLOG-138 menyebut "stempel entri terbaru" tanpa cara membacanya; spec memakai penanda waktu entri terbaru dari kolom Date. Nama berkas XLSX tidak ditulis di TC (berkas CSV: `Activity-Log-Session.csv`, `Activity-Log-User-Action.csv`), sehingga langkah 15 dan 17 tidak mengasersi nama berkas.
  - TC-GS-ACTLOG-138 dan 47 bergantung pada asumsi tidak ada baris lain yang masuk selama spec berjalan (suite `parallel: false`, sesi Client A tidak dipakai spec lain bersamaan).
  - TC-GS-ACTLOG-212 menyebut "di-intercept" tanpa menyebut endpoint; spec memakai Create Brand modul Brand tanpa menulis endpoint.
