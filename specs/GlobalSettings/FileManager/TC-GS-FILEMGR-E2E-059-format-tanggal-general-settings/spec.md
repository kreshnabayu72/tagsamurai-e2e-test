---
id: TC-GS-FILEMGR-E2E-059-format-tanggal-general-settings
title: "Format Tanggal dan Waktu General Settings pada Upload Date, Deleted Date, Date Changelog, dan Input Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-235
  - TC-GS-FILEMGR-236
  - TC-GS-FILEMGR-237
coverage:
  web: automated
---

# Format Tanggal dan Waktu General Settings pada Upload Date, Deleted Date, Date Changelog, dan Input Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`) karena spec mengubah state global General Settings. Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- State global yang diubah: General Settings Date Format dan Time Format. Hook `before` mencatat nilai awal lalu menyetel Date Format `dd/MM/yy` dan Time Format `HH:mm` (precondition TC-235; mekanisme penyetelan lewat API disediakan tim FE). Hook `after` memulihkan nilai awal walau spec gagal di tengah.
- Data milik spec (suffix `{runId}-059`, seeding lewat fixture BE di hook `before`; mekanisme seeding tidak didefinisikan di TC, disediakan tim FE/BE):
  - `budi-avatar-{runId}-059.jpg` (salinan F01), file aktif dengan Upload Date `02/09/26 14:30` (zona waktu entitas), dipakai TC-235.
  - `old-avatar-{runId}-059.png` (salinan R01) di Recycle Bin dengan Deleted Date sekarang - 1 hari; hook `before` mencatat nilai Deleted Date seed sebagai acuan format TC-236.
  - Entri Changelog File Manager `former-avatar-{runId}-059.png` (salinan C01), Action `Permanently Delete`, Date `14/09/26 02:00`, Modified By `System`, dipakai TC-237.
- Dependensi TC (TC-01 tabel utama, TC-16 Recycle Bin, TC-28 Changelog) dijalankan sebagai langkah aksi di spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus permanen lewat API file bersuffix `{runId}-059` dan pulihkan General Settings seperti di atas.

## Test Steps

### TC-GS-FILEMGR-235: Format Upload Date tabel utama dan input Filter

1. Ketik Search `budi-avatar-{runId}-059`, tekan Enter
2. Verifikasi Upload Date baris `budi-avatar-{runId}-059.jpg` tampil `02/09/26 14:30`
3. Klik Filter, pilih Upload Date 02/09/26 sampai 02/09/26
4. Verifikasi isi input Upload Date di Filter `02/09/26`
5. Tutup panel Filter lewat `✕`
6. Buka Global Settings > General Settings, ubah Date Format menjadi `M/d/yy` dan Time Format menjadi `hh:mm a`, lalu simpan
7. Tunggu aksi selesai
8. Buka Global Settings > File Manager, ketik Search `budi-avatar-{runId}-059`, tekan Enter
9. Verifikasi Upload Date baris `budi-avatar-{runId}-059.jpg` tampil `9/2/26 02:30 PM`
10. Klik Filter, pilih Upload Date 9/2/26 sampai 9/2/26
11. Verifikasi isi input Upload Date di Filter `9/2/26`
12. Tutup panel Filter lewat `✕`

### TC-GS-FILEMGR-236: Format Deleted Date modal Recycle Bin dan input Filter

13. Klik tombol Recycle Bin di toolbar, ketik Search `old-avatar-{runId}-059`, tekan Enter
14. Verifikasi Deleted Date baris `old-avatar-{runId}-059.png` tampil dengan pola `M/d/yy hh:mm a` sesuai nilai Deleted Date seed
15. Buka Filter dan pilih Deleted Date satu hari (tanggal Deleted Date baris tersebut)
16. Verifikasi isi input Deleted Date di Filter memakai pola `M/d/yy`
17. Tutup panel Filter lewat `✕`, lalu tutup modal Recycle Bin lewat `✕`

### TC-GS-FILEMGR-237: Format Date modal Changelog dan input Filter

18. Ubah General Settings menjadi Date Format `dd MMM yy` dan Time Format `HH:mm` lewat API, lalu buka Global Settings > File Manager
19. Klik ikon Changelog di toolbar, ketik Search `former-avatar-{runId}-059`, tekan Enter
20. Verifikasi Date entri `former-avatar-{runId}-059.png` tampil `14 Sep 26 02:00`
21. Buka Filter dan pilih Date satu hari (14 Sep 26)
22. Verifikasi isi input Date di Filter memakai pola `dd MMM yy`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas state global (format tanggal General Settings).
- Urutan TC sama dengan sumber (235, 236, 237) karena TC-236 membutuhkan format hasil langkah 6 TC-235 (`M/d/yy`, `hh:mm a`), dan TC-237 mengubah ke format ketiga di langkah 18. Spec tidak menghapus data.
- Nama Pre-setup literal (`budi-avatar.jpg`, `old-avatar.png`, entri C01) diganti salinan bersuffix milik spec (S-06, S-12).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 8, 13, 19 (Search nama bersuffix agar baris target tampil), langkah 5, 12, 17 (menutup panel Filter dan modal), langkah 7 (Tunggu aksi selesai sebelum pindah surface), langkah 18 (precondition TC-237 diubah lewat API, TC-235 langkah 3 memakai UI General Settings).
- Nilai TC-236 Expected a ("mis. `9/11/26 02:30 PM`") adalah contoh pada tanggal uji; spec mengasersi pola terhadap nilai Deleted Date seed (relatif sekarang - 1 hari).
- Temuan untuk QA:
  - TC-235 menyebut "zona waktu entitas" untuk Upload Date `14:30` tanpa menyebut zona waktu entitas Client uji; spec mengikuti nilai TC dengan asumsi seed menyesuaikan zona waktu entitas.
  - Mekanisme penyetelan General Settings lewat API tidak didefinisikan di TC; disediakan tim FE tanpa mengarang endpoint.
