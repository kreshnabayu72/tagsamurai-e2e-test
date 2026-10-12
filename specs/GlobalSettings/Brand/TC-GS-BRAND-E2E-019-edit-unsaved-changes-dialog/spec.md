---
id: TC-GS-BRAND-E2E-019-edit-unsaved-changes-dialog
title: "Dialog Unsaved Changes pada Popup Edit Brand"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-83
  - TC-GS-BRAND-84
  - TC-GS-BRAND-85
  - TC-GS-BRAND-86
coverage:
  web: automated
---

# Dialog Unsaved Changes pada Popup Edit Brand

## Prerequisites

- Mode: mock. Seluruh API di-mock (integration test FE tanpa backend nyata); spec ini hanya menguji perilaku menutup popup Edit yang dirty.
- Kebutuhan mock:
  - Sesi dan payload izin akun Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi) dengan capability Manage master reference lengkap. Login dilakukan sekali di hook `before` (environment variable `GS_TC_PASSWORD` untuk run non-mock; tidak ditulis di spec).
  - Respons `POST /v2/enterprise-management/brands/list`: 12 brand Pre-setup Client A, termasuk `Orion Tech`.
  - Respons `POST /v2/enterprise-management/brands/check-availability` (cek keunikan Brand Name saat mengetik, debounce sekitar 500 ms): nama tersedia (`available` true) untuk `Orion X`, sehingga tidak ada error duplikat yang muncul.
  - Endpoint `PATCH /v2/enterprise-management/brands/{brand_id}` (Update Brand) tidak boleh terpanggil di spec ini; bila terpanggil, spec dianggap gagal.
- Data: memakai brand Pre-setup `Orion Tech`; nilai `Orion X` hanya diketik dan tidak tersimpan, sehingga tidak ada cleanup.
- Kemampuan teknis: klik pada area backdrop di luar modal; penekanan Esc.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-BRAND-83: Tutup Popup Edit dirty memunculkan dialog Unsaved Changes

1. Buka Global Settings > Master Reference > Brand
2. Klik `⋯` baris `Orion Tech` > Edit
3. Ubah Brand Name menjadi `Orion X`
4. Klik `[✕]`
5. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?`
6. Verifikasi tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning)
7. Klik [Cancel] agar kembali ke popup Edit

### TC-GS-BRAND-84: Dialog Unsaved Changes Edit: Cancel kembali ke form

8. Tekan Esc
9. Verifikasi dialog `Unsaved Changes` tampil
10. Klik [Cancel]
11. Verifikasi popup Edit tetap terbuka
12. Verifikasi field Brand Name tetap `Orion X`

### TC-GS-BRAND-86: Klik backdrop Popup Edit dirty tidak menutup form

13. Klik area di luar modal (backdrop)
14. Verifikasi modal tetap terbuka
15. Verifikasi input `Orion X` dipertahankan
16. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-GS-BRAND-85: Dialog Unsaved Changes Edit: Leave membuang perubahan

17. Tekan Esc
18. Verifikasi dialog `Unsaved Changes` tampil
19. Klik [Leave]
20. Verifikasi modal tertutup
21. Verifikasi baris di tabel tetap `Orion Tech`

## Notes

- Mode: mock. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 83, 84, 86, 85 (urutan sumber 83, 84, 85, 86). Alasan: TC-GS-BRAND-85 ([Leave]) membuang perubahan dan menutup form, sehingga ditaruh paling akhir (prinsip 6 konvensi); keempat TC berbagi satu pembukaan popup Edit.
- Langkah 7 menutup dialog TC-GS-BRAND-83 dengan [Cancel] agar form tetap terbuka; bukan asersi TC. Langkah 8 dan 17 memakai Esc sebagai pemicu dialog sesuai Langkah Uji TC-GS-BRAND-84 dan TC-GS-BRAND-85.
