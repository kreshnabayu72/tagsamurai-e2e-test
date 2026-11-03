---
id: TC-FA-CF-E2E-153-state-tenant-expired
title: "State Tenant: Aksi Tulis Ditolak Saat Expired"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-589
  - TC-FA-CF-590
  - TC-FA-CF-591
coverage:
  web: automated
---

# State Tenant: Aksi Tulis Ditolak Saat Expired

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client Expired (Pre-setup #23). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_EXPIRED_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Client Expired (Pre-setup #23): entitas Expired dengan field baseline Pre-setup #12 (`Storage Capacity`, `Asset Serial Tag`, `Legacy Tag`). Nilai data mengacu `Fixture.faCustomFields.baselineGeneral` (fixture disediakan tim FE). Semua aksi tulis ditolak sehingga data Pre-setup tidak berubah (S-06).
- Data Dinamis: Field Name Create yang ditolak `Exp Create {runId}-153`; Field Name Edit yang ditolak `Exp Edit {runId}-153`.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-589: Create saat Expired

1. Klik `[+ Custom Field]`
2. Isi Field Name `Exp Create {runId}-153` dan Data Type `Text`
3. Klik `[Submit]`
4. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
5. Verifikasi toast itu sama dengan copy untuk Suspended
6. Verifikasi tidak ada redirect (halaman Custom Fields tetap tampil)
7. Verifikasi modal Create tertutup otomatis
8. Verifikasi tabel di-refresh
9. Tutup toast error

### TC-FA-CF-590: Edit, toggle, dan Delete saat Expired

10. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
11. Ubah Field Name menjadi `Exp Edit {runId}-153`
12. Klik `[Save]`
13. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil pada Edit
14. Verifikasi modal Edit tertutup
15. Verifikasi tabel di-refresh setelah Edit
16. Tutup toast error
17. Geser switch Active baris `Asset Serial Tag` ke OFF
18. Klik `[Deactivate]`
19. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil pada Deactivate
20. Verifikasi dialog Deactivate tertutup
21. Verifikasi tabel di-refresh setelah Deactivate
22. Tutup toast error
23. Klik row action `⋯` > `Delete` pada baris `Legacy Tag` sampai dialog Delete tampil
24. Klik `[Delete]` pada dialog
25. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil pada Delete
26. Verifikasi dialog Delete tertutup
27. Verifikasi tabel di-refresh setelah Delete
28. Tutup toast error

### TC-FA-CF-591: pembacaan tetap diizinkan saat Expired

29. Verifikasi tabel tampil
30. Buka Modal Changelog
31. Verifikasi Modal Changelog tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 5 memverifikasi klausa "copy yang sama untuk Suspended dan Expired" dari Expected TC-FA-CF-589 dengan membandingkan teks toast dengan teks yang diasersi pada spec 152.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 17 dan 18 (menggeser switch lalu konfirmasi `[Deactivate]`), langkah 23 (membuka dialog Delete), langkah 30 (membuka Modal Changelog), langkah 9, 16, 22, dan 28 (menutup toast error). Toast error identik diasersi pada langkah 4, 13, 19, dan 25, masing-masing sesudah aksinya; toast ditutup pada langkah 9, 16, 22, dan 28 sebelum aksi berikutnya (R-12).
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Client Expired (Pre-setup #23 hanya mendeskripsikan Company); akun disediakan tim FE.
  - TC-FA-CF-591 menyebut "Buka tabel dan Modal Changelog" tanpa asersi eksplisit selain "tampil"; tabel sudah dibuka hook `beforeEach` suite sehingga spec langsung memverifikasinya (langkah 29).
