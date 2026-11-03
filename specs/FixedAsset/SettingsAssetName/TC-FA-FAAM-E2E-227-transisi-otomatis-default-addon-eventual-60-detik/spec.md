---
id: TC-FA-FAAM-E2E-227-transisi-otomatis-default-addon-eventual-60-detik
title: "Transisi Otomatis Default Addon (Eventual, Polling 60 Detik): Pending Tag, Pending Removal, dan Pelepasan Roster"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-722
  - TC-FA-FAAM-723
  - TC-FA-FAAM-731
coverage:
  web: automated
---

# Transisi Otomatis Default Addon (Eventual, Polling 60 Detik): Pending Tag, Pending Removal, dan Pelepasan Roster

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`) dengan akses baca roster modul Tracking. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (fixture dasar, tidak dipakai langsung; spec memakai salinan bersuffix): No. 30c, 30d, 30e. Lisensi Tracking tersedia 5 untuk Pre-setup No. 30c (dicatat sebagai nilai awal).
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-227`:
  - `Pairing Wait Item {runId}-227` (Total Asset 1; Default Addon `Tracking`; satu aset Active belum TAG pairing berstatus `pending_tag`).
  - `Removal Wait Item {runId}-227` (Total Asset 1; Default Addon `Tracking` sudah dilepas; satu aset Active berstatus `pending_removal` karena transaksi aktif di modul Tracking).
  - `Release Pending Item {runId}-227` (Total Asset 2; Default Addon `Tracking`; dua aset Active, satu `pending_quota` dan satu `pending_tag`, terdaftar di roster Tracking).
- Kemampuan teknis: roster modul Tracking (mode baca); polling worker commit (muat ulang tiap 5 detik, batas 60 detik; bagian 6 konvensi) sebagai idiom baku untuk transisi otomatis mode Eventual (`FAAM-LOGIC-06i`); pairing TAG `QR` pada aset dan penyelesaian transaksi aktif di modul Tracking lewat sesi API aktor hingga tersimpan (kemampuan disediakan tim BE/FE, TC menyebutnya sebagai langkah "lewat modul `tag/`").
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus seed milik spec ini dan pulihkan lisensi Tracking tersedia 5 lewat API.
- State global yang diubah: lisensi Tracking tersedia (dipakai satu oleh TC-FA-FAAM-722; dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-722, 723, 731: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-722: Aset pending_tag berpindah ke enrolled_via_default setelah TAG ter-pairing

1. Buka roster modul Tracking (mode baca)
2. Verifikasi aset `Pairing Wait Item {runId}-227` berstatus `pending_tag`
3. Verifikasi aset `Pairing Wait Item {runId}-227` tidak memakai lisensi Tracking (lisensi Tracking tersedia 5)
4. Selesaikan pairing TAG `QR` pada aset itu lewat modul `tag/` hingga tersimpan
5. Muat ulang roster Tracking tiap 5 detik sampai status aset berubah, batas 60 detik sejak langkah 4
6. Verifikasi di roster modul Tracking aset `Pairing Wait Item {runId}-227` berstatus `enrolled_via_default`
7. Verifikasi aset itu memakai satu lisensi Tracking (lisensi Tracking tersedia menjadi 4)

### TC-FA-FAAM-723: Aset pending_removal di-unenroll setelah transaksi aktif selesai

8. Buka roster modul Tracking (mode baca)
9. Verifikasi aset `Removal Wait Item {runId}-227` berstatus `pending_removal` dan tetap terdaftar (tidak diputus paksa)
10. Selesaikan transaksi aktif aset itu di modul Tracking hingga tersimpan
11. Muat ulang roster Tracking tiap 5 detik sampai status aset berubah, batas 60 detik sejak langkah 10
12. Verifikasi di roster modul Tracking aset `Removal Wait Item {runId}-227` tidak lagi terdaftar

### TC-FA-FAAM-731: Hapus Default Addon melepas aset pending_quota dan pending_tag dari roster

13. Buka roster modul Tracking (mode baca)
14. Verifikasi aset `pending_quota` dan `pending_tag` milik `Release Pending Item {runId}-227` terdaftar di roster Tracking
15. Buka Fixed Asset > Settings > Asset Master > Asset Name
16. Ketik Search `Release Pending Item {runId}-227`, tekan Enter
17. Klik `⋯` baris `Release Pending Item {runId}-227` lalu `Edit`
18. Lepas Default Addon `Tracking`
19. Klik `[Save]`
20. Verifikasi dialog `Change Default Addon` tidak tampil
21. Verifikasi toast `Success, asset name has been updated.`
22. Buka roster modul Tracking (mode baca)
23. Verifikasi kedua aset `Release Pending Item {runId}-227` tidak lagi terdaftar di roster Tracking

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 8, 13, 15, 22 (navigasi), langkah 5 dan 11 (idiom polling worker commit), dan langkah 16 (Search untuk menemukan baris target).
- Langkah 12 dan 23 adalah asersi absence atas roster dengan anchor positif: langkah 9 (aset terdaftar sebelum aksi) dan langkah 14 (kedua aset terdaftar sebelum aksi) pada roster yang sama.
- Langkah 20 adalah asersi absence dialog dengan anchor positif langkah 21 (toast sukses tampil setelah `[Save]`).
- Temuan untuk QA:
  - TC-FA-FAAM-722 dan 723 menyebut pairing TAG dan penyelesaian transaksi "lewat modul `tag/`" atau "di modul Tracking" tanpa menyebut aktor; spec memakai sesi API aktor Total Control.
  - TC-FA-FAAM-731 menyebut roster "mode baca" tanpa path menu; spec menulis "roster modul Tracking (mode baca)".
