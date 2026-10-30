---
id: TC-GS-FILEMGR-E2E-008-capability-dicabut-saat-halaman-terbuka
title: "Capability Delete Dicabut Saat Halaman Masih Terbuka"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-FILEMGR-254
coverage:
  web: automated
---

# Capability Delete Dicabut Saat Halaman Masih Terbuka

## Prerequisites

- Mode: FE+BE (multi-konteks: dua sesi).
- Akun aktor sesi pertama: akun klon milik spec dengan nama dan capability sama seperti Agus Wibowo (Manage files: Delete), disediakan tim FE (akun klon tidak ada di Tabel Data Uji Pre-setup A1; lihat Temuan untuk QA). Email, mekanisme pembuatan, dan password disediakan tim FE; kredensial lewat env var `Spectra.env.GS_FILES_DELETE_CLONE_PASSWORD` yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`. Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Sesi kedua: pelaku perubahan state (Total Control Sinta Maharani, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`) hanya mengubah capability Manage files akun klon dari Delete menjadi Read saja, sehingga dijalankan lewat sesi API (P-2), bukan sesi UI. Kemampuan teknis: API admin untuk mengubah dan memulihkan capability role/akun (mekanisme tidak disebut di TC, PRD, atau LLD; disediakan tim FE/BE).
- Data Dinamis milik spec: `fm-staff-14-{runId}-008.jpg` (JPG, file aktif bukan foto profil aktif, pola D05) di-seed lewat fixture BE di hook `before` dan dihapus lewat API di hook `after`. Dipakai sebagai pengganti `staff-photo-14.jpg` supaya baris Pre-setup tidak berubah (S-06).
- State global yang diubah: capability akun klon (Delete menjadi Read saja); dipulihkan ke Delete di hook `after` walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Guided Tooltip: flag `guided_tooltip_seen_gs-file-manager` untuk akun klon disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.

## Test Steps

### TC-GS-FILEMGR-254: Aksi Delete setelah capability Delete dicabut saat halaman masih terbuka

1. Di sesi pertama, ketik Search `fm-staff-14-{runId}-008`, tekan Enter
2. Verifikasi baris `fm-staff-14-{runId}-008.jpg` tampil di tabel utama
3. Di sesi API Total Control, ubah capability Manage files akun klon menjadi Read saja hingga tersimpan
4. Di sesi pertama, klik ikon (⋯) baris `fm-staff-14-{runId}-008.jpg`
5. Klik `Delete`
6. Klik `[Delete]` pada dialog konfirmasi
7. Verifikasi toast error `You don't have permission to do this.`
8. Verifikasi tidak ada redirect (halaman tetap di Global Settings > File Manager)
9. Verifikasi kolom Checkbox tidak tampil setelah tabel di-refresh
10. Ketik Search `fm-staff-14-{runId}-008`, tekan Enter
11. Verifikasi baris `fm-staff-14-{runId}-008.jpg` tetap di tabel utama
12. Klik ikon (⋯) baris `fm-staff-14-{runId}-008.jpg`
13. Verifikasi opsi `Delete` tidak tampil di overlay baris
14. Tutup overlay dengan menekan Esc
15. Klik ikon Changelog di toolbar
16. Ketik Search `fm-staff-14-{runId}-008`, tekan Enter
17. Verifikasi Modal Changelog menampilkan empty state `No results found` (tidak ada entri log baru untuk `fm-staff-14-{runId}-008.jpg`)

## Notes

- Mode: FE+BE (kelas c multi-konteks). Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengecualian P-2: sesi kedua (Total Control) hanya memicu perubahan state capability dan memakai sesi API; hasil di sesi itu tidak diasersi.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 10 dan 16 (Search untuk menemukan baris target atau entri log), langkah 14 (menutup overlay).
- Langkah 2 adalah anchor positif sebelum pencabutan capability (baris ada di tabel); langkah 11 adalah anchor positif untuk asersi baris tetap ada setelah aksi ditolak.
- D-1 (asersi "tidak ada entri log baru" di spec fungsional): TC-254 Expected c diasersi dengan baseline nol pada nama file bersuffix unik di Changelog File Manager (langkah 17), anchor positif toast error (langkah 7) dan baris tetap di tabel (langkah 11) (S-12, bagian 3 prinsip 13g: asersi jumlah/state, bukan kelas g).
- Temuan untuk QA:
  - TC-254 Pre-setup memakai akun Agus Wibowo dan Sinta Maharani (Tabel A1 bersama); mencabut capability akun Pre-setup bersama melanggar S-06, sehingga spec memakai akun klon milik spec yang disediakan tim FE (Tabel A1 tidak memuatnya).
  - TC-254 Expected c ("tidak ada entri log baru") tidak menyebut surface log; spec mengasersi di Changelog File Manager saja. System Log dan Activity Log tidak diasersi.
  - TC-254 Automation `Manual Only — (d) dua sesi paralel` tidak menjadi alasan mengeluarkan TC (bagian 2 konvensi); dua sesi dipenuhi lewat sesi UI pertama dan sesi API kedua.
  - Mekanisme API admin untuk mengubah capability tidak disebut di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
