---
id: TC-FA-FAAM-E2E-239-changelog-opsi-filter-field-dan-action
title: "Modal Changelog: Opsi Filter Field dan Action Memuat Nilai yang Tercatat"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-585
  - TC-FA-FAAM-586
coverage:
  web: automated
---

# Modal Changelog: Opsi Filter Field dan Action Memuat Nilai yang Tercatat

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 28 (Changelog contoh Create, Edit, Delete oleh Sarah Johnson, David Kurniawan, Michael Wijaya; memuat Edit atas Field `Asset Name`, `Code`, `Category`, `TAG Type`, `Brand`, `Model/Type — Dell`, `UoM`, `Default Addon`, `Default Label`). Spec tidak men-seed data lain.
- Kemampuan teknis: membuka Modal Changelog, Filter, dan dropdown Field serta Action. Opsi dropdown diasersi sebagai kumpulan yang memuat nilai Pre-setup No. 28; Field tambahan dari spec lain bukan objek asersi.
- Cleanup: tidak ada data yang dibuat spec ini.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-585 dan 586: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-585: Filter Field memuat Field yang tercatat

1. Klik icon Changelog
2. Klik Filter
3. Buka dropdown Field
4. Verifikasi opsi Field memuat `Asset Name`, `Code`, `Category`, `TAG Type`, `Brand`, `Model/Type — Dell`, `UoM`, `Default Addon`, dan `Default Label`
5. Verifikasi tidak ada opsi `Model/Type` tanpa nama Brand

### Pemulihan state antar TC

6. Tutup dropdown Field

### TC-FA-FAAM-586: Filter Action memuat Create, Edit, Delete

7. Buka dropdown Action
8. Verifikasi opsi `Create`, `Edit`, `Delete`
9. Tutup dropdown Action
10. Tutup Modal Changelog

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 6 dan 9 (menutup dropdown), langkah 10 (menutup Modal Changelog). Langkah 1 dan 2 pada TC-FA-FAAM-586 ("Klik icon Changelog lalu Filter") sudah terpenuhi oleh langkah 1 dan 2 yang masih berlaku.
- Langkah 5 adalah asersi absence atas opsi dropdown dengan anchor positif langkah 4 (daftar opsi pada surface yang sama).
- Temuan untuk QA: TC-FA-FAAM-585 menyatakan opsi Field adalah "Field yang tercatat di tabel Changelog saat ini", sedangkan audit trail permanen tumbuh oleh spec lain; spec hanya mengasersi bahwa opsi yang disebut TC hadir dan tidak menyatakan himpunan opsi lengkap.
