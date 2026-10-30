---
id: TC-GS-FILEMGR-E2E-023-permanently-delete-sukses-bulk-dan-kosongkan-recycle-bin
title: "Permanently Delete Berhasil: Single, Klik Ganda, Bulk, dan Kosongkan Recycle Bin"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-90
  - TC-GS-FILEMGR-95
  - TC-GS-FILEMGR-100
  - TC-GS-FILEMGR-103
coverage:
  web: automated
---

# Permanently Delete Berhasil: Single, Klik Ganda, Bulk, dan Kosongkan Recycle Bin

## Prerequisites

- Mode: FE+BE.
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Tabel A3, 16 file di Recycle Bin. Hook `before` memastikan Tabel A3 tersedia secara idempotent. TC-GS-FILEMGR-103 menghapus permanen seluruh isi Recycle Bin environment (termasuk Tabel A3); spec lain men-seed ulang kebutuhan Recycle Bin-nya di hook `before` masing-masing, dan hook `after` spec ini men-seed ulang Tabel A3 agar Pre-setup pulih.
- Data Dinamis (seeding fixture BE di hook `before`, bersuffix per run, di Recycle Bin; seluruhnya dihapus permanen oleh spec ini, Deleted Date kurang dari retensi): `old-avatar-{runId}-023.png` (TC-GS-FILEMGR-90), `recycled-photo-02-{runId}-023.jpg` (TC-GS-FILEMGR-95), `recycled-photo-06-{runId}-023.jpg` dan `recycled-photo-07-{runId}-023.jpg` (TC-GS-FILEMGR-100). Pemilik adalah user klon milik spec.
- State global yang dibaca: Selection Limit lebih besar dari 16 (TC-GS-FILEMGR-103). Job auto-purge harian tidak boleh berjalan selama spec (menambah/menghapus baris jatuh tempo; lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE): seeding Recycle Bin dengan pemilik klon; membaca jumlah entri Changelog File Manager per File Name (baseline dicatat di hook `before`); jam server dan jam browser sinkron (S-12).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): hapus permanen sisa file seed, men-seed ulang Tabel A3, hapus user klon.
- Suite serial (`parallel: false`). Spec yang menghabisi isi Recycle Bin: jalankan sesudah spec lain bila runner mengikuti nomor (belum terbukti). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-FILEMGR-90: Permanently Delete single

1. Klik tombol Recycle Bin di toolbar, lalu catat total baris Recycle Bin dari info pagination (baseline total, sebelum Search)
2. Ketik Search `old-avatar-{runId}-023`, tekan Enter
3. Verifikasi baris `old-avatar-{runId}-023.png` tampil di Recycle Bin
4. Klik ikon `⋯` baris `old-avatar-{runId}-023.png`
5. Verifikasi opsi `Permanently Delete` tampil pada overlay
6. Verifikasi tombol Recover tidak ada pada overlay
7. Klik `Permanently Delete`, lalu klik [Permanently Delete] pada dialog
8. Verifikasi toast sukses: "Success, old-avatar-{runId}-023.png has been permanently deleted."
9. Verifikasi baris `old-avatar-{runId}-023.png` hilang dari Recycle Bin
10. Kosongkan Search (klik `(←)` pada kotak Search)
11. Verifikasi total baris Recycle Bin pada info pagination sama dengan baseline total dikurangi satu

### TC-GS-FILEMGR-95: Klik ganda cepat pada Permanently Delete

12. Ganti isi kotak search dengan `recycled-photo-02-{runId}-023`, tekan Enter
13. Klik ikon `⋯` baris `recycled-photo-02-{runId}-023.jpg`, lalu klik `Permanently Delete`
14. Klik ganda cepat pada [Permanently Delete]
15. Verifikasi hanya satu toast sukses "Success, recycled-photo-02-{runId}-023.jpg has been permanently deleted." tampil
16. Tutup modal Recycle Bin dengan `✕` di header
17. Klik ikon Changelog di toolbar, ketik Search `recycled-photo-02-{runId}-023`, tekan Enter
18. Verifikasi jumlah entri Action `Permanently Delete` untuk `recycled-photo-02-{runId}-023.jpg` tepat satu (baseline ditambah satu)
19. Tutup modal Changelog dengan `✕` di header

### TC-GS-FILEMGR-100: Bulk Permanently Delete

20. Klik tombol Recycle Bin di toolbar, lalu ketik Search `recycled-photo-0`, tekan Enter
21. Centang baris `recycled-photo-06-{runId}-023.jpg` dan `recycled-photo-07-{runId}-023.jpg`
22. Klik `Bulk Action`, klik `Permanently Delete`, lalu klik [Permanently Delete] pada dialog
23. Verifikasi toast sukses: "Success, file has been permanently deleted."
24. Verifikasi bar hilang
25. Verifikasi seleksi kembali 0
26. Verifikasi kedua baris hilang dari Recycle Bin

### TC-GS-FILEMGR-103: Kosongkan Recycle Bin lewat Select All

27. Kosongkan Search (klik `(←)` pada kotak Search)
28. Verifikasi tombol `Select All (16 records)` tampil (Recycle Bin hanya berisi Tabel A3)
29. Klik tombol `Select All (16 records)`
30. Verifikasi seluruh 16 baris tercentang lintas halaman dan bar menampilkan `16 Files selected`
31. Klik `Bulk Action`, klik `Permanently Delete`, lalu klik [Permanently Delete] pada dialog
32. Verifikasi toast sukses: "Success, file has been permanently deleted."
33. Verifikasi Recycle Bin menampilkan empty state `Recycle bin is empty`
34. Verifikasi tidak ada tombol Empty All di modul Recycle Bin
35. Verifikasi tidak ada tombol Recover di modul Recycle Bin

## Notes

- Mode: FE+BE (destruktif). Subjudul `###` memetakan langkah ke id TC granular. TC-GS-FILEMGR-103 di akhir karena menghabisi seluruh isi Recycle Bin (prinsip 5).
- Urutan TC pada spec: 90, 95, 100, 103 (sama dengan TC sumber).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1 (membuka modal dan mencatat baseline total baris dari info pagination sebelum Search), 2, 12, 20 (Search), 10 dan 27 (mengosongkan Search), 16, 17, 19 (membuka dan menutup modal).
- Asersi tambahan di luar Expected TC (S-03): langkah 3 (anchor sebelum aksi), 5 (anchor untuk absence Recover pada langkah 6), 28 (precondition hitungan 16), 9 dan 26 (anchor absence memakai toast sukses langkah 8 dan 23, butir 2 bagian 8b), 34 dan 35 (anchor: empty state `Recycle bin is empty` langkah 33).
- TC-GS-FILEMGR-90 butir b menyebut "jumlah baris menjadi 15" (16 - 1); spec mengasersi total baris Recycle Bin (info pagination) sama dengan baseline total dikurangi satu karena Recycle Bin berisi baris seed lain; baseline dicatat sebelum Search (langkah 1) dan Search dikosongkan dulu (langkah 10) agar yang dihitung total, bukan hasil Search (langkah 11).
- Temuan untuk QA:
  - Q-3: job auto-purge harian dapat menghapus baris jatuh tempo (mis. R04 `due-photo.png`) di tengah spec sehingga hitungan 16 berubah; job perlu dijeda di environment e2e.
  - Q-4: seeding Recycle Bin tidak punya mekanisme di TC; ditulis "disediakan tim FE/BE".
  - Q-5/Q-7: TC menargetkan baris Pre-setup R01, R06, R10, R11 untuk dihapus permanen (merusak Tabel A3 untuk spec lain); spec memakai file bersuffix. TC-GS-FILEMGR-103 menghapus seluruh Tabel A3 karena Select All tidak menyaring; dipulihkan lewat seeding ulang.
  - Post Condition TC-GS-FILEMGR-90 butir a (record dan file fisik terhapus permanen) dan butir b (satu entri log di tiga surface, assertion detail di Section 5) tidak memiliki langkah observasi di TC; butir b diasersi di spec `TC-GS-FILEMGR-E2E-055`. Post Condition TC-GS-FILEMGR-100 butir a dan b juga tidak diasersi di spec ini.
  - Hitungan "tepat satu entri log" (TC-GS-FILEMGR-95 b) diasersi di Changelog File Manager saja; TC tidak menyebut surface lain.
