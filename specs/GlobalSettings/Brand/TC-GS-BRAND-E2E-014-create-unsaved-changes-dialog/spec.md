---
id: TC-GS-BRAND-E2E-014-create-unsaved-changes-dialog
title: "Dialog Unsaved Changes pada Popup Create Brand"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-59
  - TC-GS-BRAND-60
  - TC-GS-BRAND-61
  - TC-GS-BRAND-62
  - TC-GS-BRAND-63
coverage:
  web: automated
---

# Dialog Unsaved Changes pada Popup Create Brand

## Prerequisites

- Mode: mock. Seluruh API di-mock (integration test FE tanpa backend nyata); spec ini hanya menguji perilaku menutup popup Create yang dirty.
- Kebutuhan mock:
  - Sesi dan payload izin akun Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi) dengan capability Manage master reference lengkap. Login dilakukan sekali di hook `before` (environment variable `GS_TC_PASSWORD` untuk run non-mock; tidak ditulis di spec).
  - Respons `POST /v2/enterprise-management/brands/list`: 12 brand Pre-setup Client A (Acme Corp sampai Zenith Corp), tanpa `Umbra`.
  - Respons `POST /v2/enterprise-management/brands/check-availability` (cek keunikan Brand Name saat mengetik, debounce sekitar 500 ms): nama tersedia (`available` true) untuk `Umbra`, sehingga tidak ada error duplikat yang muncul.
  - Endpoint `POST` Create Brand tidak boleh terpanggil di spec ini; bila terpanggil, spec dianggap gagal.
- Data: nilai `Umbra` hanya diketik dan tidak pernah tersimpan, sehingga tidak ada cleanup.
- Kemampuan teknis: penanganan dialog `beforeunload` bawaan browser (membaca bahwa dialog muncul, lalu menolak/menetap di halaman) untuk TC-GS-BRAND-63; klik pada area backdrop di luar modal; penekanan Esc dan F5.
- State global: tidak ada yang diubah. Sesi sudah berada di akun default suite (Total Control Client A), sehingga hook `after` tidak perlu memulihkan sesi.

## Test Steps

### TC-GS-BRAND-59: Tutup Popup Create dirty lewat Esc memunculkan dialog Unsaved Changes

1. Buka Global Settings > Master Reference > Brand
2. Klik [+ Brand]
3. Ketik `Umbra` pada field Brand Name
4. Tekan Esc
5. Verifikasi dialog `Unsaved Changes` (warning) tampil dengan body `You have unsaved changes. Are you sure you want to leave?`
6. Verifikasi tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning)

### TC-GS-BRAND-60: Dialog Unsaved Changes Create: klik Cancel kembali ke form

7. Klik [Cancel] pada dialog dari langkah 4 agar kembali ke form
8. Klik `[✕]`
9. Verifikasi dialog `Unsaved Changes` tampil
10. Klik [Cancel]
11. Verifikasi dialog tertutup
12. Verifikasi popup Create tetap terbuka
13. Verifikasi `Umbra` dipertahankan di field Brand Name

### TC-GS-BRAND-62: Klik backdrop Popup Create dirty tidak menutup form

14. Klik area di luar modal (backdrop)
15. Verifikasi modal tetap terbuka
16. Verifikasi input `Umbra` dipertahankan
17. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-GS-BRAND-63: Reload browser saat Popup Create dirty memunculkan konfirmasi bawaan browser

18. Tekan F5
19. Verifikasi konfirmasi bawaan browser `beforeunload` muncul
20. Tolak reload pada konfirmasi browser agar tetap berada di halaman dengan popup Create terbuka

### TC-GS-BRAND-61: Dialog Unsaved Changes Create: klik Leave menutup form tanpa menyimpan

21. Klik `[✕]`
22. Verifikasi dialog `Unsaved Changes` tampil
23. Klik [Leave]
24. Verifikasi dialog tertutup
25. Verifikasi popup Create tertutup
26. Verifikasi `Umbra` tidak ada di tabel

## Notes

- Mode: mock. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec adalah 59, 60, 62, 63, 61 (urutan sumber 59 sampai 63). Alasan: TC-GS-BRAND-61 ([Leave]) menutup form dan membuang input, sehingga ditaruh paling akhir (prinsip 6 konvensi: kasus menutup form di akhir), dan semua TC lain memakai satu pembukaan form yang sama. Hanya ada satu pembukaan form untuk lima TC.
- Langkah penghubung: langkah 7 (menutup dialog dari TC-GS-BRAND-59 dengan [Cancel]) dan langkah 20 (menolak reload), keduanya aksi tanpa `Verifikasi` agar form tetap terbuka untuk TC berikutnya.
- TC-GS-BRAND-63 bertanda Manual Only di TC sumber; tetap ditulis sebagai langkah otomatis sesuai bagian 2 konvensi (hambatan teknis bukan alasan mengeluarkan TC), kebutuhan penanganan dialog `beforeunload` tercatat di Prerequisites.
