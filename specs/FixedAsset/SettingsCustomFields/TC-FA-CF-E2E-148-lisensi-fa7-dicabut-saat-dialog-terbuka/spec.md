---
id: TC-FA-CF-E2E-148-lisensi-fa7-dicabut-saat-dialog-terbuka
title: "Lisensi FA-7 Dicabut Saat Modal atau Dialog Terbuka"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-581
  - TC-FA-CF-582
  - TC-FA-CF-583
coverage:
  web: automated
---

# Lisensi FA-7 Dicabut Saat Modal atau Dialog Terbuka

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan lisensi FA-7 aktif; field Accounting `Cost Center` (Active Required Yes) dan `Asset Tag Class` (Pre-setup #13). Nilai data mengacu `Fixture.faCustomFields.baselineGeneral` dan `Fixture.faCustomFields.baselinePurchasing` (fixture disediakan tim FE).
- Data Dinamis: Field Name hasil Edit yang ditolak `Cost Center Edit {runId}-148`.
- Kemampuan teknis: seed lisensi FA-7 Company Alpha (cabut dan aktifkan kembali saat sesi berjalan, memakai mekanisme Pre-setup #24; disediakan tim FE/BE).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: lisensi FA-7 Company Alpha dicabut pada langkah 3, 17, dan 26; langkah 14 dan 23 mengaktifkannya kembali. Hook `after` memulihkan lisensi FA-7 aktif lewat seed reset Company Alpha. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-581: lisensi dicabut saat modal Edit terbuka

1. Klik tab `Accounting`
2. Klik row action `⋯` > `Edit` pada baris `Cost Center`
3. Cabut lisensi FA-7 Company Alpha lewat Pre-setup
4. Ubah Field Name menjadi `Cost Center Edit {runId}-148`
5. Klik `[Save]`
6. Verifikasi modal Edit tertutup
7. Verifikasi tabel di-refresh
8. Verifikasi toast error `You don't have permission to do this.` tampil
9. Klik tab `General`
10. Klik tab `Accounting`
11. Verifikasi tab `Accounting` dapat dibuka dalam mode read-only
12. Verifikasi tombol `[+ Custom Field]` Hidden pada tab `Accounting`
13. Verifikasi Field Name `Cost Center` tidak berubah

### TC-FA-CF-582: lisensi dicabut saat dialog Delete terbuka

14. Aktifkan kembali lisensi FA-7 Company Alpha lewat Pre-setup dan muat ulang Settings > Custom Fields
15. Klik tab `Accounting`
16. Klik row action `⋯` > `Delete` pada baris `Cost Center`
17. Cabut lisensi FA-7 Company Alpha lewat Pre-setup
18. Klik `[Delete]`
19. Verifikasi dialog Delete tertutup
20. Verifikasi tabel di-refresh
21. Verifikasi toast `You don't have permission to do this.` tampil
22. Verifikasi field `Cost Center` tidak terhapus

### TC-FA-CF-583: lisensi dicabut saat dialog Bulk Deactivate terbuka

23. Aktifkan kembali lisensi FA-7 Company Alpha lewat Pre-setup dan muat ulang Settings > Custom Fields
24. Klik tab `Accounting`
25. Pilih `Cost Center` dan `Asset Tag Class`, lalu buka dialog Bulk Deactivate
26. Cabut lisensi FA-7 Company Alpha lewat Pre-setup
27. Klik `[Deactivate]`
28. Verifikasi dialog Bulk Deactivate tertutup
29. Verifikasi tabel di-refresh
30. Verifikasi toast `You don't have permission to do this.` tampil
31. Verifikasi status `Cost Center` dan `Asset Tag Class` tidak berubah

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14 dan 23 (mengaktifkan kembali lisensi supaya precondition "FA-7 aktif" TC berikutnya terpenuhi; TC-FA-CF-581 sampai 583 masing-masing mencabut lisensi), langkah 9 dan 10 mengikuti Langkah 4 TC-FA-CF-581.
- S-06: target aksi tulis adalah baris Pre-setup `Cost Center` dan `Asset Tag Class` yang aksinya selalu ditolak 403 (tidak ada perubahan data); Prerequisites menyatakan data hanya dibaca.
- Temuan untuk QA:
  - TC-FA-CF-581 sampai 583 menyebut "Company Alpha ... FA-7 aktif (Pre-setup #13 dan #24)" sedangkan Pre-setup #24 mendeskripsikan Company License Lapse; spec memakai Company Alpha dengan pencabutan lisensi lewat mekanisme seed Pre-setup #24 (kemampuan disediakan tim FE/BE).
  - TC-FA-CF-583 menyebut "dua field Accounting" tanpa nama; spec memakai `Cost Center` dan `Asset Tag Class` (Pre-setup #13).
  - Langkah 13 dan 22 mengasersi "tidak ada perubahan data" pada Field Name dan keberadaan field yang dibaca dari tabel.
