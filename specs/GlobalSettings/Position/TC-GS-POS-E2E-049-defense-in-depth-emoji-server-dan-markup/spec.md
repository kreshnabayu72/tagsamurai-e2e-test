---
id: TC-GS-POS-E2E-049-defense-in-depth-emoji-server-dan-markup
title: "Defense-in-Depth: Emoji Lolos Filter FE Ditolak Server pada Create dan Edit, dan Nama Berisi Markup Dirender sebagai Teks"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-46
  - TC-GS-POS-84
  - TC-GS-POS-266
coverage:
  web: automated
---

# Defense-in-Depth: Emoji Lolos Filter FE Ditolak Server pada Create dan Edit, dan Nama Berisi Markup Dirender sebagai Teks

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position (sidebar Global Settings, sub-tab Position). Spec ini tidak menguji navigasi sehingga `## Test Steps` tidak mengulang langkah buka.
- Data Pre-setup: tidak ada yang dipakai.
- Data Dinamis (suffix per run dan nomor spec): `Legal Counsel {runId}-049` (target Edit TC-GS-POS-84, di-seed lewat API di hook `before`; fixture baru `Fixture.position.editTarget049`). Nilai uji yang ditolak server adalah `Sales 🚀 Lead {runId}-049` (TC-GS-POS-46) dan `Legal 🚀 Counsel {runId}-049` (TC-GS-POS-84); record `<b>Ops</b> Lead {runId}-049` dibuat lewat UI pada TC-GS-POS-266. Nama uji diberi suffix agar cleanup deterministik bila server ternyata menerimanya.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-049` yang masih ada; kosongkan Search tabel Position.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-position` true untuk akun Total Control dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: menyetel value field Position Name langsung pada DOM (menjalankan script pada halaman) dan memicu event `input` untuk mensimulasikan emoji yang lolos filter keystroke FE; pembacaan struktur DOM sel tabel, Popup Changelog, dan dialog untuk memastikan tidak ada elemen markup hasil render.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan seperti di atas).

## Test Steps

### TC-GS-POS-46: Create, emoji lolos filter FE ditolak server

1. Klik `[+ Position]`
2. Injeksi value `Sales 🚀 Lead {runId}-049` langsung ke DOM field Position Name (bypass filter keystroke FE) dan picu event `input`
3. Klik `[Submit]`
4. Verifikasi tidak ada toast sukses
5. Verifikasi error inline di bawah field Position Name: "Position Name contains invalid characters"
6. Verifikasi Popup Create Position tetap terbuka
7. Verifikasi input Position Name dipertahankan dengan nilai `Sales 🚀 Lead {runId}-049`
8. Klik `✕` pada Popup Create Position
9. Verifikasi dialog `Unsaved Changes`
10. Klik `[Leave]`

### TC-GS-POS-84: Edit, emoji lolos filter FE ditolak server

11. Ketik Search `Legal Counsel {runId}-049` pada tabel Position, tekan Enter
12. Klik `⋯` pada baris `Legal Counsel {runId}-049`, pilih `Edit`
13. Injeksi value `Legal 🚀 Counsel {runId}-049` langsung ke DOM field Position Name (bypass filter keystroke FE) dan picu event `input`
14. Klik `[Save]`
15. Verifikasi error inline di bawah field Position Name: "Position Name contains invalid characters"
16. Verifikasi Popup Edit Position tetap terbuka
17. Verifikasi input Position Name dipertahankan dengan nilai `Legal 🚀 Counsel {runId}-049`
18. Klik `✕` pada Popup Edit Position
19. Verifikasi dialog `Unsaved Changes`
20. Klik `[Leave]`
21. Klik `(←)` pada kotak Search tabel Position

### TC-GS-POS-266: Nama berisi markup dirender sebagai teks

22. Klik `[+ Position]`
23. Isi Position Name dengan `<b>Ops</b> Lead {runId}-049`
24. Klik `[Submit]`
25. Ketik Search `Ops` pada tabel Position, tekan Enter
26. Verifikasi kolom Name tabel menampilkan teks literal `<b>Ops</b> Lead {runId}-049`
27. Verifikasi sel Name tidak berformat tebal
28. Verifikasi sel Name tidak memuat elemen `b` hasil render
29. Klik ikon Changelog, ketik Search `Ops`, tekan Enter
30. Verifikasi Changelog menampilkan teks literal `<b>Ops</b> Lead {runId}-049` pada entri Create
31. Verifikasi Changelog tidak memuat markup yang dieksekusi (tidak ada elemen `b` hasil render)
32. Tutup Popup Changelog dengan `✕`
33. Klik `⋯` pada baris `<b>Ops</b> Lead {runId}-049`, pilih `Delete`
34. Verifikasi bullet dialog `Delete Position` menampilkan teks literal `<b>Ops</b> Lead {runId}-049`
35. Verifikasi dialog tidak memuat markup yang dieksekusi (tidak ada elemen `b` hasil render)
36. Klik `[Cancel]` pada dialog `Delete Position`
37. Klik `(←)` pada kotak Search tabel Position

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`. Spec ini kelas a (defense-in-depth): nilai yang lolos filter keystroke FE diinjeksi ke DOM, bukan dikirim lewat klien HTTP; asersi memakai tampilan FE atas penolakan server (error inline) sehingga tidak ada request langsung ke server.
- Spec memuat 37 langkah (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu kelas (defense-in-depth) dan satu akun; dua TC penolakan (TC-GS-POS-46 dan 84) tidak membuat data dan TC-GS-POS-266 yang membuat record berada di akhir, sehingga kegagalan TC-GS-POS-266 tidak menghilangkan makna dua TC penolakan.
- Urutan TC di spec: 46, 84, 266. TC sumber berurutan sama. Dua TC penolakan (validasi diblokir) ditaruh sebelum TC-GS-POS-266 yang membuat record.
- Pembagian TC lintas spec: validasi emoji lewat keystroke (diblok tanpa pesan, NC-18) ada di spec Create dan Edit; spec ini hanya memuat penolakan server atas emoji yang lolos filter FE.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11 (mencari baris target), langkah 21 dan 37 (mengosongkan Search tabel lewat `(←)`), langkah 25 (mencari baris `<b>Ops</b> Lead`), langkah 29 (Search `Ops` di Popup Changelog untuk menemukan entri milik spec karena Changelog kumulatif), langkah 32 (menutup Popup Changelog dengan `✕`; popup tidak dirty), dan langkah 36 (`[Cancel]` pada dialog `Delete Position` agar record tidak dihapus oleh spec; record dihapus di hook `after`). Langkah 28 (sel Name tidak memuat elemen `b`) adalah asersi tambahan di luar Expected TC-GS-POS-266 a sebagai padanan teknis "tanpa format tebal" (langkah 26 dan 27): format tebal pada sel dihasilkan elemen `b` hasil render. Form dibuka tiga kali (langkah 1, 12, 22) dan ditutup tiga kali (langkah 8 dan 18 lewat `✕` dan `[Leave]`, langkah 24 lewat `[Submit]` sukses).
- Temuan untuk QA:
  - Post Condition TC-GS-POS-46 ("Tidak ada record baru") dan TC-GS-POS-84 ("Nama record tetap `Legal Counsel`") tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini.
  - TC-GS-POS-46 dan 84 menulis nilai uji `Sales 🚀 Lead` dan `Legal 🚀 Counsel` tanpa suffix; spec menambahkan suffix `{runId}-049` pada nilai uji sehingga record tidak bentrok antar-run bila server menerima nilai itu.
  - TC-GS-POS-266 menulis nilai `<b>Ops</b> Lead` tanpa suffix; spec memakai `<b>Ops</b> Lead {runId}-049` karena record dibuat dan diasersi.
  - TC-GS-POS-46 dan 84 tidak menyebut mekanisme injeksi DOM; spec menuliskannya sebagai kemampuan teknis di Prerequisites (script pada halaman dan event `input`).
  - TC-GS-POS-266 Expected b ("tidak ada script/markup dieksekusi") tidak menyebut cara mengamatinya; spec mengasersi tidak ada elemen `b` hasil render pada Changelog dan dialog.
