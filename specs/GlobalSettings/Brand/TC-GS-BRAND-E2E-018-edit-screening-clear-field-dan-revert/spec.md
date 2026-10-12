---
id: TC-GS-BRAND-E2E-018-edit-screening-clear-field-dan-revert
title: "Screening Popup Edit Brand, Clear Field, dan Revert ke Nilai Tersimpan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-69
  - TC-GS-BRAND-80
  - TC-GS-BRAND-81
  - TC-GS-BRAND-82
coverage:
  web: automated
---

# Screening Popup Edit Brand, Clear Field, dan Revert ke Nilai Tersimpan

## Prerequisites

- Mode: mock. Seluruh API di-mock (integration test FE tanpa backend nyata); spec ini hanya menguji tampilan dan perilaku popup Edit di browser.
- Kebutuhan mock:
  - Sesi dan payload izin akun Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi) dengan capability Manage master reference lengkap. Login dilakukan sekali di hook `before` (environment variable `GS_TC_PASSWORD` untuk run non-mock; tidak ditulis di spec).
  - Respons `POST /v2/enterprise-management/brands/list`: 12 brand Pre-setup Client A, termasuk `Orion Tech`.
  - Respons `POST /v2/enterprise-management/brands/check-availability` (cek keunikan Brand Name saat mengetik, debounce sekitar 500 ms): nama tersedia (`available` true) untuk semua nilai yang diketik pada field Brand Name (`Orion` dan `Orion Tech`), termasuk `Orion Tech` pada form Edit `Orion Tech` (nama sendiri tidak dihitung sebagai duplikat), sehingga tidak ada error duplikat yang muncul.
  - Endpoint `PATCH /v2/enterprise-management/brands/{brand_id}` (Update Brand) tidak boleh terpanggil di spec ini; bila terpanggil, spec dianggap gagal (tidak ada TC di spec ini yang men-submit).
- Data: memakai brand Pre-setup `Orion Tech`; tidak ada data yang dibuat atau diubah, sehingga tidak ada cleanup.
- Kemampuan teknis: penekanan Esc; pembacaan nilai field; deteksi muncul tidaknya dialog.
- State global: tidak ada yang diubah. Sesi sudah berada di akun default suite (Total Control Client A), sehingga hook `after` tidak perlu memulihkan sesi.

## Test Steps

### TC-GS-BRAND-69: Screening Popup Edit Brand

1. Buka Global Settings > Master Reference > Brand
2. Klik `⋯` baris `Orion Tech` > Edit
3. Verifikasi Header: Title `Edit Brand` dan icon `[✕]`
4. Verifikasi Body: field `Brand Name *` terisi `Orion Tech`
5. Verifikasi checkbox `Stay on this form after submitting` tidak tampil
6. Verifikasi Footer: `[Clear Field]` (text, primary) dan `[Save]` (filled, success)

### TC-GS-BRAND-81: Tutup Popup Edit tanpa perubahan lewat Esc tanpa dialog

7. Tekan Esc (tanpa mengubah apa pun pada popup Edit dari langkah 2)
8. Verifikasi modal tertutup tanpa dialog Unsaved Changes

### TC-GS-BRAND-80: Clear Field pada Edit mengosongkan field, bukan revert ke nilai tersimpan

9. Klik `⋯` baris `Orion Tech` > Edit
10. Klik [Clear Field]
11. Verifikasi field Brand Name kosong (`""`), bukan kembali ke nilai tersimpan
12. Verifikasi tidak ada dialog
13. Verifikasi modal tetap terbuka

### TC-GS-BRAND-82: Edit yang dikembalikan persis ke nilai tersimpan dianggap bersih

14. Ketik `Orion` pada field Brand Name (mengubah nilai dari kondisi kosong hasil langkah 10)
15. Ketik ulang field Brand Name menjadi `Orion Tech`
16. Klik `[✕]`
17. Verifikasi modal tertutup tanpa dialog Unsaved Changes

## Notes

- Mode: mock. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 69, 81, 80, 82 (urutan sumber 69, 80, 81, 82). Alasan: TC-GS-BRAND-69 dan TC-GS-BRAND-81 memakai popup Edit yang masih bersih sehingga berbagi satu pembukaan dan ditutup dengan Esc; TC-GS-BRAND-80 dan TC-GS-BRAND-82 berbagi pembukaan kedua (Clear Field membuat form dirty, lalu nilai diketik kembali ke `Orion Tech` sehingga bersih untuk ditutup lewat `[✕]`). Jumlah pembukaan sama dengan jumlah kejadian menutup form (prinsip 6 konvensi).
- TC-GS-BRAND-82 melanjutkan form yang sama dari TC-GS-BRAND-80 (field kosong hasil [Clear Field]) sesuai pengecualian prinsip 6 konvensi untuk kasus yang menguji pengosongan atau revert itu sendiri; langkah 14 mengetik `Orion` dari kosong, lalu langkah 15 mengetik ulang `Orion Tech`. Hasil yang diuji sama: nilai akhir persis `Orion Tech` dianggap bersih dan form ditutup tanpa dialog.
- Langkah 9 membuka pembukaan form kedua untuk TC-GS-BRAND-80; tidak ada langkah penghubung lain.
